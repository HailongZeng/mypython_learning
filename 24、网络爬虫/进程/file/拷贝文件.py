import os
import time
from multiprocessing import Pool

def copyFile(rPath, wPath):
    fr = open(rPath, 'rb')
    fw = open(wPath, 'wb')
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()

path = r'/Users/zenghailong/PycharmProjects/mypro001/24、网络爬虫/进程/file'
toPath = r'/Users/zenghailong/PycharmProjects/mypro001/24、网络爬虫/进程/tofile'
#读取path下的所有文件
filesList = os.listdir(path)

start = time.time()
#启动for循环处理每一个文件
for fileName in filesList:
    copyFile(os.path.join(path, fileName), os.path.join(toPath, fileName))
end = time.time()
print('总耗时：%0.2f'%(end-start))