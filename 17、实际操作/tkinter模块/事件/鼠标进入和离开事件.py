import tkinter

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('600x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离
'''
<Enter> 鼠标光标进入控件时事件触发
<Leave> 鼠标光标离开控件时事件触发
'''
label = tkinter.Label(win, text='hailong is a handsome man', bg='red')
label.pack()
def func(event):
    print(event.x, event.y)
#label.bind('<Enter>', func)
label.bind('<Leave>', func)

win.mainloop() #进入消息循环