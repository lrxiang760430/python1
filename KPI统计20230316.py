import os,sys,datetime
import pandas as pd
import xlrd
from xlutils.copy import copy
from xlwt import easyxf
import warnings

#屏蔽告警信息输出
warnings.filterwarnings('ignore')
'''
在当前目录创建包含当前日期前一天的目录，格式为“XXXXYYZZ”，
比如2023年3月15日凌晨导出前一天的数据以后，需要在脚本所在目录
创建20230314文件夹。并把当日的查询结果保存至该目录
'''
#------------------------------------------------------------------
#判断目录是否存在
ystd = datetime.datetime.now() + datetime.timedelta(days = -1)
dir_name= ystd.strftime('%Y%m%d')
path = './'+dir_name+'/'

if not os.path.exists(path):
    print('请创建目录名为当前日期前一天的目录，格式为“XXXXYYZZ”')
    print('目录名称包含四位年份、两位月份和两位日期')
    sys.exit()

#------------------------------------------------------------------
#读取目录内文件列表
file = os.listdir(path)

#把文件名读入数组
flist=[]
for f in file:
    flist.append(f)

#判断目录内原始数据文件数量
if len(flist)>11:
    print('有重复数据，请检测后再重新运行脚本。')
    sys.exit()
elif len(flist)<11:
    print('导出数据有重复，请删除多余数据后再运行脚本！')
    sys.exit()
elif len(flist)==11:
    flist_new=[]
    for fn in flist:
        flist_new.append(fn[0:10])
    flist_new=set(flist_new)
    #使用set生成一个元素无序且不重复的可迭代对象，也就是我们常说的去重
    if len(flist) != len(flist_new):
        print('导出数据有缺少项，有重复项，请核对后重新运行脚本！')
        sys.exit()    


#------------------------------------------------------------------
#读取“01UDM开户用户数”
UDMkaihu=pd.read_excel(path+flist[0],sheet_name='结果',header=None)

#删除冗余数据
c_list = UDMkaihu.values.tolist()[7]    # 得到想要设置为列索引【表头】的某一行提取出来
UDMkaihu.columns = c_list               # 设置列索引【表头】
UDMkaihu=UDMkaihu.drop(UDMkaihu.head(8).index) # 将原来的表头及表头前的数据删掉。

#获取License控制项列最大值
UDM_kaihu=UDMkaihu.License控制项实际用户数.max()
print('192开卡总数量：',UDM_kaihu)

#------------------------------------------------------------------
#读取“02UDM鉴权成功率”
UDMjianquan=pd.read_excel(path+flist[1],sheet_name='结果',header=None)

#删除冗余数据
c_list = UDMjianquan.values.tolist()[7]    # 得到想要设置为列索引【表头】的某一行提取出来
UDMjianquan.columns = c_list               # 设置列索引【表头】
UDMjianquan=UDMjianquan.drop(UDMjianquan.head(8).index) # 将原来的表头及表头前的数据删掉。

#对鉴权请求和鉴权成功次数求和
sum_req = UDMjianquan['鉴权请求消息总数 (次)'].sum()
sum_suc = UDMjianquan['鉴权成功的消息总数 (次)'].sum()

#print('鉴权请求消息总数 (次)：',sum_req,'鉴权成功的消息总数 (次)：',sum_suc)
UDM_per = sum_suc/sum_req
print('UDM 鉴权成功率（5G）{:.2%}'.format(UDM_per))


#------------------------------------------------------------------
#读取“03SMF用户会话数”
SMFhuihua=pd.read_excel(path+flist[2],sheet_name='结果',header=None)

#删除冗余数据
c_list = SMFhuihua.values.tolist()[7]
SMFhuihua.columns = c_list
SMFhuihua = SMFhuihua.drop(SMFhuihua.head(8).index)
#分别获取4G和5G用户会话数峰值
SMFhuihua_4g = SMFhuihua['PGW-C通过GTP S5/S8/S2a/S2b创建的最大同时在线Session数'].max()
SMFhuihua_5g = SMFhuihua['N16SMF 5G 最大PDU会话数'].max()
print('4G用户会话数峰值：',SMFhuihua_4g,'5G用户会话数峰值',SMFhuihua_5g)


#------------------------------------------------------------------
#读取“04互联网出口流量”
Internet = pd.read_excel(path+flist[3],sheet_name='结果',header=None)

#删除冗余数据
c_list = Internet.values.tolist()[7]
Internet.columns = c_list
Internet = Internet.drop(Internet.head(8).index)

#提取DC1和DC2互联网出口峰值
Internet_sc = Internet[Internet['网元名称']=='JNUPF001BHW']['用户平面UPF发送下行用户面报文峰值千字节速率'].max()/1000*8
Internet_kfq = Internet[Internet['网元名称']=='JNUPF002BHW']['用户平面UPF发送下行用户面报文峰值千字节速率'].max()/1000*8

#计算互联网出口日均累积（GB）
Internet_sum = (Internet['用户平面UPF接收的上行用户面报文千字节数'].sum()+Internet['用户平面UPF接收的下行用户面报文千字节数'].sum())/1000**2

print('孙村DC1互联网出口峰值（Mbps）：',Internet_sc)
print('开发区DC2互联网出口峰值（Mbps）：',Internet_kfq)
print('互联网出口日均累积（GB）：{:.2f}'.format(Internet_sum))


#------------------------------------------------------------------
#读取“05语音接通率”
Call = pd.read_excel(path+flist[4],sheet_name='结果',header=None)

#删除冗余数据
c_list = Call.values.tolist()[7]
Call.columns = c_list
Call = Call.drop(Call.head(8).index)

#计算日通话接通次数累计和试呼次数累计
Call_suc_sum=Call['ABCF接通次数'].sum()
Call_try_sum=Call['ABCF试呼次数'].sum()
print('日通话接通次数累计：',Call_suc_sum)

#计算语音接通率
Call_per=Call_suc_sum/Call_try_sum
print('计算语音接通率：{:.2%}'.format(Call_per))

#计算平均通话时长（s）
Call_time = Call['ABCF总会话通话时长'].sum()/Call_suc_sum
print('平均通话时长（s）：{:.2f}'.format(Call_time))

#计算"日均话务量（爱尔兰Erl）"
Call_Erl = Call['ABCF接通话务量'].sum()
print('日均话务量（爱尔兰Erl）：{:.2f}'.format(Call_Erl))

#计算日均总通话时长（小时）
Call_sum = Call['ABCF总会话通话时长'].sum()/3600
print('日均总通话时长（小时）：{:.2f}'.format(Call_sum))


#------------------------------------------------------------------
#读取“06EPSFB成功率”
EPSFB = pd.read_excel(path+flist[5],sheet_name='结果',header=None)

#删除冗余数据
c_list = EPSFB.values.tolist()[7]
EPSFB.columns = c_list
EPSFB = EPSFB.drop(EPSFB.head(8).index)

#计算EPS Fallback流程成功率（标准95%）
EPSFB_per = EPSFB['SMF/PGW-C统计EPS Fallback流程成功次数'].sum()/EPSFB['SMF/PGW-C统计EPS Fallback流程请求次数'].sum()
print('EPS Fallback流程成功率（标准95%）：{:.2%}'.format(EPSFB_per))


#------------------------------------------------------------------
#读取“07UPF上5G会话建立成功率”
UPF = pd.read_excel(path+flist[6],sheet_name='结果',header=None)

#删除冗余数据
c_list = UPF.values.tolist()[7]
UPF.columns = c_list
UPF = UPF.drop(UPF.head(8).index)

#计算“UPF上5G会话建立成功率（标准95%）”
UPF_per = UPF['用户平面N4接口发送的PFCP会话建立响应成功消息数'].sum()/UPF['用户平面N4接口接收的PFCP会话建立请求消息数'].sum()
print('UPF上5G会话建立成功率（标准95%）：{:.2%}'.format(UPF_per))


#------------------------------------------------------------------
#读取“08SMF上5G会话建立成功率”
SMF = pd.read_excel(path+flist[7],sheet_name='结果',header=None)

#删除冗余数据
c_list = SMF.values.tolist()[7]
SMF.columns = c_list
SMF = SMF.drop(SMF.head(8).index)
#SMF.to_excel('new.xlsx',sheet_name='结果',index=False)

#计算“SMF上5G会话建立成功率（标准95%）”
SMF_per = SMF['N16SMF发送Nsmf_PDUSession_Create Response成功消息数（会话创建）'].sum()/SMF['N16SMF接收Nsmf_PDUSession_Create Request消息数（会话创建）'].sum()
print('SMF上5G会话建立成功率（标准95%）：{:.2%}'.format(SMF_per))


#------------------------------------------------------------------
#读取“10SCSCF试呼接通”
CSCF = pd.read_excel(path+flist[8],sheet_name='结果',header=None)

#删除冗余数据
c_list = CSCF.values.tolist()[7]
CSCF.columns = c_list
CSCF = CSCF.drop(CSCF.head(8).index)
#CSCF.to_excel('new.xlsx',sheet_name='结果',index=False)

#计算“S-CSCF接通次数（次）”和“S-CSCF试呼次数（次）”
CSCF_suc_sum = CSCF['S-CSCF接通次数'].sum()
CSCF_try_sum = CSCF['S-CSCF试呼次数'].sum()

#计算“S-CSCF平均接通率”
CSCF_per = CSCF_suc_sum/CSCF_try_sum

print('S-CSCF试呼次数（次）：',CSCF_try_sum)
print('S-CSCF接通次数（次）：',CSCF_suc_sum)
print('S-CSCF平均接通率：{:.2%}'.format(CSCF_per))


#------------------------------------------------------------------
#读取“13SCSCF掉话率”
CSCF_drop = pd.read_excel(path+flist[9],sheet_name='结果',header=None)

#删除冗余数据
c_list = CSCF_drop.values.tolist()[7]
CSCF_drop.columns = c_list
CSCF_drop = CSCF_drop.drop(CSCF_drop.head(8).index)
#CSCF_drop.to_excel('new.xlsx',sheet_name='结果',index=False)

#计算“S-CSCF掉话率”
CSCF_drop_per = CSCF_drop['S-CSCF掉话次数'].sum()/CSCF_drop['S-CSCF应答次数'].sum()
print('S-CSCF掉话率：{:.2%}'.format(CSCF_drop_per))



#------------------------------------------------------------------
#读取“14UDM位置更新成功率”
updateloc = pd.read_excel(path+flist[10],sheet_name='结果',header=None)

#删除冗余数据
c_list = updateloc.values.tolist()[7]
updateloc.columns = c_list
updateloc = updateloc.drop(updateloc.head(8).index)
#updateloc.to_excel('new.xlsx',sheet_name='结果',index=False)

#计算“UDM位置更新成功响应率”
updateloc_per = updateloc[updateloc['位置更新成功响应率 (%)']!='NIL']['位置更新成功响应率 (%)'].mean()/100
print('UDM位置更新成功响应率：{:.2%}'.format(updateloc_per))


#------------------------------------------------------------------
#把所有数据追加至汇总表格

#打开要操作的Excel文件
wb = xlrd.open_workbook('每日指标.xls',formatting_info=True)
xwb = copy(wb)

sheet = xwb.get_sheet('每日指标')
rows = sheet.get_rows()
length = len(rows)
style_percent = easyxf(num_format_str='0.00%') #设置百分数格式

sheet.write(length,0,ystd.strftime('%m月%d日'))     #日期
sheet.write(length,1,UDM_kaihu)                     #192开卡总数量
sheet.write(length,2,UDM_per,style_percent)         #UDM鉴权成功率（5G）
sheet.write(length,3,SMFhuihua_4g)                  #4G用户会话数峰值
sheet.write(length,4,SMFhuihua_5g)                  #5G用户会话数峰值
sheet.write(length,5,float('%.2f' % Internet_sc))   #孙村DC1互联网出口峰值（Mbps)
sheet.write(length,6,float('%.2f' % Internet_kfq))  #开发区DC2互联网出口峰值（Mbps)
sheet.write(length,7,float('%.2f' % Internet_sum))  #互联网出口日均累积（GB）
sheet.write(length,8,Call_suc_sum)                  #日通话接通次数累计
sheet.write(length,9,float('%.2f' % Call_time))     #平均通话时长（s）
sheet.write(length,10,Call_per,style_percent)       #语音接通率
sheet.write(length,11,float('%.2f' % Call_Erl))     #日均话务量（爱尔兰Erl）
sheet.write(length,12,float('%.2f' % Call_sum))     #日均总通话时长（小时）
sheet.write(length,13,EPSFB_per,style_percent)      #EPS Fallback流程成功率（标准95%）
sheet.write(length,14,UPF_per,style_percent)        #UPF上5G汇合建立成功率（标准95%）
sheet.write(length,15,SMF_per,style_percent)        #SMF上5G汇合建立成功率（标准95%）
sheet.write(length,16,CSCF_drop_per,style_percent)  #S-CSCF掉话率
sheet.write(length,17,CSCF_try_sum)                 #S-CSCF试呼次数（次）
sheet.write(length,18,CSCF_suc_sum)                 #S-CSCF接通次数（次）
sheet.write(length,19,CSCF_per,style_percent)       #S-CSCF平均接通率
sheet.write(length,20,'')                           #核心网动态用户数，此处留空，手动录入
sheet.write(length,21,updateloc_per,style_percent)  #UDM位置更新成功响应率
xwb.save('每日指标.xls')

wb.release_resources()
del wb
