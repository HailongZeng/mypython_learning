#导入库
#库中的方法
import random
a=int(input("请输入一个数：")) #input输入的是字符串
b=random.choice([0,1,2])
if a==b:
    print("恭喜你，中奖了！")
else:
    print("很遗憾！")

#产生一个1~100之间的随机数
r1=random.choice(range(1,101))
print(r1)

#从指定范围内，按指定的基数递增的集合中选取一个随机数
#random.randrange([start,]stop[,step])
#start--指定范围的开始值，包含在范围内
#stop--指定范围的结束值，不包含在范围内
#step--指定的递增基数
print(random.randrange(1,100,2))

#随机生成[0,1)之内的小数（浮点数）
print(random.random())

#random.shuffle()将序列的所有元素随机排序，扑克牌的洗牌可用
list=[1,2,3,4,5]
random.shuffle(list)
print(list)

#随机生成一个实数（整数或者小数）
print(random.uniform(3,9))


