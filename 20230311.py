#利用python处理日志文件
import pandas as pd
df=pd.read_excel('c:/tools/logcl/02UDM鉴权成功率20230311065421_20230311065457a.xls') 
print(df)
#打印表头
print(df.columns)
#删除前几行
#df.drop(df.tail(n).index) #从尾部去掉 n 行
#df.dorp(df.head(n).index) #从头去掉 n 行
#尝试一下删除前6行
df1=df.drop(df.head(6).index)
#打印看一下效果
print(df1)
print(df1.columns)
