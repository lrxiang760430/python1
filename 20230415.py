import pandas as pd
#读取4G工参数据
#df4g=pd.read_csv('C:/tools/sd/2023年3月工参表/4g_sd.csv',sep='^',nrows=10000)
df4g=pd.read_csv('C:/tools/sd/2023年3月工参表/4g_sd.csv',sep='^')
print(df4g)
#生成4G分列数据
#df4g.to_csv('C:/tools/sd/2023年3月工参表/4g_sd_fl.csv',encoding='utf_8_sig')
#读取5G工参数据
#df5g=pd.read_csv('C:/tools/sd/2023年3月工参表/5g_sd.csv',sep='^',nrows=10000)
df5g=pd.read_csv('C:/tools/sd/2023年3月工参表/5g_sd.csv',sep='^')
print(df5g)
#encoding='utf_8_sig'
#生成5G分列数据
#df5g.to_csv('C:/tools/sd/2023年3月工参表/5g_sd_fl.csv',encoding='utf_8_sig')
#开始进行数据清洗
#df.drop_duplicates () ：删除重复行
#通过与MYSQL中去重结果进行比较，发现2023年3月份的工参数据中已经没有两行完全一样的重复行了
df4g.drop_duplicates(inplace=True);
print(df4g)
df5g.drop_duplicates(inplace=True)
print(df5g)
#打印列名
print(df4g.columns)
print(df5g.columns)
#df1=df4g[df4g['基站名称（中文）'].drop_duplicates(inplace=True)]
#dfqc=df.drop_duplicates('基站名称（中文）')
dfqcxqmc=df4g.drop_duplicates('小区名称（中文）')
print(dfqcxqmc)
#合并生成经纬度
#df['经纬度']=df['扇区经度'].map(str)+' '+df['扇区纬度'].map(str)
df4g['经纬度']=df4g['扇区经度'].map(str)+' '+df4g['扇区纬度'].map(str)
dfqcjwd=df4g.drop_duplicates('经纬度')  
print(dfqcjwd)