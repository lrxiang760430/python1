from openpyxl import load_workbook,Workbook
import pandas as pd
# 读取xls（绝对路径）
#pd.read_excel(io=r'E:\blog\Python\pandas\excel\data.xls')

#gd=pd.read_excel(r'C:\tools\工单\网络类工单-0529.xlsx')
gd=pd.read_excel(r'C:\tools\工单\5月工单.xlsx')
print(gd)
#以下这条命令取工单中的网络故障类
gd=gd[(gd.需求描述.str.contains('移网业务/投诉类/网络'))]
print(gd)

'''
print(gd['客户地市'])
gd1=gd[(gd.客户地市.str.contains('济南'))]
print(gd1)
gd1.to_excel(r'C:\tools\工单\20230530\济南.xlsx')
gd2=gd[(gd.客户地市.str.contains('青岛'))]
gd2.to_excel(r'C:\tools\工单\20230530\青岛.xlsx')
print(gd2)
gd3=gd[(gd.客户地市.str.contains('淄博'))]
print(gd3)
gd3.to_excel(r'C:\tools\工单\20230530\淄博.xlsx')
gd4=gd[(gd.客户地市.str.contains('东营'))]
print(gd4)
gd4.to_excel(r'C:\tools\工单\20230530\东营.xlsx')
gd5=gd[(gd.客户地市.str.contains('烟台'))]
print(gd5)
gd5.to_excel(r'C:\tools\工单\20230530\烟台.xlsx')
gd6=gd[(gd.客户地市.str.contains('潍坊'))]
print(gd6)
gd6.to_excel(r'C:\tools\工单\20230530\潍坊.xlsx')
gd7=gd[(gd.客户地市.str.contains('临沂'))]
print(gd7)
gd7.to_excel(r'C:\tools\工单\20230530\临沂.xlsx')
gd8=gd[(gd.客户地市.str.contains('济宁'))]
print(gd8)
gd8.to_excel(r'C:\tools\工单\20230530\济宁.xlsx')
gd9=gd[(gd.客户地市.str.contains('泰安'))]
print(gd9)
gd9.to_excel(r'C:\tools\工单\20230530\泰安.xlsx')
gd10=gd[(gd.客户地市.str.contains('威海'))]
print(gd10)
gd10.to_excel(r'C:\tools\工单\20230530\威海.xlsx')
gd11=gd[(gd.客户地市.str.contains('日照'))]
print(gd11)
gd11.to_excel(r'C:\tools\工单\20230530\日照.xlsx')
gd12=gd[(gd.客户地市.str.contains('德州'))]
print(gd12)
gd12.to_excel(r'C:\tools\工单\20230530\德州.xlsx')
gd13=gd[(gd.客户地市.str.contains('聊城'))]
print(gd13)
gd13.to_excel(r'C:\tools\工单\20230530\聊城.xlsx')
gd14=gd[(gd.客户地市.str.contains('滨州'))]
print(gd14)
gd14.to_excel(r'C:\tools\工单\20230530\滨州.xlsx')
gd15=gd[(gd.客户地市.str.contains('菏泽'))]
print(gd15)
gd15.to_excel(r'C:\tools\工单\20230530\菏泽.xlsx')
gd16=gd[(gd.客户地市.str.contains('枣庄'))]
print(gd16)
gd16.to_excel(r'C:\tools\工单\20230530\枣庄.xlsx')
'''

