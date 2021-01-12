import pandas as pd 
df=pd.read_csv(r'G:\tools\mathorcup\sphy.csv') 
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

print(df[df["order_id"]<=0])
print(df[df["user_id"]<=0])
print(df)
#print(df['price'].isin([25.00,68.00,248.00]))
print(~df['price'].isin([25.00,68.00,248.00]))
dfWrongPrice=df[~df['price'].isin([25.00,68.00,248.00])]
print(dfWrongPrice)
df.drop(index=dfWrongPrice.index,inplace=True)

dfWrongPlat=df[~df['platform'].isin(["ios","android"])]
print(dfWrongPlat)

dfWrongPay=df[~df['payment_provider'].isin(["wxpay","alipay","applepay"])]
print(dfWrongPay)

dfWrongTime=df[df['pay_time']<df['create_time']]
print(dfWrongTime)
df.drop(index=dfWrongTime.index,inplace=True)


df.info()

print(df['order_id'].duplicated())
dfOrderDu=df[df['order_id'].duplicated()]
print(dfOrderDu)
df.drop(index=dfOrderDu.index,inplace=True)
df.info()
"""
dfPayNull=df[df['payment_provider'].isnull()]
df.drop(index=dfPayNull.index,inplace=True)
df.info()
dfPlatNull=df[df['platform'].isnull()]
df.drop(index=dfPlatNull.index,inplace=True)
df.info()
"""