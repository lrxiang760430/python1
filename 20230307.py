import pandas as pd
'''
df=pd.read_excel('c:/tools/sd/工作簿2.xls')
print(df)
df.to_csv('c:/tools/sd/20230306chr.csv')
'''
#20230307.csv
df=pd.read_csv('c:/tools/sd/20230307.csv')
#df=pd.read_csv('c:/tools/sd/a1.csv')
print(df)
#打印表头
print(df.columns)
print(df.columns.values)
#学习一下list的用法
#print(list(data))
print('以下是使用list列出的')
print(list(df))
#打印主叫IMPU
#pandas里面打印指定的列并不困难，要树立信心
print(df['\t主叫IMPU\t'])
#下面学习groupby的操作
#第一个是主叫IMPU
df1=df.groupby(['\t主叫IMPU\t']).count()
print('按照主叫号码分类汇总')
print(df1)
#df1.to_csv('c:/tools/sd/主叫impu.csv')
#df1a=df1.sort_values()``

#print(df1a)
#df2.reset_index().sort_values('math_score',ascending = False).set_index('school_name')
df1a=df1.reset_index().sort_values('\t被叫IMPU\t',ascending=False).set_index('\t被叫IMPU\t')
print(df1a)
df1a.to_csv('c:/tools/sd/1aa.csv')

#下面是按照被叫号码排序
df2=df.groupby(['\t被叫IMPU\t']).count()
print('按照被叫号码分类汇总')
print(df2)
#df1.to_csv('c:/tools/sd/主叫impu.csv')
#df1a=df1.sort_values()``

#print(df1a)
#df2.reset_index().sort_values('math_score',ascending = False).set_index('school_name')
df2a=df2.reset_index().sort_values('\t被叫IMPU\t',ascending=False).set_index('\t被叫IMPU\t')
print(df2a)
df2a.to_csv('c:/tools/sd/2a.csv')

'''
#统计出现的次数
#vc = df['state'].value_counts()
df2=df['\t主叫IMPU\t'].value_counts
print('打印counts值')
print(df2)
#df1.to_csv('c:/tools/sd/主叫impu.csv')

#df2 = df1.city.value_counts()  
#df2=df.'\t主叫IMPU\t'.value_counts;
#print df2

'''

#增加一行
