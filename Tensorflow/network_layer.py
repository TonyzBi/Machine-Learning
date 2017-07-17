# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np

def nn_layer(inputs, in_size, out_size, activation_fuction=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)

    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_fuction is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_fuction(Wx_plus_b)

    return outputs

