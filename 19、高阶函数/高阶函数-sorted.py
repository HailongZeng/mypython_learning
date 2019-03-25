#排序：冒泡，选择    快速，插入，计数器
#普通排序
list1 = [4,7,2,6,3]
list2 = sorted(list1)
print(list1)
print(list2)
#按绝对值大小排序
list3 = [4,-7,2,6,-3]

#key接受函数来实现自定义排序规则
list4 = sorted(list3, key=abs)  #默认升序排序
print(list3)
print(list4)

#降序
list5 = [4,7,2,6,3]
list6 = sorted(list5, reverse=True)  #默认升序排序
print(list5)
print(list6)


def myLen(str):
    return len(str)

list7 = ['b11','a21342','c3212432','dd1244']
list8 = sorted(list7)    #默认升序排序，按首字母排序
list9 = sorted(list7, key=len)  #按元素大小排序
list10 = sorted(list7, key=myLen)
print(list7)
print(list8)
print(list9)
print(list10)