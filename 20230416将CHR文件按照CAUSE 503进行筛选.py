import pandas as pd
df=pd.read_csv('D:/tools/chr/20230416/20230416.csv')
print(df)
#print(df['name'].str.contains('li'))
#print(df[df['name'].str.contains('li')])
#df1=df["	BYE消息Reason头域内容	"].str.contains('503')
#print(df1)
#df = df.loc[df["列名"].str.contains("需要筛选的字符串", na=False),:]
df=df[df["	BYE消息Reason头域内容	"].str.contains('503',na=False)]
print(df)
df.to_csv('D:/tools/chr/20230416/chr20230416.csv')