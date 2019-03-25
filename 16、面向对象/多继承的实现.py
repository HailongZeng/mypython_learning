class Father(object):
    def __init__(self,money):
        self.money=money
    def run(self):
        print('run')
    def play(self):
        print('play')
    def func(self):
        print('func1')

class Mother(object):
    def __init__(self,faceValue):
        self.faceValue=faceValue
    def eat(self):
        print('eat')
    def func(self):
        print('func2')

#继承父类
class Child(Father,Mother):
    def __init__(self,money,faceValue,height):
        #写法
        Father.__init__(self,money)
        Mother.__init__(self,faceValue)
        self.height=height  #子类自己定义的属性

#主函数
def main():
    c=Child(300,100,100)
    print(c.money,c.faceValue,c.height)
    c.play()
    c.eat()
    #注意：父类中方法名相同，默认调用的是在括号中排前面的父类中的方法
    c.func()

if __name__=='__main__':
    main()

