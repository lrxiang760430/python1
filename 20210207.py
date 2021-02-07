#20210207.py
<<<<<<< HEAD
import pandas as pd
import pymysql
from sqlalchemy import create_engine
#engine=create_engine('10.66.66.7','root','Wbzlrx760430!','Syslog')
engine=create_engine('mysql+pymysql://root:Wbzlrx760430!@10.66.66.7:3306/Syslog')
sql="SELECT * FROM SystemEvents WHERE FromHost LIKE 'nongwang_zubo'"
df=pd.read_sql_query(sql,engine)
print(df)
df.to_csv('nw0207.csv')
=======
"""
minThree=min(9,99,999)
print(minThree)


def sum(number):
    result=0
    for i in number:
        result=result+i
    return result 

number=[6,17,6,11,14,14,0,9]
print(sum(number))

def Duration(Sleep,GetUp):
    return(24-Sleep+GetUp)

TimePoint=[(24,8),(22,7),(23,8),(23,6),(22,8),(22,6),(24,6)]



for i in TimePoint:
    SleepDuration=Duration(i[0],i[1])
    print(SleepDuration)

"""

def Duration(Sleep,GetUp=7):
    return(24-Sleep+GetUp)

TimePoint=[24,23,24,22,24,24,24]
for i in TimePoint:
    SleepDuration=Duration(i)
    print(SleepDuration)

def Grade(Title,*Score):
    Count=0
    TotalScore=0
    for i in Score:
        TotalScore=TotalScore+i 
        Count=Count+1
    Average=TotalScore//Count
    print(Title)
    print('*'*Average)

Grade('The Little Prince',5,5,4,3,5,5)
Grade('The Moon And Sixpence',5,3,2,5)


tentimes=lambda x:10*x
tentimes(7)
print(tentimes(7))


dollar=lambda x:x/6.681
pound=lambda x:x/8.8162
yen=lambda x:x/0.06052

print(dollar(10000))
print(pound(10000))
print(yen(10000))
>>>>>>> 2b65d795a3f0a7207ce3107f0143dd5afd5e50fd
