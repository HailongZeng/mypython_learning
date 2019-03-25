import tkinter
print(dir(tkinter))  #查看tkinter模块中定义的一些方法、属性名

#创建窗口
win = tkinter.Tk()
win.title('Hailong')
#win.geometry('400x400+200+0')

#与BROWSE/SINGLE/EXTENDED相似，MULTIPLE支持多选(直接点鼠标就能支持多选)
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)

for item in ['good', 'nice', 'cool', 'handsome', 'vg', 'vs', 'eg', 'he', 'hhh', 'hah', 'hahah', 'hard']:
    lb.insert(tkinter.END, item)   #tkinter模块.END 按顺序添加
#滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
#额外给属性赋值
sc['command'] = lb.yview

win.mainloop()