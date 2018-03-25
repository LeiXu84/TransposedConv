#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:48:32 2018
1)test tf.nn.local_response_normal(input, depth_radius,bias,beta,name) \
with a 'cat' image
2)comare tf.truncated_normal with tf.random_normal
@author: yongweiw
"""

import numpy as np
import tensorflow as tf
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os

""" **************************** tf.nn.lrn ****************************"""
dir_path = os.path.dirname(os.path.realpath(__file__)) # dir of current .py file
filename = dir_path + "/cat.jpg"
raw_img_data = mpimg.imread(filename)
#print(type(raw_img_data))         # <class 'numpy.ndarray'>
#print(np.shape(raw_img_data))     # (Height, Width, Channel)
#print(raw_img_data[0:10,0,0])     # uint8: [91 91 89 87 85 83 82 81 78 76]
img_H, img_W, img_C = np.shape(raw_img_data) 

" 1) display 'cat.jpg' "
plt.figure('Test-Figure 1')
plt.imshow(raw_img_data, interpolation='None')
plt.title("original cat.jpg")
plt.axis("off")
plt.show()

" **convert image from uint8 to double format, display error@.lrn otherwise **"
def im2double(img):
    min_val = np.min(img.ravel())
    max_val = np.max(img.ravel())
    out = (img.astype('float32') - min_val) / (max_val - min_val) #to use double(float64), \
    # please use 'float' instead, since tf.lrn only support float32 or float16
    return out

raw_img_double = im2double(raw_img_data)  # converted to double format


" 2)'cat image processed with .lrn (treat each channel as one feature map)' "
tmp_img_data = tf.reshape(raw_img_double, [-1,img_H,img_W,img_C]) # [batch_size, H, W, C]
lrn_img_data = tf.nn.lrn(tmp_img_data,2,0,1,1)

with tf.Session() as sess:
#    tmp_img = sess.run(tmp_img_data) # it's ok to skip tmp_img_data node, just turn to those nodes you need
    lrn_img = sess.run(lrn_img_data)
    print("original img data:",raw_img_double[0:10,0,0])
    print("lrn processed img data:",lrn_img[0,0:10,0,0])


""" **************************** tf.*_normal ****************************"""
# generate data points
num_data = 1000000   # 1 million data points
sample_1 = tf.truncated_normal((num_data,), mean=0.0, stddev=1.5, dtype=tf.float32, seed=1, name='sample_1')
sample_2 = tf.random_normal((num_data,), mean=0.0, stddev=1.5, dtype=tf.float32, seed=1, name='sample_2')

with tf.Session() as sess:
#    Sample_1 = sess.run(sample_1)
#    Sample_2 = sess.run(sample_2)
    Sample_1, Sample_2 = sess.run([sample_1, sample_2])   # data can be concatenated together

" visualize and compare histograms "
plt.hist(Sample_1, 100, (-4.2, 4.2));
plt.show()

plt.hist(Sample_2, 100, (-4.2, 4.2));
plt.show()


