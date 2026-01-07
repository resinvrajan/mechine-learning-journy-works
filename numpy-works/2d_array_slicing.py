"""
twodimensional array slicing

"""
import numpy as np
arr=np.array([
    [33,31,27],
    [31,30,29],
    [33,32,34]
])
print(arr.ndim)
print(arr.size)
print(arr.shape)

# fetch data
print(arr[0])
print(arr[1])
print(arr[2])

# slicing 
"""
synatx arr[row,col]

"""
# fetching rows from 0 to 2
print(arr[0:2])    
# fetching rows from 1 to 2
print(arr[1:3])   

# coloumn slicing
print(arr[:,0:2])
print(arr[:,1:3])
print(arr[:,1:2])
print(arr[:,1])
print(arr[::2])
print(arr[2,1])
print(arr[1:3,1:3])