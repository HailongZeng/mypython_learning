import tkinter


win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('400x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

#菜单条
menubar = tkinter.Menu(win)


#菜单
menu = tkinter.Menu(menubar, tearoff=False)
for item in ['Python', 'C', 'C++', 'OC', 'Swift', 'C#', 'shell',
             'Java', 'JS', 'PHP', '汇编', 'NodeJS', 'Quit']:
    menu.add_command(label=item)

menubar.add_cascade(label='Language', menu=menu)

def showMenu(event):
    menubar.post(event.x_root, event.y_root)
win.bind('<Button-1>', showMenu) #<Button-1>是鼠标左键，<Button-2>是鼠标滚轮，<Button—3>是鼠标右键

win.mainloop() #进入消息循环