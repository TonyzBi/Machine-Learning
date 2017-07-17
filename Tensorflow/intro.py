# -*- coding: utf-8 -*-

import tensorflow as tf
import os


os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
v1 = tf.Variable(1)
v2 = tf.Variable(5)

vsum = v1 + v2

sess = tf.Session()

tf.global_variables_initializer().run(session=sess)


print 'v1 + v2 = ', vsum.eval(session=sess)
print 'v1 + v2 = ', sess.run(vsum)


c1 = tf.constant(10)
c2 = tf.constant(5)
addc = c1 + c2

print 'c1 + c2 = ', sess.run(addc)


print '--------------------------------------'
graph = tf.Graph()
with graph.as_default():
    value1 = tf.constant([1, 2])
    value2 = tf.Variable([3, 4])
    v3 = value1 * value2

with tf.Session(graph=graph) as Mysess:
    tf.global_variables_initializer().run()
    print 'v1 + v2 : ', Mysess.run(v3)