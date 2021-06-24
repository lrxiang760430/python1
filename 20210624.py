import pandas as pd 
import datetime
starttime=datetime.datetime.now()
#account=pd.read_csv(r'c:\tools\account20210622.txt')
#account20210622
account=pd.read_csv(r'G:\tools\logfile8\logfile20210622-0522\78a.txt')
print(account)
print(account.head())

account=account[['pppoe','mac']]
print(account.head())

#去掉pppoe和mac列中的无关字符，只保留帐号和MAC地址

account['pppoe']=account['pppoe'].str.replace('net_no','')
account['pppoe']=account['pppoe'].str.replace('[','')
account['pppoe']=account['pppoe'].str.replace('{','')
account['pppoe']=account['pppoe'].str.replace('"":"','')
account['pppoe']=account['pppoe'].str.replace('"','')
account['mac']=account['mac'].str.replace('calling_station_id:','')
account['mac']=account['mac'].str.replace('"','')
account['mac']=account['mac'].str.replace(':','')


print(account.head())

#下面进行去重操作
account.info()

print(account['pppoe'].duplicated()==True)

#account=account['pppoe'].drop_duplicates()
account=account.drop_duplicates(subset=['pppoe','mac'])
print(account)

#去掉pppoe和mac里面有空值的行
account=account.dropna()
print(account)

#生成csv文件
account.to_csv('g:/tools/202178a.csv')
endtime=datetime.datetime.now()
#print(endtime - starttime)
print (endtime - starttime)


'''
account1=account[['pppoe','mac']]
print(account1)

#去掉pppoe和mac里面有空值的行
account1=account1.dropna()
print(account1)

account1.to_csv('c:\tools\202178a.csv')
'''