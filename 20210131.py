#20210131

AttendanceRecord={"OnDuty":20,"BeLate":3,"AskForLeave":2}

n1=AttendanceRecord["OnDuty"]*100
n2=AttendanceRecord["BeLate"]*50

Wages=n1+n2

print(f"Jack上个月的工资为{Wages}元")


Score = {"Here to Stay": 4.2, "The Secrets of Lost Stones": 4.7, "I Know Everything": 4.6, "The Rabbit Girls": 4.5, "Butterfly in Frost": 4.1, "Call Her Mine": 4.5, "Broken Knight": 4.8, "All the Lovely Pieces": 4.4, "Black Nowhere": 4.2, "The Loot":4.6}

for i in Score:
    if Score[i]>4.5:
        print(i)


Score = {"Here to Stay": 4.2, "The Secrets of Lost Stones": 4.7, "I Know Everything": 4.6, "The Rabbit Girls": 4.5, "Butterfly in Frost": 4.1, "Call Her Mine": 4.5, "Broken Knight": 4.8, "All the Lovely Pieces": 4.4, "Black Nowhere": 4.2, "The Loot":4.6}

TopTen=[]

MaxScore=0

for i in Score:
    TopTen.append(i)
    if Score[i]>MaxScore:
        MaxScore=Score[i]
        Title=i

print(TopTen)
print(f"得分最高的图书是{Title}")


state = {'China':['Beijing', 'Shanghai', 'Shenzhen'], 'USA':['Washington', 'NewYork', 'Boston']}

state['England']=['London','Birmingham','Manchester']

for i in state:
    print(f"{i}的前三大城市为{state[i]}")

maxThree=max(10,100,1000)
print(maxThree)

a='abc'
b='def'
print(a+b)

Num=[5,7,9,2,1,3,5,5]

n=0

for i in Num:

    if i==5:
        Num[n]=8

    n=n+1

print(Num)

n='sjdkfjjdskhsjk'

num=0

for i in n:
    num=num+1

print(num)