import re

'''
字符串切割
'''
str1 = 'sunck    is a good man'
print(str1.split(' '))
print(re.split(r' +', str1))

print('----------------------re.finditer函数---------------------------')
'''
re.finditer函数
原型：finditer(pattern, string, flags=0)
参数：
pattern：匹配的正则表达式
string：要匹配的字符串
flags：标志位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回的是一个迭代器
'''
str2 = 'sunck is a good man! sunck is a nice man! sunck is a handsome man'
d = re.finditer(r'(sunck)', str2)
while True:
    try:
        l = next(d)
        print(l)
    except StopIteration as e:
        break

print('-----------------------字符串的替换和修改-------------------------')
'''
字符串的替换和修改
sub(pattern, repl, string, count=0, flags=0)
subn(pattern, repl, string, count=0, flags=0)
pattern：正则表达式(规则)
repl：指定的用来替换的字符串
string：目标字符串
count：最多替换次数
flags：默认为0，标志位，用于控制正则表达式的匹配方式
功能：在目标字符串中以正则表达式的规则匹配字符串，再把它们替换成指定的字符串。
     可以通过count指定替换的次数。如果不指定，替换所有的匹配字符串。
区别：sub返回一个被替换了的字符串，而subn返回一个元组。第一个元素为被替换的字符串，第二个元素表示被替换的次数。
'''
str3 = 'sunck is a good good good man'
print(type(re.sub(r'(good)', 'nice', str3, count=2)))
print(re.sub(r'(good)', 'nice', str3, count=2))
print(type(re.subn(r'(good)', 'nice', str3, count=2)))
print(re.subn(r'(good)', 'nice', str3, count=2))

print('------------------------------分组------------------------------')
'''
分组
概念：除了简单的判断是否匹配之外，正则表达式还有提取子字符串的功能。用()表示的就是提取分组
'''
str4 = '010-53247654'
#m = re.match(r'((\d{3})-(\d{8}))', str4)
m = re.match(r'(?P<first>\d{3})-(?P<last>\d{8})', str4)
#使用序号获取对应组的信息，group(0)一直代表的是原始字符串
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())  #查看匹配的各组的情况
print(m.group('first'))
print(m.group('last'))

print('------------------------------编译------------------------------')
'''
编译：当我们使用正则表达式时，re模块会干两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译错误的正则表达式取匹配对象
compile(pattern, flags=0)
pattern：要编译的正则表达式
'''
pat = r'1(([3578]\d)|(47))\d{8}$'
print(re.match(pat, '13600000000'))
re_telephone = re.compile(pat)
print(re_telephone.match('13600000000'))

'''
re.match(pattern, string, flags=0)
re.search(pattern, string, flags=0)
re.findall(pattern, string, flags=0)
re.split(pattern, string, maxsplit=0, flags=0)
re.finditer(pattern, string, flags=0)
re.sub(pattern, repl, string, count=0, flags=0)
re.subn(pattern, repl, string, count=0, flags=0)
re.compile(pattern, flags=0)
'''

'''
QQ     6-10位，全是数字
mail   suncksunck@163.com
phone  010-55348765
user   6-12位
password
ip
url
'''
print('-------------------------------QQ------------------------------')
re_QQ = re.compile(r'^[1-9]\d{5,9}$')
print(re_QQ.search('1234567890'))
print(re_QQ.search('12345678901'))