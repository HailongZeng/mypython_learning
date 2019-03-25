import tkinter
import socket
import threading
win = tkinter.Tk()
win.title('QQ服务器')
win.geometry('400x400+200+20')

users = {}

def run(ck):
    print('********************')
    userName = ck.recv(1024)
    users[userName.decode('utf-8')] = ck
    print(users)
    while True:
        rData = ck.recv(1024)
        dataStr = rData.decode('utf-8')
        #xym:sunck is a good man
        infolist = dataStr.split(':')
        users[infolist[0]].send((userName.decode('utf-8')+'说:'+infolist[1]+'\n').encode('utf-8'))

def start():
    ipStr = eip.get()
    portStr = eport.get()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ipStr, int(portStr)))
    server.listen(5)
    printStr = '服务器启动成功'
    text.insert(tkinter.INSERT, printStr)
    while True:
        # 等待连接
        ck, ca = server.accept()
        print('%s -- %s 链接成功' % (str(ck), ca))
        t = threading.Thread(target=run, args=(ck,))
        t.start()

def startServer():
    s = threading.Thread(target=start)
    s.start()


labelIp = tkinter.Label(win, text = 'ip').grid(row=0, column=0)
eip = tkinter.Variable()
entryIp = tkinter.Entry(win, textvariable = eip).grid(row=0, column=1)

labelPort = tkinter.Label(win, text = 'port').grid(row=1, column=0)
eport = tkinter.Variable()
entryPort = tkinter.Entry(win, textvariable = eport).grid(row=1, column=1)

button = tkinter.Button(win, text='启动', command=startServer).grid(row=2, column=0)
text = tkinter.Text(win, width=20, height=10)
text.grid(row=3, column=0)


win.mainloop()