"""
================================ Exceptional(Error) Handling =================================
using excrptional handling we can handle run-time errors.

Exceptions stop running after exception.

We can provide a meaningfull message in place of error.

syntax:-
----------
try:
    statement
except ExceptionName:
    message
else:
    run when there is no exception
finally:
    This block runs with-exception and without exception


try :- in this block we write our code OR try our code
except :- This block handle exceptions
else :- This block will execute if there is no exception in our Code
finally :- this block execute always with exception and without exception.
----------------
raise :- This keyword is used to generate a custom exception.
"""

# print(17/0) # ZeroDivisionError
# print(lst) # NameError

l = [1,2,3,4]
# print(l[10]) # IndexError

dct = {1:10,2:20,3:30}
"""
try:
    # print(dct[5])
    print(37/0)
except KeyError as e:
    print(f"Given key {e} is Not valid")
except ZeroDivisionError as e:
    print("Any Number can not be divisible by 0.")
else:
    print("\nThis block runs when there is No exception")
finally:
    print("\nThis is finally block")
print("Hello world")
"""


num = int(input("Enter any number"))

try:
    sum = num+10
    print(sum)
except TypeError,ZeroDivisionError,NameError,ValueError:
    print("Some error occured")

# import math as m
# from math import *
# import keyword
# print(keyword.kwlist)
