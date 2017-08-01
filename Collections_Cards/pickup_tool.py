#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

inputFile1 = ''
inputFile2 = ''
outputFile = ''

if len(sys.argv) == 4:
    fileName = sys.argv[1:]
    if len(fileName) != 3:
        print "Parameter Error, Please usage: ./pickup_tool file1 file2 file3"
        sys.exit(-1)
    print sys.argv
    inputFile1, inputFile2 = sys.argv[1:-1]
    outputFile = sys.argv[-1]


if os.path.exists(inputFile1) and os.path.exists(inputFile2):
    inNum = open(inputFile1, 'r')
    outNum = open(inputFile2, 'r')
    resultNum = open(outputFile, 'w')
    excludeNums = outNum.read()
    print 'Start to pick up numbers from {0} by excluding {1}'.format(inputFile1, inputFile2)
    for num in inNum:
        if num not in excludeNums:
            resultNum.write(num)

    print 'Finished to pick up...'
    inNum.close()
    outNum.close()
    resultNum.close()






