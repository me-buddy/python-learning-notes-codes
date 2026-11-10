"""
=============================== Data types In python ===================================
=> Variables are containers for storing different kinds of data type.

variableName = value

NOTE : To get data type we use :- type(value/variableName)
ex:-
----
age = 21 
print(type(age)) => <class 'int'>

=========================================================================================
* int :- It contains whole number values(-num , +num)
ex:- 21,3423,54,65,-87,98,0

* float :- It contains decimal values.
ex:- 32.54, .76 , -65.7

* complex number :- A number with imaginary part.
# complex number => realPart + ImaginaryPart
                => 56(real) + 67j(imaginary)
ex:- 45+7j
NOTE :- Only 'j' or 'J' is allowed as imaginary part

* string :- It is a set of characters inclosed in single , double or triple inverted(Multi-line String) commas.
ex:- name = "tanay"  => <class 'str'>

* Boolean :- It contains two values 'True' and 'False'

* None :- It is used to represents Nothing

^------------ collection Data types ----------------
There are 4 main collection data types -> These are used to store multiple value in a single variable.

Mutable(changable) OR Immutable (Not Changable)
Oredred(Access by Index No) OR Unordered (No Indexing)
Allow Duplicates OR not Allow Duplicates
*1. list :- Values are stored inside square brackets with comma seperated
         => Mutable , Allow Duplicates , Ordered

ex:- user_record = ["Ram",21,"Mathura",True]
                OR
ex:- user_record = []

*2. tuple :- values are stored inside parenthesis with comma seperated
        => Immutable , Ordered , Allow Duplicates

ex:- user_record = ("Ram",21,"Mathura",True)
                OR
ex:- user_record = ("Ram",)
                OR
ex:- user_record = "Ram",
                OR
ex:- user_record = ()

*3. set :- values are stored inside curly-brackets with comma seperated values.
        => Mutable , UnOrdered , Not allow Duplicates

ex:- nums = {21,32,43,54,65,21}
            OR
ex:- nums = {21}

*4. dictionary - It stores values inside curly brackets with key and value pairs.
=> Mutable , Not Allow duplicate Keys , Unordered
^ syntax:- dictionaryName = {key:value , key:value , key:value ,...}
ex:- user = {"Name":"Ram" , "Age":21 , "Address":"Mathura"}
ex:- user = {}


"""
num = 21 #<class 'int'>
num = 21.7 # <class 'float'>
cmplx = 54J # <class 'complex'>
# print(type(cmplx))

c1 = 21+6j
c2 = 20+4j
# print(c1+c2)
name = "Raju" # single line string

# Multi-line String
a="""ram 
                                singh"""
# print(type(a))
# print(a)

isAvailable = False # <class 'bool'>
# print(type(isAvailable))

Any_degree = None # <class 'NoneType'>
# print(type(Any_degree))

user_record = ["Ram",21,"Mathura",True] # <class 'list'>

user_record = ("Ram",21,"Mathura",True) # <class 'tuple'>

user_record = "ram",


# print(type(user_record))


nums = {21,34,54,65,78,98,"Fourty",True}
nums = {21}
# print(type(nums))

user = {} # <class 'dict'>
user = {"Name":"Ram" , "Age":21 , "Address":"Mathura"} # <class 'dict'>

# print(type(user))


lst = [21,32,45,3,65,87,98]
print(lst[2])
