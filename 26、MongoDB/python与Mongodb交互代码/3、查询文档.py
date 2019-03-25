from pymongo import MongoClient
from pymongo import DESCENDING
from bson.objectid import ObjectId #用于_id查询
#连接服务器
conn = MongoClient('localhost', 27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

#查询文档
'''
#查询部分文档
res = collection.find({'age':{'$gt':30}})
for row in res:
    print(type(row))
    print(row)
'''
'''
#查询所有文档
res = collection.find()
for row in res:
    print(type(row))
    print(row)
'''
'''
#统计查询
res = collection.find().count()
print(res)
print(type(res))
'''
'''
#根据id查询
res = collection.find_one({'_id':ObjectId('5c2ed368bc232fe5ab16cbf3')})
print(res)
print(type(res))
'''
'''
#排序查询
#res = collection.find().sort('age')  #升序
res = collection.find().sort('age', DESCENDING)  #降序
for row in res:
    print(type(row))
    print(row)
'''
#分页查询
res = collection.find().skip(3).limit(3)
print(type(res))
for row in res:
    print(type(row))
    print(row)
#断开
conn.close()