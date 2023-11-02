import numpy as np

# 单条SQL语句
class simpleSQL:
    # 初始化，内部由token组成
    def __init__(self) -> None:
        self.token=[]
        
    # def __init__(self,token = None) -> None:
        # self.token=token
        
    # 添加新的token
    def add(self,x):
        self.token.append(x)
    
    # 调试用，输出信息
    def toStr(self):
        ans=""
        for i in range(len(self.token)):
            if self.token[i].type=="keyword" or self.token[i].type=="sort" or self.token[i].type=="aggregation":
                ans+=str(self.token[i].value).upper()
            else:
                ans+=str(self.token[i].value)
            # if self.token[i].value==",":
            #     print(self.token[i].type)
            #     ans+="hello"
            if i!=len(self.token)-1 \
                and self.token[i].type!="tbname_"\
                    and self.token[i].type!="dot"\
                        and self.token[i].type!="colname_"\
                            and self.token[i].type!="join"\
                                and (i+1<=len(self.token) and self.token[i+1].type!="join"):
                ans+=" "
            # print(str(self.token[i].value)+" ",end="")
        # print()
        return ans+"\n"

# 手写的键值对类，包括两个必选值和一个可选值
class key:
    def __init__(self,value,type,mod=0,domain=None) -> None:
        self.value=value
        self.type=type
        self.type_mod=mod
        self.domain=domain
        # self.name=name
        
    # 调试用，输出信息
    def toStr(self):
        print(f'value : {self.value}')
        print(f'type : {self.type}')

# 外键约束数据结构
class foreign_constraint:
    def __init__(self,tb1,col1,tb2,col2) -> None:
        self.tb1=tb1
        self.col1=col1
        self.tb2=tb2
        self.col2=col2

# 列数据结构
class column:
    def __init__(self,name,type,mod,domain,father=None) -> None:
        self.name=name
        self.data_type=type
        self.data_mod=mod
        self.domain=domain
        self.father=father
    
    def __hash__(self):
        return hash((self.name, self.father.name))  # 根据 name 和 age 的哈希值进行计算

    def __eq__(self, other):
        return (self.name, self.father.name) == (other.name, other.father.name) 
        
# 表数据结构
class Table:
    # 初始化，主要在load_json函数中使用
    def __init__(self,tb_name,col,prim_col,foreign_constraint,column_distribution) -> None:
        self.name=tb_name
        self.col=col
        self.col_data_dis={}
        self.prim_col = prim_col
        self.foreign_constraint = foreign_constraint
        self.column_distribution = column_distribution
    
    # 可用于添加新的数据分布特征
    def addCharacteristics(self,col_name,data_dis):
        col_name_set=set(self.col[0:len(self.col)])
        if col_name not in col_name_set:
            print("error: add data characteristics failed. Col name not found.")
        else:
            self.col_data_dis[col_name]=data_dis
            
# 数据库模式数据结构
# 内容是表和约束
class DBschema:
    def __init__(self,tbs,foreign_constraint=None) -> None:
        self.tables=tbs
        # self.tbNum=len(tbs)
        self.foreign_constraint=foreign_constraint
    
    # 调试用，输出信息
    def toStr(self):
        ans=""
        for i,j in enumerate(self.tables):
            ans+="table "+str(i+1)
            ans+=" : "+j.name
            ans+="\n"
        return ans
        