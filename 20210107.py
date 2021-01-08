"""
class Computer:
	def __init__(self, brand):
		self.brand = brand

	def computer_brand(self):
		print(self.brand)

class Mac(Computer):
	def __init__(self, type):
		self.brand = "Mac"
		self.type = type

	def computer_type(self):
		print(self.type)

myComputer = Mac("MacBook Air")
myComputer.computer_brand()
myComputer.computer_type()


class rectangle:
    	def __init__(self,length,width):
		self.length = length
		self.width = width
	def area(self):
		print(self.length*self.width)
class square(rectangle):
	def __init__(self,length):
		#self.length = length
		self.length=length
        
        self.width = length

figur1 = rectangle(4,6)
figur1.area()
figur2 = square(5)
figur2.area()


class OS:
    def __init__(self,brand):
	    self.brand = brand
	def introduce(self):
    #def introduce(self):
        print(self.brand)
		#print(self.brand)

class IOS(OS):
	def __init__(self,version):
		self.brand = 'IOS'
		self.version = version
	def introduce(self):
		print(self.brand+self.version)

PhoneA = OS('Android')
PhoneA.introduce()
PhoneB = IOS('13')
PhoneB.introduce()


def make_shirt(word,size):
    	print(f"一件印有{word}的{size}码衣服")

make_shirt("夜曲编程","XL")
make_shirt("I love python","L")


class shirt:
    def __init__(self,word,size): 
	    self.word=word
	    self.size=size
    def make_shirt(self):
	    print(f"一件印有{self.word}的{self.size}码衣服")

shirt1 = shirt("夜曲编程","XL")
shirt1.make_shirt()
shirt2 = shirt("I love python","L")
shirt2.make_shirt()



import datetime
today=datetime.date.today()
year=today.year
print(year==2021)


import datetime
print(datetime.date.today())


import calendar
Cal202101=calendar.month(2021,1)
print(Cal202101)


from datetime import date
Today=date.today()
print(Today)


from datetime import date
today=date.today()
year=today.year()
print(year==2021)


import os
print(os.mkdir("yequbiancheng"))




import math
print(math.sqrt(100))
print(math.fabs(-0.03))



poem="夜雨寄北"
print(poem)


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)



import numpy as np
numList=range(10,50)
arr=np.array(numList)
print(arr)

import numpy as np
arr=np.array([[1,2],[4,5],[7,9],[11,12]])
print(arr)
"""
import pandas as pd
data=[80855,77388,68024,47251,40471]
city=['GD','JS','SD','ZJ','HN']

GDP=pd.Series(data,index=city)
print(GDP)