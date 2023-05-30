import pandas as pd
df4g=pd.read_csv('C:/tools/sd/2023年3月工参表/1.csv')
print(df4g)

#df.drop_duplicates(inplace = True)
df4g.drop_duplicates(inplace=True)

#print(df4g.drop_duplicates(inplace=True))
print('------------')
print(df4g)