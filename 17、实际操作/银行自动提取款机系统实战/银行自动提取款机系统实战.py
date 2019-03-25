'''
用户
类名：User
属性：姓名，身份证号，电话号，卡
行为：

卡
类名：Card
属性：卡号，密码，余额
行为：

提款机
类名：ATM
属性：用户列表(用字典存储)
行为：开户，查询，取款，存款，转账，改密码，锁定，解锁，补卡，销户，退出


管理员
类名：Admin
属性：
行为：管理员界面，管理员操作(登陆、注销)，系统功能界面
'''
from admin import Admin
from atm import ATM
import time
import pickle  #持久化存储模块
import os

def main():
    #银行对象

    #界面对象
    admin = Admin()
    #管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return -1

    #提款机对象
    absPath = os.getcwd()
    filepath = os.path.join(absPath, 'allUsers.txt')
    if os.path.exists(filepath): #判断是否已经有账户号
        f = open(filepath, 'rb')
        allUsers = pickle.load(f)
        atm = ATM(allUsers)   #读取对象
    else:
        allUsers = {}
        atm = ATM(allUsers)  #首次开户

    while True:
        admin.symsFunctionView()
        #等待用户的操作
        option = input('请输入您的操作：')
        if option == '1':
            atm.OpenAccount()
        elif option == '2':
            atm.searchUserInfo()
        elif option == '3':
            atm.Withdraw()
        elif option == '4':
            atm.Deposit()
        elif option == '5':
            atm.Transfer()
        elif option == '6':
            atm.PasswordChange()
        elif option == '7':
            atm.lockUser()
        elif option == '8':
            atm.unlockUser()
        elif option == '9':
            atm.Replacement()
        elif option == 'a':
            atm.Cancellation()
        elif option == 'e':
            if not admin.adminOption(): #admin.adminOption()正常执行时返回0，因此要执行return -1,需要加not
                return -1
        time.sleep(2)

if __name__ == '__main__':
    main()