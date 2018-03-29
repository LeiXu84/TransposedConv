#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:38:32 2018
Test on tf.nn.conv2d_transpose(value, filter, output_shape, strides, padding='SAME'
data_format='NHWC', name=None)
'output_shape' to indicate upsampling factor
@author: yongweiw
"""

import tensorflow as tf

"a single step on transposed_conv operation"
batch_size = 50
W = tf.constant(0.1, shape=[7, 7, 128, 3])  # input_shape = [batch_size, height,width,in_channel]
output_shape = [batch_size, 8, 8, 128]
strides = [1, 2, 2, 1]

# 'forward'-- conv2d(), given output(high-dim) and filters W, find input(low-dim) with conv2d
output = tf.constant(0.1, shape=output_shape)
expected_x = tf.nn.conv2d(output, W, strides=strides, padding='SAME')
with tf.Session() as sess:
    print("expected_x [batch_size, h_in, w_in, c_in] is:")  #(50,4,4,3)
    print(expected_x.get_shape())

# 'backward' -- conv2d_transpose(), given input(x), filter W and output_shape, find output(high-dim) with conv2d_transpose
x = tf.constant(0.1, shape=[batch_size, 4, 4, 3])
# try different kernel sizes (W_ = W also works)
W_ = tf.constant(0.1, shape=[5, 5, 128, 3])  

expected_out = tf.nn.conv2d_transpose(x, W, output_shape=output_shape, strides=strides, padding='SAME')
expected_out_ = tf.nn.conv2d_transpose(x, W_, output_shape=output_shape, strides=strides, padding='SAME')
with tf.Session() as sess:
    print("expected_out [batch_size, h_in, w_in, c_in] is:")
    print(expected_out.get_shape())   # display (50, 8, 8, 128)
    
    # compare outputs with different kernels
    print("output with W kernel is:")
    print(sess.run(expected_out[0,:,:,0]))
    print("output with W_ kernel is:")
    print(sess.run(expected_out_[0,:,:,0]))
"""
output with W kernel is:
[[0.12       0.12       0.18       0.18       0.24000001 0.18
  0.18       0.12      ]
 [0.12       0.12       0.18       0.18       0.24000001 0.18
  0.18       0.12      ]
 [0.18       0.18       0.27       0.27       0.36       0.27
  0.27       0.18      ]
 [0.18       0.18       0.27       0.27       0.36       0.27
  0.27       0.18      ]
 [0.24000001 0.24000001 0.36       0.36       0.48000002 0.36
  0.36       0.24000001]
 [0.18       0.18       0.27       0.27       0.36       0.27
  0.27       0.18      ]
 [0.18       0.18       0.27       0.27       0.36       0.27
  0.27       0.18      ]
 [0.12       0.12       0.18       0.18       0.24000001 0.18
  0.18       0.12      ]]
output with W_ kernel is:
[[0.03 0.06 0.06 0.09 0.06 0.09 0.06 0.06]
 [0.06 0.12 0.12 0.18 0.12 0.18 0.12 0.12]
 [0.06 0.12 0.12 0.18 0.12 0.18 0.12 0.12]
 [0.09 0.18 0.18 0.27 0.18 0.27 0.18 0.18]
 [0.06 0.12 0.12 0.18 0.12 0.18 0.12 0.12]
 [0.09 0.18 0.18 0.27 0.18 0.27 0.18 0.18]
 [0.06 0.12 0.12 0.18 0.12 0.18 0.12 0.12]
 [0.06 0.12 0.12 0.18 0.12 0.18 0.12 0.12]]
"""