#20210129
"""
tuple=[5,11,7,13,8,9,16,29,3,17]
#print(tuple)

BiggerThan10=[]
for i in tuple:
    #print(i)
    if i>10:
        #print (i)
        BiggerThan10.append(i)
        
print(BiggerThan10)
"""

tuple=[1,3,4,3,5,6,3,3,7,9]
n=0
for i in tuple:
    if i==3:
        n=n+1
print(n)

Number=[6,29,90,26,63,44,4,79]
a=[]
b=[]
for i in Number:
    if i>50:
        a.append(i)
    else:
        b.append(i)
    
print(a)
print(b)


SchoolID=('20177314607','20176180','20178064628','20176770','20178480')
Dormitory=[]
for i in SchoolID:
    number=i[7:]
    if number!='0':
        Dormitory.append(number)

print(Dormitory)

ID=('5','4','0','1','0','1','1','9','9','9','0','1','0','9','*','*','*','*')
Year=''
Month=''
Day=''

for i in ID[6:10]:
    Year=Year+i

for j in ID[10:12]:
    Month=Month+j

for k in ID[12:14]:
    Day=Day+k


print(f"{Year}-{Month}-{Day}")    


Scores=[87,54,71,88,92,58,79,48]

Result=[]

for i in Scores:
    if i>=90:
        Result.append('A')
    elif i>=60:
        Result.append('B')
    else:
        Result.append('C')

print(Result)
