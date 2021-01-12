import pandas as pd 
#radius=pd.read_csv(r'G:\tools\mathorcup\account20200217.txt')
radius=pd.read_table(r'G:\tools\mathorcup\account20200217.txt',sep=',')


print(radius)
print(radius['[{"net_no":"8370810428527086@zc"'].duplicated())
dfOrder=radius[radius['[{"net_no":"8370810428527086@zc"'].duplicated()]
print(dfOrder)
radius.drop(index=dfOrder.index,inplace=True)
print(dfOrder)
radius.info()
print(radius)
radius.to_csv(r'G:\tools\mathorcup\account20200217a.txt')