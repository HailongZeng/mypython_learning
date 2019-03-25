'''
概念：能处理比定义时更多的参数
'''
#加了星号（*）的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，它就是一个空元组
def func(name,*args):
    print(name)
    print(type(args))
    for x in args:
        print(x)
func('Hailong','good','nice','handsome')

def mySum(*l):
    sum=0
    for i in l:
        sum+=i
    return sum
print(mySum(1,2,3,4,5,6))


#**代表键值对的参数字典，和*所代表的意义类似
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))
func2(x=1,y=2,z=3)  #必须传关键字参数，因为kwargs是一个字典


def func3(*args,**kwargs):   #可以传入任何类型参数
    pass  #代表一个空语句

