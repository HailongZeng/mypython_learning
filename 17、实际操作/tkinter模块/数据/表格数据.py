import tkinter
from tkinter import ttk

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('600x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

#表格
tree = ttk.Treeview(win)
tree.pack() #显示表格

#定义列
tree['columns'] = ('姓名', '年龄', '身高', '体重')
#设置列
tree.column('姓名', width=100)
tree.column('年龄', width=100)
tree.column('身高', width=100)
tree.column('体重', width=100)

#设置表头
tree.heading('姓名', text='姓名-name')
tree.heading('年龄', text='年龄-age')
tree.heading('身高', text='身高-height')
tree.heading('体重', text='体重-weight')

#添加数据
tree.insert('', 0, text='line1', values=('曾海龙', '22', '178', '125'))
tree.insert('', 1, text='line2', values=('曾海飞', '22', '178', '130'))

win.mainloop() #进入消息循环