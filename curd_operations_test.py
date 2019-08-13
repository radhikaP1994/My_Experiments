import psycopg2

try:

    connection = psycopg2.connect(user="postgres",password="data123",host="localhost",port="5432",database="sqldb12")
    print("database connected sucessfully")
    cursor = connection.cursor()

    # sql_create = """create table mobile1(id integer,name varchar(10)"""
    #
    # print("Table created successfully")

    # insert_query = """ INSERT INTO mobile1 (ID, NAME, PRICE) VALUES (%s,%s,%s)"""
    # values_query = (5, 'One Plus 6', 950)
    # cursor.execute(insert_query, values_query)
    # connection.commit()
    # # count = cursor.rowcount
    # print( "Record inserted successfully into mobile table")

    print("Table Before updating record ")
    sql_select_query = """select * from mobile where id = %s"""
    cursor.execute(sql_select_query, (id, ))
    record = cursor.fetchone()
    print(record)
    connection.commit()

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
