'''
tuple

本质：一种有序集合

特点：
1、与列表非常相似
2、一旦初始化就不能修改
3、使用小括号

创建tuple
格式：元组名=(元组元素1,元组元素2,元组元素3......元组元素n)

'''

#创建元组
tuple1=()
print(tuple1)
#创建带有元素的元组
#元组中的元素类型可以不同
tuple2=(1,2,3,"good",True)
print(tuple2)
#定义只由一个元素的元组
tuple3=(1,)   #注意逗号不能少，否则将创建一个int
print(tuple3)
print(type(tuple3))


#元组元素的访问
#格式：元组名[下标]
#下标从0开始
tuple4=(1,2,3,4,5)
print(tuple4[0])
print(tuple4[1])
print(tuple4[2])
print(tuple4[3])
print(tuple4[4])
#print(tuple4[5])  #下标超过了范围，即越界
#从后开始获取元素
print(tuple4[-1])
print(tuple4[-2])
print(tuple4[-3])
print(tuple4[-4])
print(tuple4[-5])
#print(tuple4[-6])  #下标超过了范围，即越界



#修改元组
#元组中的元素不能改变，但是若是元组中包含可变序列元素，可变序列可改变它之中的元素
tuple5=(1,2,3,4,5)
#tuple5[0]=100   #报错，元组不能变
print(tuple5)
tuple6=(1,2,3,4,[5,6,7])
tuple6[-1][0]=500
print(tuple6)



#删除元组
tuple7=(1,2,3)
del tuple6
#print(tuple6)  #报错，因为元组删除了，不存在



#元组的操作
#元组连接
t8=(1,2,3)
t9=(4,5,6)
print(t8+t9)  #生成了一个新的元组
print(t8,t9)

#元组重复
t10=(1,2,3)
print(t10*3)

#判断元素是否在元组中
t11=(1,2,3)
print(1 in t11)
print(2 not in t11)

#元组的截取
#格式：元组名[开始下标:结束下标]
#从开始下标开始截取，截取到结束下标之前
t12=(1,2,3,4,5,6,7,8,9)
print(t12[3:7])
print(t12[3:])
print(t12[:7])

#二维元组:元素为一维元组的元组
t13=((1,2,3),(4,5,6),(7,8,9))
print(t13[1][1])





#元组的方法
#len()   返回元组中元素的个数
t14=(1,2,3,4,5)
print(len(t14))

#max()   返回元组中的最大值
#min()   返回元组中的最小值
print(max((5,6,7,8,9)))
print(min((5,6,7,8,9)))

#tuple(list)  将列表转成元组
list=[1,2,3]
t15=tuple(list)
print(t15)

#元组的遍历
for i in (1,2,3,4,5):
    print(i)
