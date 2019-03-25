'''
启动mongodb，mongod --dbpath=路径名
另打开一个终端，输入mongo，进入mongodb命令行中
一、操作mongodb数据库
    1、创建数据库
        语法：use 数据库名
        注意：如果数据库不存在则创建，否则切换到指定的数据库
        注意：如果刚刚创建的数据库不在列表内，如果要显示它，
             我们需要向刚刚创建的数据库中插入一些数据
        ( db.student.insert({name:'tom', age:18, gender:1,
          address:'北京', isDelete:0}) )
    2、删除数据库
        前提：使用当前数据库(use 数据库名)
        db.dropDatabase()
    3、查看所有数据：
        show dbs
    4、查看当前正在使用的数据库
        a、db
        b、db.getName()
    5、断开连接
        exit
    6、查看命令api
        help

二、集合操作
    1、查看当前数据库下有哪些集合
        show collections
    2、创建集合
        a、
            语法：db.createCollection('集合名')
            示例：db.createCollection('class')
        b、
            语法：db.集合名.insert(document)
            示例：db.class.insert({id:1, class:'python01', stuNum:60})
        区别：两者的区别在于前者创建的是一个空的集合，后者创建一个空的集合并插入一个文档
    3、删除当前数据库中的集合
        语法：db.集合名.drop()
        示例：db.class.drop()

三、文档操作
    1、插入文档
        a、使用insert()方法插入文档
            语法：db.集合名.insert(document)
            插入一个：db.student.insert({name:'lileilei', age:19, gender:1,
                    address:'北京',isDelete:0})
            语法：db.集合名.insert([文档1, 文档2, ......, 文档n])
            插入多个：db.student.insert([{name:'hanmeimei', age:20, gender:0,
                    address:'上海', isDelete:0},{name:'Jack', age:22, gender:1,
                    address:'NewYork', isDelete:0}])
        b、使用save()方法插入文档
            语法：db.集合名.save(文档)
            说明：如果不指定_id字段，save()方法类似于insert()方法。
                 如果指定_id字段，则会更新_id字段的数据
            示例1：db.student.save({name:'John', age:25, gender:1,
                  address:'San Diego', isDelete:0})
            示例2：db.student.save({_id:ObjectId('5c2ed608bc232fe5ab16cbf6'),
                  name:'John', age:20, gender:1, address:'Las Vegas', isDelete:0})
    2、文档更新
        a、update()方法用于更新已存在的文档
        语法：
            db.集合名.update(
                <query>,
                <update>,
                {
                    upset:<boolean>,
                    multi:<boolean>,
                    writeConcern:<document>
                }
            )
        参数说明：
            (1)query:update的查询条件，类似于sql里update语句内where后面的内容
            (2)update:
            update的对象和一些更新的操作符($set,$inc)等，$set直接更新，$inc在原有的基础
            上累积后更新
            (3)upset:
            可选，如果不存在update的记录，是否当新数据插入，true为插入，False为不插入，默认为false
            (4)multi:
            可选，mongodb默认是false，只更新找到的第一条记录，如果这个参数为true,就按照条件查找
            出来的数据全部更新
            (5)writeConcern:可选，抛出异常的级别
        需求：将lileilei的年龄更新为25
        示例：db.student.update({name:'lileilei'},{$set:{age:25}})
        需求：将lileilei的年龄加25
        示例：db.student.update({name:'lileilei'},{$inc:{age:25}})
        需求：将name条件为lileilei的年龄全部更新为40
        示例：db.student.update({name:'lileilei'},{$set:{age:40}},{multi:true})
        b、save()方法通过传入的文档替换已有文档
            语法：
                db.集合名.save(
                    document,
                    {
                        writeConcern:<document>
                    }
                )
            参数说明：
                document:文档数据
                writeConcern:可选，抛出异常的级别
    3、文档删除
        说明：在执行remove()函数前，先执行find()命令来判断执行的条件是否存在是一个良好的习惯
        语法：
            db.集合名.remove(
                query,
                {
                    justOne:<boolean>,
                    writeConcern:<document>
                }
            )
        参数说明：
            query:可选，删除的文档的条件
            justOne:可选，如果为true或1，则只删除一个文档
        需求：删除name为tom的文档
        示例：db.student.remove({name:'tom'})
    4、文档查询
        a、find()方法
            查询集合下所有的数据
            语法：db.集合名.find()
            示例：db.student.find()
        b、find()方法
            查询指定列
            语法：
            db.集合名.find(query,
                {
                    <key>:1,
                    <key>:1,
                    ...
                    <key>:1
                }
            )
            参数说明：
                query:查询条件
                key:要显示的字段，1表示要显示
            需求：查询集合中gender为1的数据，并显示出满足条件的文档的name和age
            示例：db.student.find({gender:1},{name:1,age:1})
        c、pretty()方法以格式化的方式来显示文档
            示例：db.student.find().pretty()
        d、findOne()方法查询匹配结果的第一条数据
            示例：db.student.findOne({gender:1})
    5、查询条件操作符
        作用：条件操作符用于比较两个表达式并从Mongodb集合中获取数据
        a、大于        $gt
            语法：db.集合名.find({<key>:{$gt:<value>}})
            需求：查询年龄大于20的文档
            示例：db.student.find({age:{$gt:20}})
        b、大于等于     $gte
            语法：db.集合名.find({<key>:{$gte:<value>}})
        c、小于        $lt
            语法：db.集合名.find({<key>:{$lt:<value>}})
        d、小于等于     $lte
            语法：db.集合名.find({<key>:{$lte:<value>}})
        e、大于等于和小于等于    $gte和$lte
            语法：db.集合名.find({<key>:{$gte:<value>,$lte:<value>}})
        f、等于        :
            语法：db.集合名.find({<key>:<value>})
        g、使用_id进行查询
            语法：db.集合名.find({'_id':ObjectId('id值')})
            示例：db.student.find({'_id':ObjectId('5c2ed3e4bc232fe5ab16cbf4')})
        h、查询某个结果集的数据条数
            语法：db.集合名.find().count()
            示例：db.student.find().count()
        i、查询某个字段的值当中是否包含另一个值
            语法：db.集合名.find({<key>:/值/})
            示例：db.student.find({name:/ile/})
        j、查询某个字段的值是否以另一个值开头
            语法：db.集合名.find({<key>:/^值/})
            示例：db.student.find({name:/^li/})
    6、条件查询and和or
        a、AND条件
            语法：db.集合名.find({条件1,条件2,...,条件n})
            示例：db.student.find({gender:1,age:{$gt:22}})
        b、OR条件
            语法：
                db.集合名.find(
                    {
                        $or:[{条件1},{条件2},...,{条件n}]
                    }
                )
            示例：db.student.find({$or:[{age:22},{age:{$gte:30}}]})
        c、AND和OR联合使用
            语法：
                db.集合名.find(
                    {
                        条件1,
                        条件2，
                        $or:[{条件3},{条件4}]
                    }
                )
            示例：db.student.find({gender:1,age:{$gt:22},$or:[{name:/^li/},{name:/h/}]})
    7、limit、skip
        a、limit()：读取指定数量的数据记录
            db.student.find().limit(3)
        b、skip()：跳过指定数量的数据
            db.student.find().skip(3)
        c、limit和skip联合使用
            通常用这种方式来实现分页功能
            db.student.find().skip(1).limit(2)
    8、排序
        语法：db.集合名.find().sort({<key>:1|-1})
        示例：db.student.find().sort({age:1})
        注意：1表示升序，-1表示降序
'''