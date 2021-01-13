# -*- coding: utf-8 -*-  
#coding=gbk
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
#plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
data=pd.read_csv(r'C:\Users\lrx\Downloads\yequ(2)\书店每月销量数据.csv')
print(data)
#plt.plot(data["month"],data["sum"])
#plt.plot(data["month"],data["sum"],color="skyblue")
#plt.plot(data["month"],data["sum"],color="orange",marker="*")
plt.plot(data["month"],data["sum"],color="orange",marker="o",label="每月总销量")
plt.xlabel("月份")
plt.ylabel("销量")
plt.title("2019年8月至2020年7月书店每月销量走势")
plt.legend()

plt.show()