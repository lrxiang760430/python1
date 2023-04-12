import pandas as pd
# 显示所有列
pd.set_option('display.max_columns', None)
# # 显示所有行
pd.set_option('display.max_rows', None) 
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
#df.replace('\s+','',regex=True,inplace=True)
#df.to_csv('D:/tools/chr/20230331/20230331去掉空格.csv')

#('D:/tools/chr/20230331/20230331.csv')
#BYE原因
## # 直接筛选方法
#some = all_data[(all_data['User_id'] == 1439408) & (all_data['Date'].isna())]
#print(some)
#部分匹配
#print(df['name'].str.contains('li'))
#df1=df['\tBYE消息Reason头域内容\t'].str.contains('SIP:cause=503')
#print(df1)
#print(df[df['name'].str.contains('li')])
#print(df[df['\tBYE消息Reason头域内容\t'].str.contains('503')])
#print(df[df['\tBYE消息Reason头域内容\t'].str.contains('cause=503')])
#print(df['\tBYE消息Reason头域内容\t']='')
#df1=df['\tBYE消息Reason头域内容\t']
#df1.to_csv('D:/tools/chr/20230331/20230402cause503.csv')
#取出四列
#df1=df["	位置信息小区号	","	主叫IMPU	"]
#df1=df["	位置信息小区号	"]
df2=df["	BYE消息Reason头域内容	"]
#print(df2)
print(df)
#print(df2)
df=df.dropna
print(df)