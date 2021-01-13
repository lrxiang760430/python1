import matplotlib.pyplot as plt
plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)
plt.subplot(2,2,4)

plt.show()

"""
import pandas as pd
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
#plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
#data=pd.read_csv(r'C:\Users\lrx\Downloads\yequ(2)\书店图书销量和广告费用.csv')
#data=pd.read_csv(r'C:\Users\lrx\Downloads\yequ(2)\每月曝光量和转化率.csv')
#data=pd.read_csv(r'C:\Users\lrx\Downloads\yequ(2)\书店每月销量数据.csv')
data=pd.read_csv(r'C:\Users\lrx\Downloads\yequ(2)\书店每月销量数据百分比.csv')
print(data)
data.plot.bar("month",["一楼","二楼","三楼"],stacked=True)
plt.show()

data.plot.bar("month",["first_floor","second_floor","third_floor"])
plt.show()

plt.bar(data["month"],data["exposure"])
plt.twinx()
plt.plot(data["month"],data["CVR"])
plt.show()

plt.scatter(data["ads_fee"],data["sales"],color="green")
plt.xlabel("广告费用")
plt.ylabel("销量")
plt.show()
"""