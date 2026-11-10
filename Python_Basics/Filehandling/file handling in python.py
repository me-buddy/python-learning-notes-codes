"""
======================================= File Handling ========================================
Through file handling we can create a file , write data into the file , read data from file 
and also can handle Operating System.

here we handle 3 types of files :-
----------------------------------
1. text files :- file with extensition .txt called text files.
2. csv files  :- csv stands for Comma Seperated values , Here we handle excel files.
3. binary files :- File that has Non-textual format data. Image files , audio , video , etc.

==================================== text file handling ======================================
syntax:-
--------

fileHandler = open("fileName.txt","mode")
statements
filehandler.close()

Types of Modes :-
-----------------
r ---> read Mode
w ---> write Mode (NOTE: It Overwrite the existing data)
a ---> append Mode(write) (NOTE : add new data at the end of the file)
x ---> create Mode :- Used to create a New File.

r+ ---> read + write Mode
w+ ---> write + read
a+ ---> Append + read

! NOTE :- w mode can create an empty file if file is Not Exist.


& ~~~~~~~~~~~~~~~~~~ Write Data Into the file ~~~~~~~~~~~~~~~~~~~~~~~~
SYNTAX:- fileHandler.function()

* .write("data") :- Used to write data into the file.
* .writelines(list/tuple) :- Used to write list or tuple data into the file.
"""

ai = """
Artificial Intelligence (AI) is the broad branch of computer science focused on building systems
capable of mimicking human intelligence to perform tasks like reasoning and problem-solving. 
Machine Learning (ML) is a vital subset of AI that autonomously identifies data patterns, 
allowing machines to improve from experience without explicit, hard-coded programming
"""
ai_ml_types = ["\nMachine Learning","Deep Learning","Supervised Learning","Unsupervised Learning","Reinforcement Learning","Natural Language Processing","Computer Vision","Generative AI","Neural Networks","Transfer Learning","Federated Learning","Explainable AI","Robotics","Expert Systems","Evolutionary Algorithms"]

"""
file = open("user_records.txt","a")
# file.write("\nhello world")

# file.write(f"\n{ai}")
for line in ai_ml_types:
    file.write(f"\n=>{line}")


# file.writelines(ai_ml_types)
file.close()

"""


"""
===============================Data Science============================
* Advance Excel 
* Dasboard creation :- PowerBi and Teblu
* programming language => Python Or R language
* database => MySql and Python connectivity with Mysql
* Advance Python :- 
    => Numpy
    => Pandas
    => Matplotlib
    => seaborn
* machine learning => scikit learn , NLTK
"""


# ================================= Read Data from File =================================================
"""
1. .read() :- Default Used to read entire file data.
OR
1. .read(n) :- Used to read n number of characters data from file.

2. .readline() :- Used to read first line from file.
3. .readlines() :- Used to read all lines data from file and return in the form of list.
"""
f = open("user_records.txt","r+")
# data = f.read()
# data = f.read(10)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# data  = f.readline()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
data  = f.readlines()
# print(data)

# for line in data:
#     print(line)
f.close()