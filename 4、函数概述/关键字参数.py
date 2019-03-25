'''
概念：允许参数调用时参数的顺序与定义时不一致
'''
def myprint(str,age):
    print(str,age)
#使用关键字参数
myprint(age=18,str='hailong is good')