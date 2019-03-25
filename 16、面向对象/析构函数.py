'''
析构函数：__del__()  释放对象是自动调用

'''
class Person(object):
    def run(self):
        print('run')
    def eat(self,food):
        print('eat'+food)
    def __init__(self,name,age,height,weight):   #在__init__里面定义属性
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def __del__(self):   #1、在程序执行完之后释放对象
        print('这里是一个析构函数')
per=Person('tom',20,180,70)
#del per  #2、手动释放对象

#print(per.age)  #对象释放之后不存在了

#3、在函数里定义的对象会在函数结束时自动释放,这样可以用来减少内存空间的浪费
def func():
    per2=Person('aa',21,178,65)
func()


while 1:
    pass

