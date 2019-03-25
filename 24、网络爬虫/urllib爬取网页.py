import urllib.request


#向指定的url地址发起请求，并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen('http://www.baidu.com')
#读取文件的全部内容，会把读取到的数据赋值给一个字符串变量
#data = response.read()
#print(data)
#print(type(data))

#按行读取
#data = response.readline()

#读取文件的全部内容，会将读取到的数据赋值到一个列表变量
'''
data = response.readlines()
print(data)
print(type(data))
print(len(data))
print(type(data[100]))
print(type(data[100].decode('utf-8')))
'''
#将爬取到的网页写入file
#with open(r'/Users/zenghailong/PycharmProjects/mypro001/24、网络爬虫/file', 'wb') as f:
    #f.write(data)


#response属性
#返回当前环境的有关信息
print(response.info())

#返回状态码
print(response.getcode())
#if response.getcode() == 200 or response.getcode() == 304:
    #处理网页信息
#   pass

#返回当前正在爬取的URL地址
print(response.geturl())

'''
url = 'https://baijiahao.baidu.com/s?id=1575513288714508&wfr=spider&for=pc'
#解码
newUrl1 = urllib.request.unquote(url)
print(newUrl1)
#编码
newUrl2 = urllib.request.quote(newUrl1)
print(newUrl2)
'''