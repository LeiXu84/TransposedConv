#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 07:50:38 2018

@author: yongweiw
"""

import tensorflow as tf
from .utils import get_shape, batch_normalization, Tconv2d

class RevHashGen:
    def __init__(self, arch_params, stddev=0.002):
        self.arch_params = arch_params
        self.stddev = stddev
    
    def __call__(self, xs_hash, ys_img, is_training): # xs_hash: x_hash in batches
        batch_dim = tf.shape(xs_hash)[0]
        with tf.variable_scope('revHashGen', initializer=tf.truncated_normal_initializer(stddev=self.stddev)):
            with tf.variable_scope('projReshape'):
                projR = self.arch_params['projR']
                W_proj = tf.get_variable('W', projR['wshape'])
                x_hash_proj = tf.matmul(xs_hash, W_proj)  # projected xs_hash
                bn_x_hash_proj =batch_normalization(x_hash_proj, center=projR['bn']['center'],
                                                    scale=projR['bn']['scale'],
                                                    training=is_training) if 'bn' in projR else x_hash_proj
                x_ = tf.nn.relu(bn_x_hash_proj)
                x_input = tf.reshape(x_, projR['reshape'])
            
            # 1) transposed Conv-- layer 1
            with tf.variable_scope('RevConv1'):
                params = self.arch_params['TConv_1']  # transposed convolution
                filters_1 = tf.get_variable('filters', params['filters'])
                TConv_1 = Tconv2d(x_input, filters_1, [batch_dim] + params['output_size'])
                BN_1 = batch_normalization(TConv_1, center=params['bn']['center'], 
                                           scale=params['bn']['scale'], 
                                           training=is_training) if 'bn' in params else TConv_1
                                           
                TConv_1_out = tf.nn.relu(BN_1)
            
            # 2) transposed Conv-- layer 2
            with tf.variable_scope('RevConv2'):
                params = self.arch_params['TConv_2']
                filters_2 = tf.get_variable('filters', params['filters'])
                TConv_2 = Tconv2d(TConv_1_out, filters_2, [batch_dim] + params['output_size'])
                BN_2 = batch_normalization(TConv_2, center=params['bn']['center'],
                                           scale=params['bn']['scale'],
                                           training=is_training) if 'bn' in params else TConv_2
                
                TConv_2_out = tf.nn.relu(BN_2)
            
           # 3) transposed Conv-- layer 3
            with tf.variable_scope('RevConv3'):
                params = self.arch_params['TConv_3']
                filters_3 = tf.get_variable('filters', params['filters'])
                TConv_3 = Tconv2d(TConv_2_out, filters_3, [batch_dim] + params['output_size'])
                BN_3 = batch_normalization(TConv_3, center=params['bn']['center'],
                                           scale=params['bn']['scale'],
                                           training=is_training) if 'bn' in params else TConv_3
                                           
                TConv_3_out = tf.nn.relu(BN_3)

           # 4) transposed Conv-- layer 4                
            with tf.variable_scope('RevConv4'):
                params = self.arch_params['TConv_4']
                filters_4 = tf.get_variable('filters', params['filters'])
                TConv_4 = Tconv2d(TConv_3_out, filters_4, [batch_dim] + params['output_size'])
                BN_4 = batch_normalization(TConv_4, center=params['bn']['center'],
                                           scale=params['bn']['scale'],
                                           training=is_training) if 'bn' in params else TConv_4
                                           
                TConv_4_out = tf.nn.relu(BN_4)

           # 5) transposed Conv-- layer 5                                
            with tf.variable_scope('RevConv5'):
                params = self.arch_params['TConv_5']
                filters_5 = tf.get_variable('filters', params['filters'])
                TConv_5 = Tconv2d(TConv_4_out, filters_5, [batch_dim] + params['output_size'])
                BN_5 = batch_normalization(TConv_5, center=params['bn']['center'],
                                           scale=params['bn']['scale'],
                                           training=is_training) if 'bn' in params else TConv_5
                                           
                TConv_5_out = tf.nn.relu(BN_5)
                
           # 6) transposed Conv-- layer 46               
            with tf.variable_scope('RevConv6'):
                params = self.arch_params['TConv_6']
                filters_6 = tf.get_variable('filters', params['filters'])
                TConv_6 = Tconv2d(TConv_5_out, filters_6, [batch_dim] + params['output_size'])
                BN_6 = batch_normalization(TConv_6, center=params['bn']['center'],
                                           scale=params['bn']['scale'],
                                           training=is_training) if 'bn' in params else TConv_6
                                           
                TConv_6_out = tf.nn.tanh(BN_6)
                
                
        return TConv_6_out
                    
                
                
                                                   