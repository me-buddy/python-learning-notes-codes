"""
=> data types
=> operators
=> conditional statements
=> loop statements (for loop and while loop)
=> functions
=> collection data types (list,tuple,set,dictionary)
=> oops(object oriented programming)
=> file handling
=> exceptional handling
---------------------------
MySql -> integration with python
----------------------------
Numpy
=> pandas
=> scikit learn(Machine Learning)
=> NLTK
"""

"""
============================ Function in Python ======================================
These are the block of code that runs when we call it.

=> Code Reusability
=> Modular Programming
=> Scalability 

There are Two Types of functions :
----------------------------------
*1. Built-In Functions :- These are pre-defined , we just have to call them to use.
ex:- print() , input() , int() , str() , len() , etc.

*2. User defined functions :- These are defined by user as per their requirement.

syntax:-
---------
~~~~~~~~~~~~~~ function definition ~~~~~~~~~~~~~~~
def functionName(parameter1,parameter2,...):
    statements

~~~~~~~~~~~~~~ function calling ~~~~~~~~~~~~~~~~~~
functionName(argument1,argument2,...)
    

& parameter :- These are named placeholder inside function definition.
& argument :- These are the real values in place of Parameters.

! RULES FOR FUNCTION NAMES or VARIABLES NAMES
* never start with number
* no space between name
* No special characters  EXCEPT underscore(_)
* No reserve word OR keywords(35)
* Names are case-sensitive(ASCII value)

NOTE : We have to call functions to get result.

NOTE : Python is a INDENTATION based Programming language
"""

# ^ function with NO PARAMETER 
def sayHello():
    print("hello To all USERS")

# sayHello()

# ^ function with PARAMETER 

def user_info(name,age,address):
    print("User Name is : ",name)
    print("User Address is : ",address)
    print("User Age is : ",age)
    print("-----------------------------------------\n")

# user_info("Karan",12,"Mathura")
# user_info("Arjun",32,"Agra")
# user_info("Rahul",54,"Raya")
# user_info("Garima",65,"Vrindavan")

# ^ function with DEFAULT PARAMETER
#! NOTE : Default parameter always write after the parameter which have no default parameter.
def student(name,school_name="KMPS"):
    print("Student's name is : ",name)
    print("School Name is : ",school_name)
    print("-----------------------------------------\n")

# student()
# student("Ram")
# student("Lokesh","Delhi Public School")
# student("Dinesh","vrindavan Public School")


# def pattern_A():
#     for row in range(1,7+1):
#         for col in range(1,5+1):
#             if((col==1 or col==5) and row!=1):
#                 print("*",end=" ")
#             elif((row==1 or row==4) and (col>1 and col<5)):
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()

# pattern_A()

def pattern_A(r,c,symbol):
    for row in range(1,r+1):
        for col in range(1,c+1):
            if((col==1 or col==c) and row!=1):
                print(symbol,end=" ")
            elif((row==1 or row==r//2 + 1) and (col>1 and col<c)):
                print(symbol,end=" ")
            else:
                print(" ",end=" ")
        print()

# pattern_A(5,5,"#")
# pattern_A(15,15,"&")
#* ======================= R pattern =======================
# for row in range(1,9+1):
#     for col in range(1,5+1):
#         if(col==1):
#             print("*",end=" ")
#         elif((row ==1 or row==5) and (col<5)):
#             print("*",end=" ")
#         elif((col==5 and row<=5) and (row!=1 and row!=5)):
#             print("*",end=" ")
#         elif(row==col+4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#* ======================== O pattern =======================
# r=  int(input("Enter row number : "))
# c=  int(input("Enter col number : "))
def pattern_o(r,c):
    for row in range(1,r+1):
        for col in range(1,c+1):
            if((col==1 or col==c)and(row!=1 and row!=r)):
                print("*",end=" ")
            elif((row==1 or row==r) and (col!=1 and col!=c)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
# pattern_o(r,c)

#* ================================ Q pattern ======================================
# for row in range(1,7+1):
#         for col in range(1,7+1):
#             if((col==1 or col==5)and(row!=1 and row<6)):
#                 print("*",end=" ")
#             elif((row==1 or row==6) and (col>1 and col<5)):
#                 print("*",end=" ")
#             elif(row==col+1 and row>3):
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()


#* ============================== lambda Function ==================================
"""
It is a Anonymous Function.
No prerior Name.

It is used to write single line function in Python.

SYNTAX:-
---------

variableName = lambda parameter1 , parameter2 :  statement
"""
sayHello = lambda : print("Hello world")
greeting = lambda name: print(f"Hello Mr./Mrs. {name}")
# greeting("Tarun")
# greeting("Varun")
# greeting("Geeta")

# sayHello()

sum = lambda a,b=10 : print(a+b)
# sum(10)
# sum(5,5)

#^ ================= function with multiple parameters ====================
"""
def functionName(*args):
    statement

NOTE :- *args :- It create a tuple which we can iterate.
"""
def sumN(*args):
    sum=0

    for i in args:
        sum = sum+i
    print("The sum is : ",sum)


# sumN(10,20,30)

# --------------------------------------------------------------------------
a = "Greater"if(10>6) else "Lessthan"
# print(a)
