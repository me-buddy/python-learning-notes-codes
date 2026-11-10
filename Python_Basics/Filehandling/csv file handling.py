"""
================================= CSV(Comma Seperated Values) ================================
First we have to "import csv" module and then -

To work with csv files we have to create two objects :
------------------------------------------------------
1. reader object
2. writer object

-------------------- reader object ---------------------------
reader_obj = csv.reader(filehandler) :- return a list of values which also stored inside the lists.
dict_reader_obj = csv.DictReader(filehandler) :- return a list of values which stored inside the dictionaries.

-------------------- writer object ---------------------------
writer_obj = csv.writer(filehandler)

NOTE : in csv files we can write data row-wise , for this we have to functions:-
       1 => writer_obj.writerow(list/tuple)  => To insert single row data into the file.
       2 => writer_obj.writerows(list[list]/tuple(tuple))  => To insert multiple rows data into the file.

   
dict_writer_obj = csv.DictWriter(filehandler,fieldnames = fieldnames)

 => dict_writer_obj.writerows([{key:value,key:value,...},{key:value,key:value,...},{key:value,key:value,...},...]
           = Used to insert the list of dictionaries inside the csv file.
"""

import csv
"""
file = open("salary.csv","r")

# reader = csv.reader(file) # return a list of values which also stored inside the lists.
# print(reader) # <_csv.reader object at 0x00000199805B8940>

# print(type(reader)) # <class '_csv.reader'>



# for row in reader:
#     for col in row:
#         print(f"{col} |" ,end=" ")
#     print()

reader = csv.DictReader(file) # return a list of values which also stored inside the lists.
for i in reader:
    print(i)

file.close()

"""

#! NOTE :- By default it insert records after 1 row , To insert records without escaping any row we have to write 
#!         inside open function  - newline=""

file = open("salary.csv","r",newline="")


# We have to create a writer object , through this object we write data into the csv file.
writer_obj = csv.writer(file)
#* single row inserted into csv file
# * ---------------------------------------------------------------
# writer_obj.writerow(["Suman",56926,46166,10269,50566,38845,24251,98517,80840,68102,72694,44545,25611])


#* multiple row are insrted into the file
# * ---------------------------------------------------------------
records = [
    ["Aarav", 120, 135, 142, 150, 160, 170, 180, 175, 165, 155, 145, 130],
    ["Priya", 98, 105, 110, 120, 125, 130, 128, 122, 118, 115, 108, 100],
    ["Rahul", 200, 210, 220, 230, 240, 250, 260, 255, 245, 235, 225, 215],
    ["Sneha", 75, 80, 85, 90, 95, 100, 105, 102, 98, 92, 88, 82],
    ["Vikram", 150, 155, 160, 170, 180, 190, 200, 195, 185, 175, 165, 155]
]

# writer_obj.writerows(records)

# * Write records in the form of list of dictionaries.
# * ---------------------------------------------------------------


records_to_insert = [
    {
        "NAME": "Ananya",
        "JAN": 110, "FEB": 115, "MAR": 120, "APR": 125,
        "MAY": 130, "JUN": 135, "JUL": 140, "AUG": 138,
        "SEP": 132, "OCT": 128, "NOV": 122, "DEC": 118
    },
    {
        "NAME": "Rohan",
        "JAN": 95, "FEB": 100, "MAR": 105, "APR": 110,
        "MAY": 115, "JUN": 120, "JUL": 125, "AUG": 123,
        "SEP": 119, "OCT": 114, "NOV": 108, "DEC": 102
    },
    {
        "NAME": "Kavya",
        "JAN": 180, "FEB": 185, "MAR": 190, "APR": 200,
        "MAY": 210, "JUN": 220, "JUL": 230, "AUG": 225,
        "SEP": 218, "OCT": 212, "NOV": 205, "DEC": 195
    },
    {
        "NAME": "Arjun",
        "JAN": 70, "FEB": 75, "MAR": 80, "APR": 85,
        "MAY": 90, "JUN": 95, "JUL": 100, "AUG": 98,
        "SEP": 94, "OCT": 89, "NOV": 84, "DEC": 78
    },
    {
        "NAME": "Meera",
        "JAN": 140, "FEB": 145, "MAR": 150, "APR": 155,
        "MAY": 160, "JUN": 165, "JUL": 170, "AUG": 168,
        "SEP": 162, "OCT": 158, "NOV": 152, "DEC": 148
    }
]
fieldnames = [
    "NAME", "JAN", "FEB", "MAR", "APR", "MAY", "JUN",
    "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"
]

# dict_writer_obj = csv.DictWriter(file,fieldnames=fieldnames)
# dict_writer_obj.writeheader() #=> This function is used to write header row inside the csv file.
# dict_writer_obj.writerows(records_to_insert)

# print("Record Inserted Successfully....")


read_data = csv.reader(file)

for i in read_data:
    for j in i:
        print(j,end="\t")
    print()
file.close()