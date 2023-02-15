import pandas as pd
df=pd.read_csv('5g_sd.csv','\^')
print(df)
dflen=len(df)
#dflen.to_csv('5g总行数.csv')
print(dflen)
#M = da['F'].value_counts()
M=df['扇区经度'].count()
print(M)
M=str(M)
#M.to_csv('5g总行数.csv')
f=open('5g基站总行数.txt','w')
f.writelines(M)
f.close

#df['Full Name'] = df['First'].str.cat(df['Last'],sep=" ")
#df['经纬度']=df['扇区经度'].str.cat(df['扇区纬度'],sep=' ')
df['经纬度']=df['扇区经度'].map(str)+' '+df['扇区纬度'].map(str)
print(df)
df10=df.head(10)
print(df10)

dfqc=df.drop_duplicates('经纬度')
print(dfqc)



print(dfqc.groupby('地市编号').count())
dfgb=dfqc.groupby('地市编号').count()
dfgb.to_csv('5g分类汇总.csv')

'''
df15=dfqc[dfqc['地市编号']==371500]
print(df15)
df15.to_csv('5g1500.csv')
'''

df1=dfqc[dfqc['地市编号']==370100]
print(df1)
df1.to_csv('5g100.csv')
df2=dfqc[dfqc['地市编号']==370200]
print(df2)
df2.to_csv('5g200.csv')

df3=dfqc[dfqc['地市编号']==370300]
print(df3)
df3.to_csv('5g300.csv')

df4=dfqc[dfqc['地市编号']==370400]
print(df4)
df4.to_csv('5g400.csv')

df5=dfqc[dfqc['地市编号']==370500]
print(df5)
df5.to_csv('5g500.csv')

df6=dfqc[dfqc['地市编号']==370600]
print(df6)
df6.to_csv('5g600.csv')

df7=dfqc[dfqc['地市编号']==370700]
print(df7)
df7.to_csv('5g700.csv')

df8=dfqc[dfqc['地市编号']==370800]
print(df8)
df8.to_csv('5g800.csv')

df9=dfqc[dfqc['地市编号']==370900]
print(df9)
df9.to_csv('5g900.csv')

df10=dfqc[dfqc['地市编号']==371000]
print(df10)
df10.to_csv('5g1000.csv')

df11=dfqc[dfqc['地市编号']==371100]
print(df11)
df11.to_csv('5g1100.csv')

df12=dfqc[dfqc['地市编号']==371200]
print(df12)
df12.to_csv('5g1200.csv')

df13=dfqc[dfqc['地市编号']==371300]
print(df13)
df13.to_csv('5g1300.csv')

df14=dfqc[dfqc['地市编号']==371400]
print(df14)
df14.to_csv('5g1400.csv')

df15=dfqc[dfqc['地市编号']==371500]
print(df15)
df15.to_csv('5g1500.csv')

df16=dfqc[dfqc['地市编号']==371600]
print(df16)
df16.to_csv('5g1600.csv')

df17=dfqc[dfqc['地市编号']==371700]
print(df17)
df17.to_csv('5g1700.csv')
