import tkinter


win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('400x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

#菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)

def func():
    print('Hailong is very great')
#创建一个菜单
menu1 = tkinter.Menu(menubar, tearoff=False)
#给菜单选项添加内容
for item in ['Python', 'C', 'C++', 'OC', 'Swift', 'C#', 'shell',
             'Java', 'JS', 'PHP', '汇编', 'NodeJS', 'Quit']:
    if item == 'Quit':
        #添加分隔线
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit())
    else:
        menu1.add_command(label=item, command=func)
#向菜单条上添加菜单选项
menubar.add_cascade(label='Language', menu=menu1)

menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label='red')
menu2.add_command(label='blue')
menubar.add_cascade(label='Color', menu=menu2)


win.mainloop() #进入消息循环