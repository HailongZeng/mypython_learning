import threading
import time

def func():
    #事件对象
    event = threading.Event()
    print(type(event))
    def run():
        for i in range(5):
            #阻塞，等待事件的触发
            event.wait()
            #重置，下一次继续阻塞
            event.clear()
            print('sunck is a good man!!%d'%i)
    t = threading.Thread(target=run).start()
    return event

e = func()

#触发事件
for i in range(5):
    time.sleep(2)
    e.set()