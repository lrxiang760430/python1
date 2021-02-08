
"""
numberlist=[2,4,3,5,2,1,3,2,4]
total=0
n=0
for i in numberlist:
    total=total+i

    if total>15:
        print(f"有{n}个人可以买到牛奶")
        break
    n=n+1
"""

melonlist=[4,3.5,2,5,6,3,4.7,5.3]
n=0
buylist=[]

for i in melonlist:
    if n==3:
        break
    if i>=4:
        buylist.append(i)
        n=n+1
        continue
print(buylist)


Quality=[1,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1]
Count=0
for i in Quality:
    if i==0:
        Count=Count+1
    if Count>2:
        break
if Count>2:
    print("不合格")
else:
    print("合格")


for i in range(10):
    if i%2==1:
        print(i)

jack=35
if jack<=44:
    print("青年人")
if 45<=jack<=59:
    print("中年人")
if 60<=jack<=95:
    print("老年人")
if jack>95:
    print("长寿老人")

#逆序输出，这个可以好好琢磨一下
string="hello"
NewList=[]

for i in string:
    #这一步实现了将string中的各个字符逐个添加到NewList中
    NewList.append(i)
print (NewList)
result=""
n=4
while n>=0:
    result=result+NewList[n]
    n=n-1

print(result)


