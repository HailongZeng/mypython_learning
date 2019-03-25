'''
score=int(input("请输入分数:"))
grade=[]
if score<60:
    grade="不及格"
elif score<80:
    grade="及格"
elif score<90:
    grade="良好"
else:
    grade="优秀"
print("分数是{0},等级是{1}".format(score,grade))
'''

'''
num=0
while num<=10:
    print(num,end='\t')
    num+=1
'''

'''
for x in range(1,10):
    for y in range(1,10):
        if x>=y:
            print("{}*{}={}".format(x,y,x*y),end='\t')
    print()

while True:
    a=input("请输入一个字符（输入Q或q时退出):")
    if a=="q" or a="Q":
        print("循环结束，退出")
        break
    else:
        print(a)
'''

'''
Num=0
SalarySum=0
salarys=[]
while True:
    s=input("请输入员工的薪资(按Q或q结束):")

    if s.upper()=='Q':
        print("录入完成，退出")
        break
    if float(s)<0:
        continue
    Num+=1
    salarys.append(float(s))
    SalarySum+=float(s)
print("员工数{0}".format(Num))
print("录入薪资:",salarys)
print("平均薪资{0}".format(SalarySum/Num))
'''

'''
SalarySum=0
salarys=[]
for i in range(4):
    s=input("请输入4位员工的薪资(按Q或q结束):")

    if s.upper()=='Q':
        print("录入完成，退出")
        break
    if float(s)<0:
        continue

    salarys.append(float(s))
    SalarySum += float(s)

else:
    print("您已经全部录入4位员工的薪资")

print("录入薪资:",salarys)
print("平均薪资{0}".format(SalarySum/4))
'''

'''
#绘制不同颜色的同心圆
import turtle
t=turtle.Pen()
t.width(10)
my_colors=("red","green","yellow","black")
for i in range(5):
    t.penup()
    t.goto(0,-50*i)
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(50*(i+1))
turtle.done()   #程序执行完，窗口仍存在
'''

'''
#绘制18*18的棋盘
import turtle
t=turtle.Pen()
for i in range(19):
    t.penup()
    t.goto(-200,200-20*i)
    t.pendown()
    t.forward(360)
t.right(90)  #将画笔向右转动90度
for i in range(19):
    t.penup()
    t.goto(-200+20*i,200)
    t.pendown()
    t.forward(360)
turtle.done()
'''

'''
#eval()函数
dict1=dict(a=100,b=200)
d=eval("a+b",dict1)
print(d)
'''

'''
#递归函数计算阶乘
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
        
print(factorial(5))
'''

'''
#测试nonlocal、global关键字的用法
def outer():
    b=10

    def inner():
        nonlocal b  #声明外部函数的局部变量
        print("inner b:",b)
        b=20

    inner()
    print("outer b:",b)

outer()
'''

'''
#测试LEGB规则
str="global"
def outer():
    str="outer"

    def inner():
        str="inner"
        print(str)

    inner()

outer()
'''