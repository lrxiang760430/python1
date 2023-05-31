#print(datetime.date.today())
import datetime
import time
import os
from openpyxl import load_workbook,Workbook
import pandas as pd
#print(datetime.date.today())
df=datetime.date.today()
print(df)
#path="c:/tools/工单/"+'/'+df
time_now = time.strftime("%Y%m%d", time.localtime())
print(time_now)
path="c:/tools/工单"+'/'+time_now
print(path)
if not os.path.exists(path):
    os.makedirs(path)
    print('文件夹创建完成 '+path)
gd=pd.read_excel(r'C:\tools\工单\网络类工单-0530.xlsx')
print(gd)

gdpath=path
print(gdpath)

gd1=gd[(gd.客户地市.str.contains('济南'))]
print(gd1)
gd1path=path+'/'+'济南.xlsx'
print(gd1path)
#gd1.to_excel(path+'/'+济南.xlsx')
gd1.to_excel(path+'/'+'济南.xlsx')
#gd1.to_excel(gd1path)
gd2=gd[(gd.客户地市.str.contains('青岛'))]
gd2.to_excel(path+'/'+'青岛.xlsx')
print(gd2)
gd3=gd[(gd.客户地市.str.contains('淄博'))]
print(gd3)
gd3.to_excel(path+'/'+'淄博.xlsx')
gd4=gd[(gd.客户地市.str.contains('东营'))]
print(gd4)
gd4.to_excel(path+'/'+'东营.xlsx')
gd5=gd[(gd.客户地市.str.contains('烟台'))]
print(gd5)
gd5.to_excel(path+'/'+'烟台.xlsx')
gd6=gd[(gd.客户地市.str.contains('潍坊'))]
print(gd6)
gd6.to_excel(path+'/'+'潍坊.xlsx')
gd7=gd[(gd.客户地市.str.contains('临沂'))]
print(gd7)
gd7.to_excel(path+'/'+'临沂.xlsx')
gd8=gd[(gd.客户地市.str.contains('济宁'))]
print(gd8)
gd8.to_excel(path+'/'+'济宁.xlsx')
gd9=gd[(gd.客户地市.str.contains('泰安'))]
print(gd9)
gd9.to_excel(path+'/'+'泰安.xlsx')
gd10=gd[(gd.客户地市.str.contains('威海'))]
print(gd10)
gd10.to_excel(path+'/'+'威海.xlsx')
gd11=gd[(gd.客户地市.str.contains('日照'))]
print(gd11)
gd11.to_excel(path+'/'+'日照.xlsx')
gd12=gd[(gd.客户地市.str.contains('德州'))]
print(gd12)
gd12.to_excel(path+'/'+'德州.xlsx')
gd13=gd[(gd.客户地市.str.contains('聊城'))]
print(gd13)
gd13.to_excel(path+'/'+'聊城.xlsx')
gd14=gd[(gd.客户地市.str.contains('滨州'))]
print(gd14)
gd14.to_excel(path+'/'+'滨州.xlsx')
gd15=gd[(gd.客户地市.str.contains('菏泽'))]
print(gd15)
gd15.to_excel(path+'/'+'菏泽.xlsx')
gd16=gd[(gd.客户地市.str.contains('枣庄'))]
print(gd16)
gd16.to_excel(path+'/'+'枣庄.xlsx')
'''
time_now = time.strftime("%Y%m%d-%H:%M", time.localtime())
path = "/dybfs/*****/***/"+'/'+time_now
if not os.path.exists(path):
    os.makedirs(path)
    print('文件夹创建完成  '+path)
'''
