'''
#1、从控制台输入一个年份，判断是否是闰年
#能被4整除但是不能被100整除 或者 能够被400整除
year=int(input("请输入一个年份："))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,"是闰年")

else:
    print(year,"不是闰年")
'''

'''
#2、打印出所有三位数中的水仙花数
num1=100
while num1<1000:
    if num1==pow(num1%10,3)+pow(num1//10%10,3)+pow(num1//100,3):
        print(num1) #num1%10表示个位数，num1//10%10表示十位数，num1//100表示百位数
    num1+=1
'''

'''
#3、返回出五位数中有多少个回文数
num2=10000
while num2<100000:
    if num2%10==num2//10000 and num2//10%100==num2%10000//1000:
        print(num2)
    num2+=1
'''

'''
#4、从控制台输入一个数，判断是否是质数
num3=int(input("请输入一个数:"))
num4=1
count=0
while num4<=num3:
    if num3%num4==0:
        count+=1
    num4+=1
if count==2:
    print("%d是质数"% (num3))
else:
    print("%d不是质数" % (num3))
'''

'''
#5、从控制台输入一个数，分解质因数
num5=int(input("请输入一个数:"))
num6=1
count=0 #计算因数的个数
count1=0
a=[] #存储因数
b=[] #存储质因数
while num6<=num5:
    if num5%num6==0:
        a.append(num6)
        count+=1
    num6+=1
while count1<count:
    num7 = 1
    count2=0
    while num7<=a[count1]:
        if a[count1]%num7==0:
            count2+=1
        num7+=1
    if count2==2:
         b.append(a[count1])
    count1+=1
print(b)
'''

'''
#更简单的逻辑
num=int(input("请输入一个数:"))
i=2
while num!=1:
    if num%i==0:
        print(i)
        num//=i
    else:
        i+=1
'''

'''
#6、从控制台输入一个字符串，返回字符串的长度，不能使用len内置函数
str1=input("请输入一个字符串:")
num8=0
while str1[num8]!=None:
    num8+=1
    if num8==len(str1):
        break
print(num8)
'''

'''
#7、从控制台输入一个字符串，返回这个字符串中有几个单词，并打印出这几个单词
str2=input("请输入一个字符串:")
str3=str2.strip() #将字符串前后空格截掉
index=0
index1=0
count=0
while index<len(str3):
    while str3[index]!=" ":
        index+=1
        if index==len(str3):
            break #结束while循环

    print(str3[index1:index]) #跳过空格下标，打印出每个单词
    count+=1

    if index==len(str3):
        print(count)
        break  #结束，跳出最外层while循环

    while str3[index]==" ":
        index+=1
    index1=index #记录跳过空格新单词开始处下标
'''

'''
#8、从控制台输入一个字符串，返回这个字符串中所有数字字符的和
str4=input("请输入一个字符串:")
num10=0
sum=0
while num10<len(str4):
    #if str4[num10]>="0" and str4[num10]<="9":
    if str4[num10].isdigit():
        sum+=int(str4[num10])
    num10+=1
print("sum  = %d" % (sum))
'''

'''
#9、字符串比较大小
#从第一个字符开始比较，谁的ASCII值大谁就大，如果相等会比较下一个字符的ASCII值大小，那么谁的值大谁就大
print("Hai">"Hae")
'''

'''
#10、打印99乘法表
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print("%d X %d = %d" % (i,j,i*j),end="\t")
    print()
'''

'''
#11、输入两个数，求这两个数的最大公约数
a=int(input("请输入一个数:"))
b=int(input("请输入另一个数:"))
c=[]
num=1
while num<=a and num<=b:
    if a%num==0 and b%num==0:
        c.append(num)
    num+=1
print(max(c))
'''

'''
#12、输入一个字符串，将字符串中的大写字母转小写，小写字母转大写,注意：不允许使用swapcase方法
str=input("请输入一个字符串:")
print(str.swapcase())
'''

'''
#13、随机生成一个6位数的验证码
import random
for i in range(6):
    print(random.choice(range(10)),end="")
'''

'''
#14、用turtle模块绘制正方形，矩形，正方体、五角星、奥运五环、围棋棋盘、国际象棋棋盘

import turtle

turtle.screensize(1000,1000)

#绘制正方形
turtle.pencolor("red")
for i in range(3):
    turtle.forward(100)
    turtle.left(90)
turtle.forward(100)

turtle.clear() #删除图形

#绘制矩形
turtle.pencolor("blue")
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)

turtle.clear() #删除图形

#绘制正方体
turtle.pencolor("green")
for j in range(3):
    turtle.forward(100)
    turtle.left(90)
turtle.forward(100)

turtle.right(45)
turtle.forward(100)
turtle.right(135)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)

turtle.up()  #抬起画笔
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.down() #放下画笔

for k in range(2):
    turtle.right(45)
    turtle.forward(100)

turtle.clear() #删除图形

#绘制五角星
turtle.pencolor("yellow")
turtle.left(60)
for z in range(4):
    turtle.forward(200)
    turtle.right(144)
turtle.forward(200)

turtle.clear()  #删除图形

turtle.up()
turtle.home() #设置当前画笔位置为原点，朝向东
turtle.down()

#绘制奥运五环
turtle.pensize(10)

turtle.pencolor("red")
turtle.circle(50)
turtle.up()
turtle.forward(120)
turtle.down()

turtle.pencolor("blue")
turtle.circle(50)
turtle.up()
turtle.forward(120)
turtle.down()

turtle.pencolor("black")
turtle.circle(50)
turtle.up()
turtle.goto(60,-60)
turtle.down()

turtle.pencolor("yellow")
turtle.circle(50)
turtle.up()
turtle.forward(120)
turtle.down()

turtle.pencolor("green")
turtle.circle(50)

turtle.clear()  #删除图形

turtle.up()
turtle.home() #设置当前画笔位置为原点，朝向东
turtle.down()

#围棋棋盘
a=360
b=20
turtle.pensize(2)
for i in range(19):
    turtle.up()
    turtle.goto(-180, -180 + b * i)
    turtle.down()
    turtle.forward(a)
    i+=1

turtle.left(90)
for j in range(19):
    turtle.up()
    turtle.goto(-180+b*j, -180)
    turtle.down()
    turtle.forward(a)
    j+=1


for k in range(-1,2):
    for z in range(-1,2):
        turtle.up()
        turtle.goto(k*120,z*120)
        turtle.down()
        turtle.dot(8)
        
turtle.clear()  #删除图形

turtle.up()
turtle.home() #设置当前画笔位置为原点，朝向东
turtle.down()

#绘制国际象棋棋盘

turtle.done() #画图界面不退出，继续执行
'''

'''
#15、输入一个时间字符串，输出这个时间的下一秒
timeStr=input("请输入一个时间字符串:")

#12:23:23

timeList=timeStr.split(":")

h=int(timeList[0]) #时
m=int(timeList[1]) #分
s=int(timeList[2]) #秒

s+=1

if s==60:
    m+=1
    s=0
    if m==60:
        h+=1
        m=0
        if h==24:
            h=0

print("%.2d:%.2d:%.2d" % (h,m,s))
'''
'''
#人开枪射击子弹
'''
'''
人
类名：Person
属性：gun
行为：fire

枪
类名：Gun
属性：bulletBox
行为：shoot

弹夹
类名：BulletBox
属性：bulletCount
行为
'''
'''
#弹夹
class BulletBox(object):
    def __init__(self,count):
        self.bulletCount=count
class Gun(object):
    def __init__(self,bulletBox):
        self.bulletBox=bulletBox
    def shoot(self):
        if self.bulletBox.bulletCount==0:
            print('没有子弹了')
        else:
            self.bulletBox.bulletCount-=1
            print('剩余子弹:%d发'%(self.bulletBox.bulletCount))
class Person(object):
    def __init__(self,gun):
        self.gun=gun
    def fire(self):
        self.gun.shoot()
    def loadBullet(self,count):
        self.gun.bulletBox.bulletCount=count
#弹夹
bulletBox=BulletBox(5)

#枪
gun=Gun(bulletBox)

#人
per=Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

per.loadBullet(2)
per.fire()
per.fire()
per.fire()
'''
