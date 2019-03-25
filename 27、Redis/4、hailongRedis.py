import redis

class HailongRedis():
    def __init__(self,host='localhost',port=6379):
        self.__redis = redis.StrictRedis(host=host,port=port)  #连接redis服务器
    def set(self,key,value):
        self.__redis.set(key,value)
    def get(self,key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ''