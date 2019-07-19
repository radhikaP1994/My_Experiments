import psycopg2
import datetime

connection = psycopg2.connect(database="dd1",user="postgres",password="data123",host="localhost")

cursor = connection.cursor()

# To create table :

# sql_command = """
# CREATE TABLE employees(
# staff_number INTEGER PRIMARY KEY,
# fname VARCHAR(20),
# lname VARCHAR(30),
# gender CHAR(1),
# joining DATE,
# birth_date DATE);"""

# sql_command1 = """
# CREATE TABLE employees1(
# staff_number INTEGER PRIMARY KEY,
# fname VARCHAR(20),
# lname VARCHAR(30),
# gender CHAR(1)
# );"""

# For insert:

# sql_command = """INSERT INTO employees(staff_number, fname, lname, gender, joining, birth_date)
#     VALUES (1007, 'William', 'Shakespeare', 'm', '1961-10-25','1910-10-25');"""
# cursor.execute(sql_command)
#
# sql_command = """INSERT INTO employees(staff_number, fname, lname, gender, joining, birth_date)
#     VALUES (1002, 'William1', 'Shakespeare1', 'm', '1961-10-26','1910-10-26');"""
# cursor.execute(sql_command)
#  connection.commit()

# sql_command1= """INSERT INTO employees1(staff_number, fname, lname, gender)
#      VALUES (1001, 'William3', 'Shakespeare2', 'm');"""
# cursor.execute(sql_command1)
# sql_command1 = """INSERT INTO employees1(staff_number, fname, lname, gender)
#      VALUES (1012, 'William4', 'Shakespeare4', 'm');"""
# cursor.execute(sql_command1)
# sql_command1 = """INSERT INTO employees1(staff_number, fname, lname, gender)
#      VALUES (1003, 'William5', 'Shakespeare5', 'm');"""
# cursor.execute(sql_command1)
# sql_command1 = """INSERT INTO employees1(staff_number, fname, lname, gender)
#      VALUES (1004, 'William6', 'Shakespeare6', 'm');"""
# cursor.execute(sql_command1)

# cursor.execute(sql_command1)

#To alter the table name :

# sql_command= """ALTER table employees1 rename to employees2"""
# cursor.execute(sql_command)



connection.commit()
connection.close()






