import tkinter

#创建窗口
win = tkinter.Tk()
win.title('Hailong')
win.geometry('400x400+200+0')

'''
Text控件：文本控件，用于显示多行文本
'''
text = tkinter.Text(win, width=20, height=4)  #这里高度指行数
text.pack()
str = '''If there is anyone out there who still doubts that America
is a place where all things are possible, who still wonders if the 
founders is alive in our time, who still questions the power of our 
democracy, tonight is your answer'''
text.insert(tkinter.INSERT, str)

win.mainloop()