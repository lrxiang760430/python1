# 导入模块
import pandas as pd
import matplotlib.pyplot as plt
# 读取csv文件
cheshi = pd.read_csv(r"G:\tools\mathorcup\1.csv",encoding="ANSI")
print(cheshi)
cheshi.info()
print(cheshi.info())
print(cheshi.isnull().values==True)
#cheshi["日期"]=pd.to_datetime(cheshi["日期"], format='%d-%m-%y')
print(cheshi[cheshi.duplicated()==True])
