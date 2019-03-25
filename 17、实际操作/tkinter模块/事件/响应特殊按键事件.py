import tkinter

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('600x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离
'''
<Shift>   响应电脑上的Shift按键的事件
<Shift_L> 只响应电脑上左边的Shift按键的事件
<Shift_R> 只响应电脑上右边的Shift按键的事件
<F5>
<Return>     回车
<BackSpace>  退格

注意：对控件进行事件绑定之前要进行焦点设置，控件名.focus_set()；而对窗口绑定时不需要提前进行焦点设置
'''
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
win.bind('<Shift_L>', func)

win.mainloop() #进入消息循环