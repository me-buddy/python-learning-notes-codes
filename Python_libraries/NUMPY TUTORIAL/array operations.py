
#Array Ooperations----------------------------- 

import numpy as np

arr1 = np.array([10,20,30,40,50])
arr2 = np.array([1,2,3,4,5])

"""
np.add(arr1,arr2)       OR arr1+arr2
np.subtract(arr1,arr2)  OR arr1-arr2
np.multiply(arr1,arr2)  OR arr1*arr2
np.divide(arr1,arr2)    OR arr1/arr2
np.dot(arr1,arr2)       OR arr1@arr2


arr.reshape((row,column)) :- It reshape any existing array, but product of rowsXcolumns must be equal to size of array

"""

add = arr1+arr2 # [11 22 33 44 55]
sub = arr1-arr2 # [ 9 18 27 36 45]
mul = arr1*arr2 # [ 10  40  90 160 250]
div = arr1/arr2 # [10. 10. 10. 10. 10.]

# print(add)
# print(sub)
# print(mul)
# print(div)

#* Dot Product
# dot_product = arr1@arr2
# dot_product = np.dot(arr1,arr2)
dot_product = np.dot([1,2],[10,20]) #==> 50 
# (1*10 + 2*20) => 10 + 40 => 50
# print(dot_product)

# 1*10 + 2*20 + 3*30 + 4*40 + 5*50 => 10 + 40 + 90 + 160 + 250 => 550
# print(sum([]))


arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = arr.reshape((2,5))
# arr3 = arr.reshape((5,2))
# arr4 = arr.reshape((10,1))

print(arr2)
"""
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
"""

# t_array = arr2.transpose()
t_array = arr2.T
# print(t_array)


def combination(n,r):
    import math
    result = (math.factorial(n)) / ( math.factorial(r) * math.factorial((n-r)) )
    print(result)

# combination(5,2)

# from itertools import permutations

# arr = ([1, 2, 3],[10,20,30])

# for p in permutations(arr):
#     print(p)




