'''
设计类
类名：见名知意(看到类名就知道该类是用来干嘛的)，首字母大写，其他遵循驼峰原则
属性：见名知意，其他遵循驼峰原则
行为(方法/功能):见名知意，其他遵循驼峰原则

例子：
类名:Wife
属性:sex,age,height,weight,facevalue
行为:洗衣，做饭，生孩子，捶肩，买包，逛街
'''

'''
创建类
类：一种数据类型，本身并不占内存空间，跟所学的numbers、string、boolean等类似。用类创建实例化对象(变量)，对象占内存空间

格式：
class 类名(父类列表):
    属性
    行为(方法/功能)
'''
#  object:基类(超类)，所有类的父类；一般创建类时如果没有合适的父类，就用object代替
class Person(object):
    #定义属性(定义变量)
    name=''
    age=0
    height=0
    weight=0
    #定义方法(行为/功能)(定义函数)
    #注意：方法的参数必须以self当第一个参数
    #self代表类的实例(某个对象)
    def run(self):
        print('run')
    def eat(self,food):
        print('eat'+food)
    

