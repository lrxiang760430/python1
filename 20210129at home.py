#20210129at home
#以下为字典内容的编程学习
"""
state={"China":"BeiJing","USA":"Washington","Japan":"Tokyo","England":"NewYork"}
state["England"]="London"
state["Australia"]="Canberra"
print (state)
"""


state={"China":"Beijing","USA":"Washington","Japan":"Tokyo","England":"London"}
for i in state:
    print(i +" " + state[i])