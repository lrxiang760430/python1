#20210207.py
import pandas as pd
import pymysql
from sqlalchemy import create_engine
#engine=create_engine('10.66.66.7','root','Wbzlrx760430!','Syslog')
engine=create_engine('mysql+pymysql://root:Wbzlrx760430!@10.66.66.7:3306/Syslog')
sql="SELECT * FROM SystemEvents WHERE FromHost LIKE 'nongwang_zubo'"
df=pd.read_sql_query(sql,engine)
print(df)
df.to_csv('nw0207.csv')