"""
=========================================== Tuple in Python =======================================
Used to store multiple values inside parenthesis() with comma seperation.

=> It is Immutable
=> It is Ordered :- every value have index number (start from 0 and last at -1 index)
syntax:- tupleName[index]
=> Allow Duplicates.
=> It is hetrogenious.

syntax:-
--------

tupleName = (value1,value2,value3,....)
OR
tupleName = tuple([value1,value2,value3 ,....])
OR
tupleName = value1,value2,value3,..

===================== tuple functions ======================
1  len(tupleName) :- return length of tuple
2  .count(value) :- return the count of particular value
3  max(tupleName) :- return maximum value
4  min(tupleName) :- return minimum value
5  .index(value) :- return index number
"""

# tpl = ()
# tpl = (1,2,3,"hello")
# tpl = tuple([1,2,3,"hello"])
# tpl = (1,)

# print(type(tpl))


tpl = (1,2,3,67,45,1,1,1)

# print(tpl[0:3]) # => (1, 2, 3)

# tpl[0] = 10 # TypeError

# print(len(tpl)) # 8
# print(max(tpl)) # 67
# print(min(tpl)) # 1

# print(tpl.count(1)) # 4
# print(tpl.index(45)) # 4

