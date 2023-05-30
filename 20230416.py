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
#下面将文件根据地市编号分成17个地市
df1=df4g[df4g['地市编号']==370100]
print(df1)
df1.to_csv('4g100.csv')
df2=df4g[df4g['地市编号']==370200]
print(df2)
df2.to_csv('4g200.csv')

df3=df4g[df4g['地市编号']==370300]
print(df3)
df3.to_csv('4g300.csv')

df4=df4g[df4g['地市编号']==370400]
print(df4)
df4.to_csv('4g400.csv')

df5=df4g[df4g['地市编号']==370500]
print(df5)
df5.to_csv('4g500.csv')

df6=df4g[df4g['地市编号']==370600]
print(df6)
df6.to_csv('4g600.csv')

df7=df4g[df4g['地市编号']==370700]
print(df7)
df7.to_csv('4g700.csv')

df8=df4g[df4g['地市编号']==370800]
print(df8)
df8.to_csv('4g800.csv')

df9=df4g[df4g['地市编号']==370900]
print(df9)
df9.to_csv('4g900.csv')

df10=df4g[df4g['地市编号']==371000]
print(df10)
df10.to_csv('4g1000.csv')

df11=df4g[df4g['地市编号']==371100]
print(df11)
df11.to_csv('4g1100.csv')

df12=df4g[df4g['地市编号']==371200]
print(df12)
df12.to_csv('4g1200.csv')

df13=df4g[df4g['地市编号']==371300]
print(df13)
df13.to_csv('4g1300.csv')

df14=df4g[df4g['地市编号']==371400]
print(df14)
df14.to_csv('4g1400.csv')

df15=df4g[df4g['地市编号']==371500]
print(df15)
df15.to_csv('4g1500.csv')

df16=df4g[df4g['地市编号']==371600]
print(df16)
df16.to_csv('4g1600.csv')

df17=df4g[df4g['地市编号']==371700]
print(df17)
df17.to_csv('4g1700.csv')