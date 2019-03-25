'''
UTC(世界协调时间):格林尼治天文时间，世界标准时间，在中国来说是UTC+8
DST(夏令时):是一种节约能源而人为规定时间制度，在夏季调快1个小时

时间的表示形式：
1、时间戳
以整型或浮点型表示时间的一个以秒为单位的时间间隔。这个时间间隔
的基础值是从1970年1月1日凌晨开始算起到现在多少秒。
2、元组
一个Python的数据结构表示，这个元组有9个整型内容
year
month
day
hours
minutes
seconds
weekday
Julia day
flag(1或-1或0)
3、格式化字符串
%a  本地(locale)简化星期名称
%A  本地完整星期的简化
%b  本地简化月份名称
%B  本地完整月份名称
%c  本地对应的日期和时间表示
%d  一个月中的第几天(01-31)
%H  一天中的第几个小时(24小时制，00-23)
%I  第几个小时(12小时制，01-12)
%j  一年中的第几天(001-366)
%m  月份(01-12)
%M  分钟数(00-59)
%p  本地am或者pm的相应符
%S  秒(01-61)
%U  一年中的星期数。(00-53)，星期天是一个星期的开始。)第一个星期天之前的所有天数都放在第0周
%x  和%U基本相同，不同的是%x以星期一为一个星期的开始
%X  本地相应的日期
%y  去掉世纪的年份(00-99)
%Y  完整的年份
%Z  时区的名字(如果不存在为空字符)
%%  '%'字符

2012-07-29 12:30:02
'''
import time

#返回当前时间的时间戳。浮点数形式，不需要参数
c=time.time()
print(c)

#将时间戳转为UTC时间元组
t=time.gmtime(c)
print(t)

#将时间戳转为本地时间元组
b=time.localtime(c)
print(b)

#将本地时间元组转成时间戳
m=time.mktime(b)
print(m)

#将时间元组转成字符串
s=time.asctime(b)  #time.asctime(time.localtime(time.time()))
print(s)

#将时间戳转成字符串
p=time.ctime(c)
print(p)

#将时间元组转换成自定义格式的字符串，如果不写时间元组(即下一行代码b为填写)，默认为本地时间元组
q1=time.strftime('%Y-%m-%d %H:%M:%S', t)
q2=time.strftime('%Y-%m-%d %H:%M:%S',)
print(q1,q2)

#将时间字符串转为时间元组
w=time.strptime(q1, '%Y-%m-%d %X')
print(w)

#延迟一个时间，整型或者浮点型
#time.sleep(4)

'''
#返回当前程序的CPU执行时间
#Unix形同始终返回全部的运行时间
#windows从第二次开始，都是以第一次调用此函数的开始时间戳作为基数
y1=time.clock()
time.sleep(1)
y2=time.clock()
print(y1)
print(y2)
'''