'''
概念：是一个闭包，把一个函数当做参数返回一个替代版的函数，本质上就是一个返回函数的函数
'''

'''
#简单的装饰器
def func1():
    print('Hailong needs to learn a lot of things')

def outer(func):
    def inner():
        print('************')
        func()
    return inner

#outer(func1)()
#f是函数func1的加强版本，是innner()
f=outer(func1)
f()
'''

'''
#复杂一点的装饰器
def say(age):
    print('Hailong is %d years old'%(age))
say(-10)


def outer(func):
    def inner(age):
        if age<0:
            age=0
        func(age)
    return inner

say=outer(say)
say(-10)
'''

'''
#使用@符号将装饰器应用到函数
#python2.4开始支持@符号
def outer(func):
    def inner(age):
        if age<0:
            age=0
        func(age)
    return inner
@outer   #相当于say=outer(say)
def say(age):
    print('sunck is %d years old'%(age))
say(-10)
'''

'''
#通用装饰器:传参参数不固定---不定长参数
def outer(func):
    def inner(*args,**kwargs):
        #添加修改的功能
        print('&&&&&&&&&&&&')
        func(*args,**kwargs)
    return inner
@outer
def say(name,age):  #函数的参数理论上是无限制的，但实际上最好不要超过6、7个
    print("%s is %d years old"%(name,age))
say("Hailong",18)
'''