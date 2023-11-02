from Parserbase import *

# 辅助配置工具
class WP2(WP):
    def __init__(self) -> None:
        self.dbs=None
        pass
    
    # 负载分析函数
    def parse_workload(self,workload_path):
        # 若dbs未加载完成，则分析提前退出
        if self.dbs==None:
            print("fatal error: dbs not initialization correctly.")
            return
        # dbs正确加载
        else:
            read_cnt=0
            write_cnt=0
            predicate_num=0
            group_by_num=0
            order_by_num=0
            aggr_num=0
            
            tbl_dict={}
            tbl_col_dict={}
            # dict[tbl_name][col_name]=col_cnt
            
            # 设置输出窗口环境，显示全部信息
            pd.set_option('max_colwidth',-1)
            df = pd.read_csv(workload_path, header=None,error_bad_lines=False,sep = r'\s+\n',index_col=0) 
            # df=pd.read_csv("seats_workload.txt",header=None)
            
            tokens=""
            for i in df.index.values:
                tokens+=i
                tokens+=" "
        
            # 使用正则表达式切割分词
            sql_list=re.split('[\s]*;[\n]*[\s]*',tokens)
            # token_list=re.split(r'[\(,;\s\)\n\t]+',tokens)
            # print(sql_list[-3:])
            for i in range(len(sql_list)):
                import psqlparse
                if sql_list[i]=="" or sql_list[i]==' ':
                    continue
                # print("i: ",sql_list[i])
                real_tb_used=psqlparse.parse(sql_list[i]+";")[0].tables()
                # print(real_tb_used)
                for table_name in real_tb_used:
                    if table_name not in tbl_dict.keys():
                        tbl_dict[table_name]=1
                        tbl_col_dict[table_name]={}
                        tb_tmp=self.dbs.getTableByName(table_name)
                        # print(table_name)
                        for it in tb_tmp.col:
                            tbl_col_dict[table_name][it.name]=0
                    else:
                        tbl_dict[table_name]+=1
                
                simple_sql_token_list=re.split(r'[\(,;\s\)\n\t]+',sql_list[i])
                if simple_sql_token_list.__contains__("")==True:
                    simple_sql_token_list.remove("")
                # print(simple_sql_token_list)
                cnt_bool=False
                # 统计语义特征信息
                for id,j in enumerate(simple_sql_token_list):
                    if cnt_bool==False:
                        if j.upper()=='SELECT':
                            read_cnt+=1
                            cnt_bool=True
                        if j.upper()=='UPDATE' or j.upper()=='INSERT':
                            write_cnt+=1
                            cnt_bool=True
                    
                    if j.upper()=='AND' or j.upper()=='OR' or j.upper()=="WHERE":
                        predicate_num+=1
                    elif j.upper()=='GROUP' and simple_sql_token_list[id+1].upper()=="BY":
                        group_by_num+=1
                    elif j.upper()=='ORDER' and simple_sql_token_list[id+1].upper()=="BY":
                        order_by_num+=1
                    elif j.upper()=="SUM" or j.upper()=="MIN" or j.upper()=="MAX" or j.upper()=="AVG":
                        aggr_num+=1
                    else:
                        # if j=='supplier':
                        #     print(simple_sql_token_list[id-1:id+5])
                        pass
                        
                # 统计访问数据
                for token in simple_sql_token_list:
                    for tb_tmp in real_tb_used:
                        for col_tmp in tbl_col_dict[tb_tmp].keys():
                            if token==col_tmp:
                                # print("table_name : ",tb_tmp,"col_name : ",col_tmp)
                                tbl_col_dict[tb_tmp][col_tmp]+=1
                    tmp_res=re.match(".+\..+",token)
                    if tmp_res!=None:
                        # print(tmp_res.group().split("."))
                        if tmp_res.group().split(".")[0] in real_tb_used:
                            # print(tmp_res.group().split()[0],tmp_res.group().split()[1])
                            tbl_col_dict[tmp_res.group().split(".")[0]][tmp_res.group().split(".")[1]]+=1
        maxi=""
        maxv=0
        mini=""
        minv=100000000    
        sumv=0            
        # 计算极端值
        
        for table in self.dbs.tables:
            if table.name not in tbl_dict.keys():
                tbl_dict[table.name]=0
                tbl_col_dict[table.name]={}
                for it in table.col:
                    tbl_col_dict[table.name][it.name]=0
            
        for i in list(tbl_dict.keys()):
            sumv+=tbl_dict[i]
            if tbl_dict[i]>maxv:
                maxv=tbl_dict[i]
                maxi=i
            if tbl_dict[i]<minv:
                minv=tbl_dict[i]
                mini=i
                
        # 输出分析信息到终端
        print("type of workload :",workload_path)
        # print("total token num :",len(token_list))
        print("sample SQL1:",re.split(r'[,;\s\n\t\(\)]+',str(df.iloc[0].name)))
        print("sample SQL2:",re.split(r'[,;\s\n\t\(\)]+',str(df.iloc[1].name)))
        print("size of workload :",tokens.count(";"))
        print("read write ratio : "+str(read_cnt)+"|"+str(write_cnt)+"  "+str(read_cnt/(write_cnt+read_cnt)))
        print("group by ratio : "+str(group_by_num/(write_cnt+read_cnt)))
        print("order by ratio : "+str(order_by_num/(write_cnt+read_cnt)))
        print("aggregation ratio : "+str(aggr_num/(write_cnt+read_cnt)))
        print("average predicate num per SQL :",str(predicate_num/(read_cnt+write_cnt)))
        print("max visited table :",maxi,str(maxv/sumv))
        print("min visited table :",mini,str(minv/sumv))
        print("table access pattern :")
        # tbl_dict记录了各个表和列的访问模式
        for i in tbl_dict:
            print("\t",i,str(tbl_dict[i])+"|"+str(sumv),"\t",tbl_dict[i]/sumv)
            tmp_sum=0
            for j in tbl_col_dict[i]:
                tmp_sum+=tbl_col_dict[i][j]
            if tmp_sum==0:
                continue
            for j in tbl_col_dict[i]:
                # print('\t',j)
                print("\t\t",j,str(tbl_col_dict[i][j])+"|"+str(tmp_sum),"\t",tbl_col_dict[i][j]/tmp_sum)
        print()
        
import psqlparse
import argparse

if __name__=='__main__':
    # 调用方式
    # python workloadGen.py --config_file ./input.json
    
    # argparse设置参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--workload_file', type=str, default='./input.json')
    parser.add_argument('--config_file', type=str, default='./input.json')
    args = parser.parse_args()
    
    files=[args.workload_file]
    
    wp=WP2()
    wp.parse_schema(args.config_file)
    # print(wp.dbs.toStr())
    # print(wp.dbs.getTableByName('lineitem'))
    # print(type(wp.dbs.getTableByName('lineitem').col))
    # 对files中的文件进行分析
    for i in files:
        print(i)
        wp.parse_workload(i)