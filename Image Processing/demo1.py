# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pylab


np.ndarray
x = np.ndarray([5,5,3])
y = np.ones([5,5,3])

y[:,:,0] = y[:,:,0] * 0
y[:,:,1] = y[:,:,1] * 1
y[:,:,2] = y[:,:,2] * 0

print y
plt.imshow(y)
pylab.show()