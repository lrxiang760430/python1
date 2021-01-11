"""
# 导入pandas模块，简称pd
import pandas as pd

# 定义两个列表
GDP=[80855, 77388, 68024, 47251, 40471]
rank=[1, 2, 3, 4, 5]

# 使用Series构造函数，传入参数：列表GDP作为值，列表rank作为index
# 构造出的Series赋值给info
info = pd.Series( GDP , index = rank)

# 输出info这个Series
print(info)


import pandas as pd
data={'rank':[1,2,3,4],'GDP':[80855,77388,68024,47251]}
city=['GD','JS','SD','ZJ']

df=pd.DataFrame(data,index=city)
print(df)



# 导入pandas模块，简称pd
import pandas as pd 

# 定义一个字典data
data = {'name': ['May','Tony','Kevin'], 'score':[689,659,635]}
# 定义一个列表rank
rank = [1,2,3]

# TODO 使用pd.DataFrame()函数，传入参数：字典data作为value和columns，列表rank作为index
# 构造出的DataFrame赋值给performance
performance=pd.DataFrame(data,index=rank)

# 输出performance这个DataFrame
print(performance)


import pandas as pd 
data=pd.read_csv("tmdb_5000_credits.csv")

print(data)


import pandas as pd
data=pd.read_excel("在建工程明细表.xlsx",sheet_name="邹城",engine='openpyxl')

print(data)


import pandas as pd
data=pd.read_excel(r'G:\tools\yequ\2019年4月销售订单.xlsx',engine='openpyxl')

#import os
#print(os.getcwd)
print(data)


from datetime import datetime
start=datetime(2020,5,1,23,59,59)
end=datetime(2020,10,1)
timeSpan=end-start
print(timeSpan)
print(type(timeSpan))
"""
#! *-- coding:utf-8 --* 
import pandas as pd
data=pd.read_csv(r'G:\tools\mathorcup\训练用数据.csv')
print(data)
