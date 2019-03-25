#from.....import......语句
#作用：从模块中导入一个指定的部分到当前命名空间
#格式：from name(模块名) import name1(模块中的函数名)[,name2[,......namen]]
from 自定义一个模块 import sayGood,sayNice
'''
程序内容的函数可以将模块中的同名函数覆盖掉
def sayGood():
    print('******')
'''
sayGood()  #前面不需要加模块名
sayNice()
