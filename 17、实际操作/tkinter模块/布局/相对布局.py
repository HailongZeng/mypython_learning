import tkinter

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('600x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

label1 = tkinter.Label(win, text='good', bg='blue')
label2 = tkinter.Label(win, text='cool', bg='red')
label3 = tkinter.Label(win, text='nice', bg='pink')

#相对布局，pack(fill= ,side= )，窗体改变对label的位置有影响
#tkinter.BOTH
label1.pack(fill=tkinter.Y, side=tkinter.LEFT)
label2.pack(fill=tkinter.X, side=tkinter.TOP)
label3.pack(fill=tkinter.BOTH, side=tkinter.BOTTOM)

win.mainloop() #进入消息循环