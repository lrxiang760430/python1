import pandas as pd
df=pd.read_excel('c:/tools/sd/工作簿2.xls')
print(df)
df.to_csv('c:/tools/sd/20230306chr.csv')