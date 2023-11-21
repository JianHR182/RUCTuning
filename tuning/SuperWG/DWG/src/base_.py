from util import *
from schema import *


# data access distribution
class feature:
    def __init__(self, workloadSize, rwRatio, averageTableNum, tableDistribution, \
                 queryComparisonOperatorRatio, tableDomainDist, queryLogicPredicateNum, \
                 averageAggregationOperatorNum, averageQueryColomnNum, groupByRatio, descOrAsc) -> None:
        # feature1  : size of workload，负载规模
        self.workloadSize = workloadSize
        # feature2  : read/write ratio，读写比例
        self.rwRatio = rwRatio
        # feature3  : average table num，平均每次查询涉及的表的数目
        self.averageTableNum = averageTableNum
        # feature4  : table data distribution，表的访问分布，调用方式见下
        # tb_choice=self.dbs.tables[randNumGen(0,len(self.dbs.tables)-1,condition.avgtb)]
        # tb_choice=get1Table(self.dbs.tables,np.full(len(self.dbs.tables),1.0/len(self.dbs.tables)))
        self.tableDistribution = tableDistribution
        # feature5  : different query comparison constraint ratio，查询谓词的访问分布，调用方式如下
        # cons=randNumGen(0,3,condition.feature4)
        self.queryComparisonOperatorRatio = queryComparisonOperatorRatio
        # feature6  : query data domain distribution，列的访问分布，调用方式如下
        # data=randNumGen(0,99,[1.0/100 for i in range(100)])
        self.tableDomainDist = tableDomainDist
        # feature7  : query logic predicate num，平均每条查询语句含有的逻辑谓词数量
        self.queryLogicPredicateNum = queryLogicPredicateNum
        # feature8  : average aggregation operator num，平均每条查询语句含有的聚合操作数量
        self.averageAggregationOperatorNum = averageAggregationOperatorNum
        # feature9  : average query colomn num，平均每条语句查询需要返回的列的数量
        self.averageQueryColomnNum = averageQueryColomnNum
        # feature10 : group by ratio，平均每条语句包含的分组操作数量
        self.groupByRatio = groupByRatio
        # feature11 : if ordered, desc or asc，升序和降序两种排序的期望比例
        self.descOrAsc = descOrAsc


import json


# 该函数用来解析配置文件信息
def load_json(filePath, mode):
    jsonFile = open(filePath, mode)
    input = json.loads(jsonFile.read())
    # print(input)
    # 存放表
    all_tables = []
    # 存放约束
    cons = []
    foreign_cons = []
    # 加载表名和列名
    # 循环读入各表信息
    for table in input['Tables']:
        tb_name = table['Table Name']
        tb_col_distribution = table['Column Distribution']
        tb_cols = []
        # 循环读入表的各列信息
        for col in table['Table Columns']:
            col_name = col['Column Name']
            col_type = col['Data Type']
            col_type_mod = col['Data Type Mod']
            col_domain = col['Data Distribution']
            tb_cols.append(column(col_name, col_type, col_type_mod, col_domain))
        # 识别主键
        prim_key = key(table['Primary Key']['Name'], table['Primary Key']['Data Type'])
        for con in table['Foreign Key']:
            foreign_cons.append(foreign_constraint(tb_name, key(con['Foreign Key Name'], con['Foreign Key Type']),
                                                   con['Referenced Table'], key(con['Referenced Primary Key'],
                                                                                con['Referenced Primary Key Type'])))
        # 全部放入all_tables列表
        all_tables.append(Table(tb_name, tb_cols, prim_key, foreign_cons, tb_col_distribution))
    # 加载约束，把约束放入cons列表中
    for con in input['Constraints']:
        cons.append(input['Constraints'][con])
    # print(cons)
    # 给特征向量赋值
    fea = feature(cons[0], cons[1], cons[2], cons[3], cons[4], cons[5], cons[6], cons[7], cons[8], cons[9], cons[10])
    # print(cons[0],cons[1],cons[2],cons[3],cons[4])
    # 创建数据库Schema实例
    dbs = DBschema(tbs=all_tables, foreign_constraint=foreign_cons)
    # 设置输出文件名
    outputFile = input['Generation File']
    return dbs, fea, outputFile
    # cons应该是feature类型
    # fea=feature(cons[0],cons[1],...)，可扩展
    # return DBschema,feature


# 这是基础生成类，这是一个抽象类，未实例化过
# 主要工作的承担者是其子类SQLGen2
class SQLGen:
    def __init__(self, dbs) -> None:
        self.sql_set = []
        self.last_sql = simpleSQL()
        self.dbs = dbs

    # 先尝试使用部分特征进行生成
    def generate(self, condition):
        # feature1 : read/write ratio
        rw_choice = rand_num_sampling(0, 1, np.array([condition.rwRatio, 1 - condition.rwRatio]))
        # feature2 : average table num
        tb_num = rand_num_sampling(1, 2, condition.averageTableNum)
        # feature3 : table data distribution
        # tb_choice=self.dbs.tables[randNumGen(0,len(self.dbs.tables)-1,[1.0/len(self.dbs.tables) for i in range(len(self.dbs.tables))])]
        tb_choice = self.dbs.tables[rand_num_sampling(0, len(self.dbs.tables) - 1, condition.tableDistribution)]
        # feature4 : different query comparison constraint ratio
        # cons=randNumGen(0,3,[1.0/4 for i in range(4)])
        cons = rand_num_sampling(0, 3, condition.queryComparisonOperatorRatio)
        # feature5 : query data domain distribution
        data = rand_num_sampling(0, 99, [1.0 / 100 for i in range(100)])
        # 判断是读语句还是写语句
        if rw_choice == 0:
            # 添加固定token，这个后面子类会重写
            self.last_sql.add(key(value="select", type="keyword"))
            self.last_sql.add(key(value="*", type="colname"))
            self.last_sql.add(key(value="from", type="keyword"))
            self.last_sql.add(key(value=tb_choice.name, type="tbname"))
            self.last_sql.add(key(value="where", type="keyword"))
            self.last_sql.add(key(value=tb_choice.col[0].value, type="colname"))
            # 判断比较谓词的类型
            if cons == 0:
                self.last_sql.add(key(value=">", type="compare"))
            else:
                if cons == 1:
                    self.last_sql.add(key(value="<", type="compare"))
                else:
                    if cons == 2:
                        self.last_sql.add(key(value="=", type="compare"))
                    else:
                        if cons == 3:
                            self.last_sql.add(key(value="!=", type="compare"))
                        else:
                            pass
            self.last_sql.add(key(value=data, type="value"))
            self.last_sql.add(key(value=";", type="end"))
        # 如果是insert语句
        else:
            self.last_sql.add(key(value="insert", type="keyword"))
            self.last_sql.add(key(value="into", type="keyword"))
            self.last_sql.add(key(value=tb_choice.name, type="tbname"))
            self.last_sql.add(key(value="value", type="keyword"))
            tmp = "("
            for i in range(len(tb_choice.col)):
                if i != 0:
                    tmp += ","
                tmp += str(rand_num_sampling(0, 99, [1.0 / 100 for i in range(100)]));
            tmp += ")"
            self.last_sql.add(key(value=tmp, type="value"))
            self.last_sql.add(key(value=";", type="end"))

        self.sql_set.append(self.last_sql)
        return self.last_sql

    # 保存函数，把结果写入wg文件
    def save(self, outputFile):
        with open(outputFile, 'w') as f:
            for it in self.sql_set:
                f.write(it.toStr())
        print(f"workload saved to {outputFile}")
