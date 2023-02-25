'''

import os
#打印上级目录
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

path1=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))



'''
import pandas as pd

#df=pd.read_csv('d:/tools/sd/20230224sd4g.csv',encoding='gbk')
#在笔记本电脑上打开的路径
df=pd.read_csv('c:/tools/sd/202301山东.csv',encoding='gbk')
print(df)


#打印表头
print(df.columns)
#整行去重
df=df.drop_duplicates()
#查看整行去重后还有多少行
print(df)
#查看以'站号（E-NODEB ID）'去重还有多少行
df=df.drop_duplicates('站号（E-NODEB ID）')


print(df)
#查看以'站名'去重还有多少行
df=df.drop_duplicates('站名')
print(df)

