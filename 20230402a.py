import pandas as pd
df=pd.read_csv('D:/tools/20230401位置信息小区号.csv')
df.replace('\s+','',regex=True,inplace=True)
print(df)
df.to_csv('D:/tools/chr/20230331/20230402位置信息小区号a.csv')