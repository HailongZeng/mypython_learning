import pymysql

#连接数据库
#参数1：mysql服务所在主机的IP
#参数2：用户名
#参数3：密码
#参数4：要连接的数据库名
db = pymysql.connect('localhost','root','Zhl19960320','2019.01.02')

#创建一个cursor对象
cursor = db.cursor()

sql = 'select version()'
#sql = 'select now()'

#执行sql语句
cursor.execute(sql)

#获取返回的信息
data = cursor.fetchone()
print(data)

#断开
cursor.close()
db.close()