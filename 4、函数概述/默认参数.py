'''
概念：调用函数时，如果没有传递参数，那么则使用默认参数
'''
#以后要用默认参数，最好将默认参数放在最后
def myprint(age,str='hailong is good'):
    print(str,age)
myprint(18)