import tkinter

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('600x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

'''
label = tkinter.Label(win, text='hailong is a handsome man', bg='red')
#设置焦点
label.focus_set()
label.pack()

def func(event):
    print('event.chr =', event.char)  #返回按键对应字符
    print('event.keycode =', event.keycode) #返回按键字符对应的ASCII码

label.bind('<Key>', func)
'''
def func(event):
    print('event.chr =', event.char)  #返回按键对应字符
    print('event.keycode =', event.keycode) #返回按键字符对应的ASCII码
win.bind('a', func)  #只有按'a'时事件触发

win.mainloop() #进入消息循环