import urllib.request
import re
import os
def imageCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode('utf-8')

    '''''
    with open(r'/Users/zenghailong/PycharmProjects/mypro001/24、网络爬虫/爬虫练习/html', 'wb') as f:
        f.write(HtmlStr)
    '''''

    pat = r'img src="//img20.360buyimg.com/n7/s230x230_jfs/(.*?)"/>'
    re_image = re.compile(pat, re.S)
    imagesList = re_image.findall(HtmlStr)
    print(len(imagesList))
    print(imagesList)
    num = 1
    for imageUrl in imagesList:
        path = '/Users/zenghailong/PycharmProjects/mypro001/24、网络爬虫/爬虫练习/image/%s.jpg'%num
        #把图片下载到本地存储
        urllib.request.urlretrieve('http://img20.360buyimg.com/n7/s230x230_jfs/'+imageUrl, filename=path)
        num += 1

url = 'http://search.yhd.com/c0-0/k%25E5%25A5%25B3%25E5%25A3%25AB%25E8%25A3%25A4%25E5%25AD%2590/'

imageCrawler(url)