import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.6' ,8080))

while True:
    data = input('请输入给服务器发送的数据')
    client.send(data.encode('utf-8'))
    info = client.recv(1024)  #接收小于1024字节的数据
    print('服务器说：' ,info.decode('utf-8'))