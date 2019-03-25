'''
值传递：传递的不可变类型（数字，字符串，元组）
'''
def func1(num):
    num=10
    return num
temp=20
func1(temp)  #num=temp,但是temp不变
print(temp)

'''
引用传递：传递的可变类型
list、dict、set是可变的
'''
def func2(lis):
    lis[0]=100
li=[1,2,3,4,5]
func2(li)
print(li)