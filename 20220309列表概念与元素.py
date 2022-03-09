list1=[2021,5.12,'Huawei',True,None,[1,2,3]]
list2=[]
print(list1)
print(list2)
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[0:4]) #从list[0]顺序提取到list[3],共4个元素，list[4]是不包括的
#即左闭右开，左边的数字是包含的，右边的数字不包含
print(list1[2:5])

print(list1[::2])

print(list1[-1])
print(list1[5])
print(list1[len(list1)-1])
print(len(list1)) #列表的长度为6，说明列表中有6个元素
#但是需要认识到列表的排序是从0开始的

print(list1[5][0])
print(list1[5][1])
print(list1[5][2])
#print(list1[5][4])

#列表方法与函数
range(5)
print(range(5))
range1=range(5)
print(type(range1))

list3=list(range1)
print(list3)

for i in range(10):
	print(i)

for i in range(1,4):
	print(i)

for i in range(0,20,3):
	print(i)

switch_modes=['3700','5700','9303','9306','9312','9303']
print(switch_modes.index('9303'))


interface=[]
interface.append('Gi0/0/1')
print(interface)
interface.append('Gi0/0/2')
print(interface)
interface.insert(0,'Gi0/0/5')
print(interface)
interface.insert(1,'Gi0/0/3')
print(interface)

#print(interface.pop)
#interface.pop()
interface.pop(0)
print(interface)

a='1213241546121213'
print(a.count('1'))
vendors=['Cisco','Juniper','Huawei','Huawei','H3C','Cisco']
print(vendors.count('Huawei'))