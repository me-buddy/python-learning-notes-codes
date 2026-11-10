# return keyword in python 

# return :- used to come out from function body.

def sum(n1,n2):
    return print(n1+n2)

# sum(10,20)

"""
================================== recursion in python ===============================
When a "function calls" itself inside their "function definition" it is called recursion.
To stop function calling we have to provide a BASE CONDITION.

NOTE : By default, the Python recursion limit is typically set to 1,000. 
       This limit is a safeguard in the "CPython interpreter" designed to prevent infinite recursion
       from causing a C stack overflow and crashing the entire program.

syntax:-
--------

def functionName(parameter):
    if(base_condition):
        return
    return functionName(parameter)
"""
# for i in range(1,11):
#     print(i)

#* 1. Printing 1-10 using recursion

def counter(n):
    print(n)
    # base conditio
    if(n==10):
        return
    # function calls itself
    return counter(n+1)


# counter(1)

#* Printing 10-1 using recursion

def rev_count(n):
    print(n)
    if(n==1):
        return
    return rev_count(n-1) 

# rev_count(10)


name="Raman"
age=32
address="Mathura"
pincode = 281121
# print(f"Name is {name} Age is  {age} Address is : {address} Pincode is : {pincode}")

#* sum of n natural numbers using recursion
# 1+2+3+4+5+6+7+8+9+10 => 55 
# sum=0
# factorial = 1
# for i in range(1,11):
#     sum = sum+i
#     factorial = factorial*i

# # formated string OR f'string
# print(f"The sum of 10 terms is : {sum}")
# print(f"The factorial of 10 terms is : {factorial}")

def sumN(n):
    if(n==1):
        return 1
    return n+sumN(n-1) #10 + sumN(10-1) + sumN(9-1) + sumN(8-1) + sumN(7-1) + sumN(6-1)...sumN(2-1) + 1

# print(sumN(10))

#* factorial using recursion
def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)

# print(factorial(5))

#* Fibonnachi Series using recursion
# 0 1 1 2 3 5 8 13 21 34 55 89 ,...
# n1=0
# n2=1

# for i in range(1,11):
#     print(n1,end="\t")
#     n3 = n1+n2
#     n1=n2
#     n2=n3

def fibo(n):
    if(n==1):
        return 0
    if(n==2):
        return 1

    return fibo(n-1) + fibo(n-2)
# 5 => 4+3
# print(fibo(8)) => fibo(7)+fibo(6)

# for i in range(1,10+1):
#     print(fibo(i) , end="\t")

"""
break :- exit from loop
continue :- skip part
pass :- skip a block
return :- exit from function

"""
age=21
if(age>19):
    pass

def take_user_input(value):
    pass


