import tensorflow as tf

matrix1 = tf.constant([[2, 2]])
matrix2 = tf.constant([[3], [3]])

product = tf.matmul(matrix1, matrix2, transpose_a= True, transpose_b= True)


with tf.Session() as sess:
    print sess.run(product)


##########################################

state = tf.Variable(0, name='counter')

one = tf.constant(1)

new = tf.add(state, one)

update = tf.assign(state, new)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(50):
        sess.run(update)
        print sess.run(state)


##########################################

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print sess.run(output, feed_dict={input1: [4.5], input2: [4.]})




