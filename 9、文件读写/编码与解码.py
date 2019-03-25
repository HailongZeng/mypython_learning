#编码
path=r'/Users/zenghailong/PycharmProjects/mypro001/9、文件读写/file3.txt'
with open(path,'wb') as f1:
    str='Hailong曾 needs to get a high score in mid-term'
    f1.write(str.encode('utf-8'))

with open(path,'r') as f2:
    data=f2.read()
    print(data)
    print(type(data))
    newData=data.decode('utf-8')
    print(type(data))
