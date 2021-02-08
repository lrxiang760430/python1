#20210201.py
#以下内容为函数调用的学习
def TriangleLength(a=10,b=12,c=15):
    return a+b+c 

TriangleLength1=TriangleLength()
<<<<<<< HEAD
print(TriangleLength1)
=======
print(TriangleLength1)

#定义函数，使用不定长参数*bill
def aggregate_amount(*bill):
    total_result=0
    for i in bill:
        total_result=total_result+i
    return total_result

#调用函数计算3.12号的帐单和，赋值给Amount0312
Amount0312=aggregate_amount(28,46,41,34,28,16,43,22,31,47)
print(Amount0312)

#调用函数计算3.14号的帐单和，赋值给Amount0314
Amount0314=aggregate_amount(42,49,36,31,12,48,20)
print(Amount0314)
>>>>>>> ea7a780df00af32bc29e63badca80e9b2e443a87
