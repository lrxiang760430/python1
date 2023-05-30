#20230322
#通过这个程序把2023年1月份的4G 5G工参数据进行分列，并再存为csv文件
import pandas as pd
df1=pd.read_csv('C:/tools/sd/2023年1月份/4g_sd.csv',sep='^')
print(df1)
df1.to_csv('C:/tools/sd/2023年1月份/4g_sd_fl.csv')
#df2=pd.read_csv('C:/tools/sd/2023年1月份/5g_sd.csv',sep='^')
#print(df2)
#df2.to_csv('C:/tools/sd/2023年1月份/5g_sd_fl.csv')

#下面开始尝试进行十进制至十六进制的转换
print(df1.columns)
#print(df2.columns)

#打印 '基站ID（10进制）'
print(df1['基站ID（10进制）'])

#直接这样写，会出这样的错误提示'Series' object cannot be interpreted as an integer
#df1['基站ID（16进制）']=int(df1['基站ID（10进制）'])
#print(df1['基站ID（16进制）'])
#换个思路，单独把'基站ID（10进制）'和
