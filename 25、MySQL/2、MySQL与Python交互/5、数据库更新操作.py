import pymysql

db = pymysql.connect('localhost','root','Zhl19960320','2019.01.02')
cursor = db.cursor()

#更新数据
sql = 'update bandcard set money=1000 where id=1'
try:
    cursor.execute(sql)
    db.commit()  #提交事务，要插入数据必须写这条命令
except:
    #如果提交失败，回滚到上一次数据
    db.rollback()

cursor.close()
db.close()