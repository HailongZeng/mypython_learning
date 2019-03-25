# -*- coding: utf-8 -*-
"""
链表的实现
"""
class Node(object):
    '''
    data: 节点保存的数据
    _next: 保存下一个节点对象
    '''
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出data
        '''
        return str(self.val)

def deleteNode(self, node):# 不返回就是改变自身
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next
def Creatlist(n):
    if n<=0:
        return False
    if n==1:
        return Node(1)    # 只有一个节点
    else:
        root=Node(1)
        tmp=root
        for i in range(2,n+1):       #  一个一个的增加节点
            tmp.next=Node(i)
            tmp=tmp.next
    return root            # 返回根节点

def printlist(head):       # 打印链表
    p=head
    while p!=None:
        print p.val
        p=p.next

def listlen(head):       # 链表长度
    c=0
    p=head
    while p!=None:
        c=c+1
        p=p.next
    return c

def insert(head, n): #插入
    if n<1 or n>listlen(head):
        return

    p = head
    for i in range(1, n-1):
        p=p.next
    a = raw_input('val:')
    t = Node(val = a)
    t.next = p.next
    p.next = t #重点，改变插入的指针，再改变前一位的指针
    return head

def dellist(head, n): #删除
    if n<1 or n>listlen(head):
        return
    elif n is 1:
        head=head.next   # 删除头
    else:
        p = head
        for i in range(1, n-1):
            p=p.next
        p.next = p.next.next
    return head

l1 = Creatlist(4)
l1.val=7
l1.next.val=2
l1.next.next.val = 4
l1.next.next.next.val = 3
printlist(l1)
l2 = Creatlist(3)
l2.val=5
l2.next.val=6
l2.next.next.val = 4
printlist(l2)
p1 = l1
p2 = l2
arr1 = []
arr2 = []
while p1 != None:
    arr1.append(p1.val)
    p1 = p1.next
while p2 != None:
    arr2.append(p2.val)
    p2 = p2.next
ans = []
plus = 0
for i in range(max(len(arr1),len(arr2))):
    try:
        num = arr1[-i-1]+arr2[-i-1] + plus
        if num>=10:
            plus = 1
            n = num%10
        else:
            n = num
            plus = 0
        ans.insert(0,n)
    except:
        n = arr1[-i-1] + plus
        ans.insert(0,n)
