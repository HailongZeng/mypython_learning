'''
break语句：
作用：跳出for和while循环
注意：只能跳出距离他最近的那一层循环
'''
for i in range(10):
    print(i)
    if i==5:
        #结束整个循环
        break