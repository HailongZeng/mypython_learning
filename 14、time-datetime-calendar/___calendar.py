'''
日历模块
'''
#使用

import calendar
#返回指定某年某月的日历
print(calendar.month(2018, 10))

#返回指定年的日历
print(calendar.calendar(2018))


#闰年返回True，否则返回False
print(calendar.isleap(2000))

#返回某个月的weekday的第一天和这个月的天数
print(calendar.monthrange(2018, 10))

#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2018, 10))

#返回在Y1,Y2两年之间的闰年总数
print(calendar.leapdays(1900,2000))

