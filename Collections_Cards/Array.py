# -*- coding: utf-8 -*-

from array import array
from random import random
from random import randrange
import numpy as np

floats = array('d', (random() for i in range(10**3)))

print floats[995:-1]
print len(floats)

fp = open('float.bin','wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('float.bin', 'rb')
floats2.fromfile(fp, 10**3)
print floats2[995:-1]

print floats == floats2

x = np.arange(12)
print x

x.shape = 3,4

print x
print x[2]

print x[:,1]

print x.transpose()

numbers = np.loadtxt('floats.txt',dtype=float,comments='#',delimiter=',')
print numbers

numbers = numbers * 10
np.save('int_mutiply10',numbers)

a = dict(one = 1, two = 2, three = 3)
print a

b = {'one': 1, 'two':2, 'three': 3}
print b

c = dict(zip(['one','two', 'three'], [1, 2, 3]))
print c

d = dict([('one', 1),('two',2),('three',3)])
print d

e = [('one', 1),('two',2),('three',3)]

f = {x: y for x,y in e}
print "f:", f


def randPass(arg):
    passlist = []
    for x in range(arg):
        passlist.append(chr(randrange(65,123)))
    return ''.join(passlist)

print randPass(128)

import hashlib

hashmd5 = hashlib.md5()

hashmd5.update('admin')
print hashmd5.hexdigest()

hashmd5 = hashlib.md5()
hashmd5.update('admin')
print hashmd5.hexdigest()
