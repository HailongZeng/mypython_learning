'''
多态：一种事物的多种形态

最终目标：人可以喂任何一种动物
'''
'''
class Cat(object):
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name + '吃')

class Mouse(object):
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name + '吃')
tom = Cat('Tom')
jerry = Mouse('Jerry')
tom.eat()
jerry.eat()
'''
#思考：再添加100种动物，也都有name属性和eat方法
class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name + '吃')
class Cat(Animal):
    def __init__(self,name):
        #self.name=name
        super(Cat, self).__init__(name)
    #def eat(self):
        #print(self.name + '吃')
class Mouse(Animal):
    def __init__(self, name):
        #self.name = name
        super(Mouse, self).__init__(name)
    #def eat(self):
        #print(self.name + '吃')
#定义一个人类，可以喂猫和老鼠吃东西
class Person(object):
    '''
    def feedCat(self, cat):
        print('给你食物')
        cat.eat()
    def feedCat(self, mouse):
        print('给你食物')
        mouse.eat()
    '''
    def feedAnimal(self, ani):
        print('给你食物')
        ani.eat()
per=Person()
tom = Cat('Tom')
jerry = Mouse('Jerry')
'''
per.feedCat(tom)
per.feedMouse(jerry)
'''
#思考：人要喂100种动物，难道要写100个？
per.feedAnimal(tom)