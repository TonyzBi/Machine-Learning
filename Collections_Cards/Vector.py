# -*- coding: utf-8 -*-

from math import hypot
import os
from collections import namedtuple

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

v1 = Vector(2,3)
v2 = Vector(4,6)

print v1 + v2
print v1 * 6
print abs(v1)

path, fileName = os.path.split('/var/log/message')

print path
print fileName

#------------------------------------------------

City = namedtuple('City', 'name country populition coordinates')

import bisect
alist = [1, 3, 6, 9, 10, 11, 13, 25]

index = bisect.bisect(alist, 5)
alist.insert(index, 5)
#index = bisect.bisect(alist, 5)
print alist

bisect.insort(alist, 14)
print alist

print '{name},{age}'.format(age=18,name='KFC')