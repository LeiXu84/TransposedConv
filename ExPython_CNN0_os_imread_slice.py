"""
Created on Mon Mar 19 16:33:42 2018

@author: yongweiw
"""

import tensorflow as tf
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os

""" **************************** os.path+.imread ****************************"""
dir_path=os.path.dirname(os.path.realpath(__file__))  # dir of current .py file. e.g., /.../tensorflow/practices
print("dir of path:",dir_path)

filename = dir_path + "/cat.jpg"
raw_img_data = mpimg.imread(filename) #(720,720,3)

""" **************************** original image ****************************"""
plt.figure('Test-Figure 1')
plt.imshow(raw_img_data,interpolation='None')
plt.title("original cat.jpg")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.axis([0,700,700,0])
plt.axis('off')
plt.show()

""" **************************** tf.slice() ****************************"""
x = tf.placeholder(tf.uint8,[None,None,3])
print("dim image:",x.shape)
x_slice = tf.slice(x, [20,20,0],[-1,-1,-1])

with tf.Session() as sess:
    result = sess.run(x_slice, feed_dict={x:raw_img_data})
    print("cropped img shape:", result.shape)

plt.figure("Test-Figure 2")    
plt.imshow(result)
plt.title("cropped image")
plt.axis('off')
plt.show()
