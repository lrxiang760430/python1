import pandas as pd
#from pandas.io import sql
import pymysql
from sqlalchemy import create_engine
import time
import datetime
#engine=create_engine('10.220.247.196','root','Wbzlrx760430!','Syslog')
engine=create_engine('mysql+pymysql://root:Wbzlrx760430!@10.66.66.30:3306/radius')
sql1='SELECT * from 稿件信息'
df1=pd.read_sql_query(sql1,engine)
print(df1)

#以下执行对df1数据的去重操作

#df2=df1[['作者','题目','期刊名称及发表时间']]
#print(df2)
#以下执行对df2数据的去重操作
#显示df1的结构
df1.info()
#print(account['pppoe'].duplicated()==True)
print(df1['题名'].duplicated()==True)
#account=account.drop_duplicates(subset=['pppoe','mac'])
df1=df1.drop_duplicates(subset=['题名'])
print(df1)
#df1.to_csv('c:/tools/没有重复的稿件信息.csv')
df1.to_csv('c:/tools/没有重复的稿件信息.txt')
