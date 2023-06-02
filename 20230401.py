import pandas as pd
# 显示所有列
pd.set_option('display.max_columns',None)
# 显示所有行
pd.set_option('display.max_rows',None)

#
pd.set_option('display.max_columns', None)
df=pd.read_csv('D:/tools/chr/20230331/20230331.csv',nrows=10000)
df.to_csv('D:/tools/chr/20230331/20230401a10000.csv')