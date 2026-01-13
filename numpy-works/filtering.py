
"""
filtering
=========

"""
import numpy as np
productivity = np.array([\
   # 1  2  3  4  5  6  7  8  9  10
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8], #day 1 
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7], #day 2
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9], #day 3
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5], #day 4
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8], #day 5
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]  #day 6
])
print(productivity[productivity<8])
# working hours between 5 to 7
print(productivity[(productivity<=7) & (productivity>=5)])
# print working hrs of first employee with working hr<8
frst_emp_working=productivity[:,0]
print(frst_emp_working)
print(frst_emp_working[frst_emp_working<8])
# print last two employees working hrs <7
last_two_emp_working=productivity[:,-2:]
print(last_two_emp_working)
print(last_two_emp_working[last_two_emp_working<7])

productivity[productivity<8]=0
print(productivity)