import socket
import threading
#创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定IP端口
server.bind(('192.168.1.6' ,8080))   #ip是本机的ip，服务器端口一般大于1024
#监听
server.listen(5)
print('服务器启动成功，等待客户端的连接')
def run(clientSocket):
    data = clientSocket.recv(1024)
    print('客户端说：' + data.decode('utf-8'))
    data = input('请输入返回给客户端的数据')
    clientSocket.send(data.encode('utf-8'))
while True:
    # 等待连接
    clientSocket, clientAddress = server.accept()
    print('%s -- %s 链接成功' % (str(clientSocket), clientAddress))
    t = threading.Thread(target=run, args=(clientSocket,))
    t.start()