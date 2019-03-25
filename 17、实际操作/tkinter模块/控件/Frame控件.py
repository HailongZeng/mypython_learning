import tkinter


win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('400x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

'''
Frame控件：框架控件
在屏幕上显示一个矩形区域，多作为容器控件
'''

frm = tkinter.Frame(win)
frm.pack()

#left
frm_1 = tkinter.Frame(frm)
tkinter.Label(frm_1, text='左上', bg='pink').pack(side=tkinter.TOP)
tkinter.Label(frm_1, text='左下', bg='blue').pack(side=tkinter.TOP)
frm_1.pack(side=tkinter.LEFT)

#Right
frm_2 = tkinter.Frame(frm)
tkinter.Label(frm_2, text='右上', bg='red').pack(side=tkinter.TOP)
tkinter.Label(frm_2, text='右下', bg='yellow').pack(side=tkinter.TOP)
frm_2.pack(side=tkinter.RIGHT)

win.mainloop() #进入消息循环