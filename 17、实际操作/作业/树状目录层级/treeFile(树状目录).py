import tkinter
from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title('Hailong')
win.geometry('600x400+200+50')

path = '/Users/zenghailong/PycharmProjects/mypro001/17、实际操作'
infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path, infoWin)

win.mainloop()