import pymysql

db = pymysql.connect('localhost','root','Zhl19960320','2019.01.02')
cursor = db.cursor()

#插入数据
sql = 'insert into bandcard values(0,300),(0,400),(0,500),(0,600),(0,700)'
try:
    cursor.execute(sql)
    db.commit()  #提交事务，要插入数据必须写这条命令
except:
    #如果提交失败，回滚到上一次数据
    db.rollback()

cursor.close()
db.close()