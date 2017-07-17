# -*- coding: utf-8 -*-

import urllib
import numpy as np
from sklearn.preprocessing import normalize, scale, StandardScaler
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

raw_data = urllib.urlopen(url)

data_set = np.loadtxt(raw_data, delimiter=',')

X = data_set[:,0:7]
y = data_set[:,-1]

# normalize data to make data value between (0,1)
normalized_X = normalize(X)
# standardize data to make data value normalized distribution(0,1)
standardized_X = scale(X)

train_X = X[:601,:]
test_X = X[601:,:]
train_y = y[:601]
test_y = y[601:]

scaler = StandardScaler().fit(X)
train_X = scaler.transform(train_X)
test_X = scaler.transform(test_X)

# print X[:10,:]
# print normalized_X[:10,:]
# print standardized_X[:10:]
print X.shape, y.shape

model = ExtraTreesClassifier()
model.fit(train_X, train_y)

print model.feature_importances_



