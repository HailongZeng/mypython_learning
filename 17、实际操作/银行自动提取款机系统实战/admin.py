import time
class Admin(object):
    admin = input('请创建您的账号：')
    password = input('请创建您的密码：')
    def printAdminView(self):
        print('********************************************')
        print('*                                          *')
        print('*                                          *')
        print('*         欢迎登陆海龙私人银行                 *')
        print('*                                          *')
        print('*                                          *')
        print('********************************************')

    def symsFunctionView(self):
        print('********************************************')
        print('*                                          *')
        print('*             开户(1)          查询(2)       *')
        print('*             取款(3)          存款(4)       *')
        print('*             转账(5)          改密(6)       *')
        print('*             锁定(7)          解锁(8)       *')
        print('*             补卡(9)          销户(a)       *')
        print('*                    退出(e)                *')
        print('*                                          *')
        print('********************************************')

    def adminOption(self):  #包含登陆和退出
        inputAdmin = input('请输入管理员账号：')
        if self.admin != inputAdmin:
            print('Warning: 账号输入有误！！！')
            return -1
        inputPassword = input('请输入管理员密码：')
        if self.password != inputPassword:
            print('Warning: 密码输入有误！！')
            return -1
        # 能执行到这里说明账号密码输入正确
        print('操作成功！请稍后......')
        time.sleep(2)


