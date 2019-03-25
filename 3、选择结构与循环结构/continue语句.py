'''
continue语句
作用：跳过当前循环中的剩余语句，然后继续下一次循环

注意：跳过距离最近的循环
'''

for i in range(10):
    print(i)
    if i==3:
        continue
    print("*")
    print("&")

num=0
while num<10:
    print(num)
    num += 1
    if num==3:
        continue
    print("*")
    print("&")


