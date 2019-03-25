import tkinter


win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('400x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

'''
Spinbox:数值范围控件
'''
def update():
    print(sp.get())
    #print(v.get())
#绑定变量
#v = tkinter.StringVar()

#increment  步长，默认为1
#values     最好不要同from_0,to=100，increment=5同时使用，例：values(0,2,4,6,8)
#command=upadate    只要值改变就能执行对应的方法
sp = tkinter.Spinbox(win, from_=0, to=100, increment=5, command=update)#, textvaiable=v)
sp.pack()

#赋值，设置值
#v.set(20)
#取值
#print(v.get())


win.mainloop() #进入消息循环