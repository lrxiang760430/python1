import pandas as pd
df=pd.read_csv('D:/tools/chr/20230331/20230331bak.csv')
print(df)
df1=df['\tBYE消息Reason头域内容\t']
print(df1)
df1.to_csv('D:/tools/chr/20230331/20230402BYE.csv')
#
df2=
