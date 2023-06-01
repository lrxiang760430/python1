import pymysql       ##PyMySQL是在 Python3.x 版本中用于连接 MySQL 服务器的一个库
import pandas as pd  ##Pandas是Python的一个数据分析包 导入panda命名为pd
from sqlalchemy import create_engine ## 导入引擎


file = r'c:/tools/工单/网络类工单-0530.xlsx'    ## 文件
df = pd.read_excel(file) ## 读文件
print(df)


 ## 连接数据库
 #pip install mysql-connector-python 需要提前安装这个库
engine = create_engine("mysql+mysqlconnector://root:Wbzlrx760430!@192.168.1.78:3306/工单") ## ****代表你的数据库密码
#engine=create_engine('mysql+mysqlconnector://root:Wbzlrx760430!@localhost:3306/gd')
df.to_sql('20230530',con=engine,if_exists='replace',index=False)  ##导入数据库，如果存在就替换