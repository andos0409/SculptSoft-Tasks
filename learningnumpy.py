import numpy as np

a = np.array([[1,2,3,4],[6,8,9,10]])

a[1,:] = a[1,:] - 1

# Keep all even numbers, otherwise write -1
even = np.where(a%2==0, a, -1)

print("All even numbers:\n", even)

# Positions of even numbers in a 1-D array

b = np.argwhere(a.flatten() % 2 == 0).flatten()

print("All even numbers in flattened array:\n", b)

# 3 Dimensional Array
array = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])

print(array.shape)

# Broadcasting

arr1 = np.array([1, 2, 3]) # (1, 3)
arr2 = np.array([[1], [2], [3]]) # (3, 1)

print(arr1 * arr2)