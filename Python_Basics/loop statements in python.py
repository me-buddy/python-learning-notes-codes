"""
block code
-----------
1 conditional statement
if(condition):
    statement

2. loop statements
3. functional statement
4. exceptional handling
5. file handling
6. OOPS
============================ loop statements in python ===============================
It is a 'block of code' that runs multiple times.Until a given condition is satisfied.

In Python there are two types of loops :
-----------------------------------------
1. for loop :- when starting and terminating(ending) condition is known.
2. while loop :- When terminating(ending) condition is not Known.

* for loop in Python 
* -------------------
syntax:-
--------
for variableName in range(start,end-1,steping-1):
    statement

"""
#^ type-casting :- conversion of one data type into another data type is called type-casing
"""
ex :-
-----
1. string to integer :- int()
2. string to float :- float()
3. int/float  to string :- str()

a = str(10)
"""
#1. printing 1-10 numbers using for loop 

# for num in range(1,10+1,1):
#     print("hello world",num)
#     print("---------------------")

#2. Print a Multiplication table of user-defined number
"""
5X1 = 5
5X2 = 10
5X3 = 15
5X4 = 20
...
"""
"""
table_number = int(input("Enter table number : ")) 
for i in range(1,10+1):
    # print(i*table_number)
    print(table_number,"X",i,"=",table_number*i)
"""

#^ print number from 10-1 using for loop
# for i in range(10,0,-1):
#     print(i)

#^ Program to find sum of n natural numbers from 1-10
"""
n = int(input("Enter Number of terms : "))
# 1+2+3+4+5+6+7+8+9+10 => 55 
sum=0 #1,3,6,10,15,21,28,36,45 , 55
for i in range(1,n+1):
    # i=1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10
    sum = sum+i # 0+1=> 1 , 1+2=>3 , 3+3=>6 , 6+4=>10 , 10+5=>15 , 15+6=>21 , 21+7=>28 , 28+8=>36 , 36+9=>45 , 45+10 => 55

print(sum)
"""
# 5 => 1*2*3*4*5 => 120
# 123 => 321 X , 121 => 121 , 343=>343

"""
#* fibonnachi Series upto n number of terms
# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 , ...........
nterm = int(input("Enter n number of terms : "))
n1 = 0 #1,1,2,3,5,8,13,21,34,55
n2 = 1 #1,2,3,5,8,13,21,34,55,89

for i in range(1,nterm+1):
    # i=1,2,3,4,5,6,7,8,9,10
    print(n1,end=",") # 0,1,1,2,3,5,8,13,21,34
    n3 = n1+n2 # 0+1=>1 , 1+1=>2, 1+2=>3, 2+3=>5 , 3+5=>8 , 5+8=>13,8+13=> 21 , 13+21 => 34 , 21+34=>55 , 34+55=> 89
    n1=n2 # 1 , 1 , 2, 3, 5, 8, 13 , 21 , 34,55
    n2=n3 # 1 , 2 , 3, 5 , 8, 13, 21, 34 , 55,89
"""
# a=10
# b=20
# Using a temporary Variable
"""
temp=a # 10
a=b # a=20
b=temp # b=20
"""
# Without temporary variable
"""
a,b = b,a
print("a : ",a)
print("b : ",b)
"""

# =============================================================================================
# print("hello",end="\t")
# print("world")

#* ====================================== While Loop ==========================================
"""
It is used when we initally have no terminating(ending) value.
"""
# ans="y"
# count=0
# while(ans=="y"):
#     count+=1 # count = count+1
#     ans=input("Enter y/n : ")
    
# print("Total Count is : ",count)

#* printing 1-10 using while loop

# i=1
# while(i<=10):
#     print(i)
#     i=i+1

#* printing 10-1 using while loop
# i=10
# while(i>=1):
#     print(i)
#     i=i-1

#* find total Number in a digit
# num=124532 => 6  

# To get last digit of a number :- num%10
# To get all digits except last digit of a number :- num//10
"""
num = int(input("Enter Any Number : ")) # 123 , 12 , 1 , 0
count=0 # 1 , 2 , 3
while(num>0):
    count+=1
    num = num//10 # 123//10 => 12 , 12//10 => 1 , 1//10 => 0

print("Count is : ",count)
"""

#* Reverse the number
# 123 => 321
"""
num=int(input("Enter any number : ")) #123, 12 , 1 , 0
temp = num
rev_num=0 #3 , 32 , 321

while(num>0):
    last_digit = num%10 # 123%10 => 3 , 12%10 => 2 , 1%10 => 1
    rev_num = rev_num*10 + last_digit # 0*10+3=> 3 , 3*10+2 => 32 , 32*10 + 1 => 321
    num = num//10 # 123//10 => 12 , 12//10 => 1 , 1//10 => 0

print("Original Number : ",temp)
print("Reversed Number : ",rev_num)

if(temp==rev_num):
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")
"""
# =======================================================
"""
for num in range(1,1001):
    temp=num
    rev_num =0

    while(num>0):
        last_digit = num%10
        rev_num = rev_num*10 + last_digit
        num = num//10
    
    if(temp==rev_num):
        print(temp)
"""
# ========================= Armstrong Number ============================
# 153 => 1**3 + 5**3 + 3**3 => 1 + 125 + 27 => 153 --> Arstrong Number
# 123 => 1**3 + 2**3 + 3**3 => 1+8+27 => 36 X
# 1634 => 1**4 + 6**4 + 3**4 + 4**4 => 1+1296+81+256 => 1634 ---> Armstrong
#~ --------------------------------------------------------------------------------
# num = int(input("Enter any number :- "))
# power = len(str(num))
# temp=num
# arm_num = 0
# while(num>0):
#     last_digit = num%10
#     arm_num = arm_num+last_digit**power
#     num = num//10

# if(temp == arm_num):
#     print("\nIt is a Armstrong Number")
# else:
#     print("It is NOT a Armstrong Number")
#~ -----------------------------------------------------------------------------------
# printing all armstrong number from 1 to 100000
for num in range(1,100000+1):
    power = len(str(num))
    temp=num
    arm_num = 0
    while(num>0):
        last_digit = num%10
        arm_num = arm_num+last_digit**power
        num = num//10

    if(temp == arm_num):
        print("It is a Armstrong Number",temp)

# ================================================================================
# name="123"
# print(len(name))