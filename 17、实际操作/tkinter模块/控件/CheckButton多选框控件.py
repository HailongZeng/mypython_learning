import tkinter

#创建窗口
win = tkinter.Tk()
win.title('Hailong')
win.geometry('400x400+200+0')

def update():
    message = ''
    if hobby1.get() == True: #说明选中了
        message += 'money\n'
    if hobby2.get() == True:  # 说明选中了
        message += 'power\n'
    if hobby3.get() == True: #说明选中了
        message += 'people\n'
    text. delete(0.0, tkinter.END) #清空text中的所有内容
    text.insert(tkinter.INSERT, message)

#绑定变量
hobby1 = tkinter.BooleanVar()  #绑定布尔型的变量，因此hobby1.get()返回True或者False
hobby2 = tkinter.BooleanVar()  #绑定布尔型的变量
hobby3 = tkinter.BooleanVar()  #绑定布尔型的变量

check1 = tkinter.Checkbutton(win, text='money', variable=hobby1, command=update)
check1.pack()
check2 = tkinter.Checkbutton(win, text='power', variable=hobby2, command=update)
check2.pack()
check3 = tkinter.Checkbutton(win, text='people', variable=hobby3, command=update)
check3.pack()

text = tkinter.Text(win, width=50, height=5)
text.pack()

win.mainloop()