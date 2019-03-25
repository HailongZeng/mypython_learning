import re
#pip 包管理工具

'''
re.match函数
原型：match(pattern, string, flags=0)
pattern：匹配的正则表达式
string：要匹配的字符串
flags：默认为0，标志位，用于控制正则表达式的匹配方式，值如下 
re.I    忽略大小写
re.L    做本地户识别，表示特殊字符集\w \W \b \B \s \S
re.M    多行匹配，影响^和$
re.S    是.匹配包括换行符在内的所有字符
re.U    根据Unicode字符集解析字符，影响\w \W \b \B \d \D \s \S
re.X    使我们以更灵活的格式理解正则表达式，增加可读性，忽略空格和'#'后面的注释
参数：
功能：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，返回None
'''
#www.baidu.com
print(re.match('www', 'www.baidu.com').span())
print(re.match('www', 'ww.baidu.com'))
print(re.match('www', 'baidu.wwwcom'))
print(re.match('www', 'Www.baidu.com'))
print(re.match('www', 'wwW.baidu.com', flags=re.I))
#扫描整个字符串，返回从起始位置成功的匹配

print('-------------------------------------------')

'''
re.search函数
原型：search(pattern, string, flags=0)
参数：
pattern：匹配的正则表达式
string：要匹配的字符串
flags：标志位，用于控制正则表达式的匹配方式
功能：扫描整个字符串，并返回第一个成功的匹配
'''

print(re.search('sunck', 'good man is sunck!sunck is nice'))
print(re.search('sunck', 'good man is sunck!sunck is nice').span())

print('-------------------------------------------')

'''
re.findall函数
原型：findall(pattern, string, flags=0)
参数：
pattern：匹配的正则表达式
string：要匹配的字符串
flags：标志位，用于控制正则表达式的匹配方式
功能：扫描整个字符串，并返回结果列表
'''
print(re.findall('sunck', 'good man is sunck!Sunck is nice'))
print(re.findall('sunck', 'good man is sunck!Sunck is nice', flags=re.I))

print('--------------匹配单个字符和数字---------------------')
'''
.                匹配除换行符以外的任意字符
[0123456789]     []是字符集合，表示匹配方括号中所包含的任意一个字符
[sunck]          匹配's','u','n','c','k'中任意一个字符
[a-z]            匹配任意小写字母
[A-Z]            匹配任意大写字母
[0-9]            匹配任意数字，类似[0123456789]
[0-9a-zA-Z]      匹配任意的数字和字母
[0-9a-zA-Z_]     匹配任意的数字、字母和下划线
[^sunck]         匹配除了's','u','n','c','k'这几个字符以外的所有字符，中括号中的^称为脱字符，表示不匹配集合中的字符
[^0-9]           匹配所有的非数字字符
\d               匹配所有的数字，效果同[0-9]
\D               匹配非数字字符，效果同[^0-9]
\w               匹配数字、字母和下划线，效果同[0-9a-zA-Z_]
\W               匹配非数字、字母和下划线，效果同[^0-9a-zA-Z_]
\s               匹配任意的空白符(空格、换行、回车、换页、制表)，效果同[ \f\n\r\t]
\S               匹配任意的非空白符，效果同[^ \f\n\r\t]
'''
print(re.search('.', 'sunck is a good man'))
print(re.search('[0123456789]', 'sunck is a good man 3'))
print(re.findall('\d', 'zenghailong19960320'))


print('---------------锚字符（边界字符）-----------------')
'''
^                行首匹配，和在[]里的^不是一个意思
$                行尾匹配

\A               匹配字符串开始，它和^的区别是：\A只匹配整个字符串的开头，即使在re.M模式下它也不会匹配它行的行首
\Z               匹配字符串结尾，它和$的区别是：\Z只匹配整个字符串的结尾，即使在re.M模式下它也不会匹配它行的行尾
\b               匹配一个单词的边界，也就是指单词和空格间的位置,'er\b'可以匹配never，但是不能匹配'nerve'
\B               匹配非单词边界，'er\B'可以匹配nerve，但是不能匹配'never'
'''
print(re.search('^sunck', 'sunck is a good man!'))
print(re.search('man!$', 'sunck is a good man!'))
print(re.findall('^sunck', 'sunck is a good man\nsunck is a nice man', re.M))
print(re.findall('\Asunck', 'sunck is a good man\nsunck is a nice man', re.M))
print(re.findall('man$', 'sunck is a good man\nsunck is a nice man', re.M))
print(re.findall('man\Z', 'sunck is a good man\nsunck is a nice man', re.M))
print(re.search(r'er\b', 'never'))
print(re.search(r'er\b', 'nerve'))
print(re.search(r'er\B', 'never'))
print(re.search('er\B', 'nerve'))

print('----------------------匹配多个字符---------------------')
'''
说明：下方的x、y、z、n、m均为假设的普通字符，不是正则表达式的元字符，此处n、m为int
(xyz)       匹配小括号内的xyz(作为一个整体去匹配)
x?          匹配0个或者1个x
x*          匹配0个或者任意多个x(.*表示匹配0个或者任意多个字符(换行符除外))
x+          匹配至少一个x
x{n}        匹配确定的n个x(n是一个非负整数)
x{n,}       匹配至少n个x
x{n,m}      匹配至少n个至多m个x(注意：m >= n)
x|y         |表示或，匹配的是x或者y字符
'''
print(re.findall(r'(good)', 'sunckgood is a good man, sunck is a nice man'))
print(re.findall(r'a?', 'aaabaa'))     #非贪婪匹配(尽可能少地匹配)
print(re.findall(r'a*', 'aaaabaa'))    #贪婪匹配，尽可能多地匹配
print(re.findall(r'a+', 'aaaabaa'))    #贪婪匹配，尽可能多地匹配
print(re.findall(r'a{3}', 'aaaabaa'))
print(re.findall(r'a{3,}', 'aaaabaa')) #贪婪匹配，尽可能多地匹配
print(re.findall(r'a{2,5}', 'aaaabaa'))
print(re.findall(r'((s|S)unck)', 'sunck--Sunck'))


#需求，提取sunck......man
str = 'sunck is a good man!sunck is a nice man!sunck is a very handsome man'
print(re.findall(r'sunck.*?man', str))

print('-------------------特殊-----------------')
'''
*?    +?    x?   最小匹配，通常都是尽可能多地匹配，可以使用这种解决贪婪匹配
(?:x)    类似于(xyz),但它不表示一个组
'''
#注释：C语言：/* part1 */   /* part2 */
print(re.findall(r'//*.*?/*/', r'/* part1 */  /* part2 */'))