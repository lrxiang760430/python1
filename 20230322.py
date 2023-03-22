#20230322
#通过这个程序把2023年1月份的4G 5G工参数据进行分列，并再存为csv文件
import pandas as pd
df1=pd.read_csv('C:/tools/sd/2023年1月份/4g_sd.csv',sep='^')
print(df1)
df1.to_csv('C:/tools/sd/2023年1月份/4g_sd_fl.csv')
df2=pd.read_csv('C:/tools/sd/2023年1月份/5g_sd.csv',sep='^')
print(df2)
df2.to_csv('C:/tools/sd/2023年1月份/5g_sd_fl.csv')