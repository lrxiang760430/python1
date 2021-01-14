import pandas as pd 
df2019=pd.read_csv(r'C:\Users\lrx\Downloads\Lily(1)\2019年下半年订单表.csv')
df2020=pd.read_csv(r'C:\Users\lrx\Downloads\Lily(1)\2020年上半年订单表.csv')
dfEV=pd.read_csv(r'C:\Users\lrx\Downloads\Lily(1)\Exposure.csv')


print(df2019)
print(df2020)
print(dfEV)

dfYear=pd.concat([df2019,df2020])
dfYear["下单时间"]=pd.to_datetime(dfYear["下单时间"])

dfnewYear=dfYear.set_index("下单时间")

dfSales=dfnewYear["数量"].groupby(dfnewYear["商品ID"]).resample("M").sum()

dfnewSales=dfSales.reset_index()
#print(dfYear)
dfnewSales["下单时间"]=dfnewSales["下单时间"].dt.strftime("%Y-%m")
print(dfnewSales)

dfTotal=pd.merge(dfEV,dfnewSales,left_on=["ID","Month"],right_on=["商品ID","下单时间"])

print(dfTotal)
df=dfTotal[["Month","ID","Exposure","数量"]]
df["购买转化率"]=df["数量"]/df["Exposure"]
print(df)

plt.rcParams["font.sans-serif"] = "Arial Unicode MS"

#画出第一个商品（2，3，1）


"""
以下为完整的代码
# 导入模块
import pandas as pd
import matplotlib.pyplot as plt
# 读取csv文件
df2019= pd.read_csv("/Users/Lily/2019年下半年订单表.csv")
df2020= pd.read_csv("/Users/Lily/2020年上半年订单表.csv")
# 使用pd.concat()函数纵向合并df2019、df2020
dfYear= pd.concat([df2019,df2020])

# 将"下单时间"这列字符串类型的数据转化成时间类型
dfYear["下单时间"] = pd.to_datetime(dfYear["下单时间"])
# 将"下单时间"这列设置成新的索引
dfnewYear = dfYear.set_index("下单时间")
# 使用groupby()函数,将「订单数据表」按「商品ID」进行分组，「按月采样」计算出订单「数量」的和
dfSales = dfnewYear["数量"].groupby(dfnewYear["商品ID"]).resample("M").sum()
# 还原索引index
dfnewSales = dfSales.reset_index()
# 将"下单时间"这列设置成“年-月”的字符串类型
dfnewSales["下单时间"] = dfnewSales["下单时间"].dt.strftime("%Y-%m")

# 读取csv文件
dfEV= pd.read_csv("/Users/Lily/Exposure.csv")

# 使用pd.merge()函数，横向关联dfEV、dfnewSales，指定左边DataFrame的关联列为["ID","Month"]，右边DataFrame的关联列为["商品ID", "下单时间"]
dfTotal = pd.merge(dfEV, dfnewSales, left_on=["ID","Month"],right_on = ["商品ID", "下单时间"])

# 索引出dfTotal中"Month"、"ID"、"Exposure"、"数量"这几列
df = dfTotal[["Month","ID","Exposure","数量"]]

# 得到“购买转化率”并添加在df最后一列
df["购买转化率"] = df["数量"]/df["Exposure"]


# 可视化
# 定义字体
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"

# 画出第一个商品
# 使用plt.subplot()函数分割出画布的第一部分 
plt.subplot(2,3,1)
# 布尔索引出第一个商品的数据
df1=df[df["ID"]==700010]
# 以df1["Month"]为横坐标，df1["Exposure"]为纵坐标，使用plt.bar()函数画出柱状图并使用color参数设置颜色为红色"red"
plt.bar(df1["Month"],df1["Exposure"],color="r")
# 使用plt.xticks()函数将x轴刻度设置为90度
plt.xticks(rotation=90)
# 使用plt.twinx()函数连接“折线图+柱状图”
plt.twinx()
# 以df1["Month"]为横坐标、df1["购买转化率"].round(2)保留2位小数为纵坐标，使用plt.plot()函数画出折线图并使用marker参数设置标记样式为圆点"o"
plt.plot(df1["Month"],df1["购买转化率"].round(2),marker="o")
# 使用plt.title()函数，将图表标题设置为"700010"
plt.title(700010)
   
# 以同样的方式画出剩下的商品

# 画出第二个商品

plt.subplot(2,3,2)
df2=df[df["ID"]==700011]
plt.bar(df2["Month"],df2["Exposure"],color="r")
plt.xticks(rotation=90)
plt.twinx()
plt.plot(df2["Month"],df2["购买转化率"].round(2),marker="o")
plt.title(700011)

# 画出第三个商品
plt.subplot(2,3,3)
df3=df[df["ID"]==700012]
plt.bar(df3["Month"],df3["Exposure"],color="r")
plt.xticks(rotation=90)
plt.twinx()
plt.plot(df3["Month"],df3["购买转化率"].round(2),marker="o")
plt.title(700012)

# 画出第四个商品
plt.subplot(2,3,4)
df4=df[df["ID"]==700013]
plt.bar(df4["Month"],df4["Exposure"],color="r")
plt.xticks(rotation=90)
plt.twinx()
plt.plot(df4["Month"],df4["购买转化率"].round(2),marker="o")
plt.title(700013)

# 画出第五个商品
plt.subplot(2,3,5)
df5=df[df["ID"]==700014]
plt.bar(df5["Month"],df5["Exposure"],color="r")
plt.xticks(rotation=90)
plt.twinx()
plt.plot(df5["Month"],df5["购买转化率"].round(2),marker="o")
plt.title(700014)

# 画出第六个商品
plt.subplot(2,3,6)
df6=df[df["ID"]==700015]
plt.bar(df6["Month"],df6["Exposure"],color="r")
plt.xticks(rotation=90)
plt.twinx()
plt.plot(df6["Month"],df6["购买转化率"].round(2),marker="o")
plt.title(700015)

# 可视化展示
# 使用plt.tight_layout()函数来调整子图布局
plt.tight_layout()
# 使用plt.show()函数显示图像
plt.show()

"""