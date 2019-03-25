##代码作用与'返回整体xlsx数据.py'代码一致
#有序字典
from collections import OrderedDict
#读取数据
from pyexcel_xls import get_data

def readXlsAndXlsxFile(path):
    dic = OrderedDict()

    #抓取数据
    xdata = get_data(path)  #获取到整体数据
    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic
path = ''
dic = readXlsAndXlsxFile(path)
print(dic)
print(len(dic))