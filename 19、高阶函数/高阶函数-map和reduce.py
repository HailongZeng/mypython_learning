#Google 文章

#python内置了map()和reduce()函数

#map()
#原型   map(fn,lsd)
#参数1是函数
#参数2是序列
#功能：将传入的函数依次作用在序列中的每一个元素并把结果作为一个新的iterator返回

#将单个字符转换成对应的字面量整数
def chr2int(chr):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[chr]
list1 = ['2','1','6','5']
res = map(chr2int, list1) #chr2int('2')/chr2int('1')/chr2int('6')/chr2int('5')
print(res)
#print(list(res))
print(tuple(res))

#将整数元素的序列转换为字符串类型
#[1,2,3,4]——>['1','2','3','4']
l = map(str, [1,2,3,4])
print(list(l))



#reduce(fn,lsd)
#参数1为函数
#参数2位列表
#功能：一个函数作用在序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素累计运算
#reduce(f,[a,b,c,d])
#f(f(f(a,b),c),d))
#求一个序列的和
list2 = [1,2,3,4,5]
#1+2
#1+2+3
#1+2+3+4
#1+2+3+4+5
#使用reduce函数前需要引入库
from functools import reduce
def mySum(a, b):
    return a + b
r = reduce(mySum,list2)
print(r)



#将字符串转换成对应字面量数字
def str2int(str):
    def fc(x, y):
        return x*10+y
    def fs(chr):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[chr]
    return reduce(fc, map(fs, list(str)))
print(str2int('12367'))


'''
#自定义map函数（简单功能）
def myMap(func, li):
    resList = []
    for parase in li:
        res = func(parase)
        resList.append(res)
    return resList
def chr2int(chr):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[chr]
list1 = ['2','1','6','5']
res = myMap(chr2int, list1) #chr2int('2')/chr2int('1')/chr2int('6')/chr2int('5')
print(res)
'''