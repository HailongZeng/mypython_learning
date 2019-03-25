import os
'''
os:包含了普遍的操作系统的功能
'''

#获取操作系统类型 nt-windows  posix-Linux、Unix或者Mac OS X
print(os.name)

#打印操作系统详细的信息(windows不支持)
print(os.uname())

#获取操作系统中的环境变量
print(os.environ)
#获取指定环境变量
print(os.environ.get('PATH'))

#获取当前目录  ./a/
print(os.curdir)
#获取当前工作目录，即当前python脚本所在的目录
print(os.getcwd())

#以列表的形式返回指定目录下的所有的文件
print(os.listdir(r'/Users/zenghailong/PycharmProjects/mypro001'))

#在当前目录下创建新目录
os.mkdir('sunck')
#删除目录
#os.rmdir('sunck')

#获取文件属性
print(os.stat('sunck'))

#重命名
os.rename('sunck','Hailong')

#删除普通文件
#os.remove('file1.txt')

#运行shell命令
#os.system('')





#有些方法存在os模块里，还有一些存在于os.path
#查看当前的绝对路径
print(os.path.abspath('.'))

#拼接路径
p1=r'/Users/zenghailong/PycharmProjects/mypro001/10、os模块'
p2='sunck/abc/d'
#注意：参数2里开始不要有斜杠，否则只会输出p2，不会拼接
print(os.path.join(p1,p2))

#拆分路径
path2=r'/Users/zenghailong/PycharmProjects/mypro001/10、os模块/sunck/abc/d.txt'
print(os.path.split(path2))

#获取扩展名
print(os.path.splitext(path2))

#判断是否是目录
path3=r'/Users/zenghailong/PycharmProjects/mypro001/10、os模块'
print(os.path.isdir(path3))

#判断文件是否存在
path4=r'/Users/zenghailong/PycharmProjects/mypro001/10、os模块/os模块.py'
#判断在当前文件夹中的，可使用相对路径。若判断不在当前文件夹中的文件，则需要使用绝对路径
print(os.path.isfile(path4))

#判断目录是否存在
#path5=r'/Users/zenghailong/PycharmProjects/mypro001/10、os模块/sunck'
path5=r'/Users/zenghailong/PycharmProjects/mypro001/10、os模块'
print(os.path.exists(path5))

#获得文件大小(字节)  一个汉字--3个字节
print(os.path.getsize(path4))

#获得文件的目录
print(os.path.dirname(path4))
print(os.path.basename(path4))
