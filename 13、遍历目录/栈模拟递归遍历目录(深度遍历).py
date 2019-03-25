import os

def getAllDirDE(path):
    stack=[]
    stack.append(path)

    #处理栈，当栈为空的时候结束循环
    while len(stack)!=0:
        #从栈里取出数据
        dirPath=stack.pop()
        #目录下所有文件
        filesList=os.listdir(dirPath)


        #处理每一个文件，如果是普通文件则打印出来，如果是目录则将目录的地址压栈
        for fileName in filesList:
            fileAbsPath=os.path.join(dirPath,fileName)
            if os.path.isdir(fileAbsPath):
                #是目录就压栈
                print("目录："+fileName)
                stack.append(fileAbsPath)
            else:
                #是文件就打印
                print('普通：'+fileName)
getAllDirDE(r'/Users/zenghailong/PycharmProjects/mypro001')