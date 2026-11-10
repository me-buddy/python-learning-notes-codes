"""
====================================== Binary File handling =======================================
=> A file with non-human redable format.

A binary file contains :-
--------------------------
=> .bin
=> image (.jpg/.png/.gif/.webp/etc...)
=> audio file => fileName.mp3
=> video file => fileName.mp4
=> pdf(Portable Document Format)
=> executables files => .exe

===================================================================================================
syntax:-
--------
fileHandler = open("fileName.extension","rb")
statement
fileHandler.close()
!OR
with open("fileName.extension","mode") as fileHandler:
    statement

Modes of Binary files :-
-------------------------
rb OR r+b
wb 
ab
xb
---------
rb+ => read + write
wb+ => write + read
ap+ => append + read

"""


"""
data = b"hello world" # convert string into byte stream

# f = open("binary_file.bin","wb")
# f.write(data)

f = open("binary_file.bin","rb")
value = f.read(4)
# print(value) # b'hello world'
print(value)
f.close()

"""

#* ============================ pickle Module ======================================
# This module is used to handle python objects(list / tuple / set / dictionary....)

# ^ extension :- fileName.dat
"""
step1 :- import pickle module
=> import pickle

&Write data into the file
=> pickle.dump(data , fileHandler)

&Read data from the file
=> pickle.load(fileHandler)


"""
import pickle

user = {
    "Name":"kiran",
    "Age" :21,
    "Address" : "Kanpur",
    "Marks" : 90.32
}

#! write data into the file
# with open("Records.dat","wb") as file:
#     pickle.dump(user,file)
#     print("Data inserted successfully...")


#! read data from the file

with open("Records.dat","r+b") as file:
    user_data = pickle.load(file)
    # print(user_data)

#* NOTE : read(copy) an image and write(paste) into another file   
"""
with open("nature.jpg","rb") as image_file:
    img = image_file.read()

with open("nature2.jpg","wb") as file:
    file.write(img)

"""

#^ ======================== pillow module ====================================
# This module is dedicated for working with images 

# First we have to install pillow module => pip install pillow

from PIL import Image
img = Image.open("nature.jpg")
# img.show()
img2 = img.resize((400,400))
# img2 = img.crop((100,200,300,400))
# img2 = img.rotate(180)
# print(img2)

# img2.show()


from pypdf import PdfReader
reader = PdfReader("pdo.pdf")
# print(len(reader.pages))

# Extract text from the very first page (index 0)
# first_page = reader.pages[1]
# text = first_page.extract_text()

# print(text)

for pages in reader.pages:
    print(pages.extract_text())
    print("\n===========================================================================\n")

#* ===============================================
# import math
# import math as m
# from math import *
# print(floor(21.32))