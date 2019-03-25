import tkinter
print(dir(tkinter))  #查看tkinter模块中定义的一些方法、属性名

#创建窗口
win = tkinter.Tk()
win.title('Hailong')
win.geometry('400x400+200+0')

#绑定变量
lbv = tkinter.StringVar()
#与BROWSE相似，但是不支持鼠标按住后下滑移动选中位置
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)
lb.pack()
for item in ['good', 'nice', 'cool', 'handsome']:
    lb.insert(tkinter.END, item)   #tkinter模块.END 按顺序添加

#打印当前列表中的选项
print(lbv.get())
#设置选项
#lbv.set(('1', '2', '3'))

#绑定事件，给控件绑定事件，而不是给变量
def myPrint(event):
    print(lb.get(lb.curselection()))  #获取当前选定下标处的值
lb.bind('<Double-Button-1>',myPrint)  #Double-Button-1表示左键双击
win.mainloop()