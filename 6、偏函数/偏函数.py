#偏函数理论上不用自定义
import functools  #可以帮助我们生成一个偏函数

print(int('1010',base=2))  #base表示进制的意思

#偏函数
def int2(str,base=2):
    return int(str,base=2)
print(int2('1011'))

#把一个参数固定住，形成一个新的函数
int3=functools.partial(int,base=2)
print(type(int3))
print(int3('111')