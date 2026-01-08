import numpy as np
# array=np.full((5,7),7)
# print(array)
# array[1:4,2:5]=0
# print(array)
# array[2,3]=1
# print(array)

array=np.full((5,7),7)
print(array)

print(array)
array_zeros=np.zeros((3,3),dtype="int16")
array_zeros[1,1]=1
array[1:4,2:5]=array_zeros
print(array)