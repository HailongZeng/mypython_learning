import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input('请输入数据：')
    client.sendto(data.encode('utf-8'), ('192.168.1.6', 12345))
    info = client.recv(1024)
    print('服务器说：', info.decode('utf-8'))