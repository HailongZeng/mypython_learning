from user import User
from card import Card
import random
import os
import pickle
import time

class ATM(object):
    def __init__(self, allUsers):
        self.allUsers = allUsers  #卡号-用户
    #开户
    def OpenAccount(self):
        #目标：向用户字典中添加一对键值对(卡号-用户)
        name = input('请输入您的姓名：')
        id = input('请输入您的身份证号：')
        phone = input('请输入您的手机号：')

        prestoreMoney = int(input('请输入预存款金额：'))
        if int(prestoreMoney) < 0:
            print('预存款输入有误！！开户失败')
            return -1  #退出程序

        setPassword = input('请设置您的密码：')
        if not self.checkPassword(setPassword):  #重新输入密码已确认设置密码
            print('密码输入错误！！开户失败......')
            return -1 #结束跳出程序
        #所有需要的信息完全，开始生成卡号
        cardID=self.GetCardID()
        card = Card(cardID, setPassword, prestoreMoney)
        user = User(name, id, phone, card)
        #存到字典中
        self.allUsers[cardID] = user  #创建卡号-用户字典
        print('开户成功！！请牢记卡号(%s)......' % (cardID))
        # 开户成功后将当前系统中的用户信息保存到文件中
        absPath = os.getcwd()
        filepath = os.path.join(absPath, 'allUsers.txt')
        f = open(filepath, 'wb')
        pickle.dump(self.allUsers, f)
        f.close()
        time.sleep(3)

    #查询
    def searchUserInfo(self):
        cardNum = input('请输入您的卡号：')
        user = self.allUsers.get(cardNum)  #获取该卡号的持卡人信息
        # 验证是否存在卡号
        if not user:
            print('该卡号不存在！！查询失败......')
            return -1

        #判断是否锁定
        if user.card.cardLock:
            print('该卡已经被锁定！！请解锁后再进行其他操作......')
            return -1

        #验证密码
        if not self.checkPassword(user.card.cardPassword):
            print('密码输入错误！！该卡已经被锁定！！请解锁后再进行其他操作......')
            user.card.cardLock = True
            return -1
        print('账号：%s  余额：%d' % (user.card.cardID, user.card.cardMoney))

    #取款
    def Withdraw(self):
        cardNum = input('请输入您的卡号：')
        user = self.allUsers.get(cardNum)  # 获取该卡号的持卡人信息
        # 验证是否存在卡号
        if not user:
            print('该卡号不存在！！取款失败......')
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print('该卡已经被锁定！！请解锁后再进行其他操作......')
            return -1

        # 验证密码
        if not self.checkPassword(user.card.cardPassword):
            print('密码输入错误！！该卡已经被锁定！！请解锁后再进行其他操作......')
            user.card.cardLock = True
            return -1
        #取款
        money = int(input('请输入取款金额：'))
        if money > user.card.cardMoney:
            print('余额不足！！取款失败......')
            return -1
        time.sleep(2)
        user.card.cardMoney -= money
        print('账号：%s  余额：%d' % (user.card.cardID, user.card.cardMoney))

    #存款
    def Deposit(self):
        cardNum = input('请输入您的卡号：')
        user = self.allUsers.get(cardNum)  # 获取该卡号的持卡人信息
        # 验证是否存在卡号
        if not user:
            print('该卡号不存在！！存款失败......')
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print('该卡已经被锁定！！请解锁后再进行其他操作......')
            return -1

        # 验证密码
        if not self.checkPassword(user.card.cardPassword):
            print('密码输入错误！！该卡已经被锁定！！请解锁后再进行其他操作......')
            user.card.cardLock = True
            return -1
        # 取款
        money = int(input('请输入存款金额：'))
        time.sleep(2)
        user.card.cardMoney += money
        print('账号：%s  余额：%d' % (user.card.cardID, user.card.cardMoney))

    #转账
    def Transfer(self):
        cardNum1 = input('请输入您的卡号：')
        user1 = self.allUsers.get(cardNum1)  # 获取该卡号的持卡人信息
        # 验证是否存在卡号
        if not user1:
            print('该卡号不存在！！转账失败......')
            return -1

        # 判断是否锁定
        if user1.card.cardLock:
            print('该卡已经被锁定！！请解锁后再进行其他操作......')
            return -1

        # 验证密码
        if not self.checkPassword(user1.card.cardPassword):
            print('密码输入错误！！该卡已经被锁定！！请解锁后再进行其他操作......')
            user1.card.cardLock = True
            return -1
        cardNum2 = input('请输入收款人的卡号：')
        user2 = self.allUsers.get(cardNum2)  # 获取该卡号的持卡人信息，即收款人信息
        money = int(input('请输入转账金额：'))
        #转款人卡中钱减少
        user1.card.cardMoney -= money
        print('账号：%s  余额：%d' % (user1.card.cardID, user1.card.cardMoney))
        #收款人卡中钱增多
        user2.card.cardMoney += money
        print('账号：%s  余额：%d' % (user2.card.cardID, user2.card.cardMoney))

    #修改密码
    def PasswordChange(self):
        cardNum = input('请输入您的卡号：')
        user = self.allUsers.get(cardNum)  # 获取该卡号的持卡人信息
        # 验证是否存在卡号
        if not user:
            print('该卡号不存在！！修改密码失败......')
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print('该卡已经被锁定！！请解锁后再进行其他操作......')
            return -1

        # 验证密码
        if not self.checkPassword(user.card.cardPassword):
            print('密码输入错误！！该卡已经被锁定！！请解锁后再进行其他操作......')
            user.card.cardLock = True
            return -1

        #修改密码
        setPassword = input('请设置您的新密码：')
        if not self.checkPassword(setPassword):  # 重新输入密码已确认设置密码
            print('密码输入错误！！修改密码失败......')
            return -1  # 结束跳出程序
        user.card.cardPassword = setPassword  #更新密码
        print('密码修改成功！！请记住您的新密码......')

    #锁定
    def lockUser(self):
        cardNum = input('请输入您的卡号：')
        # 验证是否存在卡号
        user = self.allUsers.get(cardNum)  # 获取该卡号的持卡人信息
        if not user:
            print('该卡号不存在！！锁定失败......')
            return -1

        if user.card.cardLock:
            print('该卡已经被锁定！！请解锁后再使用其他功能......')
            return -1 #结束该功能

        # 验证密码
        if not self.checkPassword(user.card.cardPassword):
            print('密码输入错误！！锁定失败......')
            return -1

        tempId = input('请输入您的身份证号码：')
        if tempId != user.id:
            print('身份证输入失败！！')
            return -1
        #锁死
        user.card.cardLock = True
        print('锁定成功......')

    #解锁
    def unlockUser(self):
        cardNum = input('请输入您的卡号：')
        user = self.allUsers.get(cardNum)  # 获取该卡号的持卡人信息
        # 验证是否存在卡号
        if not user:
            print('该卡号不存在！！解锁失败......')
            return -1

        # 判断是否锁定
        if not user.card.cardLock:
            print('此卡没有被锁定！！无需解锁......')
            return -1
        #锁定了只需身份证可以解锁，无需验证密码
        tempId = input('请输入您的身份证号码：')
        if tempId != user.id:
            print('身份证输入失败！！解锁失败......')
            return -1
        # 解锁
        user.card.cardLock = False
        print('解锁成功......')

    #补卡
    def Replacement(self):
        #补卡相当于重新开户,且先要进行销户
        self.Cancellation()
        self.OpenAccount()

    #销户
    def Cancellation(self):
        cardNum = input('请输入您的卡号：')
        user = self.allUsers.get(cardNum)  # 获取该卡号的持卡人信息
        # 验证是否存在卡号
        if not user:
            print('该卡号不存在！！销户失败......')
            return -1
        tempId = input('请输入您的身份证号码：')
        if tempId != user.id:
            print('身份证输入失败！！销户失败......')
            return -1

    #验证密码
    def checkPassword(self, realPassword):
        for i in range(3):
            tempPassword = input('请输入您的密码：')
            if tempPassword == realPassword:
                return -1
        return False
    #生成卡号函数
    def GetCardID(self):
        str = ''
        for i in range(6):
            #随机生成数字
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            str += ch
        #判断是否重复
        if not self.allUsers.get(str): #allUsers{}中存储着卡号-用户的键值对
            return str

#优化任务：
#将各函数方法中重复的部分重新构建成一个新的函数
#文本内容需要能够读出
#admin输入的账号和密码需要和开户时字典中的卡号和密码一致