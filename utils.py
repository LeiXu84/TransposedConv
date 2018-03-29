#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 08:17:27 2018

@author: yongweiw
"""

import tensorflow as tf

def get_shape(tensor):
    return tensor.get_shapee().as_list()

def batch_normalization(*args, **kargs):
    with tf.name_scope('bn'):
        bn = tf.layers.batch_normalization(*args, **kargs)
        return bn
    
def Tconv2d(x, W, output_shape):
    return tf.nn.conv2d_transpose(x, W, output_shape=output_shape, 
                                  strides=[1, 2, 2, 1], padding='SAME')