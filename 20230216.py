import pandas as pd
print("测试在vscode中上传新建的python文件")
df=pd.read_csv('C:/tools/sd/12月份新/4g_sd.csv','^')
print(df)
df.to_csv('C:/tools/sd/12月份新/4g_sdnew.csv')