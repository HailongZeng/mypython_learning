import tkinter

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('600x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

label1 = tkinter.Label(win, text='good', bg='blue')
label2 = tkinter.Label(win, text='cool', bg='red')
label3 = tkinter.Label(win, text='nice', bg='pink')

#绝对布局，窗口的变化对label位置没有影响，place(x=%d, y=%d)
label1.place(x=10, y=10)
label2.place(x=50, y=50)
label3.place(x=100, y=100)

win.mainloop() #进入消息循环