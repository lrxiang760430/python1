import pandas as pd 
account1=pd.read_csv(r'G:\tools\刘伟\宽带在线用户统计\eboss宽带账号-2021-7-18号之前未到期.txt')
account2=pd.read_csv(r'G:\tools\temp\4567a.csv')
print(account1)
print(account1.head())
print(len(account1))
print(type(account1.loc[0]))
l1=len(account1)
print("l1= ",l1)
print(account2)
account2=account2[['pppoe']]

print(account2.head())
print(len(account2))
l2=len(account2)
print("l2= ",l2)
x=account2
y=account1
print("x= ",x)
print(y)
#返回x中不包含y的部分
ans = pd.merge(left=x, right=y, how='left', indicator=True)
ans = ans.loc[ans._merge == 'left_only', :].drop(columns='_merge')

print(ans)
ans.to_csv('g:/tools/bossnoradius20210720.csv')


x=account1
y=account2
print("x= ",x)
print(y)
#返回x中不包含y的部分
ans = pd.merge(left=x, right=y, how='left', indicator=True)
ans = ans.loc[ans._merge == 'left_only', :].drop(columns='_merge')

print(ans)
ans.to_csv('g:/tools/bossnoradius20210720a.csv')


'''
i1=0
i2=100
j1=0
j2=100
a1=[]
b1=[]
while i1<i2:
    str(a1.append(account1.loc[i1]))
    print(a1[i1])
    i1=i1+1

while j1<j2:
    str(b1.append(account2.loc[j1]))
    print(b1[j1])
    j1=j1+1
    
print(type(a1[1]))

print(type(b1[1]))
'''
