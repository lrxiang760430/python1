import pymysql       ##PyMySQL是在 Python3.x 版本中用于连接 MySQL 服务器的一个库
import pandas as pd  ##Pandas是Python的一个数据分析包 导入panda命名为pd
from sqlalchemy import create_engine ## 导入引擎

file = r'c:/tools/sd/chr/chr20230425.csv'    ## 文件
#df = pd.read_excel(file) ## 读文件
df = pd.read_csv(file) ## 读文件
print(df)
#gd=gd[(gd.需求描述.str.contains('移网业务/投诉类/网络'))]
#df1=df["	BYE消息Reason头域内容	"].str.contains('503')
#df5=df.loc[df['\t返回SIP状态码\t'].astype(str).str.contains('65535',na=False)]


df1=df[['\t返回SIP状态码\t','\t主叫IMPU\t']]
print(df1)
#print(df5)
#b = a.split() 
#df6=df5.split()
#print(df6)
'''
#df.replace(' ' ,'')
df7=df5.replace(' ' ,'')
print(df7)
engine = create_engine("mysql+mysqlconnector://root:Wbzlrx760430!@192.168.1.78:3306/工单") ## ****代表你的数据库密码
#engine=create_engine('mysql+mysqlconnector://root:Wbzlrx760430!@localhost:3306/gd')
#df6.to_sql('20230530b',con=engine,if_exists='replace',index=False)  ##导入数据库，如果存在就替换

df1=df.loc[df['\tBYE消息Reason头域内容\t'].astype(str).str.contains('503',na=False)]
#df1=df.BYE消息Reason头域内容.str.contains('503')#print(df['	返回SIP状态码	'])
print(df['\tBYE消息Reason头域内容\t'])
print(df1)
#df1['2']=df1['\t返回SIP状态码\t'].astype(str)+df1['\t主/被叫业务请求时刻\t'].astype(str)
df2=df1['\t返回SIP状态码\t'].astype(str)+df1['\t主/被叫业务请求时刻\t'].astype(str)+df1['\t被叫振铃时刻\t'].astype(str)+df1['\t被叫应答时刻\t'].astype(str)+df1['\t通话结束时刻\t'].astype(str)+df1['\t主叫IMPU\t'].astype(str)+df1['\t被叫IMPU\t'].astype(str)+df1['\t终端型号\t'].astype(str)+df1['\t位置信息小区号\t'].astype(str)+df1['\tBYE消息Reason头域内容\t'].astype(str)
print(df2)
## 列拼接,默认是并集
#pd.concat([df1,df2],axis=1)
#df2=df.concat(['\t返回SIP状态码\t','\t主/被叫业务请求时刻\t'],axis=1)
#print(df2)

 ## 连接数据库
 #pip install mysql-connector-python 需要提前安装这个库
engine = create_engine("mysql+mysqlconnector://root:Wbzlrx760430!@192.168.1.78:3306/工单") ## ****代表你的数据库密码
#engine=create_engine('mysql+mysqlconnector://root:Wbzlrx760430!@localhost:3306/gd')
df2.to_sql('20230530a',con=engine,if_exists='replace',index=False)  ##导入数据库，如果存在就替换

'''