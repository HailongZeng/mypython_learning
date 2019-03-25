#一个.py文件就是一个模块


'''每一个模块(.py文件)都有一个__name__属性，当其值等于'__main__'
的时候，表明该模块自身在执行。否则被引入了其他文件。
'''
#当前文件如果为程序的入口文件，则__name__属性的值为__main__
if __name__=='__main__':
    print('this is a self-defined module!')
else:
    print(__name__)
    def sayGood():
        print('Hailong is a good man!')

    def sayNice():
        print('Hailong is a nice man!')

    def sayHandsome():
        print('Hailong is a handsome man!')
