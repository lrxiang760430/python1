#20210208yq.py

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_information(self):
        print(f"{self.name}是一条{self.age}岁的狗")

    def sit(self):
        print(f"{self.name}蹲下了")

    def roll_over(self):
        print(f"{self.name}正在打滚")


my_dog=Dog("Judy",2)

my_dog.get_information()
my_dog.sit()
my_dog.roll_over()


class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"餐馆的名字是{self.restaurant_name}")
        print(f"餐馆的主营菜系是{self.cuisine_type}")

    def open_restaurant(self):
        print("餐馆正在营业中")

restaurant=Restaurant("全聚德","烤鸭")

restaurant.describe_restaurant()
restaurant.open_restaurant()

number=[8,1,1,8,1,1,8]
for i in number:
    print(i * "*")
