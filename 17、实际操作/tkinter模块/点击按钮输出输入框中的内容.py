import tkinter

#创建窗口
win = tkinter.Tk()
win.title('Hailong')
win.geometry('400x400+200+0')

def showInfo():
    print(entry.get())  #获取输入框中的设置值

entry = tkinter.Entry(win, show='*')
entry.pack()

button = tkinter.Button(win, text='按钮', command=showInfo)
button.pack()

win.mainloop()