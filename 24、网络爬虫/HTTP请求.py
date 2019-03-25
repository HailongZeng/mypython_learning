import urllib.request

'''
使用场景：进行客户端与服务端之间的消息传递时使用
GET:通过URL网址传递信息，可以直接在URL网址上添加要传递的信息
POST:可以向服务器提交数据，是一种比较流行的比较安全的数据传递方式
PUT:请求服务器存储一个资源，通常要指定存储的位置
DELETE:请求服务器删除一个资源
HEAD:请求获取对应的HTTP报头信息
OPTIONS:可以获取当前URL所支持的请求类型
'''
print('---------------------------Get请求-------------------------')
'''
特点：把数据拼接到请求路径的后面传递给服务器
优点：速度快
缺点：承载的数据量小，不安全
'''
url1 = 'http://www.baidu.com'
response = urllib.request.urlopen(url1)
data1 = response.read().decode('utf-8')
print(data1)
print(type(data1))

print('---------------------------Post请求------------------------')
'''
特点：把参数进行打包，单独传输
优点：数量大，安全(当对服务器数据进行修改时建议使用post)
缺点：速度慢
'''
import urllib.parse
url2 = 'http://www.baidu.com'
#将要发送的数据合成一个字典
#字典的键去网址里找，一般为input标签的name属性的值
data2 = {'username':'sunck',
         'passwd':'666'}
#对将要发送的数据进行打包
postData = urllib.parse.urlencode(data2).encode('utf-8')
#请求体
req = urllib.request.Request(url2, data=postData)
#请求
req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))


