import telnetlib

def telnetDoSomething(IP, user, passwd, command):
    try:
        # 链接服务器
        telnet = telnetlib.Telnet(IP)
        # 设置调试级别
        telnet.set._debuglevel(2)

        # 读取输入用户名信息
        rt = telnet.read_unitl('Login username:'.encode('utf-8'))
        # 写入用户名
        telnet.write((user + '\r\n').encode('utf-8'))

        # 读取输入密码信息
        rt = telnet.read_unitl('Login password:'.encode('utf-8'))
        # 写入密码
        telnet.write((passwd + '\r\n').encode('utf-8'))

        # 读取验证IP
        rt = telnet.read_unitl('Domain name:'.encode('utf-8'))
        # 写入IP
        telnet.write((IP + '\r\n').encode('utf-8'))

        # 登陆成功，写指令
        rt = telnet.read_unitl('>'.encode('utf-8'))
        telnet.write((command + '\r\n').encode('utf-8'))

        # 上面命令执行成功，会继续读>
        # 失败，一般不会是>
        rt = telnet.read_unitl('>'.encode('utf-8'))

        # 断开链接
        telnet.close()
        return True
    except:
        print('error')
        return False


if __name__ == '__main__':
    IP = '10.0.142.197'
    user = 'xumingbin'
    passwd = '1103'
    command = 'tasklist'
    print(telnetDoSomething(IP, user, passwd, command))