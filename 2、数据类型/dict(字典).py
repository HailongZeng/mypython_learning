'''
dict(字典)

概述：使用键-值对(key-value)存储，具有极快的查找速度

注意：字典是无序的

key的特性：
1、字典中的key必须唯一
2、key必须是不可变的对象
3、字符串、整数等都是不可变的，可以作为key
4、list是可变的，不能作为key

和list的比较：
1、查找和插入的速度极快，不会随着key-value的增加而变慢；
2、需要占用大量的内存，内存耗费多；

list的优缺点：
1、查找和插入的速度会随着数据量的增多而减慢；
2、占用空间小，浪费的内存小。

思考：保存多位学生的姓名与成绩

使用字典，学生姓名作为key，学生成绩作为值
'''
dict1={"Tom":60,"lilei":80}
print(dict1)

#元素的访问
#获取：格式 字典名[key]
print(dict1["lilei"])
#print(dict1["sunck"])  #dict1中没有sunck这个键
print(dict1.get("sunck")) #dict1中没有sunck这个键,获得的值为None

#添加:格式 字典名[key]=value
dict1["hanmeimei"]=90
print(dict1)
#因为一个key对应一个value，所以，多次对一个key的value赋值，其实就是修改值
dict1["lilei"]=70
print(dict1)

#删除：格式 字典名.pop(key)
dict1.pop("Tom")
print(dict1)

#遍历
for key in dict1:
    print(key,dict1[key])

print(dict1.values())   #获得dict1中所有value的列表
for value in dict1.values():
    print(value)

print(dict1.items())    #获得dict1中所有的键值对的列表，列表中的元素为元组
for k,v in dict1.items():
    print(k,v)

for i,v2 in enumerate(dict1):
    print(i,v2)
