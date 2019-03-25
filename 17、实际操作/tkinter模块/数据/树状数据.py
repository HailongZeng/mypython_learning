import tkinter
from tkinter import ttk

win = tkinter.Tk() #创建主窗口
win.title('Hailong') #设置标题
win.geometry('600x400+0+0') #设置大小和位置 #int x int表示大小，后面两个是距离屏幕左方和上方的距离

tree = ttk.Treeview(win)
tree.pack()

#添加一级树枝
treeF1 = tree.insert('', 0, '中国', text='中国-CHN', values=('F1'))
treeF2 = tree.insert('', 1, '美国', text='美国-USA', values=('F2'))
treeF3 = tree.insert('', 2, '英国', text='英国-UK', values=('F3'))

#二级树枝
treeF1_1 = tree.insert(treeF1, 0, '黑龙江', text='中国-黑龙江', values=('F1_1'))
treeF1_2 = tree.insert(treeF1, 1, '吉林', text='中国-吉林', values=('F1_2'))
treeF1_3 = tree.insert(treeF1, 2, '辽宁', text='中国-辽宁', values=('F1_3'))

treeF2_1 = tree.insert(treeF2, 0, '德州', text='美国-德州', values=('F2_1'))
treeF2_2 = tree.insert(treeF2, 1, '加州', text='美国-加州', values=('F2_2'))
treeF2_3 = tree.insert(treeF2, 2, '宾州', text='美国-宾州', values=('F2_3'))

#三级树枝
treeF1_1_1 = tree.insert(treeF1_1, 0, '哈尔滨', text='黑龙江-哈尔滨', values=('F1_1_1'))
treeF1_1_2 = tree.insert(treeF1_1, 1, '五常', text='黑龙江-五常', values=('F1_1_2'))

win.mainloop()  #进入消息循环