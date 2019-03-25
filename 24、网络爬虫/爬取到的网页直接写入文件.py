import urllib.request

urllib.request.urlretrieve('http://www.baidu.com', filename=r'/Users/zenghailong/PycharmProjects/mypro001/24、网络爬虫/file.html')
#urlretrueve在执行的过程中，会产生一些缓存

#清除缓存
#urllib.request.urlcleanup()
