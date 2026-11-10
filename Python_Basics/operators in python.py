"""
================================ Operators in Python ==================================
Operators are some special symbols used to perform some specific operations.

*1.Arithematic operators :- + , - , * , /(return float value) , %(Modulas[Remainder find]) , // (floor division [return integer]), **(exponential[power])
# print(13//3) # 4
# print(12/3) 4.0
# print(2**5) 32

& 2.Assignment operator :-  = (Assignment Operator) , +=  , -= , *= , /= , //= , %= , **=        
a += 20 # a = a+20
b-=2 # b=b-2 => b = 20-2 => b=18

^ Relational/Comparision Operators :- Used to compare "two values" and return boolean value (True/False), it create a condition
  >(greater than) , < , == (isEqual to), >= (greater than OR equal to) , <= , != (Not Equal to)
# print(a>b) # False
# print(a<b) # True
# print(a==b) # False
# print(a>=b) # False
# print(a<=b) # True
# print(a!=b) # True

* Logical Operators :- Used to compare "two conditions" and return boolean Value(True/False)
syntax:- (condition1) logicalOperator (condition2)
There are three logical operators :-
------------------------------------
1. and :- It return True if Both conditions are True , return False if either one OR both conditions are False.
2. or :- It return True if either one condition is True , It return False if Both conditions are False.
3. not :- It reverse the condition. not (True) => False , not(False) => True
EX:-
----
a=10
b=20
c=a+b
# print("Sum is : ",c)
# print(b)

num1 = 5
num2 = 8
num3 = 10

result1 = (num1>num2) and (num1<num3) # False
result1 = (num1<num2) and (num1>num3) # False
result1 = (num1<num2) and (num1<num3) # True

result2 = (num1>num2) or (num1<num3) # True
result2 = (num1<num2) or (num1>num3) # True
result2 = (num1>num2) or (num1>num3) # False

result3 = not (num1<num2) # False
result3 = not (num1>num2) # True
print(result3)

^5. Membership Operators :- in , not in
These are used to check membership of a value , from a list/tuple/set/dictionary OR String 
EX: 
users = ["Ram","Shyam","Karan","Jatin"]

# print("Ram"  in  users) # True
# print("Tarun"  in  users) # False
# print("Tarun"  not in  users) # True

st = "ram singh"
print("r" in st) # True
print("R" in st) # False

!6. Identity operators :- is , is not
a=10
b=10

a=10 # integer
b="10" # string

# print(a==b) # False
# print(a is b) # False

& Bitwise operators :- These Are used to perform operations in between two bits.
 => & (bitwise And)
 => | (bitwise or)
 => ~ (bitwise not)
 => ^ (bitwise XOR)
 => >> (bitwise right shift)
 => << (bitwise left shift)

! Ternary operator :- It is a single line conditional statement.
syntax:- (true statement) if(condition) else (false statement)
--------
"""

# print(15 ^ 34)
# print(~-15)

# print(15>>2)
# print(123>>2)

# print(bin(125))
# print(125>>3)
# print(512+256+128+64+32+8)
# print(125<<3)

age = 21

vote  = ("You can Vote") if(age>=18) else ("You can not vote")
print(vote)