#20210207.py
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import time
import datetime
#engine=create_engine('10.66.66.7','root','Wbzlrx760430!','Syslog')
engine=create_engine('mysql+pymysql://root:Wbzlrx760430!@10.66.66.7:3306/Syslog')

sql='select * from SystemEvents WHERE FromHost LIKE "jining_zubo"'
df=pd.read_sql_query(sql,engine)
print(df)
df.to_csv('c:/tools/log/jining.csv')

localtime=time.localtime(time.time())
print(localtime)
newtime=time.asctime(localtime)
print(newtime)
#print datetime.now()
str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #获取当前时间并转化成字符串
print (str)
str1='c:/tools/log/jining'+str[0:10]+'.csv'
print(str1)
#
df.to_csv(str1)
"""
#jining_zubo
sql1='SELECT * FROM SystemEvents WHERE FromHost LIKE "jining_zuboo" and Message like "%%attack%%"'
#ChengWang_ZuBo 城网
sql2='SELECT * FROM SystemEvents WHERE FromHost LIKE "ChengWang_ZuBo" and Message like "%%attack%%"'
#nongwang_zubo 农网
sql3='SELECT * FROM SystemEvents WHERE FromHost LIKE "nongwang_zubo" and Message like "%%attack%%"'
#yanzhou7706 兖州
sql4='SELECT * FROM SystemEvents WHERE FromHost LIKE "yanzhou7706" and Message like "%%attack%%"'
#Qfgd_Core_S7706 曲阜

#sishui_zubo 泗水
#ZCGD-S7712-1
sql6='SELECT * FROM SystemEvents WHERE FromHost LIKE "ZCGD-S7712-1" and Message like "%%attack%%"'
#weishan_zubo 微山
#jiaxiang_zubo 嘉祥
#jinxiang_zubo 金乡
#yutai_zubo 鱼台
#liangshan_zubo 梁山
#wenshang_zubo 汶上
#sql='SELECT * FROM SystemEvents WHERE FromHost LIKE "ChengWang_ZuBo" and Message like "%%attack%%"'
#ChengWang_ZuBo
#df2=pd.read_sql_query(sql,engine)
df1=pd.read_sql_query(sql1,engine)
print(df1)
df2=pd.read_sql_query(sql2,engine)
print(df2)
df3=pd.read_sql_query(sql3,engine)
print(df3)
df3.to_csv('nw0208attack.csv')
df6=pd.read_sql_query(sql6,engine)
print(df6)
#print(df2)
#df2.to_csv('\tools\log\cw0208attack.csv')
#df2.to_csv('cw0208attack.csv')
df1.to_csv('c:/tools/log/sgs0208attack.csv')
df2.to_csv('c:/tools/log/cw0208attack.csv')
df3.to_csv('c:/tools/log/nw0208attack.csv')
df6.to_csv('c:/tools/log/zc0208attack.csv')
"""