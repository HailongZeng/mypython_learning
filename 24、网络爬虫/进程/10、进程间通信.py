from multiprocessing import Process, Queue
import os, time
def write(q):
    print('启动写子进程%s'%(os.getpid()))
    for chr in ['A','B','C','D']:
        q.put(chr)
        time.sleep(1)
    print('结束写子进程%s' % (os.getpid()))
def read(q):
    print('启动读子进程%s' % (os.getpid()))
    while True:
        value = q.get(True)
        print('value =' + value)
    print('结束读子进程%s' % (os.getpid()))

if __name__ == '__main__':
    print('启动父进程')
    #父进程创建队列，并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()

    #这句话保证子进程结束后再向下执行
    pw.join()
    
    #pr进程里是个死循环，无法等待其结束，只能强行结束
    pr.terminate()

    print('结束父进程')

