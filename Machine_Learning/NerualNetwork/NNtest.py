# -*- coding: utf-8 -*-

from nerualnetwork import NerualNetwork
import numpy as np

nn = NerualNetwork([2,2,1], 'tanh')
X = np.array([[0, 0], [0, 1], [1, 0],[1, 1]])
y = np.array([0, 1, 1, 0])

nn.fit(X, y)

for i in [[0, 0], [0, 1], [1, 0],[1, 1]]:
    print nn.predict(i)
