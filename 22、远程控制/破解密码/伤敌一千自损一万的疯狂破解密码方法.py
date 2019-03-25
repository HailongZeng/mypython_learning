import time
import itertools
#mylist = list(itertools.product('0123456789', repeat=4))
#print(len(mylist))
passwd = (''.join(x) for x in itertools.product('0123456789', repeat=4))  #迭代器
while True:
    try:
        time.sleep(0.5)
        str = next(passwd)
        print(str)
    except StopIteration as e:
        break
