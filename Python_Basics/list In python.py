"""
List is used to store multiple values in a single variable inside square brackets and comma seperation.
----

1. List is Mutable :- Allow Changes.
listName[indexNumber] = newValue

2. List is Ordered :- In list every value have an index number, Which starts from 0.
3. List allow Duplicate values
4. List store different data types values called Hetrogenious Data Type.

SYNTAX:-
--------
listName = [value1 , value2 , value3 ,....]
OR
listName = list(value1 , value2 , value3 ,....)
"""

student1_information = ["Ram",21,"Mathura",78,192,8979837949,True,21]
# print(student1_information)
# print(type(student1_information))

# print(student1_information[0:3]) # ['Ram', 21, 'Mathura']

student1_information[0] = "Mohan"
# print(student1_information)

#^ To check value is Present or Not in list
# print(value in listName )

# print(21 in student1_information)

#^ List is Iterable  :- we can access values through loop.

# for value in student1_information:
    # print(value)

# lst = [1,2,3,4,5,6,7,7,8,9,0,54,5,4,3,2,3,3,4,4,43,3]
# val = int(input("Enter value which you want find : "))
# count=0

# for i in lst:
#     if(i==val):
#         count+=1

# print(f"Total count of {val} is : {count}")


"""
=========================================== List Functions ====================================
!~~~~~~~~~~~~~~~~ functions related to adding values into the list ~~~~~~~~~~~~~~~~~~~~~~~~

=> len(listName) :- It return the length of the list.Number of values inside the list.

1 .append(value) :- It is used to insert single value at the end of the list.
syntax : listName.append(value)

2 .insert(index,value) :- Used to add value at particular Index number
syntax:- listName.insert(index,value)

3 .extend(lstName) :- Used to merge two lists.
syntax :- list1.extend(list2)
!~~~~~~~~~~~~~~~~ functions related to removing values from the list ~~~~~~~~~~~~~~~~~~~~~~~~
4 .pop() :- By default it removes last value from the list.
OR
4 .pop(index) :-it also removes particular index value from the list.

5 .remove(value) :- It removes particular value from the list.

6 .clear() :- Remove all values from list and return an empty list.

7 del listName :- del keyword is used to delete the list.

!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ List extra Methods ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
8 .sort() :- It arrange list in by default Accending Order.
OR
8 .sort(reverse=True) :- It arrange list in  decending Order.

9 sorted(listName) :- Arrange values in Accending Order but reflection shows in another list. Original has no change.

10 .reverse() :- It reverse the list

11 reversed(listname) :- Change show in list copy , Original remains Same OR no change.

12 max(listName) :- return maximum value from the list
13 min(listName) :- return minimum value from the list

14 .index(value) :- Return index number of given value from the list

15 .copy() :- create deep copy of the list.

16 .count(value) :- return the count of the value from the list.

17 sum(list) :- It is used to add all values inside list
"""
lst = [1,2,3,4]
lst.append(10)
lst.insert(1,20)
# print(lst)

l1=[10,20,30,21,32,43,"Ram",True,28.32]
l2=["a","b","c"]

# l1.extend(l2)
# l1.append(l2)
# print(l1[3][1])
# print(len(l1))

# l1.pop()
# l1.pop(1)

# l1.remove("Ram")
# l1.clear() # []
# del l1 # NameError
# print(l1)
#* This program remove 3 values from the list by taking choice from user for string or int or float value removal.
def remove_3Values_from_list():
    for i in range(3):
        print(l1,end="\n\n")
        choice=input("""
    Choose from following :
    ------------------------------
    1 for string value remove
    2 for integer value remove
    3 for floating value remove
    => """)
        
        print()

        if(choice =="1"):
            value_st = input("Enter value you want to remove : ")
            l1.remove(value_st)
        elif(choice=="2"):
            value_int = int(input("Enter value you want to remove : "))
            l1.remove(value_int)
        elif(choice =="3"):
            value_float = float(input("Enter value you want to remove : "))
            l1.remove(value_float)
        else:
            print("Invalid Choice.....")


    print(l1)

# ==================================== extra methods =============================================
lst = [21,32,43,5,5,21,-21,32,45,-324,37,4,76]

# lst.sort() # [-324, -21, 4, 5, 5, 21, 21, 32, 32, 37, 43, 45, 76]

# lst.sort(reverse=True) # [76, 45, 43, 37, 32, 32, 21, 21, 5, 5, 4, -21, -324]

# lst2 = sorted(lst) # [-324, -21, 4, 5, 5, 21, 21, 32, 32, 37, 43, 45, 76]

# lst.reverse() # [76, 4, 37, -324, 45, 32, -21, 21, 5, 5, 43, 32, 21]

# lst2 = reversed(lst)
# for i in lst2:
#     print(i,end=" , ")

# print(lst2)

# print(max(lst)) # 76
# print(min(lst)) # -324

# print(lst.index(-21)) # 6

"""
In Programming there are two kinds of Copy
--------------------------------------------
^1. shallow copy :- change in copy also shows reflect in original.
ex:-
-----
a = lst

^2. deep copy :- change in copy can not affect original
ex:-
-----
a = lst.copy()

"""
# a = lst.copy() # ===> deep Copy
# a = lst # =====> shallow copy
# a.append("Hello")
# print(lst)

# print(lst.count(5)) # 2

# ======================== list comprehension =====================
#^ syntax:- [ variable for variable in range(start,end,step) ]
#! OR
#^ syntax:- [ variable for variable in range(start,end,step) if condition]

# lst = [value for value in range(1,11)] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst=[value for value in range(1,11) if value%2==0 ]

# for i in range(1,11):
#     if(i%2==0):
#         lst.append(i)

# print(lst)


# print(sum(range(1,5)))