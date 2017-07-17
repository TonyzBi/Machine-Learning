# -*- coding: utf-8 -*-

import numpy as np
import random

def gradientDescent(x, y, theta, alpha, m, numIteration):
    xTran = x.transpose()
    for i in range(0, numIteration):
        hypothesis = np.dot(x, theta)  #get H(x)
        loss = hypothesis - y  # H(x) - y
        cost = np.sum(loss ** 2)/(2 * m)
        gradient = np.dot(xTran, loss) / m
        print 'Iteration %d / Cost: %f' % (i, cost)
        theta = theta - alpha * gradient

    return theta

def genData(numPoints, bias, variance):
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)

    for i in range(0, numPoints):
        # bias feature
        x[i][0] = 1
        x[i][1] = i
        #out target variables
        y[i] = (i + bias) + random.uniform(0, 1) * variance

    return x, y


x, y = genData(100, 25, 10)
print 'X: ', x
print 'Y: ', y
m, n = np.shape(x)

numIteration = 100000
alpha = 0.0005
theta = np.ones(n)

theta = gradientDescent(x, y, theta, alpha, m, numIteration)

print theta

