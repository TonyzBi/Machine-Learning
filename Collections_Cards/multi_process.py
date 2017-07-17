# -*- coding: utf-8 -*-

from multiprocessing import Pool
import time

def mul(x):
    #print x*x
    time.sleep(1)
    return x*x

pool = Pool(processes=4)
res_list = []

for i in range(10):
    res = pool.apply_async(mul,[i, ])
    # return object of process result
    res_list.append(res)


for x in res_list:
    print x.get(timeout=120)


print '----------------多进程---------------------'


print pool.map(mul, range(10))
