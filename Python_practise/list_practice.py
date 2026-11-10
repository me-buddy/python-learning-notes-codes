
#Nested list :- A list inside the list is called nested list.
# ex:- [1,2,3,[4,5,6,[7,8,9]]]

#* flatten a nested list
"""
lst = [[1,2,3],[10,20,30],["a","b","c"]]
lst2=[]
for i in lst:
    for j in i:
        lst2.append(j)

print(lst2) # [1, 2, 3, 10, 20, 30, 'a', 'b', 'c']
"""


# *1 Remove Duplicates While Preserving Order
"""
nums = [1,2,2,3,4,1,5,21,43,32,21,-10,-10]
# st = set(nums)

nums2 = []

for value in nums:
    if(value not in nums2):
        nums2.append(value)

print(nums2)
"""

# *2 Find the Second Largest Number
# Find the second largest element in a list without using sort().
"""
nums = [10, 20, 4, 45, 99,21,3423,534]
# nums.sort()
# print(nums)
# print(nums[-2])

largest = nums[0] # here wwe assume that the largest value is at 0 index.

for i in nums:
    if(i>largest):
        largest = i
    
second_largest = 0
for i in nums:
    if(i<largest):
        second_largest = i


print("Largest value in list : ",largest)
print("Second largest :- ",second_largest)
"""

# *3 Split List Into Chunks
# Divide a list into smaller lists of size n.

# Example:
# ----------
# nums = [1,2,3,4,5,6,7]
# n = 3
# Output: [[1,2,3],[4,5,6],[7]]

"""
nums = [1,2,3,4,5,6,7,21,32,43,5,46,5,786,89,10,20,30]
n = 3
lst = []

l = len(nums)//n
count=0

for i in range(0,l):
    l = []

    if(count == len(nums)):
        break

    else:

        for j in range(n):
            l.append(nums[count])
            # print(count,end=" ")
            count+=1

    lst.append(l)
    
    print()
    
print(lst)
# 0,1,2 || 3,4,5 || 6,7,8 ||....

"""

"""
nums = [1,2,3,4,5,6,7,21,32,43,5,46,5,786,89,10,20]
n = 3

lst1=[]
temp_lst =[]

for i in nums:
 
    temp_lst.append(i)
    if(len(temp_lst)==n):
        lst1.append(temp_lst)
        temp_lst = []

if temp_lst:
    lst1.append(temp_lst)
    
print(lst1)
"""

# *4 Find Common Elements Between Two Lists
# Return the common elements without duplicates.
"""
a = [1,2,3,4,5]
b = [3,4,5,6,7]
# Output: [3,4,5]
c = []

for i in a:
    if(i in b):
        c.append(i)
print(c)
"""


# *5 Move All Zeros to the End
# Move all 0s to the end while maintaining the order of non-zero elements.
"""
nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
lst=[]

# This loop is used to insert those values into lst which are not equal to 0
for i in nums:
    if(i!=0):
        lst.append(i)

# This loop is used to insert those values into lst which are equal to 0
for i in nums:
    if(i==0):
        lst.append(i)
print(lst)
"""

# *6 Check if a List is a Palindrome
# Determine whether a list reads the same forward and backward.
"""
nums = [1,2,3,2,1]

rev_lst = nums[::-1]

print(nums)
print(rev_lst)

if(nums == rev_lst):
    print("palindrome")
else:
    print("Not Plindrome")
"""


# *7 Find Frequency of Each Element
# Count how many times each element appears in a list.
"""
nums = [1,2,2,3,1,4,2]
# Output:
# {1:2, 2:3, 3:1, 4:1}

dct = {}
for i in nums:
    dct.update({i:nums.count(i)})
print(dct)

# (.update() =>[used to merge two dictionaries] )= (.extend() =>[used to merge two lists])
"""

# *8 Rotate a List Left by k Positions
# Rotate the list to the left by k positions.
"""
nums = [1,2,3,4,5]
k = 2
# Output: [3,4,5,1,2]

print(nums[k:])
print(nums[:k])

rotate_lst = nums[k:] + nums[:k]
print(rotate_lst)


l1=[1,2,3]
l2=[4,5,6]

# l1.extend(l2) :- add new list and not create another list
# l3=l1+l2 :- add two lists but create a new list.
# print(l3)
"""

# *9 Find All Pairs With Given Sum
# Find all unique pairs whose sum equals a target value.

nums = [1,2,3,4,5,6]
target = 7
# Output: [(1,6), (2,5), (3,4)]

lst=[]
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)+1):
        if(i+j == target):
            lst.append((i,j))
    
# print(lst)

def sayHello():
    print("Hello from list file")