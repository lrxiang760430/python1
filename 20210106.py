"""
def area(Height,Width):
    return Height*Width
Size=area(10,15)
print(Size)


def length(Height,Width):
    return 2*(Height+Width)

zc=length(15,10)
print(zc)


a=max(1,2,3,4)
print(a)


a=min(1,2,3,4)
print(a)

a="world"
print(len(a))



def PrintFourTimes(content):
    print(content)
    print(content)
    print(content)
    print(content)
c=PrintFourTimes("China")



def jf(a,b):
    return(a+b)
result=jf(788,1667)
print(result)



def compare(a,b):
    if a>b:
        return a
    else:
        return b
print(f"{compare(18,22)}比较大")


def area(Height=1,Width=5):
    return Height*Width

Area1=area(5,3)
print(Area1)
Area2=area()
print(Area2)



def length(Height=10,Width=20):
    return 2*(Height+Width)

l1=length(5,10)
print(l1)
l2=length()
print(l2)



def addSum(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum

Number=addSum(1,2,3)
print(Number)
Number=addSum(1,2,3,4,5,6)
print(Number)




def multiSum(*numbers):
    sum=1
    for i in numbers:
        sum=sum*i
    return sum


a=multiSum(1,2,3)
print(a)
b=multiSum(1,2,3,4,5,6)
print(b)





def change(a,b):
    for i in b:
        a=a-i
    return a

money=100
price=[8,17,22]
print(change(money,price))


def change(b,a=100):
    for i in b:
        a=a-i
    return a

price=[8,17,22]
print(change(price))


def change(a,*b):
    for i in b:
        a=a-i
    return a

money=100
print(change(money,8,17,22))    


def addSum(*numbers):
    sum=0
    print(sum)

print(addSum())
print(sum)


GlobalNumber=100
def printNumber():
    GlobalNumber=20
    print(GlobalNumber)

printNumber()
print(GlobalNumber)




square=lambda x:x*x
square(9)
print(square(9))


twice=lambda x:2*x
twice(5)
print(twice(5))



def f1(n):
    if n==1:
        return 1
    return n*f1(n-1)



def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

print(factorial(3))



twice=lambda x:2*x
twice(3)
print(twice(3))


def mylove(content):
    return content


print(f"My favorite book is{mylove("Harry Potter")}")



def  mylove(title):
    print(f"My favorite book is {title}")


mylove('Harry Potter')

def factorial(n):
    reslut=1
    while n>0:
        reslut=reslut*n
        n=n-1
    return reslut

print(factorial(5))
BookA.print_name()


class Book:
    def __init__(self,name):
        self.name=name

    def print_name(self):
        print(self.name)

BookA=Book("harry_potter")


class Person:
    def __init__(self,name):
        self.name=name

    def print_name(self):
        print(self.name)


class Dog:
    def __init__(self,Dogname):
        self.Dogname=Dogname
    
    def print_DogName(self):
        print(self.DogName)


class Dog:
    def __init__(self,Dogname):
        self.name=Dogname

    def print_DogName(self):
        print(self.name)

wangcai=Dog('wangcai')
wangcai.print_DogName()


NumberList=[1,2,3,4,5]
print(NumberList)
NumberList.append(6)
print(NumberList)

PersonDict={"Name":"LiMing","Age":17,"Gender":"male"}
print(PersonDict)
PersonDict.clear()
print(PersonDict)


class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    def get_course(self):
        return max(self.score)

Tony=Student('Tony',20,[69,88,100])
print(Tony.get_course())


class bottle:
    def __init__(self,capacity):
        self.capacity=capacity
    def introduce(self):
        return self.capacity

a=bottle(600)
print(a.introduce())


class food:
    def __init__(self,caloric):
        self.caloric=caloric
    def introduce(self):
        return self.caloric

milk=food('200')
print(milk.introduce())
"""

class Poker:
    def __init__(self,colour,num):
        self.colour=colour
        self.num=num
    def play(self):
        print(f"打出一张{self.colour}{self.num}")

p=Poker("黑桃","A")
p.play()