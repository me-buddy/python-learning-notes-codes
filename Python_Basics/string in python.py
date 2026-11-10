"""
String :- It is a set of characters inclosed in single or double or triple inverted commas.
! NOTE :- String is IMMUTABLE(not changable),change will reflect in their COPY not Original.

! NOTE :- In string every character have an Index Number.Which starts from 0 and last in -1 index

Syntax:- strinName[startIndex : endIndex-1 : stepValue-1]

! NOTE :- String is Iterable(We can access string characters through for loop) 

Syntax:-
--------
stringName = "value"

for i in stringName:
    print(i)


There are two types of string :-
--------------------------------
1. single line string :- written inside inside single OR double inverted commas.
2. multi-line string :- written inside triple inverted commas. 
"""

a="hello"

user_info = '''
~~~~~~~~~~~~~~~~~~~~~
Name : Ram
---------------------
Age :21
---------------------
Address : Mathura
---------------------
PinCode : 28001
~~~~~~~~~~~~~~~~~~~~~

'''
# print(type(a))
# print(user_info)


name = "Harish Kumar"
# print(name)
# print(name[2]) => r
# print(name[-3]) => m

# print(name[0:5+1]) => Harish
# print(name[0 : 6 : 2]) => Hrs
# print(name[0 : 6 : 3]) => Hi

# print(name[2:]) => rish Kumar
# print(name[:6]) => Harish
# print(name[::2]) => Hrs ua

#^ To reverse a string
st = "hello"
# print(st[::-1])

#^ Take a string value from user and check whether a string is PALINDROME or NOT
# If we reverse a string and we get same meaning of that string it is called string Palindrome.
"""
ex:-
-----
sms => sms
kanak => kanak
malayalam => malayalam
ram => mar X
"""

# str = input("Enter any String : ")
# if(str == str[::-1]):
#     print(f"{str} is a Palindrome")
# else:
#     print(f"{str} is NOT a Palindrome")

# * number palindrome
# num=int(input("Enter any number: "))
# temp=num
# sum=0
# while num>0:
#     last_digit = num%10
#     sum = sum*10 + last_digit
#     num = num//10   
# print(sum)

# if(temp==sum):
#     print(f"{temp} is palindrome")
# else:
#     print(f"{temp} is not palindrome")


#* ============== Iterate Over a String ================

st = "I live in Mathura"

# for i in st:
#     print(i)

#^ count particular character in string
char = "a"
count = 0

for i in st:
    if(i==char):
        count+=1# count = count+1

# print(f"{char} count in string is {count}")

# ! =================================================================================================

#& =================================== String Built-In Functions ====================================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
-------------------------------------------------------
SYNTAX :- stringName.functionName()
-------------------------------------------------------
1. len(stringName) :- return the length of the string.

2 .upper(stringName) :- Convert all characters into upper-case
3 .lower(stringName) :- Convert all characters into lower-case
15 .title():- convert first character of every word into upper case

4 .capitalize(stringName) :- Convert first characters into upper-case and all remaining characters into lower case

5 .startswith("character") :- check whether a string is start with particular character, and return Boolean Value(True/False)
6 .endswith("character") :- check whether a string is ends with particular character, and return Boolean Value(True/False)

7 .split(splitValue) :- This will convert a string into A list
#^ NOTE :- default split value is space

8 " ".join(list) :- convert list to string

9 .lstrip() :- This function is used to remove all left hand side spaces from string.
10 .rstrip() :- This function is used to remove all right hand side spaces from string.
11 .strip() :- This function is used to remove all left and right hand side spaces from string.


12 .index("character/word") :- Return the index number of the first match of the given string/character/word

13 .count("character") :- return the count of the given character from string.

14 .format(st1,st2,st3,st4,..) :- used to format a string MEANS concat message with variables inside a invereted commas.

16 .replace("oldString" , "newString") :- replace old string with new string.

17 .isnumeric()
18 .isalpha()
19 .isalnum()
20 .isidentifier()
"""

st = "machine Learning"
# print(len(st)) => 16
# print(st.upper()) => MACHINE LEARNING

# print(st.lower()) => machine learning

# print(st.capitalize()) => Machine learning

# print(st.startswith("c")) # False
# print(st.endswith("g")) => True

a = st.split() # ['machine', 'Learning']
a = st.split("i") # ['mach', 'ne Learn', 'ng']
# print(a)

lst = ["Ram","is","a","good","boy"]
st = " ".join(lst) # Ram is a good boy
# print(st)


s1 = "       hello      "
s2 ="world"

# print(s1.lstrip(),s2)#hello       world
# print(s1.rstrip(),s2)#       hello world
# print(s1.strip(),)#hello world

st = "Hello world"

# print(st.index("world")) # 6

# print(st.count("e"))

x=10
y=20
sum = x+y
sub = x-y
mul = x*y

# print(f"The sum , difference OR multiplication of {x} and {y} is {sum} , {sub} , {mul}")
# .format()
# print("The sum , difference OR multiplication of {0} and {1} is {2} , {3}, {4}".format(x,y,sum,sub,mul))

st = "2132cd"
# print(type(st))

# print(st.isnumeric()) # False
# print(st.isalpha()) # False
# print(st.isalnum()) # True
st = "def@fv"
# print(st.isidentifier()) #False

st = "Ram singh live in mathura"
st2 = st.replace("Ram","Shyam") # Shyam singh
# print(st2)

print(st.title()) # Ram Singh Live In Mathura