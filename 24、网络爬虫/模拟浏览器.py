import urllib.request
import random
url = 'http://www.baidu.com'

'''
headers = {
    "User-Agent": "Mozilla/5.0(Windows NT 10.0; WOW64)
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115"
    Safari/537.36"
}
#设置一个请求体
req = urllib.request.Request(url, headers = headers)
#发起请求
response = urllib.request.urlopen(req)
#print(response)
data = response.read().decode('utf-8')
print(data)
'''
agentsList = [
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'
]
agentStr = random.choice(agentsList)
req = urllib.request.Request(url)
#向请求体里添加了User-Agent
req.add_header('User-Agent', agentStr)
response = urllib.request.urlopen(req)
data = response.read().decode('utf-8')
print(data)