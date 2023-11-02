## shap-final.py使用方法
* 第一行with代码中，前两个文件是调优过程（蒲照给我）的文件：第一个文件records是调优过程中记录的各组参数取值和对应的吞吐量。第二个文件knobs-40.json包含了使用了多少个参数以及这些参数的名字。
* 第一行with代码中，最后一个文件shap_result.json是我传给mapping（简浩然）的文件，包含了使用第二个文件中的记录得到的这些参数的最新排名。
* knobsname按顺序存储这些参数的名字，eachturn_knobs_value是record中每一条记录中各个参数的值构成的数组，knobs_value最终是由多个turn_knobs_value数组构成的数组。
* df把knobs_value装换为dataframe，df_target把throughput转换为nparray
* 之后把df作为X，把吞吐量tps构成的数组df_target作为y，传入xgboost拟合，然后用shap进行解释分析得到最终的排名。
* knobsort函数得到每个参数的shapley value的绝对值之和，最终参数的shapley value的绝对值之和越大，参数排名越高。排名后的数组是result_dict，将result_dict写入json文件，最终的排名文件存在shap_result.json文件中。

## 读取数据的文件路径和写入结果的文件路径设置好后，直接执行getshapvalues()函数即可。