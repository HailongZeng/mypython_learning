from multiprocessing import Process
import time
import os
class SunckProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name
    def run(self):
        print('子进程(%s--%s)启动'%(self.name, os.getpid()))
        #子进程的功能
        time.sleep(3)
        print('子进程(%s--%s)结束' % (self.name, os.getpid()))