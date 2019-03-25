import tkinter
from tkinter import ttk
import os

class TreeWindows(tkinter.Frame):
    def __init__(self, master, path, otherWin):
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=0)

        self.otherWin = otherWin

        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)
        print(os.path.split(path))
        #os.path.split会将path切割成最后一级path和剩下的前面的path，并存入一个列表中
        root = self.tree.insert('', 'end', text=os.path.split(path)[-1], open=True, values=(path))
        self.loadTree(root, path)

        #滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)

        #绑定事件
        self.tree.bind('<<TreeviewSelect>>', self.func)
    def func(self, event):
        self.v = event.widget.selection()  #widget事件属性：是触发事件的小构件
        for sv in self.v:
            file = self.tree.item(sv)['text']
            self.otherWin.ev.set(file)
            apath = self.tree.item(sv)['values'][0]
            print(apath)

    def loadTree(self, parent, path):
        for fileName in os.listdir(path):
            absPath = os.path.join(path, fileName)
            #插入树枝
            tree = self.tree.insert(parent, 'end', text=os.path.split(absPath)[-1], open=True, values=(absPath))
            #判断是否是目录
            if os.path.isdir(absPath):
                self.loadTree(tree, absPath)
