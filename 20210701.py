import pandas as pd
import pymysql
from sqlalchemy import create_engine
import time
import datetime
engine=create_engine('mysql+pymysql://root:Wbzlrx760430!@10.66.66.30:3306/qufu pon')

#把'电视台6800'的数据赋值给df10
sql10='select * from 电视台6800'
df10=pd.read_sql_query(sql10,engine)
print(df10)
#去掉df10中的'.'
df10['MAC地址']=df10['MAC地址'].str.replace('.','')
print(df10)

#把'防山6800'的数据赋值给df11
sql11='select * from 防山6800'
df11=pd.read_sql_query(sql11,engine)
print(df11)
#去掉df11中的'.'
#account['pppoe']=account['pppoe'].str.replace('net_no','')
df11['MAC地址']=df11['MAC地址'].str.replace('.','')
print(df11)

#把radius数据赋值给df3
sql3='select * from 202178a'
df3=pd.read_sql_query(sql3,engine)
print(df3)
print(pd.merge(df11,df3,left_on='MAC地址',right_on='mac'))
df11a=pd.merge(df11,df3,left_on='MAC地址',right_on='mac')

sql2='select * from boss'
df2=pd.read_sql_query(sql2,engine)
print(df2)
df11b=pd.merge(df11a,df2,left_on='pppoe',right_on='宽带账号')

#生成csv文件
#account.to_csv('g:/tools/202178a.csv')
df11b.to_csv('d:/tools/log/qufu/防山6800.csv')










'''
sql2='select * from boss'
df2=pd.read_sql_query(sql2,engine)
print(df2)
sql3='select * from 202178a'
df3=pd.read_sql_query(sql3,engine)
print(df3)
#sql2='UPDATE "防山6800" SET "MAC地址"=replace("MAC地址",".","")'
#sql2='UPDATE `电视台6800` SET `MAC地址`=replace(`MAC地址`,'.','')'
#df2=pd.read_sql_query(sql2,engine)
#sql2='UPDATE "陵城6800-1" SET "MAC地址"=replace("MAC地址",".","")'
#df2=pd.read_sql_query(sql2,engine)
#print(df2)
df10.to_csv('d:/tools/log/qufu/防山6800.csv')
'''
