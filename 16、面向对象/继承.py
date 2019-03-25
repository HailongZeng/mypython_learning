'''
继承的作用：
1、简化了代码，减少冗余
2、提高了代码的健壮性
3、提高了代码的安全性
4、是多态的前提


缺点：耦合与内聚是描述类与类之间的关系的。耦合性越低，内聚性越高代码越好
'''
class Person(object):
    def __init__(self,name,age,money):
        self.name=name
        self.age=age
        self.__money=money #私有属性
    def setMoney(self):
        if money<0:
            money=0
        self.__money=money
    def getMoney(self):
        return self.__money

    def run(self):
        print('run')

    def eat(self,food):
        print('eat '+food)

class Student(Person):  #()中换成父类的类名
    def __init__(self,name,age,money,stuId):
        #调用父类(Person)中的__init__
        super(Student,self).__init__(name,age,money)
        #子类可以有自己独有的属性
        self.stuId=stuId
    #子类可以有自己独有的方法
    def stuFunc(self):
        print(self.__money)


stu=Student('tom',18,-10,'A53281581')
'''
print(stu.name,stu.age)
stu.run()
stu.eat('apple')
#stu.stuFunc()  #不能直接访问，因为__money是父类的私有属性
'''

print(stu.getMoney())