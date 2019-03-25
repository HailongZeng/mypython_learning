import csv

def writeCsv(path, data):
    with open(path, 'w') as f:
        writer = csv.writer(f)
        for rowData in data:
            print('rowData = ',rowData)
            writer.writerow(rowData)

path = '/Users/zenghailong/PycharmProjects/mypro001/17、实际操作/作业/读写csv文件/00001.csv'
writeCsv(path, [[1,2,3],[4,5,6],[7,8,9]])