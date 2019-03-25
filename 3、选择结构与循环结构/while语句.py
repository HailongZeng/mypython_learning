'''
while语句：

格式：
while 表达式：
    语句

逻辑：当程序执行到while语句时，首先计算"表达式"的值，如果"表达式"的值为假，则结束整个while语句。如果"表达式"的值为真，
则执行"语句"，执行完"语句"再去计算"表达式"的值。如果"表达式"的值为假，则结束整个while语句。如果"表达式"的值为真，
则执行"语句"，执行完"语句"再去计算"表达式"的值。如此循环往复，直到表达式的值为假才结束。
'''

'''
死循环：表达式永远为真的循环
'''

'''
while-else语句：

格式：
while 表达式：
    语句1
else:
    语句2

逻辑：在条件语句（表达式）为False时执行else中的"语句2"
'''

'''
#计算1+2+3+...+100
sum=0
num=1
while num<=100:
    sum+=num
    num+=1
print("sum = %d" % (sum))
'''

'''
#打印某字符串
str="Hailong is very kind"
index=0
while index<len(str):
    print("str[%d] = %s" % (index,str[index]))
    index+=1
'''

