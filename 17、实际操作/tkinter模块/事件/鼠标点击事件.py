import tkinter

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('600x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

'''
<Button-1> 单击鼠标左键
<Button-2> 单击鼠标中键(滚轮)
<Button-3> 单击鼠标右键
<Double-Button-1> 双击鼠标左键
<Double-Button-2> 双击鼠标中键(滚轮)
<Double-Button-3> 双击鼠标右键
<Triple-Button-1> 三击鼠标左键
<Triple-Button-2> 三击鼠标中键(滚轮)
<Triple-Button-3> 三击鼠标右键
'''
def func(event):  #event是事件对象，具有事件属性
    print(event.x, event.y)

#button1 = tkinter.Button(win, text='leftmouse button')
button1 = tkinter.Label(win, text='leftmouse button')  #随意用控件去定义button1
button1.bind('<Button-1>', func) #bind给控件绑定事件
button1.pack()

win.mainloop() #进入消息循环