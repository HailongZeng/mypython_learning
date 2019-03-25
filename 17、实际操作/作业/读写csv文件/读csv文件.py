import csv

def readCsv(path):
    infoList = []
    with open(path, 'r') as f:
        allFileInfo = csv.reader(f)  #将csv中的数据读出来存入allFileInfo中，allFileInfo是一个对象(object)
        for row in allFileInfo:  #一行一行取数据
            infoList.append(row)  #将数据存入列表
    return infoList

path = '/Users/zenghailong/PycharmProjects/mypro001/17、实际操作/作业/读写csv文件/00001.csv'  #把csv文件的路径写到path中，供后面使用
info = readCsv(path)
print(info)
