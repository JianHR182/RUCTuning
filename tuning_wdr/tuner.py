import utils
import config
from pyDOE import lhs
import numpy as np
from hebo.design_space.design_space import DesignSpace
from hebo.optimizers.hebo import HEBO
import sys
import os
import time
from stress_testing_tool import stress_testing_tool
from hord_problem import Problem
from poap.controller import BasicWorkerThread, ThreadController
from pySOT.experimental_design import LatinHypercube
from pySOT import strategy, surrogate
from ConfigSpace import ConfigurationSpace, Integer
# from smac import HyperparameterOptimizationFacade as HPOFacade
# from smac import Scenario
# from smac.initial_design import LatinHypercubeInitialDesign


class tuner:
    def __init__(self, db):
        self.method = config.method
        self.iteration = config.iteration
        self.database_name = config.db
        self.knobs_number = config.knobs_number
        self.sampling_number = config.sampling_number
        self.knobs_detail = utils.get_knobs_detail(config.knobs_file, self.knobs_number)
        self.benchmark = config.benchmark

        self.id = int(time.time())
        self.logger = utils.get_logger('log/tune_log/{}.log'.format(self.id))

        self.stt = stress_testing_tool(self.knobs_detail, self.id, db)

    def tune(self):
        if self.method == 'HEBO':
            self.LHS()
            self.HEBO(self.id)
        elif self.method == 'HORD':
            self.HORD()
        # elif self.method == 'SMAC':
        #     self.SMAC()
        elif self.method == 'TEST':
            self.LHS()
        # self.test_best_config()

    def LHS(self):
        if self.sampling_number == 0:
            return

        lb, ub, enum_knobs = [], [], []
        for index, knob in enumerate(self.knobs_detail):
            if self.knobs_detail[knob]['type'] == 'integer':
                lb.append(self.knobs_detail[knob]['min'])
                ub.append(self.knobs_detail[knob]['max'])
            elif self.knobs_detail[knob]['type'] == 'enum':
                lb.append(0)
                ub.append(len(self.knobs_detail[knob]['enum_values']) - 1)
                enum_knobs.append([index, knob])

        lb = np.array(lb)
        ub = np.array(ub)
        points_dict = []
        points = (lb + (ub - lb) * lhs(self.knobs_number, self.sampling_number)).astype(int).tolist()
        for point in points:
            temp = {}
            for index, knob in enumerate(self.knobs_detail):
                if index == self.knobs_number:
                    break
                temp[knob] = point[index]

            points_dict.append(temp)
        for index, point in enumerate(points_dict):
            print('random sampling epoch {}\t total {}'.format(index + 1, self.sampling_number))
            tps = self.stt.test_config(point)
            self.logger.info(str(self.id) + '\trandom ' + str(index + 1) + '\t' + str(point) + "\ttps = " + str(tps) + '\n')

    def HEBO(self, id):
        data = utils.load_sampling_data('./history_results/{}'.format(id))
        params = []

        for name in self.knobs_detail.keys():
            if self.knobs_detail[name]['type'] == "integer":
                if self.knobs_detail[name]['max'] > sys.maxsize:
                    params.append({'name': name, 'type': 'int', 'lb': int(self.knobs_detail[name]['min']) / 1000000,
                                   'ub': int(self.knobs_detail[name]['max']) / 1000000})
                else:
                    params.append({'name': name, 'type': 'int', 'lb': int(self.knobs_detail[name]['min']),
                                   'ub': int(self.knobs_detail[name]['max'])})
            elif self.knobs_detail[name]['type'] == "enum":
                params.append(
                    {'name': name, 'type': 'int', 'lb': 0, 'ub': len(self.knobs_detail[name]['enum_values']) - 1})

        space = DesignSpace().parse(params)

        hebo_batch = HEBO(space)
        hebo_batch.observe(data[data.columns[:-1]], np.array(data['tps']).reshape(-1, 1))

        for step in range(self.iteration):
            print('model suggest epoch {}\t total {}'.format(step + 1, self.iteration))
            rec_x = hebo_batch.suggest(n_suggestions=1)

            tmp = rec_x
            temp_config = {}
            tmp = tmp.reset_index(drop=True)
            for key in self.knobs_detail.keys():
                temp_config[key] = int(tmp.loc[0, key])

            y = self.stt.handle_HEBO_config(rec_x)
            hebo_batch.observe(rec_x, np.array([[y]]))
            self.logger.info(str(self.id) + '\tsuggest ' + str(step + 1) + '\t' + str(temp_config) + "\ttps = " + str(y) + '\n')

    def HORD(self):
        problem = Problem(self.knobs_detail, self.iteration)

        controller = ThreadController()
        ''' create and reset surrogate '''
        _surrogate = surrogate.RBFInterpolant(
            dim=problem.dim,
            lb=problem.lb,
            ub=problem.ub,
        )

        ''' reset surrogate'''
        controller.strategy = strategy.DYCORSStrategy(
            max_evals=self.iteration + self.sampling_number,
            opt_prob=problem,
            exp_design=LatinHypercube(
                dim=problem.dim,
                num_pts=self.sampling_number  # problem.dim * 2
            ),
            surrogate=_surrogate
        )

        ''' add extern-dataset '''

        worker = BasicWorkerThread(controller, self.stt.handle_HORD_config)
        controller.launch_worker(worker)

        ''' Main Loop '''
        # remembe to change the sleeping time
        controller.run()

    # def SMAC(self):
    #     params = {}
    #     for name in self.knobs_detail.keys():
    #         if self.knobs_detail[name]['type'] == "integer":
    #             if self.knobs_detail[name]['max'] > sys.maxsize:
    #                 params[name] = Integer(name, bounds=(
    #                 int(self.knobs_detail[name]['min']) / 1000000, int(self.knobs_detail[name]['max']) / 1000000))
    #             else:
    #                 params[name] = Integer(name, bounds=(
    #                 int(self.knobs_detail[name]['min']), int(self.knobs_detail[name]['max'])))
    #         elif self.knobs_detail[name]['type'] == "enum":
    #             params[name] = Integer(name, bounds=(0, len(self.knobs_detail[name]['enum_values']) - 1))
    #
    #     configspace = ConfigurationSpace(seed=0, space=params)
    #     scenario = Scenario(configspace, deterministic=True, n_trials=self.iteration + self.sampling_number)
    #
    #     smac = HPOFacade(
    #         scenario,
    #         self.stt.handle_SMAC_config,
    #         overwrite=True,  # Overrides any previous results that are found that are inconsistent with the meta-data
    #         initial_design=LatinHypercubeInitialDesign(scenario, max_ratio=1, n_configs=self.sampling_number)
    #     )
    #
    #     smac.optimize()

    def test_best_config(self):
        data = utils.load_sampling_data('./records')
        best_config = data.iloc[data['tps'].idxmin()].to_dict()

        self.stt.test_config(best_config)

        random_config = data.iloc[250].to_dict()

        self.stt.test_config(random_config)
        default_config = {"wal_buffers": '16MB', "shared_buffers": '1GB', "max_process_memory": '20GB',
                          "maintenance_work_mem": '16MB', "work_mem": '64MB', "effective_cache_size": '128MB',
                          "effective_io_concurrency": 1, "temp_buffers": '1MB', "vacuum_cost_limit": 200,
                          "vacuum_cost_page_dirty": 20, "vacuum_cost_page_hit": 1, "vacuum_cost_page_miss": 10,
                          "autovacuum_vacuum_cost_limit": -1, "backend_flush_after": 0}

        self.stt.test_config(default_config)
        self.stt.test_config(default_config)
