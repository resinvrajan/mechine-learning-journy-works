"""
slicing onedimensional array

"""

import numpy as np
lst=[10,20,30,40,50]
arr=np.array(lst)
# getting specific element
print(arr[3])
# slicing the element
"""
syntax arr[start:stop]  * end excluded

"""
print(arr[1:4]) #[20 30 40]
print(arr[1:6]) #[20 30 40 50]