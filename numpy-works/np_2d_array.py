"""
2d array

1 2 3
4 5 6
7 8 9

"""
import numpy as np
two_dimensional_array=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(two_dimensional_array.ndim)
print(two_dimensional_array)

# "size" will return total number of elements is an atribute
print(two_dimensional_array.size)
# "shape" will return the number of columns and rows is an atribute
print(two_dimensional_array.shape)