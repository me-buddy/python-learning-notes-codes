"""
Numpy
pandas
matplotlib and seaborn
MACHINE LEARNING
----------------------------------------------
Scikit-learn ==> supervised and unsupervised
Deep learning ==> Tensorflow
----------------------------------------------
ml engineer :- math (algorithms => maths formulas)
FastAPI
url + api key

Data Science :- Excel (20-25) + PowerBi(1 month) + basic Python + mysql + advance python + ML(Scikit-learn)
---------------

====================================================================================================================
NumPy (Numerical Python) it is created by "Travis Oliphant" in 2005.
It is used to work with arrays.

array ==> similar structure to python list

we have to install numpy before use :- pip install numpy.

=> array is lightweight compared to python list.
=> array is fast
=> arrays are best for work with large amount of data.

=> NOTE :- Array stores homogenious data types => same data type values

=> provide large number of functionalities.

=> arrays are memory efficient => we can handle/set array size
=> NOTE :- Arrays are Mutable(We can change values by targeting their index)


import numpy ====> Named Import
numpy.function()

import numpy as np ===> import with alias
np.function()

from numpy import * ===> To import all functions with their name
functionName()

from numpy import function1 , function2 , function3



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ array properties ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
=> .dtype
=> .ndim => to get number of dimensions
=> .ndmin => To set number of dimensions
=> .size => return total number of values inside a array.
=> .nbytes => return the memory size in bits  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ----------------------------- different methods to create an array --------------------------
=> np.array(list/tuple) :- It convert a list or tuple into an array.
=> np.arange(start,end-1) :- Creates an array in between start to end-1
=> np.zeros((row,col)) :- Creates an array(matrix) and fill all values with 0.
=> np.ones((row,col)) :- Creates an array(matrix) and fill all values with 1.
=> np.linspace(start,end,step) :- creates an array from start to end AND difference between two values are same.
=> np.identity(size,dtype) :- creates a digonal metrix and fill diagonal values with 1
                                    OR
=> np.eye(size,dtype) :- creates a digonal metrix and fill diagonal values with 1
* ---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------
Step1 :- create an array ===> pass a list or tuple as value
=> np.array(list/tuple)
"""

import numpy as np

lst =  [1,2,3,4]
arr =  np.array([1,2,3,4])

# print(lst) # [1, 2, 3, 4]
# print(arr) # [1 2 3 4]
# Array stores values in a continious way.



ar = np.array([1,2,3,4,5,6],dtype="int8")
# print(ar) # [1.  2.  3.  4.  5.5]

# print(ar.dtype) # int8
# print(ar.size) # 6
# print(ar.ndim) # 1
lst = [[[1,2,3],[10,20,30],[11,12,13]]]
# print(lst)
print()
ar2 = np.array([[1,2,3],[10,20,30],[11,12,13]])
# print(ar2)
# print(ar2.ndim) # 2
# print(ar2[1][1]) # 20
ar2[1][1] = 100
# print(ar2)


ar3 = np.array(
    [
        [
            [
                [
                    [100,200,300],
                    [1,2,3],
                    [10,20,30],
                    [10,20,30]
                ]
            ]
        ]
    ] , dtype="int32"
)
print(ar3)
# print(ar3.ndim)
# print(ar3[0][0][0][1][1])
# print(ar3[1])

print(ar3.size) # 9
print(ar3.nbytes) #72 => 9*8 => each value stores 8 bits data.
"""
1D => 1 dimensional ===> single line => ---------------------
2D => 2 => length X width
3D => length X width X height
"""

arange_array = np.arange(1,11)
# print(arange_array) # [ 1  2  3  4  5  6  7  8  9 10]


zeros = np.zeros((3,2),dtype="int32")
# NOTE :- default data type in zeros array is "float64"
# print(zeros.dtype) # int32
# print(zeros)
"""
[[0 0]
 [0 0]
 [0 0]]
"""

ones = np.ones((4,3),dtype="int8")
# NOTE :- default data type in ones array is "float64"
# print(ones)
"""
[[1 1 1]
 [1 1 1]
 [1 1 1]
 [1 1 1]]
"""





linspace_array = np.linspace(1,5,10) # 10 values in between 1 - 5
# print(linspace_array)
"""
[1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222
 3.66666667 4.11111111 4.55555556 5.        ]
"""

linspace_array2 = np.linspace(0,1,5) # 5 values between  0 to 1
# print(linspace_array2)
"""
[0.   0.25 0.5  0.75 1.  ]
"""

identity = np.identity(4,dtype="int8")
# print(identity)

"""
[[1 0 0 0]
 [0 1 0 0]
 [0 0 1 0]
 [0 0 0 1]]
"""

eye = np.eye(4,dtype="int8")
# print(eye)

#* To Fill diagonal values as our requirement
matrix = np.zeros((3, 3), dtype=int)
# np.fill_diagonal(2DArray , diagonal_value)
np.fill_diagonal(matrix, 7)

# print(matrix)
# Output:
# [[7 0 0]
#  [0 7 0]
#  [0 0 7]]

#* ============== create array with random values =================
# np.random.rand(rows,cols) :- Create a Random values array and all values are in between 0 and 1.
# np.random.randint(start,end,totalValues) :- create an array from start to end with specified length.
# np.random.seed(number) :- After generating a random matrix it fixed the values on every code run.

arr_rand = np.random.rand(2,3)
# print(arr)

np.random.seed(1)
arr_randint = np.random.randint(1,10,(5,5))

np.random.seed(22)
arr_randint2 = np.random.randint(1,10,(5,5))
print(arr_randint)
print(arr_randint2)