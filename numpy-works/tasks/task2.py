import numpy as np

productivity = np.array([
   # 1  2  3  4  5  6  7  8  9  10
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8], #employee1 
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7], #employee2
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9], #employee3
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5], #employee4
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8], #employee5
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]  #employee6
])
# 1. Calculate the total number of hours worked by each employee over 10 days.
print(np.sum(productivity,axis=1))
# 2. Calculate the total work hours for each day across all employees.
print(np.sum(productivity,axis=0))
# 3. Find the average working hours per employee.
average=np.average(productivity,axis=1)
print(average)
# 4. Find the average working hours per day.
print(np.average(productivity,axis=0))
# 5. Identify the employee index who worked the maximum total hours.
total=np.sum(productivity,axis=1)
print(total)
print(np.argmax(total))
# 6. Identify the employee index who worked the minimum total hours.
print(np.argmin(total))
# 7. Find the day index with the highest total working hours.
total_day=np.sum(productivity,axis=1)
print(np.argmax(total_day))
# 8. Identify employees who are overworked if average hours exceed 8 per day.
print(np.where(average>8))
# 9. Calculate the difference between the most productive and least productive employee.
print(np.max(total)-np.min(total))