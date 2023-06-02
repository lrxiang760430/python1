import pandas as pd
# 显示所有列
#pd.set_option('display.max_columns',None)
# 显示所有行
#pd.set_option('display.max_rows',None)

#
#pd.set_option('display.max_columns', None)
df=pd.read_csv('D:/tools/chr/20230331/20230331.csv')
#通过使用nrows参数来实现读取若干行，这样可以加快程序的读取速度
#df=pd.read_csv('D:/tools/chr/20230331/20230331.csv',nrows=100)
#print(df)
#去掉空格的操作
#a.replace('\s+','',regex=True,inplace=True) 
#print(a.values)
df.replace('\s+','',regex=True,inplace=True)
df.to_csv('D:/tools/chr/20230331/20230331去掉空格.csv')