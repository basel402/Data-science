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
arr = np.array(['a', '2', '3'], dtype='i') # raise a value error cant cast the 'a' as int32

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i') # you can put int instead of 'i'
print(newarr,newarr.dtype) # prints [1 2 3] , int32


# copy vs veiw 
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() # no relation between them
y = arr.view() # any change happen to any happen to the other
print(x.base) # none
print(y.base) # [1,2,3,4,5]


# array shape
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape) # print [[[[[1 2 3 4]]]]] , shape of array : (1, 1, 1, 1, 4)


# array reshape -> it returns a (view) array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1) # 3d array and the 3rd dim the machine predicts it as you put -1  ->  8 / (2*2)
print(newarr)


# array iteration
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr): # it flattens the array and prints its elements directly instead of making ndim for loops
  print(x)


# array joining
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr) # prints [[1 2 5 6] [3 4 7 8]]



