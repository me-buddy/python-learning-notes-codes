"""
Connect Python with Mysql :- mysql-connector-python 
-------------------------
pip install mysql-connector-python

NOTE :- When we connect mysql and python we requires a server.
        For providing server, we convert our PC into a server.
        We install XAMPP , this convert Our PC into a Server.

        Inside Xampp start apache and mysql manually.
        If mysql is not start => go to services button and right click on mysql and stop mysql.

Apache Port number => 80443
Mysql Port Number => 3306

Browser => localhost/phpmyadmin ====> It is used to create databases and tables , also store tables records

localhost Address => 127.0.0.1 
=================================================================================================================

import mysql.connector

step1 :- We have to create a connection.
--------
#connection Object
conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="databaseName"
        )

step2 :- Create a Cursor
--------
It is used to execute mysql queries in python.
Cursor Object is created by Connection Object.

cursor = conn.cursor()

=> mysql.connector.connect()
=> connection.cursor()
=> cursor.execute("mysql Query")

====================================================================================
Creating => database , table
read => from table
update
delete 

====================================================================================
.execute("sql_query",value) :- It can insert one value at a time.
.executemany("sql_query",value) :- It can insert multiple records into a table.
.fetchone() :- To get first record from table
.fetchall() :- To get all record from table
.commit() :- To insert records forcefully into the table.
====================================================================================
"""

import mysql.connector

#* creating a connection
connection = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="",
    database = "sreyas"
)
# print(type(connection)) # <class 'mysql.connector.connection.MySQLConnection'>

    
#* creating a cursor 
cursor = connection.cursor() # <class 'mysql.connector.cursor.MySQLCursor'>

#* select Query 
# cursor.execute("Select * from practice")
# row = cursor.fetchall()

# for records in row:
#     for record in records:
#         print(record,end="\t")
#     print("\n-------------------------------------------")

#* Insert Query 
#! NOTE :- single record values should be in a tuple/list
#! NOTE :- multiple records values should be in a nested list OR nested tuple.
#! NOTE :- After insert/update/delete records query we have to commit the changes.

# %s => Prepared Statement, Used to protect from SQL injection.
insert_query = "INSERT INTO practice(name,class,address) VALUES (%s,%s,%s)"
value = ["Lokesh","10","Delhi"] 
values = [
    ["Ram","11","Mathura"],
    ["Shyam","12","Agra"],
    ["Ghanshyam","10","Kanpur"]
]


# cursor.execute(insert_query,value)
# cursor.executemany(insert_query,values)
# connection.commit()
# print("Records Inserted successfully....")

#* Update query in Mysql
# Update tableName SET columnName = value WHERE considition; 

update_query = "UPDATE practice SET name= %s WHERE id = %s;"
update_value = ("Rahul",13)
# cursor.execute(update_query , update_value)
# connection.commit()
# print("Record Updated Successfully...")

#* Delete Query 
# DELETE FROM tableName WHERE condition;

delete_query = "DELETE FROM practice WHERE id = %s"
delete_value = (12,)
# cursor.execute(delete_query,delete_value)
# connection.commit()
# print("Record Deleted successfully...")

cursor.execute("select * from practice")
rows = cursor.fetchall()

for row in rows:
    for val in row:
        print(val,end="\t")
    print()
connection.close()

"""
while loop :-
--------------
1. insert record
    => take values from user for all columns
2. update record
    => update value and update condition
3. delete record
    => take id from user
4. get single record
    => fetchone()
5. get all record
    => fetchall()
6. exit
    => break
"""