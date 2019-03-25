'''
生产者：产生数据，放进队列中
消费者：处理数据，从队列中拿出数据
先进先出
'''
import threading
import queue
import time
import random

#生产者
def product(id,q):
    while True:
        num = random.randint(0, 10000)
        q.put(num)
        print('生产者%d生产了%d数据放入了队列'%(id,num))
        time.sleep(3)
    #任务完成
    q.task_done()


#消费者
def customer(id,q):
    while True:
        item = q.get()
        if item is None:
            break
        print('消费者%d消费了%d数据'%(id,item))
    #任务完成
    q.task_done()

if __name__ == '__main__':
    #消息队列
    q = queue.Queue()
    #启动生产者
    for i in range(4):
        threading.Thread(target=product, args=(i,q)).start()
    #启动消费者
    for i in range(4):
        threading.Thread(target=customer, args=(i,q)).start()