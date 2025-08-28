import numpy as np

# numpy -> numerical python

# Create a numpy array you can put a tuple instead of a list 
arr = np.array([1,2,3],ndmin = 1)
print(arr,arr.ndim,type(arr)) # print [1, 2 , 3] , 1 , numpy.ndarray


# array slicing [from, to, step]
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2]) # print [3,8]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4]) # print [[2 3 4] [7 8 9]]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) # print [2,4]


# Datatypes in numpy
arr = np.array([1, 2, 3, 4], dtype='S') # you can put the datatype or not
print(arr,arr.dtype) # prints [b'1' b'2' b'3' b'4'] |S1
