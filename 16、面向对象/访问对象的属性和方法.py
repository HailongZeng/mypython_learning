class Person(object):

    name=''
    age=0
    height=0
    weight=0

    def run(self):
        print('run')
    def eat(self,food):
        print('eat '+food)
    def openDoor(self):
        print('我已经打开了冰箱门')
    def fillElephant(self):
        print('我已经将大象装进了冰箱了')
    def closeDoor(self):
        print('我已经关闭了冰箱')

per=Person()

'''
访问属性
格式：对象名.属性名
赋值：对象名.属性名=新值
'''
per.name='tom'
per.age=18
per.height=160
per.weight=80
print(per.name,per.age,per.height,per.weight)

'''
访问方法
格式：对象名.方法名(参数列表)  即使参数列表为空，小括号也不能省略
'''
per.openDoor()
per.eat('apple')

#问题：目前来看Person创建的所有对象属性都是一样的
per2=Person()
print(per2.age)
per3=Person()
print(per3.age)