'''
重写：将函数重新写一遍

__repr__() 给机器用的，在Python解释器里面直接敲对象名，然后再敲回车后调用的方法
__str__()  在调用print打印对象时自动调用，是给用户用的，是一个描述对象的方法
注意：在没有__str__函数，却有__repr__函数的时候，__repr__=__str__
'''
class Person(object):
    def __init__(self,name,age,height,weight):   #在__init__里面定义属性
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def __str__(self):
        return('%s-%d-%d-%d'%(self.name,self.age,self.height,self.weight))
    def __repr__(self):
        return('%s-%d-%d-%d'%(self.name,self.age,self.height,self.weight))
per=Person('tom',20,160,80)
#print(per.name,per.age,per.height,per.weight)
print(per)

#优点：当一个对象的属性值很多，并未都需要打印，重写了__str__方法后，简化了代码

#人开枪射击子弹