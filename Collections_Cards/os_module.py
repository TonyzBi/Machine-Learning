# -*- coding: utf-8 -*-

import os
import sys

print os.getcwd()
print os.getlogin()

os.chdir('..')
print os.getcwd()
print os.stat('/Users/administrator/PycharmProjects/Collections_Cards/vector.py').st_size
os.chdir('Collections_Cards')
print os.listdir('.')
print os.geteuid()

print sys.argv

print False and True
