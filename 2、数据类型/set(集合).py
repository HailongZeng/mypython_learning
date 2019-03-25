'''
set（集合）:类似dict，是一组key的集合，不存储value

本质：无序和无重复元素的集合
'''

#创建
#创建set需要一个list或者tuple或者dict作为输入集合
#重复元素在set中会自动被过滤
s1=set([1,2,3,4,5,1,2])
print(s1)

#添加 add()
s2=set((1,2,3,4,5))
s2.add(6)
s2.add(3)  #可以添加，但是重复元素会被过滤
#s2.add([7,8,9])  #set的元素不能是列表，因为列表可变，set是作为key的集合
s2.add((7,8,9))
#s2.add({1:"a"})  #set的元素不能是字典，因为字典可变
print(s2)

#插入整个list,tuple,字符串分成元素插入 update()
s3=set([1,2,3,4,5])
s3.update([6,7,8])
print(s3)
s3.update(("abc!"))
print(s3)

#删除  remove()
s4=set([1,2,3,4,5])
s4.remove(3)
print(s4)

#遍历
s5=set([1,2,3,4,5])
for i in s5:
    print(i)
#set没有索引
#print(s5[3])  #报错，因为集合是无序的，没有索引
s5.update("abs")
for index,data in enumerate(s5):
    print(index,data)

s6=set([1,2,3])
s7=set((2,3,4))
#交集
a1=s6 & s7
print(a1)
#并集
a2=s6 | s7
print(a2)