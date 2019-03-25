import pymysql

db = pymysql.connect('localhost','root','Zhl19960320','2019.01.02')
cursor = db.cursor()

#检查表是否存在，如果存在则删除
cursor.execute('drop table if exists bandcard')

#建表
sql = 'create table bandcard(id int auto_increment primary key, money int not null)'
cursor.execute(sql)

cursor.close()
db.close()