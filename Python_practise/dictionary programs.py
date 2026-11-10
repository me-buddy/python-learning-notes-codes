"""
144. Difference between key and value.
*1. keys are unique and values can be duplicates
*2. list can not be used as a key ,but tuple is allowed as keys

146. Write a program to delete key from dictionary.
* dct.pop(key)

147. Explain dictionary comprehension.
* {key:value for key in range(start,end)}

148. Write a program to merge two dictionaries.
* dct1.update(dct2)

149. Write a program to check if key exists.
*if("a" in dct1):
*    print("Present")
*else:
*    print("Not present")

150. Difference between get() and direct access.
151. Write a program to count frequency of characters in string using dictionary.
152. Write a program to convert two lists into dictionary.
153. Write a program to find max and min key in dictionary.
154. Explain nested dictionary.
155. Write a program to sort dictionary by keys.
156. Write a program to sort dictionary by values.
157. Difference between shallow copy and deep copy in dict.
158. What is items() in dictionary?
159. Write a program to swap keys and values in dictionary.
160. What happens if we use unhashable object as key?
"""

lst = [i for i in range(1,11) if(i%2!=0)]
tpl = (i for i in range(1,11))
st = {i for i in range(1,11)}

squares_dct = {i:i**2 for i in range(1,11)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# print(squares_dct)

user = ["Ram","Shyam","Karan"]
marks = [89,78,57]
# {"Ram":89 , "shyam":78, "karan":57}

dct = { i:j for i,j in zip(user,marks)}

# print(dct)

zp = zip(user,marks)
# print(zp) # <zip object at 0x000001F82CA4A080>
# We have to iterate the zip object

# for i,j in zp:
#     print(i,j)

dct1 = {"a":1,"b":2,"c":3}
dct2 = {"x":101,"y":102}



#* 151. Write a program to count frequency of characters in string using dictionary.
st = "hello"
# {"h":1,"e":1,"l":2,"o":1}
# print(st.count("l"))
# dct={}
# for i in st:
#     dct[i] = st.count(i)
#! OR
dct={i:st.count(i) for i in st}

# print(dct)

#* 152. Write a program to convert two lists into dictionary.

user = ["Ram","Shyam","Karan"]
marks = [89,78,57]
dct = {}

# for i in range(len(user)):
#     dct[user[i]] = marks[i]
# print(dct)
#! OR
# for key,value in zip(user,marks):
#     dct[key] = value

# print(dct)


#* 153. Write a program to find max and min key in dictionary.

# dct = {1:10,2:30,3:20,4:100,5:-21}
# min=min(dct.values())
# max=max(dct.values())
# for i in dct:
#     if(dct[i]==min):
#         print(i,min)
#     if(dct[i]==max):
#         print(i,max)     


dct = {-1:10,2:30,3:20,4:100,5:-21,-10:39,9:389}

keys = dct.keys()
values = dct.values()
# print(type(keys)) # <class 'dict_keys'>
# print(type(values)) # <class 'dict_values'>

keys_list = sorted(list(keys))
values_list = sorted(list(values))

dct_sort_by_key = {}
dct_sort_by_value = {}

# here we have to get value from dictionary by its key
for i in keys_list:
    dct_sort_by_key[i] = dct[i]

# print(dct_sort_by_key)

# here we have to get key from dictionary by its value
for i in range(len(values_list)):
    for key in dct:
        if(dct[key] == values_list[i]):
            dct_sort_by_value[key] = values_list[i]
            break

# print(dct_sort_by_value)


# *159. Write a program to swap keys and values in dictionary.
dct = {1:10 , 2:20 , 3:30 , 4:40 , 5:50}
dct2={}
"""
for key in dct:
    print("key : ",key)
    print("Value : ",dct[key])
    print("-----------------------")

    dct2[dct[key]] = key

print(dct2)

"""

# ============================== scope of a variable in functions ================================
"""
A variable have two scopes :
----------------------------
1. local scope :- A variable declared inside function body has local scope.
2. global scope :- A variable declared outside function body has global scope.

NOTE :- global variable can be used inside and outside the function.
        But local variable can only used inside function body , not outside function body.

We can convert local scope to global scope using 'global keyword'

"""
a=10

def add():
    global b
    b=20
    sum = a+b
    print(sum)

add()
print(a)
print(b)