'''
try......except......else
格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
except 错误码 as e:
    语句3
......
except 错误码 as e:
    语句n
else:
    语句e

注意：else语句可有可无；错误码可百度获得

作用：用来检测try语句块中的错误，从而让except语句捕获错误信息

逻辑：当程序执行到try-except-else语句
1、如果当try"语句t"执行出现错误，会匹配第一个错误，如果匹配上，就执行对应的语句1，若未匹配，继续向下匹配，直至匹配到
错误码为止，并输入相应错误码的语句。
2、如果try"语句t"执行出现错误，但是没有匹配的异常，错误将会被提交到上一层的try语句。或者到程序的最上层。
3、如果try"语句t"执行没有出现错误，执行else下的语句e。（前提是有else语句）
'''
try:
    #print(3/0)
    #print(num)
    print(3/1)
except NameError as e:
    print("没有定义该变量")
except ZeroDivisionError as e:
    print("除数为0了")
else:
    print("代码没有问题")
print("************")


#使用except而不使用任何的错误码
try:
    print(4/0)
except:
    print("程序出现了异常")


#使用except带着多种异常
try:
    print(5/0)
except (NameError,ZeroDivisionError) as e:
    print("出现了NameError或ZeroDivisionError异常")


#特殊
#1、错误其实是class(类)，所有的错误都继承父类BaseException,所以在捕获的时候，它捕获了该类型的错误，还把子类一网打尽
# BaseException是所有异常的基类，如果BaseException放在前面，则先执行BaseException对应的语句
try:
    print(5/0)
except BaseException as e:
    print("异常1")
except ZeroDivisioError as e:
    print("异常2")

#2、内存错误不能跳过
#3、跨越多层调用,main调用了func2，func2调用了func1,func1出现了错误，这时只要main捕获了错误就会捕获错误
def func1(num):
    print(1/num)
def func2(num):
    func1(num)
def main():
    func2(0)
try:
    main()
except ZeroDivisionError as e:
    print("********")


