import pandas as pd
# 显示所有列
pd.set_option('display.max_columns',None)
# 显示所有行
pd.set_option('display.max_rows',None)

#
pd.set_option('display.max_columns', None)
#df=pd.read_csv('D:/tools/chr/20230331/20230331.csv')
#通过使用nrows参数来实现读取若干行，这样可以加快程序的读取速度
df=pd.read_csv('D:/tools/chr/20230331/20230331.csv',nrows=100)
#print(df)
#去掉空格的操作
#a.replace('\s+','',regex=True,inplace=True) 
#print(a.values)
df.replace('\s+','',regex=True,inplace=True)
print(df)
print(df.columns)
print(list(df))
#看一下是否空都去掉了
df.to_csv('D:/tools/chr/20230331/20230402.csv')
'''''
#np.set_printoptions(threshold=np.inf) # 加上这一句
#df.to_csv('D:/tools/chr/20230331/20230331a10000.csv')
#print(df[	主叫IMPU	])
df1=df.columns
#print(df1,file='D:/tools/chr/20230331/20230331jj.csv')
#print(df["	主叫IMPU	"])
df1=df["	主叫IMPU	"]
#print(df1.value_counts())


df1a=df1.value_counts();
df1a.to_csv('D:/tools/chr/20230331/20230401主叫.csv')
print(df1a)
df2=df["	被叫IMPU	"]
print(df2)
df2a=df2.value_counts()
print(df2a)
df2a.to_csv('D:/tools/chr/20230331/20230401被叫.csv')

df3=df["	位置信息小区号	"]
print(df3)
df3a=df3.value_counts()
print(df3a)
df3a.to_csv('D:/tools/chr/20230331/20230401位置信息小区号.csv')

'''