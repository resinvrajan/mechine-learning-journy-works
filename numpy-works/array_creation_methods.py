"""
array creation methods
======================
np.array()
nap.zeros((size))
np.ones((size))
np.full((size))
np.random.rand(size)
np.random.randint(low,high,(size))
"""
import numpy as np
array_zeros=np.zeros((2,3))      #default dtype=float
print(array_zeros)
array_zeros=np.zeros((2,3),dtype="int16") #changing dtype=int
print(array_zeros)
ones_array=np.ones((4,2))
print(ones_array)
five_array=np.full((3,3),5)   # defualt dtype=int
print(five_array)


rand_array=np.random.rand(4,7)   #default dtype=float
print(rand_array)

rand_int_array=np.random.randint(10,15,(3,3))
print(rand_int_array)