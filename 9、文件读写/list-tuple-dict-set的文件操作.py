import pickle   #数据持久性模块
#相当于把数据存到磁盘
myList=[1,2,3,4,5,'Hailong']
path=r'/Users/zenghailong/PycharmProjects/mypro001/9、文件读写/file4.txt'
f=open(path,'wb')
pickle.dump(myList,f)
f.close()

#读取
f1=open(path,'rb')
tempList=pickle.load(f1)
print(tempList)
f.close()