
import pandas as pd 
df=pd.read_csv(r'c:\tools\视频会员订单数据源.csv') 
print (df)

df["price"]=df["price"]/100

print (df)

df['create_time']=pd.to_datetime(df['create_time'])
print(df)
df['pay_time']=pd.to_datetime(df['pay_time'])
print(df)
df.info()

print(df['payment_provider'].isnull())
df.info()

df['platform'].fillna("unknown",inplace=True)
df.info()
"""
dfPayNull=df[df['payment_provider'].isnull()]

df.drop(index=dfPayNull.index,inplace=True)

df.info()

dfPlatNull=df[df['platform'].isnull()]

df.drop(index=dfPlatNull.index,inplace=True)

df.info()

"""