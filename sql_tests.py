# importing module

import psycopg2

# connecting to the database

connection = psycopg2.connect("dbname=radhika1 user=postgres password=database123 host=localhost")

# cursor

crsr = connection.cursor()

# SQL command to create a table in the database

sql_command = """CREATE TABLE emp (

staff_number INTEGER PRIMARY KEY,

fname VARCHAR(20),

lname VARCHAR(30),

gender CHAR(1),

joining DATE);"""

# execute the statement

crsr.execute(sql_command)

# SQL command to insert the data in the table

sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-2");"""

crsr.execute(sql_command)

# another SQL command to insert the data in the table

sql_command = """INSERT INTO emp VALUES (2 "Bill2", "Gates2", "F", "1980-10-3");"""

crsr.execute(sql_command)

# To save the changes in the files. Never skip this.

# If we skip this, nothing will be saved in the database.

connection.commit()

# close the connection

connection.close()


# cursor object

crsr = connection.cursor()

# execute the command to fetch all the data from the table emp

crsr.execute("SELECT * FROM emp")

# store all the fetched data in the ans variable

ans= crsr.fetchall()

# loop to print all the data

for i in ans:

   print(i)