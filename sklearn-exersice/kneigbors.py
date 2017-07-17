# -*- coding: utf-8 -*-

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

iris_X = iris.data
iris_y = iris.target

print type(iris_X)
print iris_X[:5, :]

train_X, test_X, train_y, test_y = train_test_split(iris_X, iris_y, test_size= 0.25)

print 'Train : ', len(train_X)
print 'Test : ', len(test_X)

cf = KNeighborsClassifier()
cf.fit(train_X, train_y)

predict_y = cf.predict(test_X)

print predict_y
print test_y
