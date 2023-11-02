#!/usr/bin/env python
# vim: set fileencoding=utf-8
from base_ import *
import argparse

# 根据表访问概率图，不放回抽样采样出n个table
# 同时还要返回对应表的实际访问的条件概率（在已经确定选取表的范围是这n张表的情况下）
def getNTable(dbs,n,pdg):
    # print(n)
    all_tb=[dbs.tables[i] for i in range(len(dbs.tables))]
    # all_tb=[i for i in len(dbs.tables)]
    tb_set=set()
    tb_selected = []
    tb_sub_distribution = []
    if len(all_tb)<n:
        print("fatal error : dbs table num not enough.")
        return -1,set()
    # 可能会抽出同一个表
    # 使用set容器去重
    while len(tb_set)<n:
        x=rand_num_sampling(0,len(all_tb)-1,pdg)
        if x!=-1:
            tb_set.add(dbs.tables[x])
            if dbs.tables[x] not in tb_selected:
                tb_selected.append(dbs.tables[x])
                tb_sub_distribution.append(table2dist[dbs.tables[x]])
            else:
                continue
            # print(str(len(tb_set))+"add"+str(fea.tableDistribution[x]))
        else:
            # 如果中途采样失败，说明概率分布图有问题，直接返回-1
            return -1,set()
    # 因为条件改变，让tb_sub_distribution和变为1
    sum_of_tsd = 0
    for i in tb_sub_distribution:
        sum_of_tsd = sum_of_tsd + i
    # print(tb_sub_distribution)
    for i in range(len(tb_sub_distribution)):
        tb_sub_distribution[i] = tb_sub_distribution[i]/sum_of_tsd
    # print(tb_sub_distribution)
    # 返回集合和tb_sub_distribution，也即新的条件概率表
    return 1,tb_set,tb_sub_distribution

# getNTable的特例，可以用于全表的子集，同时优化计算时间
def get1Table(tbs,pdg):
    # print("get1"+str(len(tbs)-1))
    return tbs[rand_num_sampling(0,len(tbs)-1,pdg)]

# 根据访问概率，选取列
def get1Column(tb,pdg):
    return tb.col[rand_num_sampling(0,len(tb.col)-1,pdg)]

# 在给定表中，根据联合概率分布选取n个列
def from_tb_get_N_columns_for_aggregation(tbs,aggregationNum):
    col_set=set()
    while(len(col_set)<aggregationNum):
        tb_choice=tbs[rand_num_sampling(0,len(tbs)-1,np.full(len(tbs),1.0/len(tbs)))]
        col_choice=get1Column(tb_choice,np.full(len(tb_choice.col),1.0/len(tb_choice.col)))
        real_col_choice=column(
            col_choice.name,
            col_choice.data_type,
            col_choice.data_mod,
            col_choice.domain,
            tb_choice
        )
        col_set.add(real_col_choice)
        # pass
    return list(col_set)

# 加入了动态特征处理的负载生成器
class SQLGen2(SQLGen):
    
    def generate(self,condition):
        hasJoin=False
        hasOr=False
        
        if condition.averageQueryColomnNum[0]!=0:
            print("fatal error : SELECT * is not allowed, please fix the averageQueryColomnNum paramiter.")
            return
        
        self.last_sql=simpleSQL()
        rw_choice=rand_num_sampling(0,1,np.array([condition.rwRatio,1-condition.rwRatio]))
        if rw_choice==0:
            # 读语句
            tb_num=rand_num_sampling(1,2,condition.averageTableNum)
            # 判断语句涉及的表的数目
            if tb_num==1:
                # 根据采样函数确定表和列
                tb_choice=get1Table(self.dbs.tables,condition.tableDistribution)
                
                self.last_sql.add(key(value="select",type="keyword"))
                has_aggregation_and_not_aggregation=False
                select_column_name_list=[]
                
                on=rand_num_sampling(0,2,condition.averageAggregationOperatorNum)
                
                aqcn=min(len(tb_choice.col),len(condition.averageQueryColomnNum)-1)
                # qcn=rand_num_sampling(0,aqcn,[1.0/(aqcn+1) for i in range(aqcn+1)])
                real_exp=condition.averageQueryColomnNum[0:aqcn+1]
                sum_tmp=sum(real_exp)
                real_exp_fixed=[it/sum_tmp for it in real_exp]
                qcn=rand_num_sampling(0,aqcn,real_exp_fixed)
                on=min(on,qcn)
                
                if on>0 and on!=qcn:
                    has_aggregation_and_not_aggregation=True
                
                # 计算查询需要返回的列的数目和聚合操作的数目
                if qcn==0:
                    self.last_sql.add(key(value="*",type="colname"))
                else:
                    if qcn==on or on==0:
                        res=from_tb_get_N_columns_for_aggregation(tbs=[tb_choice],aggregationNum=qcn)
                        n_col=[res[i] for i in range(len(res))]
                        for i,col in enumerate(n_col):
                            # on=2 qcn=3
                            if on!=0:
                                if col.data_type in ['varchar','bpchar','timestamp','blob']:
                                    aggregation_type=0
                                else:
                                    aggregation_type=rand_num_sampling(1,3,[1.0/3 for i in range(3)])  
                                if aggregation_type==0:
                                    tmp=f'count({col.name}) as count_value_{col.name}'
                                    # select_column_name_list.append(f"count_value_{col.name}")
                                elif aggregation_type==1:
                                    tmp=f'avg({col.name}) as average_value_{col.name}'
                                    # select_column_name_list.append(f"average_value_{col.name}")
                                elif aggregation_type==2:
                                    tmp=f'min({col.name}) as minimum_value_{col.name}'
                                    # select_column_name_list.append(f"minimum_value_{col.name}")
                                elif aggregation_type==3:
                                    tmp=f'max({col.name}) as maximum_value_{col.name}'
                                    # select_column_name_list.append(f"maximum_value_{col.name}")
                                    
                                if i!=qcn-1:
                                    self.last_sql.add(key(value=tmp,type="colname_"))
                                else:
                                    self.last_sql.add(key(value=tmp,type="colname"))
                                
                            else:
                                if i!=qcn-1:
                                    self.last_sql.add(key(value=f"{col.name}",type="colname_"))
                                else:
                                    self.last_sql.add(key(value=f"{col.name}",type="colname"))
                                # print(i.value)
                                
                            if i!=qcn-1:
                                self.last_sql.add(key(value=",",type="dot"))
                        pass
                    else:
                        assert(has_aggregation_and_not_aggregation==True)
                        aggregation_cols=from_tb_get_N_columns_for_aggregation(tbs=[tb_choice],aggregationNum=on)
                        not_aggregation_cols=from_tb_get_N_columns_for_aggregation(tbs=[tb_choice],aggregationNum=qcn-on)
                        for i,col in enumerate(not_aggregation_cols):
                            self.last_sql.add(key(value=f"{col.name}",type="colname_"))
                            self.last_sql.add(key(value=",",type="dot"))
                            select_column_name_list.append(col.name)
                        
                        for i,col in enumerate(aggregation_cols):
                            if col.data_type in ['varchar','bpchar','timestamp','blob']:
                                aggregation_type=0
                            else:
                                aggregation_type=rand_num_sampling(1,3,[1.0/3 for i in range(3)])  
                            if aggregation_type==0:
                                tmp=f'count({col.name}) as count_value_{col.name}'
                                # select_column_name_list.append(f"count_value_{col.name}")
                            elif aggregation_type==1:
                                tmp=f'avg({col.name}) as average_value_{col.name}'
                                # select_column_name_list.append(f"average_value_{col.name}")
                            elif aggregation_type==2:
                                tmp=f'min({col.name}) as minimum_value_{col.name}'
                                # select_column_name_list.append(f"minimum_value_{col.name}")
                            elif aggregation_type==3:
                                tmp=f'max({col.name}) as maximum_value_{col.name}'
                                # select_column_name_list.append(f"maximum_value_{col.name}")
                            
                            if i!=len(aggregation_cols)-1:
                                self.last_sql.add(key(value=tmp,type="colname_"))
                                self.last_sql.add(key(value=",",type="dot"))
                            else:
                                self.last_sql.add(key(value=tmp,type="colname"))      
       
                self.last_sql.add(key(value="from",type="keyword"))
                self.last_sql.add(key(value=tb_choice.name,type="tbname"))
                
                self.last_sql.add(key(value="where",type="keyword"))
                qc_num=rand_num_sampling(1,3,condition.queryLogicPredicateNum)
                # 依次增加查询逻辑谓词
                for i in range(qc_num):
                    if i!=0:
                        if rand_num_sampling(0,1,[0.5,0.5])==0:
                            self.last_sql.add(key(value="and",type="predicate"))
                        else:
                            self.last_sql.add(key(value="or",type="predicate"))
                            hasOr=True
                    
                    # tb_choice=get1Table(self.dbs,np.full(len(self.dbs.tables),1.0/len(self.dbs.tables)))
                    # col_choice=get1Column(tb_choice,np.full(len(tb_choice.col),1.0/len(tb_choice.col)))
                    # 根据列分布采样出选择的列，下面同理
                    col_choice=get1Column(tb_choice,tb_choice.column_distribution)

                    self.last_sql.add(key(value=tb_choice.name,type="tbname_"))
                    self.last_sql.add(key(value=".",type="dot"))
                    self.last_sql.add(key(value=col_choice.name,type="colname"))
                    
                    # 特判
                    # varchar类型、blob类型的数据不匹配大于、小于比较
                    if col_choice.data_type in ['varchar','bpchar','blob']:
                        # print(condition.queryComparisonOperatorRatio[2:4])
                        newratio=condition.queryComparisonOperatorRatio[2:4]
                        newsum=sum(newratio)
                        # print(newsum)
                        for i,it in enumerate(newratio):
                            newratio[i]=1.0/newsum*newratio[i]
                        # print(newratio)
                        # 等比例放缩概率分布图，不然采样函数会报错
                        cons=rand_num_sampling(0,1,newratio)
                        # print(col_choice.type)
                        if cons==0:
                            self.last_sql.add(key(value="=",type="compare"))
                        elif cons==1:
                            # self.last_sql.add(key(value="!=",type="compare"))
                            self.last_sql.add(key(value="=",type="compare"))
                        else:
                            pass
                        # print(col_choice.domain)
                        # data=rand_str_sampling(str_len=len(col_choice.domain[1]))
                        if col_choice.data_type in ['varchar','bpchar']:
                            data=rand_str_sampling2(min_len=col_choice.domain[0],max_len=col_choice.domain[1])
                            self.last_sql.add(key(value="\'"+data+"\'",type="value"))
                        else:
                            self.last_sql.add(key(value="NULL",type="value"))
                        # print(data)

                    else:
                        # 类型：timestamp或数字
                        # print(col_choice.data_type)
                        cons=rand_num_sampling(0,3,condition.queryComparisonOperatorRatio)
                        # print(cons)
                        # print(col_choice.type)
                        # 根据访问概率，确定选择的比较谓词
                        if cons==0:
                            self.last_sql.add(key(value=">",type="compare"))
                        elif cons==1:
                            self.last_sql.add(key(value="<",type="compare"))
                        elif cons==2:
                            self.last_sql.add(key(value="=",type="compare"))
                        elif cons==3:
                            # self.last_sql.add(key(value="!=",type="compare"))
                            self.last_sql.add(key(value="=",type="compare"))
                        else:
                            pass
                        # print(col_choice.domain)
                        # print(col_choice.domain[0],col_choice.domain[1])
                        # 根据列值域，选择查询的范围
                        if col_choice.data_type=="timestamp":
                            # data=rand_timestamp_sampling(precision=col_choice.data_mod)
                            start_ts=datetime.datetime.strptime(col_choice.domain[0],"%Y-%m-%d %H:%M:%S")
                            end_ts=datetime.datetime.strptime(col_choice.domain[1],"%Y-%m-%d %H:%M:%S")
                            data=rand_timestamp_sampling2(start_ts,end_ts,col_choice.data_mod)
                            self.last_sql.add(key(value="\'"+str(data)+"\'",type="value"))
                        # blob类型
                        else:
                            num_domain=int(col_choice.domain[1])-int(col_choice.domain[0])+1
                            if col_choice.data_type=="numeric" and col_choice.data_mod[0]==col_choice.data_mod[1]:
                                data=rand_decimal_sampling(col_choice.data_mod[0])
                            else:
                                data=rand_num_sampling(
                                    int(col_choice.domain[0]),
                                    int(col_choice.domain[1]),
                                    [1.0/num_domain for i in range(num_domain)]
                                )
                            self.last_sql.add(key(value=data,type="value"))
                
                
                # 判断是否含有分组操作
                hasGroupBy=rand_num_sampling(0,1,condition.groupByRatio)
                # col_choice=get1Column(tb_choice,tb_choice.column_distribution)
                if has_aggregation_and_not_aggregation==True:
                # if hasGroupBy==1 and has_aggregation_and_not_aggregation==True and col_choice.name in select_column_name_list:
                    # 最后处理group by
                    self.last_sql.add(key(value="group by",type="keyword"))
                    for i,it in enumerate(select_column_name_list):
                        if i!=len(select_column_name_list)-1:
                            self.last_sql.add(key(value=it,type="colname_"))
                            self.last_sql.add(key(value=",",type="dot"))
                        else:
                            self.last_sql.add(key(value=it,type="colname"))
                else:
                    hasGroupBy=0
                    pass
                
                # tb_choice=get1Table(self.dbs.tables,condition.tableDistribution)

                # 升序还是降序
                # hasOrderBy=rand_num_sampling(0,1,condition.descOrAsc)
                hasOrderBy=1
                descOrAsc=rand_num_sampling(0,1,condition.descOrAsc)
                # col_choice_old=col_choice
                
                col_choice=get1Column(tb_choice,tb_choice.column_distribution)
                
                if hasGroupBy==1:
                    if hasOrderBy==1 \
                        and col_choice.data_type in ["int","double","float","timestamp","tinyint","bigint"]\
                            and col_choice.name in select_column_name_list:
                        self.last_sql.add(key(value="order by",type="keyword"))
                        self.last_sql.add(key(value=col_choice.name,type="colname"))
                        if descOrAsc==0:
                            self.last_sql.add(key(value="desc",type="sort"))
                        else:
                            self.last_sql.add(key(value="asc",type="sort"))
                    else:
                        pass
                else:
                    pass
                # if hasGroupBy==1 and col_choice_old.data_type=="varchar" and col_choice_old.name==col_choice.name:
                #     # 完善simple_sql
                #     if hasOrderBy==1 and col_choice.data_type!="varchar" and col_choice.data_type!="blob" and descOrAsc==0:
                #         self.last_sql.add(key(value="order by",type="keyword"))
                #         self.last_sql.add(key(value=col_choice.name,type="colname"))
                #         self.last_sql.add(key(value="desc",type="sort"))
                #     elif hasOrderBy==1 and col_choice.data_type!="varchar" and col_choice.data_type!="blob":
                #         self.last_sql.add(key(value="order by",type="keyword"))
                #         self.last_sql.add(key(value=col_choice.name,type="colname"))
                #         self.last_sql.add(key(value="asc",type="sort"))
                #     else:
                #         pass
                # else:
                #     pass
                
            # 整体思路上一阶段相似
            elif tb_num==2:
                hasJoin=True
                # 必然含有JOIN操作
                # 根据联合概率分布，不放回采样出要访问的表
                bool,tbs,tbs_sub_distribution=getNTable(dbs=dbs,n=2,pdg=np.full(len(dbs.tables),1.0/len(dbs.tables)))
                tbs_=list(tbs)
                if bool==-1:
                    print("fatal error : dbs sampled failed.")
                else:
                    self.last_sql.add(key(value="select",type="keyword"))
                    
                    has_aggregation=False
                    select_column_name_list=[]
                    
                    # 计算查询需要返回的列的数目和聚合操作的数目
                    on=rand_num_sampling(0,2,condition.averageAggregationOperatorNum)
                    if on>0:
                        has_aggregation=True

                    # print(f"on:{on}")
                    aqcn=len(condition.averageQueryColomnNum)-1
                    # qcn=rand_num_sampling(0,aqcn,[1.0/(aqcn+1) for i in range(aqcn+1)])
                    
                    qcn=rand_num_sampling(0,aqcn,condition.averageQueryColomnNum)
                    
                    if qcn==0:
                        self.last_sql.add(key(value="*",type="colname"))
                    else:
                        res=from_tb_get_N_columns_for_aggregation(tbs_,qcn)
                        n_col=[res[i] for i in range(len(res))]
                        n_col_from_tb=[res[i].father.name for i in range(len(res))]
                        for i,col in enumerate(n_col):
                            # if i<on:
                            if on!=0:
                                if col.data_type in ['varchar','bpchar','timestamp','blob']:
                                    aggregation_type=0
                                else:
                                    aggregation_type=rand_num_sampling(1,3,[1.0/3 for i in range(3)])  
                                if aggregation_type==0:
                                    tmp=f'count({n_col_from_tb[i]}.{col.name}) as count_value_{col.name}'
                                elif aggregation_type==1:
                                    tmp=f'avg({n_col_from_tb[i]}.{col.name}) as average_value_{col.name}'
                                elif aggregation_type==2:
                                    tmp=f'min({n_col_from_tb[i]}.{col.name}) as minimum_value_{col.name}'
                                elif aggregation_type==3:
                                    tmp=f'max({n_col_from_tb[i]}.{col.name}) as maximum_value_{col.name}'
                                
                                if i!=qcn-1:
                                    self.last_sql.add(key(value=tmp,type="colname_"))
                                else:
                                    self.last_sql.add(key(value=tmp,type="colname"))
                                    
                                select_column_name_list.append(f"{n_col_from_tb[i]}.{col.name}")
                            else:
                                if i!=qcn-1:
                                    self.last_sql.add(key(value=f"{n_col_from_tb[i]}.{col.name}",type="colname_"))
                                else:
                                    self.last_sql.add(key(value=f"{n_col_from_tb[i]}.{col.name}",type="colname"))
                                
                                select_column_name_list.append(f"{n_col_from_tb[i]}.{col.name}")
                                
                            # print(i.value)
                            if i!=qcn-1:
                                self.last_sql.add(key(value=",",type="dot"))

                    self.last_sql.add(key(value="from",type="keyword"))

                    self.last_sql.add(key(value=tbs_[0].name,type="tbname"))
                    self.last_sql.add(key(value=",",type="join"))
                    self.last_sql.add(key(value=tbs_[1].name,type="tbname"))
                    
                    self.last_sql.add(key(value="where",type="keyword"))
                    
                    self.last_sql.add(key(value=tbs_[0].name,type="tbname_"))
                    self.last_sql.add(key(value=".",type="dot"))
                    self.last_sql.add(key(value=tbs_[0].col[0].name,type="colname"))
                    
                    self.last_sql.add(key(value="=",type="compare"))
                    
                    self.last_sql.add(key(value=tbs_[1].name,type="tbname_"))
                    self.last_sql.add(key(value=".",type="dot"))
                    self.last_sql.add(key(value=tbs_[1].col[0].name,type="colname"))
                    
                    qc_num=rand_num_sampling(1,3,condition.queryLogicPredicateNum)
                    if qc_num>1:
                        
                        for i in range(qc_num-1):
                            if rand_num_sampling(0,1,[0.5,0.5])==0:
                                self.last_sql.add(key(value="and",type="predicate"))
                            else:
                                self.last_sql.add(key(value="or",type="predicate"))
                                hasOr=True
                            
                            tb_choice=get1Table(tbs_,tbs_sub_distribution)
                            
                            # print(len(tbs_),tbs_sub_distribution)
                            # print(tbs_[0].name)
                            # print(tbs_[1].name)
                            # print(tb_choice.name)
                            # print(self.last_sql.toStr())
                            
                            col_choice=get1Column(tb_choice,tb_choice.column_distribution)
                            
                            self.last_sql.add(key(value=tb_choice.name,type="tbname_"))
                            self.last_sql.add(key(value=".",type="dot"))
                            self.last_sql.add(key(value=col_choice.name,type="colname"))
                        
                            if col_choice.data_type in ['varchar','bpchar','blob']:
                                # print(condition.queryComparisonOperatorRatio[2:4])
                                newratio=condition.queryComparisonOperatorRatio[2:4]
                                newsum=sum(newratio)
                                # print(newsum)
                                for i,it in enumerate(newratio):
                                    newratio[i]=1.0/newsum*newratio[i]
                                # print(newratio)
                                cons=rand_num_sampling(0,1,newratio)
                                # print(col_choice.type)
                                if cons==0:
                                    self.last_sql.add(key(value="=",type="compare"))
                                elif cons==1:
                                    # self.last_sql.add(key(value="!=",type="compare"))
                                    self.last_sql.add(key(value="=",type="compare"))
                                else:
                                    pass
                                # print(col_choice.domain)
                                # data=rand_str_sampling(str_len=len(col_choice.domain[1]))
                                
                                if col_choice.data_type in ['varchar','bpchar']:
                                    data=rand_str_sampling2(min_len=col_choice.domain[0],max_len=col_choice.domain[1])
                                    self.last_sql.add(key(value="\'"+data+"\'",type="value"))
                                else:
                                    self.last_sql.add(key(value="NULL",type="value"))
                            else:  
                                cons=rand_num_sampling(0,3,condition.queryComparisonOperatorRatio)
                                if cons==0:
                                    self.last_sql.add(key(value=">",type="compare"))
                                elif cons==1:
                                    self.last_sql.add(key(value="<",type="compare"))
                                elif cons==2:
                                    self.last_sql.add(key(value="=",type="compare"))
                                elif cons==3:
                                    # self.last_sql.add(key(value="!=",type="compare"))
                                    self.last_sql.add(key(value="=",type="compare"))
                                else:
                                    pass
                                # data=rand_num_sampling(0,99,[1.0/100 for i in range(100)])
                                
                                if col_choice.data_type=="timestamp":
                                    # data=rand_timestamp_sampling(precision=col_choice.data_mod)
                                    start_ts=datetime.datetime.strptime(col_choice.domain[0],"%Y-%m-%d %H:%M:%S")
                                    end_ts=datetime.datetime.strptime(col_choice.domain[1],"%Y-%m-%d %H:%M:%S")
                                    data=rand_timestamp_sampling2(start_ts,end_ts,col_choice.data_mod)
                                    self.last_sql.add(key(value="\'"+str(data)+"\'",type="value"))
                                else:
                                    num_domain=int(col_choice.domain[1])-int(col_choice.domain[0])+1
                                    if col_choice.data_type=="numeric" and col_choice.data_mod[0]==col_choice.data_mod[1]:
                                        data=rand_decimal_sampling(col_choice.data_mod[0])
                                    else:
                                        data=rand_num_sampling(
                                            int(col_choice.domain[0]),
                                            int(col_choice.domain[1]),
                                            [1.0/num_domain for i in range(num_domain)]
                                        )
                                    self.last_sql.add(key(value=data,type="value"))
                    else:
                        pass
            else:
                pass
            
            if hasOr==True or hasJoin==True:
                self.last_sql.add(key(value="limit",type="keyword"))
                self.last_sql.add(key(value=10,type="value"))
        
        # DELETE FROM students WHERE name='John' AND age=21;
        # 写语句
        elif rw_choice==1:
            # 让插入语句和删除语句保持相对平衡，让数据库整体规模保持稳定
            insert_delete_choice=rand_num_sampling(0,1,[0.5,0.5])
            if insert_delete_choice==0:
                tb_choice=self.dbs.tables[rand_num_sampling(0,len(self.dbs.tables)-1,condition.tableDistribution)]
                self.last_sql.add(key(value="insert",type="keyword"))
                self.last_sql.add(key(value="into",type="keyword"))
                self.last_sql.add(key(value=tb_choice.name,type="tbname"))
                self.last_sql.add(key(value="values",type="keyword"))
                tmp="("
                for i in range(len(tb_choice.col)):
                    if i!=0:
                        tmp+=","
                    # 判断数据类型
                    if tb_choice.col[i].data_type in ['varchar','bpchar']:
                        # tmp+="\'"+rand_str_sampling(str_len=len(tb_choice.col[i].domain[1]))+"\'"
                        tmp+="\'"+rand_str_sampling2(min_len=tb_choice.col[i].domain[0],max_len=tb_choice.col[i].domain[1])+"\'"
                    elif tb_choice.col[i].data_type=="timestamp":                    
                        # tmp+="\'"+str(rand_timestamp_sampling(precision=tb_choice.col[i].data_mod))+"\'"
                        start_ts=datetime.datetime.strptime(tb_choice.col[i].domain[0],"%Y-%m-%d %H:%M:%S")
                        end_ts=datetime.datetime.strptime(tb_choice.col[i].domain[1],"%Y-%m-%d %H:%M:%S")
                        data=rand_timestamp_sampling2(start_ts,end_ts,tb_choice.col[i].data_mod)
                        tmp+="\'"+str(data)+"\'"
                    elif tb_choice.col[i].data_type=="blob":
                        tmp+="NULL"
                    else:
                        # 根据这一列的值域选择修改的值
                        num_domain=int(tb_choice.col[i].domain[1])-int(tb_choice.col[i].domain[0])+1
                        if tb_choice.col[i].data_type=="numeric" and tb_choice.col[i].data_mod[0]==tb_choice.col[i].data_mod[1]:
                            data=rand_decimal_sampling(tb_choice.data_mod[0])
                        else:
                            data=rand_num_sampling(
                                int(tb_choice.col[i].domain[0]),
                                int(tb_choice.col[i].domain[1]),
                                [1.0/num_domain for i in range(num_domain)]
                            )
                        tmp+=str(data)
                tmp+=")"
                self.last_sql.add(key(value=tmp,type="value"))
                # self.sql.add(key(value=";",type="end"))
            # 删除语句，思路同理
            else:
                tb_choice=self.dbs.tables[rand_num_sampling(0,len(self.dbs.tables)-1,condition.tableDistribution)]
                res=from_tb_get_N_columns_for_aggregation([tb_choice],1)
                col=res[0]
                # if col.data_type=='blob':
                while col.data_type=='blob':
                    tb_choice=self.dbs.tables[rand_num_sampling(0,len(self.dbs.tables)-1,condition.tableDistribution)]
                    res=from_tb_get_N_columns_for_aggregation([tb_choice],1)
                    col=res[0]
                else:
                    self.last_sql.add(key(value="delete",type="keyword"))
                    self.last_sql.add(key(value="from",type="keyword"))
                    self.last_sql.add(key(value=tb_choice.name,type="tbname"))
                    self.last_sql.add(key(value="where",type="keyword"))
                    
                    self.last_sql.add(key(value=col.name,type="colname"))
                    self.last_sql.add(key(value="=",type="compare"))
                    if col.data_type in ['varchar','bpchar']:
                        # self.last_sql.add(key(value="\'"+str(rand_str_sampling(len(col.domain[1])))+"\'",type="value"))
                        tmp_str_value=rand_str_sampling2(min_len=col.domain[0],max_len=col.domain[1])
                        self.last_sql.add(key(value="\'"+str(tmp_str_value)+"\'",type="value"))
                    elif col.data_type=="timestamp":
                        # tmp_date_value=rand_timestamp_sampling(precision=col.data_mod)
                        start_ts=datetime.datetime.strptime(col.domain[0],"%Y-%m-%d %H:%M:%S")
                        end_ts=datetime.datetime.strptime(col.domain[1],"%Y-%m-%d %H:%M:%S")
                        tmp_date_value=rand_timestamp_sampling2(start_ts,end_ts,col.data_mod)
                        self.last_sql.add(key(value="\'"+str(tmp_date_value)+"\'",type="value"))
                    else:
                        num_domain=int(col.domain[1])-int(col.domain[0])+1
                        if col.data_type=="numeric" and col.data_mod[0]==col.data_mod[1]:
                            data=rand_decimal_sampling(tb_choice.data_mod[0])
                        else:
                            data=rand_num_sampling(
                                int(col.domain[0]),
                                int(col.domain[1]),
                                [1.0/num_domain for i in range(num_domain)]
                            )
                        self.last_sql.add(key(value=data,type="value")) 
        else:
            print("fatal error : inner memory wrong.")
            pass
        
        self.last_sql.add(key(value=";",type="end"))
        if len(self.last_sql.token)==1:
            print(f"fatal error {rw_choice} : NULL SQL")
            print(f"insert_delete_choice : {insert_delete_choice}")
        self.sql_set.append(self.last_sql)
        return self.last_sql

    # 批量生成
    def generate_N(self, condition, outputFile):
        # print(outputFile)
        self.sql_set=[]
        # ans=list()
        for i in range(condition.workloadSize):
            self.generate(condition)
        
        # 输出生成状态
        if condition.workloadSize==len(self.sql_set):
            print("workload generation succeeded.")
            self.save(outputFile)
        else:
            print("fatal error : generation failed. Please check your schema input.")
            return

if __name__=='__main__':
    # 调用方式
    # python workloadGen.py --config_file ./input.json
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_file', type=str, default='./input.json')
    
    # config_file参数也即配置文件路径
    args = parser.parse_args()
    
    all_tables,fea,outputFile=load_json(args.config_file,'r')
    table2dist = {}
    for i in range(len(all_tables.tables)):
        table2dist[all_tables.tables[i]] = fea.tableDistribution[i]
    dbs=all_tables
    sg=SQLGen2(dbs=dbs)
    # sg.generate(condition=fea)
    # print(sg.last_sql.toStr())
    sg.generate_N(condition=fea,outputFile=outputFile)