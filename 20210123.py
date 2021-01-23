import pandas as pd 
account=pd.read_csv(r'C:\tools\radius-20210122\radius-7\radius-7\78.txt',encoding='ANSI')



print(account)
print(account.head())
account.info()


#修改列名
#account.columns.str={'pppoe','a','b','c','d','e','f','g','h','i','j','k','mac','13'}
#account.rename(columns={'[{"net_no":"18302211224@zc"','pppoe'},inplace=True)
account.columns=["pppoe","1","2","3","4","5","6","7","8","9","10","11","mac","13"]
account.info()

#去掉pppoe和mac列中的无关项
account['pppoe']=account['pppoe'].str.replace('net_no','')
account['pppoe']=account['pppoe'].str.replace('[','')
account['pppoe']=account['pppoe'].str.replace('{','')
account['pppoe']=account['pppoe'].str.replace('"":"','')
account['pppoe']=account['pppoe'].str.replace('"','')
account['mac']=account['mac'].str.replace('calling_station_id:','')
account['mac']=account['mac'].str.replace('"','')
account['mac']=account['mac'].str.replace(':','')
print(account.head())

#把pppoe列中重复的项去掉
#account.dropna()
account=account.drop_duplicates(subset=['pppoe','mac'])
print(account)
#把pppoe和mac列中有空白值的去掉
account.dropna()
print(account)

#只保留pppoe和mac列
account1=account[['pppoe','mac']]
print(account1)
account1.to_csv('pppoemac23.csv')
#print(account.head())
#account=(account.columns={'pppoe','a','b','c','d','e','f','g','h','i','j','k','mac','13'})
#account=account.columns{'pppoe','a','b','c','d','e','f','g','h','i','j','k','mac','13'}
