import urllib.request
import ssl
import re
import os
from collections import deque
def writeFileBytes(htmlBytes, toPath):
    with open(toPath, 'wb') as f:
        f.write(htmlBytes)
def writeFileStr(htmlBytes, toPath):
    with open(toPath, 'w') as f:
        f.write(str(htmlBytes))
def getHtmlBytes(url):
    headers = {
        "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context, timeout=0.5)
    return response.read()
def qqCrawler(url, toPath):
    htmlBytes = getHtmlBytes(url)
    htmlStr = str(htmlBytes)

    pat = r'((http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)'
    re_url = re.compile(pat)
    urlsList = re_url.findall(htmlStr)
    #去重
    urlsList = list(set(urlsList))

    pat = r'[1-9]\d{5,9}'
    re_qq = re.compile(pat)
    qqsList = re_qq.findall(htmlStr)
    # 去重
    qqsList = list(set(qqsList))
    f = open(toPath, 'a')
    for qqStr in qqsList:
        f.write(qqStr+'\n')
    f.close()

    return  urlsList

    '''
    writeFileBytes(htmlBytes,'/Users/zenghailong/PycharmProjects/mypro001/24、网络爬虫/爬虫练习/2、爬取网络中的QQ号码/file1.html')
    writeFileStr(htmlStr,'/Users/zenghailong/PycharmProjects/mypro001/24、网络爬虫/爬虫练习/2、爬取网络中的QQ号码/file2.txt')
    '''

def center(url, toPath):  #中央控制器
    queue = deque()
    queue.append(url)
    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = qqCrawler(targetUrl, toPath)
        for item in urlList:
            tempUrl = item[0]
            queue.append(tempUrl)
toPath = r'/Users/zenghailong/PycharmProjects/mypro001/24、网络爬虫/爬虫练习/2、爬取网络中的QQ号码/qqFile'
url = 'http://tieba.baidu.com/p/5471533241?traceid='
#qqCrawler(url, toPath)
center(url, toPath)
