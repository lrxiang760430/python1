# -*- coding: utf-8 -*-  
#coding=gbk
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
#plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
data=pd.read_csv(r'C:\Users\lrx\Downloads\yequ(2)\sdmysssl.csv')
print(data)
#plt.plot(data["month"],data["sum"])
#plt.plot(data["month"],data["sum"],color="skyblue")
#plt.plot(data["month"],data["sum"],color="orange",marker="*")
plt.plot(data["month"],data["sum"],color="orange",marker="o",label="Ã¿ÔÂ")
plt.legend()

plt.show()