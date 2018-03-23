#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 10:34:49 2018

@author: yongweiw
"""

"""
tf.Variable-- create new variables every time called (posibly add suffix to var name with same name)
tf.get_variable-- create a new variable with the name as the vargument, or to retrieve the one that was created before
two types of scopes:
    1) name scope using tf.name_scope
    2) variable scope using tf.variable_scope
.scope will be added as prefix to variable name for both types of scope
..name_scope ignored by tf.get_variable (variable_scope doesn't)
... keywords: name=, shape, dtype, initial_value
"""
import tensorflow as tf

"**********tf.name_scope()**********"
with tf.name_scope("my_scope_1"):
    v1 = tf.get_variable("var_1", shape=[1], dtype =tf.float32)  #keyword an be obmitted
    v2 = tf.Variable([1], name="var_2", dtype=tf.float32)
    result = tf.add(v1, v2)
    
print(v1.name) # var_1:0
print(v2.name) # my_scope_1/var_2:0
print(result.name) #my_scope_1/Add:0

"**********tf.variable_scope()**********"
with tf.variable_scope("my_scope_2"):
    v1 = tf.get_variable("var_1", shape=[1], dtype =tf.float32)  #notice: keyword arg after keyword arg
    v2 = tf.Variable(1, name="var_2", dtype=tf.float32)
    result = tf.add(v1, v2)    
print(v1.name) # my_scope_2/var_1:0
print(v2.name) # my_scope_2/var_2:0
print(result.name) #my_scope_2/Add:0

"********** variable sharing **********"
with tf.name_scope("foo"):
    with tf.variable_scope("var_scope_3"):
        v3 = tf.get_variable(name="var_3", shape=[1])
with tf.name_scope("bar"):
    with tf.variable_scope("var_scope_3", reuse=True):   #var_scope_3
        v4 = tf.get_variable("var_3", [1])
        
assert v3 == v4
print("")
print(v3.name) # var_scope_3/var_3:0
print(v4.name) # var_scope_3/var_3:0

"********** alternative usage (tf.variable_scope()) **********"
with tf.variable_scope("a_variable_scope") as scope:
    initializer = tf.constant_initializer(value=4.5)
    var3 = tf.get_variable(name='var3', shape=[1], dtype=tf.float32, initializer=initializer)
    scope.reuse_variables()  # !reuse statement!
    var3_reuse = tf.get_variable(name='var3',)
    var4 = tf.Variable(name='var4', initial_value=[2.7], dtype=tf.float32)
    var4_reuse = tf.Variable(name='var4', initial_value=[2.7], dtype=tf.float32)
    
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    "tf.variable_scope.reuse_variables()"
    print(var3.name)            # a_variable_scope/var3:0
    print(sess.run(var3))       # [ 4.5]
    print(var3_reuse.name)      # a_variable_scope/var3:0
    print(sess.run(var3_reuse)) # [ 4.5]
    "defined by tf.Variable()"
    print(var4.name)            # a_variable_scope/var4:0   #notice--0
    print(sess.run(var4))       # [ 2.1]
    print(var4_reuse.name)      # a_variable_scope/var4_1:0  #notice--_1:0
    print(sess.run(var4_reuse)) # [ 2.7]
    
    
    