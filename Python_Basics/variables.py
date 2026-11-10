"""
================================== variables in python ======================================
=> These are the container for storing different data types values.
=> These are memory locations inside our computer RAM.

ROM :- Non-volatile (Bios)
RAM :- volatile (changable)

syntax:-
---------
variableName = value

To get value into output :
---------------------------
print(variableName)
OR
print("Message",variableName)

Rules for variable declaration :-
---------------------------------
1. Never start with number
ex:- 1Name ="Ram" X
ex:- Name1 = "Ram" --> valid

2. No space between Name 
ex:- first name ="Ram" X
ex:- firstName ="Ram" --> valid

3. No special symbol except Underscore(_)
ex:- first@name="Tarun" X
ex:- first_name="Tarun" valid

4. Variable Names are case-sensitive
ex:- Name="Ram"
Ex :- name="kanha"

HERE Name and name are two different variables.
Due to its ASCII(American Standard Code for Information Interchange) value.

A => 65
a => 97

chr(number) :- return ASCII character
ord("character") :- return ASCII NUMBER

5. No reserve-word OR keyword
ex :- def ="user" X
ex:- Def ="user" Valid

NOTE :- There are 35 keywords 

from keyword import kwlist
print(len(kwlist))

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
'raise', 'return', 'try', 'while', 'with', 'yield']
"""

name="Raman singh"
age=21
address = "mathura"

# print("My age is : ",age)

name1="Ram"

lastName ="Singh"
# print(lastName)

# print(chr(128519))
# print(ord("A"))
