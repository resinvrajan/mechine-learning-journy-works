import numpy as np
# 1. Extract the 3rd element
arr = np.array([3, 6, 9, 12, 15, 18])
print(arr[2])
# 2. Extract elements from index 2 to 4
arr = np.array([5, 10, 15, 20, 25, 30])
print(arr[2:5])
# 3. Extract all even-indexed elements
arr = np.array([2, 4, 6, 8, 10, 12])
print(arr[::2])
# 4. Select elements greater than 30
arr = np.array([11, 22, 33, 44, 55])
print(arr[arr > 30])
# 5. Replace all numbers greater than 20 with -1
arr = np.array([7, 14, 21, 28, 35])
arr[arr > 20] = -1
print(arr)
# 6. Pick elements at positions [0, 2, 4]
arr = np.array([1, 2, 3, 4, 5])
print(arr[[0, 2, 4]])
# 7. Multiply every element by 2 using broadcasting
arr = np.array([10, 20, 30, 40])
print(arr * 2)
# 8. Reverse the array using advanced indexing
arr = np.array([100, 200, 300, 400, 500])
print(arr[::-1])
# 9. Extract the first row
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr[0])
# 10. Extract the last column
print(arr[:, -1])
# 11. Select elements greater than 10
arr = np.array([[2, 4, 6],
                [8, 10, 12],
                [14, 16, 18]])
print(arr[arr > 10])
# 12. Select elements at (0,0), (1,1), (2,2)
print(arr[[0, 1, 2], [0, 1, 2]])
# 13. Multiply every element by 5 using broadcasting
arr = np.array([[1, 2],
                [3, 4],
                [5, 6]])
print(arr * 5)
# 14. Extract subarray [[3,4],[7,8]]
arr = np.array([[1,  2,  3,  4],
                [5,  6,  7,  8],
                [9, 10, 11, 12]])
print(arr[0:2, 2:4])
# 15. Multiply only the first column by 10
arr = np.array([[2, 4],
                [6, 8],
                [10, 12]])
arr[:, 0] *= 10
print(arr)
