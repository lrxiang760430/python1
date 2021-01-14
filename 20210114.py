import pandas as pd 
df2019=pd.read_csv(r'C:\Users\lrx\Downloads\Lily(1)\2019年下半年订单表.csv')
df2020=pd.read_csv(r'C:\Users\lrx\Downloads\Lily(1)\2020年上半年订单表.csv')


print(df2019)
print(df2020)

dfYear=pd.concat([df2019,df2020])
dfYear["下单时间"]=pd.to_datetime(dfYear["下单时间"])

dfnewYear=dfYear.set_index("下单时间")

dfSales=dfnewYear["数量"].groupby(dfnewYear["商品ID"]).resample("M").sum()

dfnewSales=dfSales.reset_index()
#print(dfYear)
dfnewSales["下单时间"]=dfnewSales["下单时间"].dt.strftime("%Y-%m")
print(dfnewSales)