import psycopg2
import pandas as pd
import csv

# data = pd.read_csv("E:/Excel_file/Book.csv")
# df = pd.DataFrame(data)
# print(df)
try:
    conn = psycopg2.connect("dbname=radhika1 user=postgres password=database123 host=localhost")
    print("PostgreSQL connection created successfully...")
    cur = conn.cursor()
    cur.execute("truncate table Employee")
    conn.commit()
    print("Total number of rows deleted :", cur.rowcount)

    with open("E:/Excel_file/Book.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # Skip the header row.
            count =0
            for row in reader:
                cur.execute("INSERT INTO Book VALUES (%s, %s, %s, %s, %s, %s, %s)",row)
                count += cur.rowcount
            print("Total number of rows inserted :",count)

    print(row)
    conn.commit()
    print("commited successfully")



    cur.execute("SELECT Name, Number, Position, Salary from Book")
    rows = cur.fetchall()
    for row in rows:
       print ("Name = ", row[0])
       print ("Number = ", row[1])
       print ("Position = ", row[2])
       print ("Salary = ", row[3], "\n")
    print("Operation done successfully")



    cur.execute("UPDATE Book set SALARY = 25000.00 where Name = 'Avery Bradley'")
    conn.commit()
    print("Total number of rows updated :", cur.rowcount)


except(Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # closing database connection.
    if (conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")



