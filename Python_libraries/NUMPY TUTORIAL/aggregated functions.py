"""
Aggregated Functions :- These are used to perform operations on an array and return single value.
-----------------------
=> np.min(array) :- return minimum value from array 
=> np.max(array,axis=0/1) :- return maximum value from array 
=> np.mean(array,axis=0/1) :- return average of an array. 
=> np.median(array,axis=0/1) :- return median of an array 
=> np.sum(array,axis=0/1) :- return sum of all values from array 
=> np.prod(array,axis=0/1) :- return product(multiply) of all elements 
=> np.std(array,axis=0/1) :- return standard deviation of an array. 
=> np.var(array,axis=0/1) :- return variance of an array. 

=> np.sort(arr,axis=0/1) :- sort and arrange array by row-wise or column wile
=> np.argsort(arr,axis=0/1) :- return index values of min value from the array.
"""
import numpy as np

arr = np.array([
    [1,2,3,4,5],
    [10,20,30,40,50],
    [-11,2,3,34,4],
    [12,32,4,35,4],
    [1000,2,3,32,43]
])

# srt = np.sort(arr,axis=1)
arg_srt = np.argsort(arr)
print(arg_srt)

# print(arr.ndim)
# print(arr.size)
# print(arr.dtype)
# print(arr)
print()
min = np.min(arr)
min = np.min(arr,axis=0)
max = np.max(arr)
sum = np.sum(arr) # 165 ==> sum of all values from the array.
#^ axis = 0 ===> column-wise
#^ axis = 1 ===> row-wise
sum = np.sum(arr,axis=0) # => Perform sum on each element - column-wise 
sum = np.sum(arr,axis=1) # => Perform sum on each element - column-wise 

prod = np.prod(arr,axis=1)
# print(prod)

std = np.std(arr,axis=1)
# print(std)
print()
# print(sum)

# print(min)


# =============================================== e-commerce dataset =========================================
records = np.array([
    [1, "ShopEase",      "Fashion",     "USA",        "New York",    12500, 13200, 12800, 14100, 15600, 18200, 17400],
    [2, "QuickCart",     "Groceries",   "Canada",     "Toronto",      9800, 10200, 10150, 10500, 11300, 12600, 11900],
    [3, "ElectroHub",    "Electronics", "Germany",    "Berlin",      22100, 21500, 22900, 23400, 24800, 27600, 26800],
    [4, "HomeNest",      "Furniture",   "UK",         "London",       7600,  8100,  7900,  8500,  9100, 10400,  9800],
    [5, "BeautyBloom",   "Cosmetics",   "France",     "Paris",       11200, 11650, 11800, 12100, 12900, 14100, 13600],
    [6, "SportZone",     "Sports",      "Australia",  "Sydney",       9400,  9800, 10100, 10500, 11200, 12400, 11900],
    [7, "BookVerse",     "Books",       "India",      "Delhi",        5100,  5400,  5600,  5900,  6500,  7100,  6900],
    [8, "PetWorld",      "Pet Supplies","USA",        "Chicago",      8700,  9000,  9200,  9600, 10200, 11300, 10800],
    [9, "ToyPlanet",     "Toys",        "Japan",      "Tokyo",       13400, 13800, 14100, 14700, 15600, 17200, 16800],
    [10,"FreshBasket",   "Groceries",   "India",      "Mumbai",      24600, 25100, 25700, 26300, 27800, 30100, 29400]
],dtype=object)

print()
# print(records[][5:])
lst=[]
for row in records:
    lst.append(row[5:])

# print(lst)
# for i in lst:
#     print(i)

days_records = np.array(lst)
# print(days_records) 
# print("\nMinimum value from each column from days_records array :- \n")

days    =  np.array(["mon","tue","wed","thu","fri","sat","sun"])
min_sale = np.min(days_records,axis=0)
max_sale = np.max(days_records,axis=0)
sum    =   np.sum(days_records,axis=0)
mean   =   np.mean(days_records,axis=0,dtype='int64')

# print(mean)

data = [min_sale,max_sale,sum,mean]

# for i in days:
#     print(i,end="\t")
# print()


# for record in data:
#     for value in record:
#         print(value,end=" \t")
#     print()



arr = np.array([1,2,3,-10,21,54,212,19])

# print(arr.argsort()) # [3 0 1 2 7 4 5 6]

# print(arr)

# print(np.indices(arr))

# ================================================================================================
# lst = []
# for i in arr:
#     if(i>10):
#         lst.append(i)

# print(np.array(lst))

#^ Filtering in an Array 
#* np.where(condition) :- It creates a new array and return all those indexis of values that satisfies the condition.

arr2 = arr[np.where(arr>10)]
# print(arr2) # (array([4, 5, 6, 7]),)
# [ 21  54 212  19]

# print(arr[0])

#* =============================== merging of two or More array ===============================
ar1 = np.array([[1,2,3,4],[11,22,33,44]])
ar2 = np.array([[10,20,30,40],[21,32,43,54]])
# print(ar1+ar2) # [12 24 35 47]

#^ np.concatenate((arr1,arr2,...),axis=0/1) :- Used to merge two or more arrays.
"""
axis=0 => concatenate arrays row-wise
axis=1 => concatenate arrays column-wise
"""
#^ np.vstack((arr1,arr2,...)) :- Used to merge two or more arrays Vertically.
#^ np.hstack((arr1,arr2,...)) :- Used to merge two or more arrays Horizontally.

ar3 = np.concatenate((ar1,ar2),axis=0)
"""
[[ 1  2  3  4]
 [11 22 33 44]
 [10 20 30 40]
 [21 32 43 54]]
"""

ar4 = np.concatenate((ar1,ar2),axis=1)
"""
[[ 1  2  3  4 10 20 30 40]
 [11 22 33 44 21 32 43 54]]
"""
# print(ar4)

vstack = np.vstack((ar1,ar2))
# print(vstack)
"""
[[ 1  2  3  4]
 [11 22 33 44]
 [10 20 30 40]
 [21 32 43 54]]
"""

hstack = np.hstack((ar1,ar2))
# print(hstack)
"""
[[ 1  2  3  4 10 20 30 40]
 [11 22 33 44 21 32 43 54]]
"""

#! NOTE :- .astype("dataType") => Create a new array from existing array with user defined data type.
a = arr.astype("float64")
# print(a)


#! np.any(condition) :- return True if any one value of an array satisfied the condition,else return False
print(np.any(arr>15)) # True