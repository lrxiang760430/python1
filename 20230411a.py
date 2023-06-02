import pandas as pd
df1=pd.read_csv('D:/tools/sd/202303/4g_sd.csv',sep='^')
print(df1)
df1.to_csv('D:/tools/sd/202303/4g_sdfl.csv')
df2=pd.read_csv('D:/tools/sd/202303/5g_sd.csv',sep='^')
print(df2)
df2.to_csv('D:/tools/sd/202303/5g_sdfl.csv')