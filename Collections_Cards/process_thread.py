# -*- coding: utf-8 -*-

from multiprocessing import Pool
from threading import Thread
import time
import os


def thread_fuc(pn, n):
    time.sleep(1)
    file_name = 'P{0}_{1}'.format(pn, n) + '.txt'

    context = '%s Process ID: %s   ----> Thread: %s' % (pn, os.getpid(), n)
    with open(file_name, 'w') as fp:
        fp.write(context)

def process_fuc(pn):
    #创新4个线程
    for i in range(4):
        t = Thread(target=thread_fuc, args=(pn,i, ))
        t.start()

    return 'Process No: {0}'.format(pn)

if __name__ == '__main__':
    #print 'rr'
    res_list = []
    pool = Pool(processes=4)
    for i in range(12):
        res = pool.apply_async(process_fuc,[i,])
        res_list.append(res)

    for j in res_list:
        print j.get()
