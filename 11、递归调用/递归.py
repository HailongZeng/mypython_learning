'''
递归调用：一个函数
'''
'''
方式：
1、写出临界条件
2、找这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果
'''

#输入一个数（大于等于1），求1+2+3+......+n的和
def sum1(n):
    sum1=0
    for x in range(1,n+1):
        sum1+=x
    return sum1
print(sum1(10))


'''
1+2+3+4+5
sum2(2)   sum2(1)+2
sum2(3)   sum2(2)+3
sum2(4)   sum2(3)+4
sum2(5)   sum2(4)+5
'''
def sum2(n):
    if n==1:
        return 1
    else:
        return n+sum2(n-1)
print(sum2(5))