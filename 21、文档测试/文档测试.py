import doctest

#doctest模块可以提取注释中的代码执行
#doctest严格按照Python交互模式的输入提取

def mySum(x, y):
    '''
    Get the sum from x and y
    :param x: first parameter
    :param y: second parameter
    :return: sum

    example:
    #注意有空格
    >>> print(mySum(1,2))
    3

    '''
    return x + y

print(mySum(1, 2))


#进行文档测试
doctest.testmod()
