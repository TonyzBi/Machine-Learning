# -*- coding: utf-8 -*-

from __future__ import print_function
import tensorflow as tf
import numpy as np

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# create tensorflow structure

weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)

train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

session = tf.Session()

session.run(init)

for step in range(500):
    if step % 20 == 0:
        session.run(train)
        print('--------------------------')
        print(session.run(loss))
        print(step, session.run(weights), session.run(biases))

