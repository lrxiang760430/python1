import pymysql ##PyMySQL是在 Python3.x 版本中用于连接 MySQL 服务器的一个库
import pandas as pd##Pandas是Python的一个数据分析包 导入panda命名为pd
from sqlalchemy import create_engine ## 导入引擎

file = r'c:/tools/chr/20230530.csv'## 文件
#df = pd.read_excel(file) ## 读文件
df = pd.read_csv(file) ## 读文件
print(df)
#gd=gd[(gd.需求描述.str.contains('移网业务/投诉类/网络'))]
#通过" BYE消息Reason头域内容 "里面有503，把掉话的记录筛选出来
df=df.loc[df['\tBYE消息Reason头域内容\t'].astype(str).str.contains('503',na=False)]
#df5=df.loc[df['\t返回SIP状态码\t'].astype(str).str.contains('65535',na=False)]

df5=df[['\t返回SIP状态码\t','\t主叫IMPU\t']]
print(df5)
#employees_df["Age"]=employees_df["Age"].apply(str)
#把df5里面的表头转换成字符
df5['\t返回SIP状态码\t']=df5['\t返回SIP状态码\t'].apply(str)
df5['\t主叫IMPU\t']=df5['\t主叫IMPU\t'].apply(str)
#然后把df5表头里面的‘\t’去掉，生成新的列
df5['返回SIP状态码']=df5['\t返回SIP状态码\t'].replace('\t','')
df5['主叫IMPU']=df5['\t主叫IMPU\t'].replace('\t','')
#df5['\t返回SIP状态码\t'] = df5['\t返回SIP状态码\t'].apply(lambda _: str(_))
print(df5)
#df5['\t主叫IMPU\t'] = df5['\t主叫IMPU\t'].apply(lambda _: str(_))
print(df5)
#df5=df5.replace('   ','')
print(df5)
#只取我们需要的列（即列名中不带‘\t’）
df6=df5[['返回SIP状态码','主叫IMPU']]
print(df6)
#df6=df6.strip()
#df6=df6.str.strip()
#df5['\t返回SIP状态码\t']=df5['\t返回SIP状态码\t'].str.strip()
#df5=re.sub


#print(re.sub('\s|\t|\n','',df5['\t主叫IMPU\t']))

#print(type(object))
#print(type(df5))

#engine = create_engine("mysql+mysqlconnector://root:Wbzlrx760430!@192.168.1.78:3306/工单") ## ****代表你的数据库密码
engine=create_engine('mysql+mysqlconnector://root:Wbzlrx760430!@localhost:3306/工单')
df6.to_sql('20230530b',con=engine,if_exists='replace',index=False)  ##导入数据库，如果存在就替换