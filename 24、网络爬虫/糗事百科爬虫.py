import urllib.request
import ssl
import re
def jokeCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)

    # 使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)

    HTML = response.read().decode('utf-8')

    '''
    with open(r'/Users/zenghailong/PycharmProjects/mypro001/24、网络爬虫/file2.html','w') as f:
        f.write(HTML)
    '''

    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat, re.S)
    divsList = re_joke.findall(HTML)
    #print(divsList)
    #print(len(divsList))
    print(type(divsList))
    dic = {}
    for div in divsList:
        #用户名
        re_u = re.compile(r"<h2>(.*?)</h2>", re.S)
        username = re_u.findall(div)
        username = username[0]
        print(type(username))
        #段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        duanzi = re_d.findall(div)
        duanzi = duanzi[0]
        print(type(duanzi))
        dic[username] = duanzi
    return dic




url = 'https://www.qiushibaike.com/text/page/1'
info = jokeCrawler(url)

for k,v in info.items():
    print(k, v)
