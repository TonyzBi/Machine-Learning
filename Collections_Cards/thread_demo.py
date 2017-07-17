# -*- coding: utf-8 -*-
import threading
import time


def func(argv):
    print argv

t1 = threading.Thread(target=func, args=('hello',))

t1.start()


print '----------------------------------------------------------'
e1 = threading.Event()
e2 = threading.Event()

def producer():
    while True:
        #print 'Cheff: Waiting for somebody to buy dumpling..'
        # 等来买包子
        e1.wait()
        e1.clear()
        #print 'Cheff: somebody come to buy ...'
        print '------------------------------------------------------'
        print 'Cheff: I am making a dumpling....'
        time.sleep(2)
        print 'Cheff: Finished to make dumpling'
        #通知包子已做好
        e2.set()
        print 'Cheff: Here is the dumpling, Here you are..'

def consumer():
    while True:
        #print 'Costumer: come to buy dumplings ...'
        # informi: coming to buy dumpling
        e1.set()
        time.sleep(1)
        print 'Customor: waiting for dumpling for ready...'

        e2.wait()
        e2.clear()
        print 'Customor: Dumplings has been ready, I got a dumplings...'
        time.sleep(1)


p = threading.Thread(target=producer)
p.start()

c = threading.Thread(target=consumer)
c.start()



