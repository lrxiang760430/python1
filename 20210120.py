import os
#import xlrd
import pandas as pd 
onuggl=pd.read_csv(r'G:\tools\python1\ONU设备巡检20181204A.csv',encoding='ANSI')
oltxj=pd.read_csv(r'G:\tools\python1\OLT设备巡检20181204.csv',encoding='ANSI')
onuanduser=pd.read_csv(r'G:\tools\python1\cw20200305.csv')
radius=pd.read_csv(r'G:\tools\python1\radius.csv')
boss=pd.read_csv(r'G:\tools\python1\boss.csv')
onuinfo=pd.read_csv(r'G:\tools\python1\ONU基本信息.csv')
print('ONU基本信息.csv')
print(onuinfo)


print(boss)
#客户编码      客户名称            手机号                     NAME                   帐号   带宽      产品到期时间                     地址3 REGION_NAME TOWN_NAME   ORG_NAME
print(radius)
#用户拨号账号         用户MAC
#pppoe           mac
print(onuanduser)
#"OLT IP地址","网元ID","MAC地址"
#print(onuggl)
print(onuggl.head())
#  网元ID    所属OLT名称      所属子网             网元名称            型号         MAC地址 / SN  在线状态     距离  ONU下挂用户MAC数    ONU接收OLT光功率  PON上行宽带利用率  PON下行宽带利用率

#将'ONU接收OLT光功率'中有空白的这一行删除
onuggl=onuggl.dropna(subset=['ONU接收OLT光功率'])

#去掉['MAC地址 / SN'中的":"
onuggl['MAC地址 / SN']=onuggl['MAC地址 / SN'].str.replace(":","")
#print(oltxj)
print(oltxj.head())
#局点     OLT设备类型      OLT设备IP地址 OLT设备hostname   SMC  ...             电源      风扇                                   OLT版本信息                                     OLT业务板卡类型和数量统计
onuandolt=pd.merge(onuggl,oltxj,left_on='所属OLT名称',right_on='局点')
print(onuandolt)
print(onuandolt.info())
print(onuandolt.head())

onuinfo1=pd.merge(boss,radius,left_on='帐号',right_on='pppoe')
print(onuinfo1)

onuinfo2=pd.merge(onuinfo1,onuanduser,left_on='mac',right_on='MAC地址')
print(onuinfo2)
onuinfo2.to_csv('onuinfo2.csv')


#onuinfoall=pd.merge(onuinfo2,onuinfo,left_on='OLT IP地址',right_on='OLT的IP地址')
onuinfoall=pd.merge(onuinfo2,onuinfo,left_on=['OLT IP地址','网元ID'],right_on=['OLT的IP地址','网元名称'])
print(onuinfoall)
onuinfoall.to_csv('onuinfoall1.csv')

"""
onuandolt.to_csv("onuadnolt2.csv")

onuandoltanduser=pd.merge(onuandolt,onuanduser,left_on='MAC地址 / SN',right_on='MAC地址')

print(onuandoltanduser)
print(onuandoltanduser.info())
onuandoltanduser.to_csv('onuandoltanduser.csv')

onuinfo1=pd.merge(boss,radius,left_on='帐号',right_on='pppoe')
print(onuinfo1)
onuinfo1.to_csv('onuinfo1.csv')
print(onuinfo1['MAC'])
print(onuandoltanduser['MAC地址'])
onuinfo=pd.merge(onuinfo1,onuandoltanduser,left_on='mac',right_on='MAC地址')
print(onuinfo)
onuinfo.to_csv('onuinfo.csv')
#for line in s:
#    print(line)
#onu=pd.ExcelFile(r'G:\tools\python1\ONU设备巡检20181204A.xls')
#onu=xlrd.open_workbook(r'G:\tools\python1\ONU设备巡检20181204A.xls')



#print(onuggl)
#print(onuggl.head(5))
#onuggl.info()
#查看ONU接收OLT光功率为空值的项
#print(onuggl[onuggl['ONU接收OLT光功率'].isnull()==True])
#print(onuggl.dropna(axis=0,how='any'))
#onuggl.drop(onuggl['ONU接收OLT光功率'].isnull()==True,axis=0)
#onuggl.dropna()
#print(onuggl.dropna())
#onuggl.drop(onuggl['ONU接收OLT光功率']=='NaN')
#onuggl.info()
#onu1=onuggl.dropna(axis=0,how='any')
#onu1=onuggl.drop(onuggl['ONU接收OLT光功率']=='NaN',axis=0)
#onu1=onuggl.dropna(subset=['ONU接收OLT光功率'])
#print(onu1)
#onu1.info()
"""