import pandas as pd
t1000=pd.read_csv(r'C:\tools\1000w.csv')
print(t1000)
"""
#下面开始数据清洗过程
#查看有缺失值的行数
#查看行内是否有空值
t1000.isnull().any(axis=1)
print(t1000.isnull().any(axis=1))
#df.isnull().sum(axis=1)   #所有列的空值

#print(f'出现空值的行数:{t1000.isnull().sum(axis=1)}')
print(t1000.isnull().sum(axis=1))
t1000.info()
#df.info()可以计算空值的个数，也可以查看是否有空值
#df.isnull().any()或者df.isnull().T.any()同样可以查看是否有空值，df.isnull().any()查看列空值，df.isnull().T.any()查看行空值
print('t1000.isnull().T.any')
print(t1000.isnull().T.any)
#计算某列的空值个数

#df['坐落地址'].isnull.sum()
print(t1000['上行业务量GB'].isnull().sum)
"""
t1000['上行业务量GB'].isnull().sum
print(t1000['上行业务量GB'].isnull().sum)
#根据数据决定是否删掉有数据缺失的行
#判断是否有异常值
#删除异常值
#查看有多少行重复的
#删除重复行
