# -*- coding: utf-8 -*-

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

data = datasets.load_boston()

data_X = data.data
data_y = data.target

#print data_X[:4,]

train_X, test_X, train_y, test_y = train_test_split(data_X, data_y, test_size= 0.25)

model = LinearRegression()

#minmaxmodel = MinMaxScaler(feature_range=(0, 1))
#nor_train_X, nor_train_y = minmaxmodel.fit(train_X, train_y)
#nor_test_X = minmaxmodel.transform(test_X)
#nor_test_y = minmaxmodel.transform(test_y)

model.fit(train_X, train_y)

predict_y = model.predict(test_X)

print predict_y[:10]
print test_y[:10]
print model.score(test_X, test_y)

#plt.scatter(predict_y, test_y)
#plt.show()