'''
turtle模块是一个简单的绘图模块
提供一个小海龟，可以把它理解为一个机器人，只能听得懂有限的命令

绘图窗口的原点(0,0)在正中间，默认海龟的方向是右侧

运动命令
forward(d)   向前移动d长度
backward(d)  向后移动d长度
right(d)     向右转动d度
left(d)      向左转动d度
goto(x,y)    移动到坐标为(x,y)的位置
speed(speed) 画笔绘制的速度[0,10]

画笔控制命令
hideturtle()       隐藏海龟
showturtle()       显示海龟
up()               画笔抬起，在移动时不会绘图
down()             画笔落下，移动会绘图
setheading(d)      设置海龟的朝向
home()             设置当前画笔位置为原点，朝向东
setx()             将当前x轴移动到指定位置
sety()             将当前y轴移动到指定位置
pensize(d)         画笔的宽度
pencolor(colorstr) 画笔的颜色
circle(r,steps=e)  绘制一个圆形，r为半径，e为次数
dot(r)             绘制一个指定直径和颜色的原点


画笔填充命令
begin_fill()        开始填充
fillcolor(colorstr) 设置填充颜色
end_fill()          结束填充
filling()           返回当前是否在填充状态

全局控制命令
done()             程序继续执行
undo()             撤销上一次的动作
reset()            恢复所有设置，清空窗口，重置turtle状态
clear()            清空窗口，不会重置turtle是否可见
stamp()            复制当前图形
isvisible()        返回当前turtle
screensize(width,height,bg)    设置turtle窗口的宽和高以及背景颜色
write(s,font=(“font_name”,font_size,”font_type”))  写文本，s为文本内容，font是字体的参数，里面分别为字体名称，大小和类型；
'''
#导入turtle库
import turtle

turtle.screensize(800,600)

turtle.speed(5)
turtle.forward(100)
turtle.right(45)
turtle.goto(-100,-200)
turtle.up()
turtle.goto(-100,100)
turtle.down()
turtle.pencolor("red")
turtle.pensize(10)
turtle.forward(30)
turtle.setheading(50)
#turtle.reset()
#turtle.clear()
turtle.circle(50,steps=5)

turtle.goto(150,100)
turtle.begin_fill()
turtle.fillcolor("blue")
turtle.circle(50)
turtle.end_fill()

turtle.forward(50)
turtle.undo()
turtle.hideturtle()
turtle.isvisible()

turtle.done()
