import pandas as pd
df=pd.read_csv('D:/tools/chr/20230412/20230412.csv')
print(df)
#print(df['name'].str.contains('li'))
#print(df[df['name'].str.contains('li')])
#df1=df["	BYE消息Reason头域内容	"].str.contains('503')
#print(df1)
#df = df.loc[df["列名"].str.contains("需要筛选的字符串", na=False),:]
df=df[df["	BYE消息Reason头域内容	"].str.contains('503',na=False)]
print(df)
df1=df["	BYE消息Reason头域内容	"]
print(df1)
df2=df["	终端型号	"]
print(df2)
df12=df1+df2
print(df12)
#df12.to_csv('D:/tools/chr/20230412/20230412ab.csv')
df3=df["	主叫IMPU	"]
print(df3)
df4=df["	被叫IMPU	"]
print(df4)
df1234=df1+'^'+df2+'^'+df3+'^'+df4
print(df1234)
df1234.to_csv('D:/tools/chr/20230412/20230413abcd.csv')