import numpy as np
import sys
from pySOT.optimization_problems import OptimizationProblem


class Problem(OptimizationProblem):
    def __init__(self, knobs: dict, max_iteration: int):
        """ Init HORD problem to solve.

        Args:
            knobs (list): parameter list.
            max_iteration (int): max tunning round.
        """
        self.dim = len(knobs.keys())
        self.knobs = knobs
        self.max_iteration = max_iteration

        self.buildSearchSpace()

    def buildSearchSpace(self):
        """ Build HORD parameter search space.

        Args:
            knobs (list): parameter list.
        """
        self.int_var = []
        self.cont_var = []
        self.search_space = {}

        self.lb = np.zeros(self.dim, dtype=np.int64)
        self.ub = np.zeros(self.dim, dtype=np.int64)

        for count,name in enumerate(self.knobs.keys()):
            if self.knobs[name]['type'] == 'integer':
                if self.knobs[name]['max'] > sys.maxsize:
                    self.ub[count] = int(self.knobs[name]['max'] / 1000000)
                    self.lb[count] = int(self.knobs[name]['min'] / 1000000)
                else:
                    self.ub[count] = self.knobs[name]['max']
                    self.lb[count] = self.knobs[name]['min']
                
            elif self.knobs[name]['type'] == 'enum':
                self.lb[count] = 0
                self.ub[count] = len(self.knobs[name]['enum_values']) - 1
                       
            self.int_var.append(count)

        self.int_var = np.array(self.int_var)
        self.cont_var = np.array(self.cont_var)


