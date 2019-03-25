'''
self代表类的实例，而非类
哪个对象调用方法，那么该方法中的self就代表哪个对象

self.__class__代表类名
'''
class Person(object):
    def run(self):
        print('run')
    def eat(self,food):
        print('eat'+food)
    def say(self):
        print('Hello, my name is %s, I am %d years old'%(self.name,self.age))
        print(self.__class__)
        p=self.__class__('tt',30,180,80)
        print(p)
    #self不是关键字，换成其他标识符也是可以的,但是一般最好使用self
    def play(a):
        print('play '+a.name)
    def __init__(self,name,age,height,weight):   #在__init__里面定义属性
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
per1=Person('tom',20,160,80)
per1.say()
per1.play()

per2=Person('John',22,170,80)
per2.say()