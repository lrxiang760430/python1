import pandas as pd
import pymysql
from sqlalchemy import create_engine
import time
import datetime
#engine=create_engine('10.220.247.196','root','Wbzlrx760430!','Syslog')
engine=create_engine('mysql+pymysql://root:Wbzlrx760430!@10.220.247.196:3306/study')

sql1='select * from 收费关联户电费查询3月'
df1=pd.read_sql_query(sql1,engine)
print(df1)
df1.to_csv('d:/tools/log/wens03.csv')


sql2='select * from 收费关联户电费查询4月'
df2=pd.read_sql_query(sql2,engine)
print(df2)
df2.to_csv('d:/tools/log/wens04.csv')


sql3='SELECT `收费关联户电费查询3月`.D,`收费关联户电费查询3月`.O,`收费关联户电费查询4月`.O FROM `收费关联户电费查询3月` ,`收费关联户电费查询4月` WHERE `收费关联户电费查询3月`.D = `收费关联户电费查询4月`.D AND `收费关联户电费查询4月`.o> `收费关联户电费查询3月`.O'
df3=pd.read_sql_query(sql3,engine)
print(df3)
df3.to_csv('d:/tools/log/wens0303.csv')