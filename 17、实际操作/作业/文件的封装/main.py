from dealFile import DealFile

d = DealFile()

path = '/Users/zenghailong/PycharmProjects/mypro001/17、实际操作/作业/文件的封装/GreedIsGood.pdf'

def func(str):
    print(str + '!')
#func---回调函数
d.readPDF(path, func)