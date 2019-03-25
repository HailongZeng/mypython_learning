import socket

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind(('192.168.1.6', 12345))
print('启动服务器成功......')
while True:
    data, addr = udpServer.recvfrom(1024)
    print(addr)
    print('客户端说：', data.decode('utf-8'))
    info = input('请输入数据：')
    udpServer.sendto(info.encode('utf-8'), addr)
