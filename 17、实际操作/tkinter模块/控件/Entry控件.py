import tkinter

#创建窗口
win = tkinter.Tk()
win.title('Hailong')
win.geometry('400x400+200+0')

'''
Entry控件：输入控件---用于显示简单的文本内容
'''


e = tkinter.Variable() #绑定变量
entry = tkinter.Entry(win, textvariable = e, show='*')   #show='*'，密文显示   不管输入什么内容，都以'*'显示
entry.pack()

#e就代表输入框这个对象
#设置值
e.set('hailong')  #因为show的存在，将显示出7个*，但表示的密文是hailong

#取值
print(e.get())  #输出输入框中的设置值
print(entry.get())  #输出输入框中的设置值，注意设置值时不可以用entry，而应该使用e

win.mainloop()  #窗口循环