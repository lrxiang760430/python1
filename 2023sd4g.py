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
df1=df.drop_duplicates()
#查看整行去重后还有多少行
print(df1)
print('以上是整行去重后得到的行数')

#查看以'站号（E-NODEB ID）'去重还有多少行
df2=df.drop_duplicates('站号（E-NODEB ID）')
print(df2)
print('以上是以站号（E-NODEB ID）去重')

#查看以'站名'去重还有多少行
df3=df.drop_duplicates('站名')
print(df3)
print('以上是以站名去重')

#下面开始以经纬度去重
#首先完成经纬度的合并
#这个是之前编写的代码
#df['经纬度']=df['扇区经度'].map(str)+' '+df['扇区纬度'].map(str)
df['经纬度']=df['经度'].map(str)+' '+df['纬度'].map(str)
#打印
print(df)
print(df.columns)
print('以上看看是否有合并后的经纬度了')
df4=df.drop_duplicates('经纬度')
print(df4)
print('以上显示以经纬度去重后的数量')
#根据TAC去重 跟踪区码（TAC）
df=df.drop_duplicates('跟踪区码（TAC）')
print(df)
print('以上显示以跟踪区码（TAC）去重后的数量')