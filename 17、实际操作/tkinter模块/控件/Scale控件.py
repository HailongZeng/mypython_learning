import tkinter


win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('400x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

'''
供用户通过拖拽指示器改变变量的值，可以水平，也可以竖直
tkinter.HORIZONTAL  水平
tkinter.VERTICAL    竖直
length    水平时表示宽度，竖直时表示高度
tickinterval 显示值将会为该值的倍数，如果没有该命令，默认只有from_的值
'''
scale = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=20, length=200)
scale.pack()

#设置值，即刚进入窗口的值
scale.set(20)

#取值
def showNum():
    print(scale.get())

tkinter.Button(win, text='按钮', command=showNum).pack()


win.mainloop() #进入消息循环