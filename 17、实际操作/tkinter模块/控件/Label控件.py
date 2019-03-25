import tkinter
win = tkinter.Tk()
win.title('Hailong')
win.geometry('400x400+0+0')

'''
Label:标签控件，可以显示文本和位图
'''
#win      父窗体
#text     显示的文本内容
#bg       背景色
#fg       字体颜色
#font     字体
#width    宽度
#height   高度
#wraplength 指定text文本中多宽进行换行
#justify    设置文本对齐方式，默认居中对齐
#anchor     位置(n--north,e--east,s--south,w--west,center--居中,ne,se,sw,nw)
label = tkinter.Label(win,
                      text = 'Hailong',
                      bg = 'pink',
                      fg = 'red',
                      font = ('黑体', 20),
                      width = 10,
                      height = 4,
                      wraplength = 100,
                      justify = 'left',
                      anchor = 'ne')
#显示出来
label.pack()
win.mainloop()