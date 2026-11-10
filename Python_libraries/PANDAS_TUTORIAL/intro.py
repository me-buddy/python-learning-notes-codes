"""
1. read data
2. clean data 
3. sorting 
4. handling missing values
5. statistical operations
6. grouping records
7. merging dataFrames
8. report generation
9. Prepare for ML

--------------------------------
Machine Learing
----------------
Numpy => 
Pandas => Data Preprecessing
=> Data addregate
=> data cleaning
=> Merge different Files.
=> Statistical operations
=> To convert one format data into another format data(excel,csv,sql,json,etc..)


Matpltlib
Seaborn
--------
Scikit learn
NLTK
scipy
--------------------------
csv
excel
sql
websites
json
...
"""
import numpy as np
import pandas as pd
# print(pd.__version__) # 3.0.3

"""
Pandas Data-Struture :- Representation of data through Pandas.
-----------------------
1. Series :- Single dimensional List/array.
=> pd.Series(list/tuple/dictionary)

2. DataFrame :- Represents data in tabular format.
=> pd.dataFrame(multi-dimensional list / nested dictioanary)

"""
lst = [[1,2],[10,20],[40,50]]
ar = np.array([[1,2],[10,20],[40,50]])
# print(lst)
# print(ar)

names = ["Ram","Rahul","Raj","Mohan","Omprakash","Kanha"]
marks = [89,43,54,65,76,87]
# series = pd.Series(marks,index=names)
# print(series) # <class 'pandas.Series'>


# series = pd.Series({"Name":"Ram","Age":"22","Address":"Mathura"})
# print(series)


dataframe = pd.DataFrame([[1,"Ram"],[10,"Shyam"],[40,"Tarun"]],columns=["Id","Names"])
# print(dataframe)


data = { "Name": ["Alice", "Bob", "Charlie"],
    	"Age"  : [25, 30, 35], 
   	    "City" : ["New York", "Los Angeles", "Chicago"] }
df = pd.DataFrame(data)
print(df)
