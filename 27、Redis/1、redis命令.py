'''
连接redis服务器
1、输入：redis-cli，得到127.0.0.1:6379>，然后再输入ping得到PONG，代表redis服务器已经连接成功
shutdown终止redis服务器连接
ps -ef | grep -i redis
kill -9 进程号
一、键(key)
    1、查找键，参数支持正则，pattern见正则
        keys pattern
    2、判断键是否存在，如果存在返回1，不存在返回0
        exists key [key ...]
    3、查看键对应的value类型
        type key
    4、删除键及对应的值，返回1表示该键存在且删除成功，返回0表示不存在该键
        del key [key ...]
    5、设置过期时间，以秒为单位，超过时间后该键自动消失
        expire key seconds
    6、查看有效时间，以秒为单位
        ttl key

二、字符串(string)
    概述：String是redis最基本的类型，最大能储存512MB的数据，String类型是二进制安全的，即可以
    存储任何数据，比如数字、图片、序列化对象等。
    1、设置
        a、设置键值
            set key value
        b、设置键值及过期时间，以秒为单位
            setex key seconds value
        c、设置多个键值
            mset key value [key value ...]
    2、获取
        a、根据键获取值，如果键不存在则返回None
            get key
        b、根据多个键获取多个值
            mget key [key ...]
    3、运算
        要求：值是字符串类型的数字
        a、将key对应的值加1
            incr key
        b、将key对应的值减1
            decr key
        c、将key对应的值加整数
            incrby key intnum
        d、将key对应的值减整数
            decrby key intnum
    4、其它
        a、追加值
            append key value
        b、获取值长度
            strlen key

三、哈希(hash)
    概述：hash用于存储对象
    {
        name:'tom',
        age:18
    }
    1、设置
        a、设置单个值
            hset key field value
        b、设置多个值
            hmset key field value [field value ..]
    2、获取
        a、获取一个属性的值
            hget key field
        b、获取多个属性的值
            hmget key field [field ...]
        c、获取所有属性和值
            hgetall key
        d、获取所有属性
            hkeys key
        e、获取所有值
            hvals key
        f、返回包含数据(键值对)的个数
            hlen key
    3、其它
        a、判断属性是否存在，存在返回1，不存在返回0
            hexists key field
        b、删除属性及值
            hdel key field [field ...]
        c、返回值的字符串长度
            hstrlen key field

四、列表(list)
    概述：列表的元素类型为String，按照插入顺序排序，在列表的头部或尾部添加元素
    1、设置
        a、在头部插入
            lpush key value [value ...]
        b、在尾部插入
            rpush key value [value ...]
        c、在一个元素的前|后插入新元素，pivot为列表中已有的数据
            linsert key before/after pivot value
        d、设置指定索引的元素值
            lset key index value
            注意：index从0开始
            注意：index可以为负数，表示偏移量从list的尾部开始，如-1表示最后一个元素
    2、获取
        a、移除并返回key对应的list的第一个元素
            lpop key
        b、移除并返回key对应的list的最后一个元素
            rpop key
        c、返回存储在key的列表中的指定范围的元素
            lrange key start end
            注意：start end都是从0开始
            注意：偏移量可以是负数
    3、其它
        a、裁剪列表，改为原集合的一个子集
            ltrim key start end
            注意：start end都是从0开始
            注意：偏移量可以是负数
        b、返回存储在key里的list的长度
            llen key
        c、返回列表中索引对应的值
            lindex key index

五、集合(set)
    概述：无序集合，元素类型为String类型，元素具有唯一性，不重复
    1、设置
        a、添加元素
            sadd key member [member ...]
        b、删除并获取一个集合里面的元素
            spop key
        c、从集合里删除一个或多个元素
            srem key member [member ...]
    2、获取
        a、返回key集合中所有元素
            smembers key
        b、返回集合元素个数
            scard key
    3、其它
        a、求多个集合的交集
            sinter key [key ...]
        b、求多个集合的差集
            sdiff key [key ...]
        c、求多个集合的合集
            sunion key [key ...]
        d、判断元素是否在集合中，存在返回1，不存在返回0
            sismember key member

六、有序集合(zset)
    概述：
    a、有序集合，元素类型为String，元素具有唯一性，不能重复
    b、每个元素都会关联一个double类型的score(表示权重)，通过权重的大小排序，元素的score可以相同
    1、设置
        a、添加
            zadd key score member [score member ...]
            zadd z1 1 a 5 b 3 c 2 d 4 e
        b、从集合里删除一个或多个元素
            zrem key member [member ...]
    2、获取
        a、返回指定范围的元素
            zrange key start end
        b、返回元素个数
            zcard key
        c、返回有序集合key中，score在min和max之间的元素的个数
            zcount key min max
        d、返回有序集合key中，成员member的score值
            zscore key member
'''