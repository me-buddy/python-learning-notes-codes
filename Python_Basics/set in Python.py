"""
====================================== set ========================================
Set Properties :
----------------
1. Set in Mutable
NOTE :- we can add some values OR remove some values ,BUT can not change inserted value.
2. Unordered
3. Not Allow Duplicate
4. Hetrogenious

syntax:-
---------
setName = set() ===> create an empty set
OR
setName = {1} 
setName = {1,} 
OR
setname = {value1 , value2 , value3 , .....}

* set is Iterable
for variableName in setName:
    statement...

! NOTE :- Set Does Not allow list as a value. , But allow Tuple

&=================== set functions ==================
=> len(setname) :- return the length of the set.
=> .add(value) :- To add a value into the set.
=> .remove(value) :- to remove a value from set. Return KeyError If value is Not Present in set
=> .discard(value) :- remove value from set. Return No Error  if value is Not present
=> .pop() :- It remove any random value from the set.
=> .clear() :- return an empty set.
=> del setName :- Remove set.

=> .copy() :- create a shallow copy of a set.

=> .union(set2Name) :- Used to combine two sets.
=> .intersection(set2Name) :- Return a set which contains Common Values from Both sets.

=> .difference(set2Name) :- return a set which contains different values from set2Name.
OR
=> set1 - set2 :- return a set which contains different values from set2Name.

=> set1.issubset(set2) :- Return True if set1 have all values which presents in set2, else return False
=> set1.issuperset(set2) :- Return True if set2 have all values which presents in set1, else return False


=> sorted(set) :- return a LIST and arraneg in Accending Order.
"""

st = {10,20,30,40,50,"hello"}
# print(type(st))
# st[0]=100 ==> TypeError
# print(st[0]) ==> TypeError

# for i in st:
#     print(i)

st.add(("Ram","Tarun"))
st.remove(10)

# print(len(st))

# st.clear() # set()
# del st
st2 = st.copy()
# print(st)
st.pop()
# print(st)



s1 = {10,20,30,40,50,60}
s2 = {10,20,90,80,59,60}

union = s1.union(s2)
intersection = s1.intersection(s2)
differnce =  s2.difference(s1)
differnce =  s2-s1

# print(union)

t1 = {10,20,30,324,-10,40,50,100}
t2 = {10,20,30}
# print(t2.issubset(t1))
# print(t1.issuperset(t2))



# t1.discard(100)
# t3 = sorted(t1) +> [-10, 10, 20, 30, 40, 50, 100, 324]
# print(t3)