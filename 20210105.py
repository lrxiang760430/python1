"""
i=1598
if (i%17==0):
    print ("Yes")
else:
    print("No")


Number=[1,2,3,4,5]
for i in Number:
    if i<5:
        print(f"还剩{5-i}圈")
    else:
        print("完成")


GenderTuple=("male","female")
print(GenderTuple)
print(GenderTuple[0])



SomeNumber=(10,20,30,40,50)
print(SomeNumber[1:3])
print(SomeNumber[1:5])


tuple = (-1, 3, 67, -9, 5, 6, 23)
list = [-1, 3, 67, -9, 5, 6, 23]
print(tuple)
print(list)


Number = (2, 5, 6, 3, 4, 2, 2, 7, 8, 2)
c=0
for i in Number:
    if i==2:
        c=c+1
print (c)


Number = (2, 5, 6, 3, 4, 2, 2, 7, 8, 2)
c=0
for i in Number[3:8]:
    c=c+i
    print (i)
print (c)


StudentHeight={"Tony":171,"Kevin":181,"Asum":185,"Alita":165}
print(StudentHeight)
print(StudentHeight["Alita"])



Result = {'Tony':69, 'Lihua':64, 'Rain':93, 'Jack':61, 'Xiuxiu':82, 'Peiqi':67, 'Black':77}
print(Result["Tony"])



Result = {'Tony':69, 'Lihua':64, 'Rain':93, 'Jack':61, 'Xiuxiu':82, 'Peiqi':67, 'Black':77}
print(Result.keys())


Result = {'Tony':69, 'Lihua':64, 'Rain':93, 'Jack':61, 'Xiuxiu':82, 'Peiqi':67, 'Black':77}
n=0
for i in Result.keys():
    if Result[i] <n:
        continue
    n=Result[i]
print (n)


def sentence(content,punctuation):
    print(content,punctuation)

sentence("这是函数","!")


def PrintTwice(content):
    print(content)
    print(content)

PrintTwice("ChengDu")
"""


def PrintThreeTimes(content):
    print(content)
    print(content)
    print(content)
    
PrintThreeTimes("Beijing")





