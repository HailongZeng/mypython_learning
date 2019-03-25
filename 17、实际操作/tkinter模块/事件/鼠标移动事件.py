import tkinter

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('600x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

'''
<B1-Motion>  左键移动
<B2-Motion>  中键(滚轮)移动
<B3-Motion>  右键移动
'''
label = tkinter.Label(win, text='hailong is a handsome man')
label.pack()
def func(event):
    print(event.x, event.y)
label.bind('<B1-Motion>', func)
win.mainloop() #进入消息循环