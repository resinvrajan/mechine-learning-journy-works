import numpy as np

attendance = [
  
  #m  t  w  h  f
  [1, 1, 1, 1, 1], # Student 1
  [1, 0, 1, 1, 1], # Student 2
  [1, 1, 0, 1, 1], # Student 3
  [0, 1, 1, 1, 0], # Student 4
  [1, 1, 1, 0, 1], # Student 5
  [1, 0, 0, 1, 1], # Student 6
  [1, 1, 1, 1, 0], # Student 7
  [0, 1, 1, 0, 1], # Student 8
  [1, 1, 0, 1, 0], # Student 9
  [1, 0, 1, 1, 1]  # Student 10

]
"""
functions
==========
sum,max,min,avg
axis=0   ->coloumn
axis=1   ->row
count_nonzero to get peritcular value count
"""

arr=np.array(attendance)
print(arr)

# update student10 present in tuesday

arr[9,1]=1
print(arr)

# print studenwise present count
print(np.sum(arr,axis=1))
# print daywise present count
print(np.sum(arr,axis=0))

# studentwise absent count
print(np.count_nonzero(arr==0,axis=1))
# dailywise absent count
print(np.count_nonzero(arr==0,axis=0))
