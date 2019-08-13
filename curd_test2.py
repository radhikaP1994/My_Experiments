import psycopg2

connection = psycopg2.connect(user="postgres",password="data123",host="localhost",port="5432",database="sqldb12")
print("database connected sucessfully")
# cursor = connection.cursor()




