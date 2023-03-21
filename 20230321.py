#可以测试用python处理chr数据
import pandas as pd
#使用,作为分隔符
df=pd.read_csv('C:/tools/sd/chr/20230321/chr20230321.csv',sep=',')
#df=pd.read_csv('C:/tools/sd/chr/20230321/1679297411403_call_s_cscf_5_0.csv')
print(df)
#打印表头
print(df.columns)
#将表头存到一个csv文件中
df1=df.columns
#df1.dataframe.to_csv('20230321chr文件的表头.csv')
print(df1)
#df_data1 = pd.DataFrame(dict_data)
df2=pd.DataFrame(df)
#print('打印df2')
#print(df2)
#尝试打印到txt文件
#import sys
#import os
#df2.write
print(df['CHR消息魔术字'])
print(df["	主叫IMPU	"])
print(df["	被叫IMPU	"])
print(df["	位置信息小区号	"])

#增加去掉四个不正常的项目的操作

df=df[df["	Q850释放原因	"]!='\tNo answer from user (user alerted)\t']
print(df)
df=df[df["	Q850释放原因	"]!='\tNormal call clearing\t']
print(df)
df=df[df["	Q850释放原因	"]!='\tCall rejected\t']
print(df)
df=df[df["	Q850释放原因	"]!='\tUser busy\t']
print(df)



#学习打印出现的次数
#vc = df['state'].value_counts()
#print(vc)
#print(type(vc))
print('统计主叫号码出现的频次')
zjimpu=df["	主叫IMPU	"].value_counts()
print(zjimpu)
zjimpu.to_csv('C:/tools/sd/chr/20230321/主叫号码排序1.csv')

#print(type(zjimpu))
print('统计被叫号码出现的频次')
bjimpu=df["	被叫IMPU	"].value_counts()
print(bjimpu)
bjimpu.to_csv('C:/tools/sd/chr/20230321/被叫号码排序1.csv')

print('统计位置信息小区号出现的频次')
wzxxxqh=df["	位置信息小区号	"].value_counts()
print(wzxxxqh)
wzxxxqh.to_csv('C:/tools/sd/chr/20230321/位置信息小区号排序1.csv')
