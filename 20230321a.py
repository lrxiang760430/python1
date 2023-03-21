#可以测试用python处理chr数据
import pandas as pd
#使用,作为分隔符
#df=pd.read_csv('C:/tools/sd/chr/20230321/chr20230321.csv',sep=',')
df=pd.read_csv('C:/tools/sd/chr/20230321/1679297411403_call_s_cscf_5_0.csv')
print(df)
#先学习打印"	Q850释放原因	"这一列
# df=df["	Q850释放原因	"]='Normal call clearing	'
print(df["	Q850释放原因	"])


'''''
df1=df["	Q850释放原因	"]
df1.to_csv('C:/tools/sd/chr/20230321/Q850释放原因.csv')
#"	Normal, unspecified	"
df=df[df["	Q850释放原因	"]!='Normal call clearing']
print(df)
df=df[df["	Q850释放原因	"]!='Call rejected']
print(df)
df=df[df["	Q850释放原因	"]!='"	Normal, unspecified	"']
print(df)
df=df[df["	Q850释放原因	"]!='No answer from user (user alerted)']
print(df)
df.to_csv('C:/tools/sd/chr/20230321/Q850释放原因1.csv')
'''''
#df=df[df["	Q850释放原因	"]!='\t255\t']
#print(df)
df=df[df["	Q850释放原因	"]!='\tNo answer from user (user alerted)\t']
print(df)
df=df[df["	Q850释放原因	"]!='\tNormal call clearing\t']
print(df)
df=df[df["	Q850释放原因	"]!='\tCall rejected\t']
print(df)
df=df[df["	Q850释放原因	"]!='\tUser busy\t']
print(df)
