"""
conditional statement :
-------------------------
Main Types of Conditional Statements

if statement: The simplest form, executing a block of code if a specified condition is true.
-------------

if-else statement: Executes one block if the condition is true and another block (the else block) if it is false.
------------------

if-elif-else chain: Used to check multiple conditions sequentially. 
------------------- Python executes only the first block whose condition is true and skips the rest.


Nested if statements: An if or if-else statement placed inside another if block to check for further conditions.
----------------------

Ternary Operator (Conditional Expression): A compact, one-line version of if-else typically used for variable assignment 
----------------------------------------- (e.g., x = "true" if condition else "false").

"""

# age=17
# result = ("You can Vote")if(age>=18) else("You can not Vote")
# print(result)

#* =======================================================================================================================
'''
NOTE :- Python is Indentation based (Use tab space for run a block[if-else , loop , functions , filehandling,...].)
If we have more than two conditions :
-------------------------------------
if(condition):
    statement1
elif(condition):
    statement2
elif(condition):
    statement3
elif(condition):
    statement4
...
else:
    last statement


python
c,c++
js
php
react
node.js
express.js

------------------------------------------------
1. On the basis of their Syntax
=> statically typed :- describe in details => data type , add semicolon ,...
=> Dynamically Typed :- No need to declare data type :- python , js(frontEnd , backEnd(Node, express))

2. On the basis of Code execution
=> Interpreter based
=> Compiler Based 

front end :- html , css(bootstrap,tailbind css,..) , js(React.js)
back end :- python(Django,Flask) , Php , JS(Node.js + Express.js)
'''


# =============================================================================================================
#* Swap two numbers
"""
num1 = 20
num2 = 10

print(num1) ===> 10
print(num2) ===> 20

There are two ways to swap two values :
----------------------------------------
1. using a temporary variable
"""

n1 = 20
n2 = 10

#* 1. using a temporary variable
"""
temp = n1 # 20
n1 = n2 # 10
n2 = temp # 20
"""
#* 1. Without creating a temporary variable
# n1,n2 = n2 , n1
# print("N1 : ",n1)
# print("N2 : ",n2)


#^ find data type of a variable
a = "hello"
# print(type(a))

#^ 5. Convert temperature from Celsius to Fahrenheit
"""
=> celcius TO fehrenhite :- 
f = (9/5) * celcius + 32

=> fehrenhite TO celcius :- 
c = (feh - 32) * 5/9
"""

c = 10
f = (9/5) * c + 32
# print(f)
# B(bracket)O(open)D(division)M(multiplication)A(Addition)S(substraction)


# print(20+5*2/5-10)
"""
20+10/5-10
20+2.0-10
22.0 - 10
=> 12.0
"""
"""
OPERATOR PRECEDENCE ORDER :- PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)
----------------------------
1. () => Parenthesis 
2. ** => exponential
3. * , / , // , % 
4. +, - 

"""

"""
* ====================== user input in python ==========================
To take value from user we use input() function.

syntax:
--------
^=> This will take String value from user
*variabelName = input('Message')

^ Take Integer value from user => int() ------> Type-casting (Conversion of one data type to another data type)
* variableName = int(input("Message"))

^ Take Float value from User => float()
*variableName = float(input("Message"))
"""

# name = input("Enter Your Name : ")

# age = int(input("Enter Your Age : "))

# print("The entered Name is : ",name)
# print("The entered Age is : ",type(age))

# n1 = float(input("Enter Num1 : "))
# n2 = float(input("Enter Num2 : "))

# sum = n1+n2
# print("the sum is : ",sum)

#& Convert temperature from Celsius to Fahrenheit
# celcius = float(input("Enter tempreture in Celcius : "))
# feh = (9/5)*celcius+32
# print("In Fehrenhite : ",feh)

#& Perform all arithmetic operations between two numbers 
"""
Take 3 things from user
1. num1
2. num2
3. Operator (+,-,/,*,%,//,**)
"""


"""
num1 = float(input("Enter num1 : "))
num2 = float(input("Enter num2 : "))
operator = input("Enter your Operator (+,-,/,*,//,** OR %) : ")

if(operator == "+"):
    sum = num1+num2
    print("The sum is : ",sum)
elif(operator == '-'):
    sub = num1 - num2
    print("The substraction is : ",sub)
elif(operator == "*"):
    mul = num1*num2
    print("The multiplication is: ",mul)
elif(operator=="/"):
    div = num1 / num2
    print("The division of num1 with num2 is : ",div)
elif(operator=="//"):
    floor = num1//num2
    print("The floor division of num1 with num2 is : ",floor)
elif(operator=="**"):
    exp = num1**num2
    print("The power of num1 with respect to num2 is : ",exp)
else:
    print("Invalid operator.....")

"""
# year = int(input("Enter year : "))

# check_for_leap_year = ("It is a leap Year")if((year%4==0 or year%400==0) and( year%100!=0)) else("It is not a leap Year")
# print(check_for_leap_year)
