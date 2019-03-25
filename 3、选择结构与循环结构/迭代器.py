from collections.abc import Iterable
from collections.abc import Iterator
'''
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象
(Iterable)，可以用isinstance()去判断一个对象是否为Iterable对象

可以直接作用于for的数据类型：
1、序列数据类型：如list、tuple、dict、set、string
2、generator，是包括生成器和带yield的generator function


'''
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance("",Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(1,Iterable))

'''
迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
直到最后跑出一个StopIteration错误表示无法继续返回下一个值。

可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator对象)

可以使用isinstance()函数判断一个对象是否为Iterator对象
'''
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance("",Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance(1,Iterator))

l=(x for x in range(5))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
#print(next(l))  #报错，StopIteration

#转成Iterator对象  iter()
a=iter([1,2,3,4,5])
print(next(a))
print(next(a))

print(isinstance([1,2,3,4,5],Iterator))
print(isinstance(iter([1,2,3,4,5]),Iterator))

endstr="end"
str=""

for line in iter(input,endstr):
    str+=line+"\n"

print(str)