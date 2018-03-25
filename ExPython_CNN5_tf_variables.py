from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf

"""
Created on Sun Mar 25 14:06:22 2018
1) tf.constant()
2) tf.matmul()
3) tf.Session.run()
@author: yongweiw
"""

" ********** build a graph **********"
var_1=tf.constant([[1,2],[3,4]])
var_2=tf.constant([[5,6],[7,8]])
# tf.matmul()
var_3=tf.matmul(var_1, var_2)
print("var_1:", var_1)
print("var_2:", var_2)
print("type of var_1:",type(var_1))  # <class 'tensorflow.python.framework.ops.Tensor'>
print("var_3:", var_3)
print("\n")

"********** Execute the graph and store the value that `c` represents in `result` **********"
# construct a 'Session' to excute the graph
sess=tf.Session()
result_var_1=sess.run(var_1)
result_var_11=var_1.eval(session=sess)
print("result_var_1:\n", result_var_1)
print("result_var_11:\n", result_var_11)

result_var_2=sess.run(var_2)
print("result_var_2:\n", result_var_2)

result_var_3=sess.run(var_3)
print("result_var_3:\n",result_var_3)

"********** close the session **********"
sess.close()