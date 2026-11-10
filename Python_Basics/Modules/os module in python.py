"""
================================ OS (operating System) ====================================
import os

* we can create a folder(direcrtory)
* delete the folder
* rename the file
* get list of all files available in a directory(folder)
* Change working directory.
---------------------------------------------------------------------------------------------
* os.getcwd()
* os.mkdir() :- create an empty directory(folder)
* os.rmdir("address_of_directory") :- It is used to remove any directory from computer
NOTE:- Remove ONLY EMPTY Folders
^ To remove Non-Empty Folder :-
^ import shutil ======> shutil.rmtree("address_of_directory")

* os.listdirs("address_of_directory") => return a list of all files and subfolders in the current working diretory.

* os.rename("oldName","NewName") :- Used to rename the folder and also rename the file

~~~~~~~~~~~~~~~~~~~~~~~
* os.path.exists("file/folderName") :- return boolean value(True/False) for given file and folder.
* os.path.relpath("complete_address") :- return file name from complete address.
* os.path.dirname("complete_address") :- return folder address  from complete address.
* os.path.split("complete_address") :- return a tuple of folder address and file names.
"""

import os
import shutil
# * return current working directory(cwd)
# print(os.getcwd()) # C:\Users\sagar\Desktop\shreyas AIML
# os.mkdir("Users")

# os.rmdir("Users") # OSError
# os.rmdir(r"C:\Users\sagar\Desktop\Records")

# shutil.rmtree("Users")

list_of_all_files = os.listdir()
# print(list_of_all_files)

# for file in list_of_all_files:
#     print(file)

# for file in os.listdir(r"C:\Users\sagar\Desktop\boby,pawan , Prachi,Shankar python course"):
#     print(file)

# os.rename("Users","USERS")

# os.rename("pdo.pdf","pdo_php.pdf")

# print(os.getenv("VARIABLE_NAME"))

# print(os.path.exists("pdo_php.pdf"))
"""
if(os.path.exists("customer.txt")):
    with open("customers.txt","r") as f:
        data = f.read()
        print(data)

else:
    with open("customer.txt","w") as f:
        f.write("File is created")
    print("File Created Successfully......")

"""

size = os.path.getsize("customers.txt") # by default it return value in the form of bytes.
# print("File Size in KB",(size/1024)) 
# print("File Size in MB",(size/1024)/1024)


# print(os.path.relpath(r"C:\Users\sagar\Desktop\shreyas AIML\customers.txt"))
# print(os.path.split(r"C:\Users\sagar\Desktop\shreyas AIML\customers.txt")) # ('C:\\Users\\sagar\\Desktop\\shreyas AIML', 'customers.txt')

# os.path.join("USERS","Data","customer.txt")
# print("File Joined")

# print(os.path.dirname(r"C:\Users\sagar\Desktop\shreyas AIML\customer.txt"))


for root, dirs, files in os.walk(r'C:\Users\sagar\Desktop\shreyas AIML'):
    print(f"Current Folder: {root}")
    print(f"Subfolders inside it: {dirs}")
    print(f"Files inside it: {files}")