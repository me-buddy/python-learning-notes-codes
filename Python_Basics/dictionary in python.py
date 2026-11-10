"""
============================ dictionary in python ===============================
These are used to store data in the form of key and value pairs in curly brackets.

syntax:-
---------
dictionaryName = {}
OR
dictionaryName = {key:value , key:value , ....}

To get particular value from dictionary :
------------------------------------------
dictionaryName[key] ===> return value 

=> Dictionary is Mutable(changable)
=> Dictionary is Unordered => There is no indexing
=> Not allow Duplicate keys :- It updates previous key with last inserted duplicate key and value.
=> Dictionary is Hetrogenious.

Dictionary is Iterable :- We can loop through the dictionary.

syntax:
--------
~ This loop return all keys 
for key in dictionaryName:
    print(key)

~ This loop return all values
for key in dictionaryName:
    print(dictionaryName[key])


Check particular key in dictionary :
--------------------------------------
key in dictionaryName :-- Return True if present else return False
"""

user_records = {"Name":"Ram" , "Age":21 ,"Roll No.":1012 ,"Marks":[32,54,65,76,43],"Age":28}
# print(user_records)
user_records["Name"] = "Karan"
# print(user_records["Name"])

# for key in user_records:
#     print(key ,"-", user_records[key])

# print("Address" in user_records) # False

sum_marks  = sum(user_records["Marks"])
# print(sum_marks)


"""
=========================== dictionary Methods ============================
* len(dictionaryName) :- return the length of the dictionary

* .keys() :- return a list of all keys from dictionary
* .values() :- return a list of all values from dictionary

* .items() :- Return a list of tuple which contains all key and values.

* .get(key) :- Return the value of the given key.
NOTE :- If key is Not present it return None , Not Error(KeyError)

* .update(dictionary) :- Merge two dictionaries

---------------------- remove methods ------------------------
* .pop(key) :- Used to remove particular key and value pair.

* .popitem() :- Used to remove last key and value pair.

* .clear() :- return an empty dictionary

* del dictionaryName :- Delete the dictionary.

---------------------- other methods --------------------------
* .copy() :- Creates a Shallow copy.
"""

# print(len(user_records))

keys = user_records.keys()
values = user_records.values()

items = user_records.items()

# print(keys) # dict_keys(['Name', 'Age', 'Roll No.', 'Marks'])
# print(values) # dict_values(['Karan', 28, 1012, [32, 54, 65, 76, 43]])

# print(items) # dict_items([('Name', 'Karan'), ('Age', 28), ('Roll No.', 1012), ('Marks', [32, 54, 65, 76, 43])])

# -------------------------------------------------
# for key,value in user_records.items():
#     print(key , value)
# -------------------------------------------------


# print(user_records.get("Address")) => return None
# print(user_records["Address"]) => return KeyError

# ============= add new key and value pair ==============
user_records["Address"] = "Mathura"

user_records.update({"pnCode":219073})

# print(user_records)

dct1 = {"a":1,"b":2,"c":3}
dct2 = {"x":101,"y":102}

dct1.update(dct2)
# print(dct1)

# ----------------------------
# key= input("Enter key you want to remove :")
# if(key in user_records):
#     user_records.pop(key)
# else:
#     print("Given key is Not Available")
# ----------------------------

# user_records.pop(key)
# user_records.popitem()
# ----------------------------

# user_records.clear() # {}
# ----------------------------

# del user_records
# print(user_records) # NameError

dct1 = {"a":1,"b":2,"c":3}

dct2 = dct1 # deep Copy
dct2 = dct1.copy() # shallow Copy

dct2.update({"x":200})
print(dct1)