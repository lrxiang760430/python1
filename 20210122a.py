import pandas as pd 
account=pd.read_csv(r'H:\tools\radius-7\radius-7\78.txt',encoding='ANSI')
print(account)
print(account.head())
account.info()
account.columns=['pppoe','1','2','3','4','5','6','7','8','9','10','11','mac','13']
account.info()

#去掉pppoe和mac列中的无关字符，只保留帐号和MAC地址
#onuggl['MAC地址 / SN']=onuggl['MAC地址 / SN'].str.replace(":","")
account['pppoe']=account['pppoe'].str.replace('net_no','')
account['pppoe']=account['pppoe'].str.replace('[','')
account['pppoe']=account['pppoe'].str.replace('{','')
account['pppoe']=account['pppoe'].str.replace('"":"','')
account['pppoe']=account['pppoe'].str.replace('"','')
account['mac']=account['mac'].str.replace('calling_station_id:','')
account['mac']=account['mac'].str.replace('"','')
account['mac']=account['mac'].str.replace(':','')

#"":"
print(account.head())

#下面进行去重操作
account.info()

print(account['pppoe'].duplicated()==True)

#account=account['pppoe'].drop_duplicates()
account=account.drop_duplicates(subset=['pppoe','mac'])
print(account)

account1=account[['pppoe','mac']]
print(account1)

#去掉pppoe和mac里面有空值的行
account1=account1.dropna()
print(account1)

account1.to_csv('account20210122a.csv')

"""

#[{"net_no":"8370810395886945@zc"  acct_terminate_cause:"2"   acct_output_octets:"329536152"  ...  nas_ip:"1.2.3.4"  calling_station_id:"40:16:9f:24:36:35"    acct_output_packets:"329849"}]

#给包含用户帐户和MAC地址的这两列改列名
account.rename(columns={'[{"net_no":"8370810395886945@zc"','pppoe'})

#account.to_csv('account.csv')

"""