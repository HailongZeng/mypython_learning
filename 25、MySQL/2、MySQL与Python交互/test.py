from hailongSQL import HailongSQL

s = HailongSQL('localhost','root','Zhl19960320','2019.01.02')
res = s.get_all('select * from bandcard where money>400')
for row in res:
    print('%d--%d'%(row[0],row[1]))