"""
============================================= numpy =====================================
numpy => Numerical Python
* It is created by "Travis Oliphant" in 2005

It is used to work with arrays.
NOTE :- In python list provides the basic functionalities of an array.

=> As compared to list arrays are faster.
=> Compared to list provides many built-in functions for different fields.

^ Inside terminal, We Have to install numpy before use :-  pip install numpy
^ -------------------------------------------------------
import numpy as np
-----------------------------------------------

let users = ["ram","lakhan","shyam"]; ==> in js
"""

import numpy as np
# To create array with numpy
lst = [1,2,3,4,5,6,7,8,9,10]
array = np.array([1,2,3,4,5,6,7,8,9,10])

# print(type(lst))
# print(type(array)) # <class 'numpy.ndarray'>

# print(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(array) # [ 1  2  3  4  5  6  7  8  9 10]

#* NOTE : There are maximum 64 number of dimensional array

arr = np.array([[1,2,3],[10,20,30]],ndmin=2 , dtype="int16")
l = [[1,2,3],[10,20,30]]
print(arr)

# print(array.ndim)
# print(arr.ndim)
arr2 = arr.reshape(6)

print(arr.shape) # no. of rows and columns (2,3)
print(arr.size) # no. of total values stored inside the array => 6
print(arr.dtype) # return data type of an array => int16

# print(arr2)

ar = np.array((1,2,3,4,5,6,7,8,9,10))
print(ar.sum())
print(ar.mean())
print(ar.std())
print(ar.var())
print(arr.flatten())

ar3 = np.arange(1,11)
ar4 = ar3.reshape(2,5)
# print(ar4)


a1 = np.array((1,2,3))
a2 = np.array((11,12,13))

print(a1+a2)
print(a2-a1)
print(a2/2)
print()
zr = np.zeros((5,5),dtype="int16")
ones = np.ones((3,9))
# print(ones)

# print(np.add(a1,a2))
# print(np.dot(a1,a2)) # 74

print(arr.min())
print(arr.max())

print(end="\n\n")

lst = ["raman","karan","lakshman","jatin","neha","umesh"]
random_array = np.random.randint(1,100,5)

random_lst_array = np.unique(np.random.choice(lst,3))
random_lst_array = np.random.choice(lst,3)

# print(random_lst_array)

array_2d = np.array((["Num1","Num2","Num3"],[10,20,30],[101,201,301]))
ar3 = array_2d.transpose()
ar4 = array_2d.T
print(ar4)
