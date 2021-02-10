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


