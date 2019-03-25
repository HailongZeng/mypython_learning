import redis

pool = redis.ConnectionPool(host='localhost',port=6379)
r = redis.Redis(connection_pool=pool)

r.set('age',22)
print(r.get('age').decode('utf8'))