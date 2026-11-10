"""
========================== random module ===============================
it is used to work with random values.

* .random() :- It generates random floating values from 0 to 1.
* .uniform(start,end) :- generate random floating values in a range.
* .randrange(start,end) :- generate random integer values from start to end
NOTE :- It does not include ending value.
* .randint(start,end) :- generate random integer values from start to end
NOTE :- It includes ending value.

* .choice(string/list/tuple/set) :- It is used to pick any random values from collection

* .shuffle(list/tuple) :- It regenerate a new order of all elements on each run.

* .sample(range/list/tuple/string,n) :- It is used to generate a list of random samples from given range/list/tuple.
"""
import random

# print(random.random())
# print(random.randrange(1,5))
# print(random.randint(1000,9999))

lst = ["Ram","Shyam","Karan","Boby","Nitin"]

# print(random.choice(lst))
# print(random.choice("Hello"))
"""
values = ["a","b","c","1","2","3","4",'#',"%","&"]
captcha=[]
for i in range(4):
    captcha.append(random.choice(values))

st=" ".join(captcha)    
print(st)
"""


# random.seed(4)
# random.shuffle(lst)
# print(lst)

# print(random.uniform(1,5))


# ================================================================
# number Guess Game

"""
point=0

for i in range(1,5+1):
    print("Round : ",i)
    print("--------------------")
    generated_num = random.randint(1,10)
    user_num = int(input(f"Guess {i} number : "))

    print(f"Computer genererated Number is : {generated_num}\n")
    if(generated_num == user_num):
        point+=1

print("\n-------------------------------------")
print("Your Score out of 5 is : ",point)
print("-------------------------------------")
"""

# 2. Rock, Paper, Scissors Game
"""
rock , paper => paper
paper , scissor => scissor
scissor,rock => rock
"""

'''
choices = ["Rock","Paper","Scissor"]

computer_choice = random.choice(choices)
user_choice = input("""
Choose One of them :-
---------------------
=> Rock
=> Paper
=> Scissor
~~~~~~~~~~~~~~~~~~~~~
=> """).capitalize()

print("\nComputer Choose : ",computer_choice)

computer_score=0
user_score = 0
if(computer_choice == "Paper" and user_choice == "Rock"):
    print("\nComputer Wins")
elif(computer_choice=="Scissor" and user_choice == "Paper"):
    print("\nComputer Wins")
elif(computer_choice == "Rock" and user_choice == "Scissor"):
    print("\nComputer Wins")
elif(computer_choice == user_choice):
    print("\nMatch Draw")
else:
    print("\nUser Wins")

'''


# print(random.sample(range(10,20),5))
# print(random.sample(["Ram","Shyam","Karan","Boby","Nitin"],3)) # ['Karan', 'Shyam', 'Ram']