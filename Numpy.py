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


# array search
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x) # print array of indices of even elements in the arr

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x) # print the index of first element >= parameter sent , you can send array instead of one element and it will return array of indices


# array sort 
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr)) # it sorts every array insde the 2d array , u can use function sort normally with 1d arrays


# array filtering
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr) # every true element is put in the array and the false is execluded

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr) # prints even elements in the arr only



# random in numpy, you can put "size" parameter to determine the shape of x -> 2d array on anything
x=random.randint(100) # random num from 0 -> 100
x = random.rand() # random float num from 0 -> 1 
x = random.choice([3, 5, 7, 9]) # random num in this array
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)) # defines 1d array of size 100 and probability of each number to occur in the answer
random.shuffle(arr) # shuffles the array inplace
random.permutation(arr) # shuffle the array not inplace











