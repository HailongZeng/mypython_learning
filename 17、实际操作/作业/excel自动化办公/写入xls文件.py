#有序字典
from collections import OrderedDict
#写入数据
from pyexcel_xls import save_data


def makeExcelFile(path, data):
    dic = OrderedDict()
    for sheetName, sheetValue in data.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d) #将d加到dic中

    save_data(path, dic)


path = '/Users/zenghailong/PycharmProjects/mypro001/17、实际操作/作业/excel自动化办公/1.xls'
makeExcelFile(path, {'表1':[[1,2,3],[4,5,6],[7,8,9]],'表2':[[11,22,33],[44,55,66],[77,88,99]]})