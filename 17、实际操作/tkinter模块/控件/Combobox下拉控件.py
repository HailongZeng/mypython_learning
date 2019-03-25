import tkinter
from tkinter import ttk

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('400x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

#绑定变量
cv = tkinter.StringVar()
com = ttk.Combobox(win, textvariable=cv)
com.pack()

#设置下拉数据
com['value'] = ('黑龙江', '吉林', '辽宁')

#设置默认值
com.current(0)

#绑定事件
def func(event):
    print(com.get())
    print(cv.get())
com.bind('<<ComboboxSelected>>', func)

win.mainloop() #进入消息循环
