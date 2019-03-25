import tkinter

#创建窗口
win = tkinter.Tk()
win.title('Hailong')
#win.geometry('400x400+200+0')

'''
Text控件：文本控件，用于显示多行文本
'''
#创建滚动条
scroll = tkinter.Scrollbar()
text = tkinter.Text(win, width=30, height=4)  #这里高度指行数

scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)  #设置滚动条放到窗体的右侧(RIGHT),按Y方向填充
text.pack(side=tkinter.LEFT, fill=tkinter.Y)  #设置文本放到窗体的左侧(LEFT),按Y方向填充

#将scroll和text关联
scroll.config(command=text.yview)
text.configure(yscrollcommand=scroll.set)

str = '''If there is anyone out there who still doubts that America
is a place where all things are possible, who still wonders if the 
founders is alive in our time, who still questions the power of our 
democracy, tonight is your answer'''
text.insert(tkinter.INSERT, str)

win.mainloop()  #进入消息循环