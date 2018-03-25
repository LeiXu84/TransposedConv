#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:45:20 2018

@author: yongweiw
"""

import tensorflow as tf

"""******************* define variables within scopes *******************"""
value = [0, 1, 2, 3, 4, 5, 6, 7]
with tf.variable_scope("collection_scope1"):
    v1 = tf.get_variable(name='v1',shape=[2, 4],initializer=tf.constant_initializer(value))

with tf.variable_scope("collection_scope2"):
    v2 = tf.get_variable(name='v2', shape=[4, 2], initializer=tf.constant_initializer(value))

"""******************* add variables to collection *******************"""
tf.add_to_collection('var_collection', v1)
tf.add_to_collection('var_collection', v2)

"""******************* print collection contents ******************* """
device = "/GPU:3"
with tf.device(device):
    with tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)) as sess:
        sess.run(tf.global_variables_initializer())
        vc = tf.get_collection('var_collection')
        print("vc contents:", vc) 
        for var in vc: 
            print(var)
            print(sess.run(var))
        
        
""" 
 1) 1st print: [<tf.Variable 'collection_scope1/v1:0' shape=(1,) dtype=float32_ref>, 
 <tf.Variable 'collection_scope2/v2:0' shape=(1,) dtype=float32_ref>]
2) 2nd and 3rd:
    <tf.Variable ...>,
    [v1 value]
    <tf.Variable ...>,
    [v2 value]
"""

