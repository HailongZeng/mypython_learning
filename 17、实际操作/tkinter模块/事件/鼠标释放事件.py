import tkinter

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('600x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离
'''
<ButtonRelease-1> 鼠标左键释放事件
<ButtonRelease-2> 鼠标中键(滚轮)释放事件
<ButtonRelease-3> 鼠标右键释放事件
'''
label = tkinter.Label(win, text='hailong is a handsome man', bg='red')
label.pack()
def func(event):
    print(event.x, event.y)
label.bind('<ButtonRelease-1>', func)

win.mainloop() #进入消息循环