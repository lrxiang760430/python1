import pandas as pd 
import datetime
#pd.apply()
df_test=pd.read_csv(r'G:\tools\mathorcup\NS_new.csv')
print(df_test)

#用来计算日期差的包
def dataInterval(data1,data2):
    d1=datetime.datetime.strptime(data1,"%Y-%m-%d")
    d2=datetime.datetime.strptime(data2,"%Y-%m-%d")
    delta=d1-d2
    return delta.days

#用来计算日期间隔天数的调用的函数
def getInterval(arrLike):
    PublishedTime=arrLike['PublishedTime']
    ReceivedTime=arrLike['ReceivedTime']
    days=dataInterval(PublishedTime.strip(),ReceivedTime.strip())
    return days

df_test["TimeInterval"]=df_test.apply(getInterval,axis=1)
df_test.head()
print(df_test.head())
