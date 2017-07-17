# -*- coding: utf-8 -*-

from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model

datafile = r'./delivery.csv'
#该函数将 csv文件转化的np  array格式
dataset = genfromtxt(datafile, delimiter=',')

print dataset

X = dataset[:, :-1]
Y = dataset[:, -1]

lm = linear_model.LinearRegression()

lm.fit(X, Y)

print 'Coef: ', lm.coef_
print 'Intercept: ', lm.intercept_

predictY = lm.predict([102, 6])

print 'Predict Y: ', predictY

