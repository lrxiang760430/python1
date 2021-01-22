print('I love three things in this world.')
print('Sun moon and you.')
print('Sun for morning,')
print('moon for night,')
print('and you forever.')


print('Hello World:)')
print('Hello Again')
print('I like coding.')
print('This is fun.')
print('I can do it.')



Yestearday=20190320
Today=20190321
Tomorrow=20190322

print(Yestearday)
print(Today)
print(Tomorrow)


Weight=73.5
Myweight=70.5
Myweight=Weight
print(Myweight)


MyBirthday=19920708
print('my birthday is')
print(MyBirthday)


ThisYear=1992
print(ThisYear)
MyWeight=55
print(MyWeight)
YourWeight=MyWeight
print(YourWeight)


beer=6
milk=15
bread=10
total=beer*2+milk*1+bread*3
print(total)


print(1980*0.85)


Weight=40
Height=1.3
BMI=Weight/(Height*Height)
print(BMI)


MySlogan="happy new year"
print(MySlogan)

MySlogan='''I
love
sleeping'''
print(MySlogan)

Score="70:66"
print(f"湘北{Score}陵南")

print(True and True)
print(False and True)
print(1==1 and 2==1)
print(1==1 or 2!=1)
print(False and 0!=0)
print(True or 1==1)


print(not(True and False))
print(not(1==1 and 0!=1))
print(not(1!=10 or 3==4))
print(1==1 and not (3==1 or 1==0))

TonyAge=10
TonyHeight=145
HowardAge=13
HowrdHeight=133

print(TonyAge<=11 and TonyHeight>=130)
print(HowardAge<=11 and HowrdHeight>=130)


BoxNum=(100 // 3)
print(BoxNum)


Left=(100 % 3)
print(Left)


total=90*2
average=total/3
print(average)


name="Tony"
print(f"夜曲网吧有优惠 {name}速来")




num=66
if(num%2==0):
    print("yes")
else:
    print("no")


iphonexr=5099
iphonexs=7299
xiaomi9=3699
huaweip30pro=5488
if iphonexr<6000:
    print("可以购买iphonexr")
if iphonexs<6000:
    print("可以购买iphonexs")
if xiaomi9<6000:
    print("可以购买xiaomi9")
if huaweip30pro<6000:
    print("可以购买huaweip30pro")


ChengduPopulation=1633
BeijingPopulation=2171
if(ChengduPopulation>BeijingPopulation):
    print("Chengdu has more people")
else:
    print("Beijing has more people")




MyWeight=80
MyHeight=1.8

BMI=MyWeight/(MyHeight*MyHeight)

if BMI<18.5:
    print("under weight")
elif BMI<23.9:
    print("normal weight")
elif BMI<27:
    print("over weight")
elif BMI<32:
    print("fat")
else:
    print("obese")


a=17*87+343-8*134
if a>0:
    print("正数")
else:
    print("负数")


a=8.5+6+8
if a>20:
    print(f"需要交{(a-20)*20}元")
else:
    print("不需要补交运费")


FamousBag=["CHANEL","LV","Gucci","Fendi"]
#print(FamousBag)
FamousBag[3]="Prada"
print(FamousBag)


animals=["bear","python","peacock"]
print(f"the first animal in the list is {animals[0]}")
print(f"the second animal in the list is {animals[1]}")
print(f"the third animal in the list is {animals[2]}")


a="NocturneProgramming"
print(a[0])
print(a[3])
print(a[9])


list1=[1,2,3,4]
list2=[]

list2.append(list1[3])
list1.pop
list2.append(list1[2])
list1.pop
list2.append(list1[1])
list1.pop
list2.append(list1[0])
list1.pop

print(list2)


dayList=["星期日","星期二","October","星期三","星期五"]

dayList.pop(2)

dayList.insert(1,"星期一")
dayList.insert(4,"星期四")
dayList.append("星期六")

print(dayList)


NumberList=[10,11,12,13,14,15]
print(NumberList)
n=0
while n<6:
    print(NumberList[n])
    n=n+1
    continue


NumberList=[10,11,12,13,14,15]
for i in NumberList:
    print(i)


Numbers=[0,1,2,3,4,5,6,7,8,9]
for i in Numbers:
    if(i%2==1):
        print(i)

animals=['bear','python','peacock','kangaroo','whale','platypus']        

numbers=['1st','2nd','3rd','4th','5th','6th']

num=[0,1,2,3,4,5]

for n in num:
    print(f'The {numbers[n]} animal in the list is {animals[n]}')



num=[73,76,73,90,87]
for i in num:
    print(i)


price=[3,15,11,9,12,3,9,15,18,14]
sum=0
for i in price:
    sum=sum+i
print(sum)



NumList=[83,80,18,4,88,21,96,20,40,59]
num=0
for i in NumList:
    if num<i:
        num=i
print(num)


NumList=[83,80,18,4,88,21,96,20,40,59]
num=NumList[0]
for i in NumList:
    if num>i:
        num=i
print(num)

NumberList=[10,11,12,13,14,15]
Counter=0
while Counter<6:
    print(NumberList[Counter])
    Counter=Counter+1
    continue


Counter=0
while Counter<10:
    if Counter%2==0:
        print(Counter)
    Counter=Counter+1

n=0
i=0
while i<101:
    n=n+i
    i=i+1
print(n)


n=1
while n<=10:
    print('*'*n)
    n=n+1


NumberList=[5,11,7,13,8,9,16]
for i in NumberList:
    if(i>10):
        print(i)
        continue


NumberList=[78,56,12,14,61,41,38]
for i in NumberList:
    if(i>60):
        print(i)
        break


Record = [60, 0, 73, 139, 64, 48, 73, 63, 0, 59, 100, 121, 44, 30, 0, 0, 43, 67, 64, 51, 106, 0, 80, 0, 119, 59, 0, 58, 100, 90]
Count=0
for i in Record:
    if i>0:
        continue
    Count=Count+1
print(f'这个月有{Count}天没有背单词')


numberlist=[2,4,3,5,2,1,3,5,2,4]
total=0
n=0
for i in numberlist:
    total=total+i
    if total>15:
        print(f"有{n}个人可以买")




