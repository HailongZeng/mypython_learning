class Person(object):

    def run(self):
        print('run')
    def eat(self,food):
        print('eat'+food)
    def __init__(self,name,age,height,weight,money):   #在__init__里面定义属性
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.__money=money

    #通过内部方法，修改私有属性
    #通过自定义的方法实现对私有属性的赋值和取值
    def setMoney(self,money):
        #数据的过滤
        if money<0:
            money=0
        self.__money=money
    def getMoney(self):
        return self.__money
per=Person('hanmeimei',20,165,50,10000)
per.age=10
print(per.age)

#如果要让的属性内部不被外部直接访问,那么需要在属性前加两个下划线(__)
#在python中，如果在属性前加两个下划线，那么这个属性就变成了私有属性(private)
##per.__money=0
#print(per.__money) #外部使用

#不能直接访问per.__money是因为Python解释器把__money变成了_Person__money,
#我们仍然可以用_Person__money去访问，但是强烈建议不要这么访问，不同的解释器可能存在解释的变量名不一致
'''
per.a=100
print(per.a)
'''

per.setMoney(-10)
print(per.getMoney())

#在Python中，__XXX__属于特殊变量，可以直接访问
#在Python中，_XXX属于特殊变量，这样的实例变量外部也可直接访问