import tensorflow as tf
hello = tf.constant('hello')
sess = tf.version()
print(sess.run(hello))