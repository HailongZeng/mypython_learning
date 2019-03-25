import tkinter

def func():
    print('Hailong has to be outstanding in the final exam')

win = tkinter.Tk()
win.title('hailong')
win.geometry('400x400+200+20')


#创建按钮
button1 = tkinter.Button(win, text='按钮1', command=func, width=10, height=5)
button1.pack()

button2 = tkinter.Button(win, text='按钮2', command=lambda:print('Hailong has to control himself')) #匿名函数
button2.pack()

button3 = tkinter.Button(win, text='按钮3', command=win.quit)  #退出窗口
button3.pack()

win.mainloop()