import time
path=r"/Users/zenghailong/PycharmProjects/mypro001/9、文件读写/file2.txt"
f=open(path,'w')
#写文件
#1、将信息写入缓冲区
f.write('Hailong is really handsome\n')

#2、刷新缓冲区
#直接把内部缓冲区的数据立刻写入文件，而不是被动地等待；自动刷新缓冲区写入
#f.flush()

f.close()



with open(path,'a') as f2:
    f2.write("good man")