#存储5个人的年龄，求他们的平均年龄
age1=18
age2=20
age3=23
age4=50
age5=70
print((age1+age2+age3+age4+age5)/5)

#思考：要存储100个人的年龄
#解决：使用列表
#本质：是一种有序的集合


'''
创建列表
格式：
列表名=[列表选项1,列表选项2,列表选项3...列表选项n]
'''

#创建了一个空列表
list1=[]
print(list1)

#创建了带有元素的列表
list2=[18,20,23,50,70]
print(sum(list2)/len(list2))

#注意：列表中的元素可以是不同数据类型的
list3=[1,2,"Hailong","good"]
print(list3)

#列表元素的访问  注意：不要越界（下标超出了可表示的范围）
#取值  格式：列表名[下标]
list4=[1,2,3,4,5]
print(list4[2])

#替换
list4[2]=9
print(list4)

#列表操作：
#列表组合
list5=[1,2,3]
list6=[4,5,6]
list7=list5+list6
print(list5)
print(list6)
print(list7)

#列表的重复
list8=[1,2,3]
list9=list8*3
print(list8)
print(list9)

#判断元素是否在列表中
list10=[1,2,3,4,5]
print(3 in list10)
print(4 not in list10)

#列表截取
list11=[1,2,3,4,5,6,7,8,9]
print(list11[2:6])
print(list11[3:])
print(list11[:5])

#二维列表
list12=[[1,2,3],[4,5,6],[7,8,9]]
print(list12[1])
print(list12[1][1])

#列表方法
#append 在列表的末尾添加新的一个元素   list.append(元素)
list13=[1,2,3,4,5]
print(list13)
list13.append(6)
print(list13)
list13.append([7,8,9])
print(list13)

#extend 在列表的末尾追加另一个列表中的多个元素，注意添加列表  list1.extend(list2)
list14=[1,2,3,4,5]
print(list14)
list14.extend([6,7,8])
print(list14)

#insert 在指定下标处添加一个元素，不覆盖原数据，原数据向后顺延   list.insert(下标,元素）
list15=[1,2,3,4,5]
print(list15)
list15.insert(1,100)
print(list15)
list15.insert(2,[1,2])
print(list15)

#pop 移除列表中指定下标处的元素，默认移除最后一个元素   list.pop(下标)
list16=[1,2,3,4,5]
print(list16)
list16.pop()
print(list16)
list16.pop(2)
print(list16)

#remove 移除列表中的某个元素第一个匹配的结果   list.remove(元素)
list17=[1,2,3,4,5,4,5,1]
print(list17)
list17.remove(4)
print(list17)

#clear 清除列表中所有的数据   list.clear()
list18=[1,2,3,4,5]
print(list18)
list18.clear()
print(list18)

#index 从列表中指定范围内找出某个指定元素第一个匹配的索引值  list.index(元素[,start][,end])
list19=[1,2,3,4,5,3,4,5,3]
index19=list19.index(3)
print(index19)
index20=list19.index(3,3,7)
print(index20)

#len 列表中的元素个数   len(list)
list20=[1,2,3,4,5]
print(len(list20))

#max 获取列表中的最大值  max(list)
list21=[1,2,3,4,5]
print(max(list21))

#min 获取列表中的最小值  min(list)
list22=[1,2,3,4,5]
print(len(list22))

#查看元素在列表中出现的次数  list.count(元素))
list23=[1,2,3,4,5,2,3,3,4,1,3]
print(list23.count(3))
num=0
all=list23.count(3)
while num<all:
    list23.remove(3)
    num+=1
print(list23)

#倒序    list.reverse()
list24=[1,2,3,4,5]
print(list24)
list24.reverse()
print(list24)

#排序  list.sort() 从小到大排序   list.sort(reverse=True) 从大到小排序
list25=[2,3,1,4,5]
print(list25)
list25.sort()  #sorted(list25) sorted内置函数
print(list25)

#拷贝
#赋值
list26=[1,2,3,4,5]
print(list26)
list27=list26
print(list27)
list27[1]=200
print(list26)
print(list27)
print(id(list26))
print(id(list27))

#浅拷贝，内存的拷贝  拷贝父对象，不会拷贝对象的内部的子对象。
#即拷贝列表name里面的一级元素的内存地址，不拷贝name里的小列表里的元素的内存地址。
list28=[1,2,3,4,5]
print(list28)
list29=list28.copy()
print(list29)
list29[1]=200
print(list28)
print(list29)
print(id(list28))
print(id(list29))

#list(tuple)   将元组转成列表
list30=list((1,2,3,4,5))
print(list30)


#浅拷贝
import copy
list1=[1,2,3,4,[1,2]]
list2=copy.copy(list1)
list2[4][0]=200
print(list1)
print(list2)
print(id(list1))
print(id(list2))
print(id(list1[4]))
print(id(list2[4]))


'''
#深拷贝
import copy
list1=[1,2,3,4,[1,2]]
list2=copy.deepcopy(list1)
list2[4][0]=200
print(list1)
print(list2)
print(id(list1))
print(id(list2))
print(id(list1[4]))
print(id(list2[4])
'''