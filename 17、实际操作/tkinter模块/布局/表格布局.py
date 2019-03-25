import tkinter

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('600x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

label1 = tkinter.Label(win, text='good', bg='blue')
label2 = tkinter.Label(win, text='cool', bg='red')
label3 = tkinter.Label(win, text='nice', bg='pink')
label4 = tkinter.Label(win, text='handsome', bg='yellow')

#表格布局，grid(row=%d,column=%)
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=0, column=2)

win.mainloop() #进入消息循环