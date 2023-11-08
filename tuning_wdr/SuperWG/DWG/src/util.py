from typing import get_type_hints
from functools import wraps
from inspect import getfullargspec
import numpy as np
import random
import datetime

# 定义函数参数类型的检查函数
def parameter_check(obj, **kwargs):
    hints = get_type_hints(obj)
    for label_name, label_type in hints.items():
        # print(label_name)
        # print(label_type)
        # 返回类型不检查 跳过 只检查实际传入参数的类型是否正确
        if label_name == "return":
            continue
        # 判断实际传入的参数是否与函数标签中的参数一致
        if not isinstance(kwargs[label_name], label_type):
            print(f"参数：{label_name} 类型错误 应该为：{label_type}")

# 使用装饰器进行函数包裹
def wrapped_func(decorator):
    @wraps(decorator)
    def wrapped_decorator(*args, **kwargs):
        func_args = getfullargspec(decorator)[0]
        kwargs.update(dict(zip(func_args, args)))
        parameter_check(decorator, **kwargs)
        return decorator(**kwargs)
    return wrapped_decorator

# 测试函数1
@wrapped_func
def add0(a: int, b: int) -> int:
    return a + b

# 测试函数2
@wrapped_func
def add1(a: int, b: float = 520.1314) -> float:
    return a + b

# 蒙特卡洛采样法的简单实现
# 根据概率分布图，在[l,r]之间进行概率采样，返回采样结果
# 参数说明：l为区间左端点，r为区间右端点，pdg为概率分布列表
def rand_num_sampling(l,r,pdg):
    # 先检查概率分布图和区间是否对应
    if r-l+1 != len(pdg):
        print("l is "+str(l)+" r is "+str(r)+" and pdg is "+str(pdg))
        print("error : pdg not match [l,r]")
        return l-1
    one_=sum(pdg)
    
    # 检查概率分布和是否为1
    if abs(one_-1.0)>1e-5:
        print("error : probability sum "+str(one_)+" do not equal 1")
        return l-1
    pdg_=np.array(pdg)
    pdg_=[round(i*10000000) for i in pdg_]
    maxv=sum(pdg_)
    num=random.randint(0,maxv-1)
    index=0
    for i in range(len(pdg_)):
        num=num-pdg_[i]
        if num<0:
            index=i
            break
    # 返回采样值
    return l+index

# 随机字符串生成
# str_len代表生成长度
def rand_str_sampling(str_len=16):
    random_str =''
    base_str ='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length =len(base_str) -1
    
    for i in range(str_len):
        random_str +=base_str[random.randint(0, length)]
    return random_str

def rand_str_sampling2(min_len=16,max_len=16):
    real_len=rand_num_sampling(min_len,max_len,np.full(max_len-min_len+1,1.0/(max_len-min_len+1)))
    return rand_str_sampling(real_len)

def rand_timestamp_sampling(precision=0):
    # 获取当前时间
    current_time = datetime.datetime.now()

    # 生成随机的年份、月份、日期、小时、分钟和秒数
    year = random.randint(1970, current_time.year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # 假设每个月最大为28天
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    
    # 生成随机的微秒数
    microsecond = random.randint(0, 999999)
    # 根据精度截断微秒数
    microsecond = microsecond // (10 ** (6 - precision))
    # 创建时间戳
    timestamp = datetime.datetime(year, month, day, hour, minute, second, microsecond)
    return timestamp

def rand_timestamp_sampling2(timestamp1, timestamp2, precision=0):
    # 获取两个时间戳之间的时间差
    time_diff = (timestamp2 - timestamp1).total_seconds()
    # 生成一个随机的时间差（秒数）
    random_seconds = random.uniform(0, time_diff)
    # 创建一个时间间隔对象，以便添加到timestamp1
    time_interval = datetime.timedelta(seconds=random_seconds)
    # 添加时间间隔以生成随机时间戳
    random_timestamp = timestamp1 + time_interval
    # 根据精度截断微秒数
    microsecond = random_timestamp.microsecond // (10 ** (6 - precision))
    random_timestamp = random_timestamp.replace(microsecond=microsecond)

    return random_timestamp

# 生成一个小于1的浮点数
# 专门处理numeric类型的生成
def rand_decimal_sampling(precision):
    if precision==0:
        return 0
    rand_int=rand_num_sampling(0,10**precision-1,np.full(10**precision,1.0/(10**precision)))
    return rand_int/(10**precision)