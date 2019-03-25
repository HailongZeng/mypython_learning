import tkinter

win = tkinter.Tk()
win.title('hailong')
win.geometry('400x400+200+20')

def update():
    print(r.get())  #r.get()得到的是value的值

#绑定变量  一组单选框需要绑定同一个变量，才能实现单选，否则可以多选
r = tkinter.IntVar()  #绑定Int类型变量
#r = tkinter模块.StringVar() #绑定String类型变量
#radio1和radio2需绑定同一变量，才能实现单选
radio1 = tkinter.Radiobutton(win, text='one', value=14, variable=r, command=update)
radio1.pack()
radio2 = tkinter.Radiobutton(win, text='two', value=1, variable=r, command=update)
radio2.pack()

win.mainloop()