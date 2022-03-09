dict={'Vendor':'Cisco','Model':'WS-C3750E-480D-S','Ports':48,'IOS':'12.2(55)SE12','CPU':36.3}
print(dict)
print(dict['Vendor'])
print(dict['CPU'])  #通过键，获取值
dict['CPU']=80
print(dict['CPU'])
dict['num_of_devices']=10
print(dict)
print(len(dict))
print(dict.keys()) #返加字典所有的键
print(dict.values()) #返加字典所有的值
