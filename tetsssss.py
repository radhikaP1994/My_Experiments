from sqlalchemy import create_engine
import psycopg2
from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean, Integer
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

conn = create_engine("postgres+psycopg2://postgres:12345@localhost/ddd")
Base = declarative_base()

# conn.connect()
# cur=conn.cursor()
# print("connection successfull")
# print(conn)
# metadata = MetaData()
class student(Base):
    __tablename__='student'
    id=Column(Integer(), primary_key=True)
    fname=Column( String(200), nullable=False)
    lname=Column(String(200), nullable=False)
    contact=Column(Integer(), default=False)

Base.metadata.create(conn)


# ab="""create table student(s_id integer primary key,sname varchar(20),sadd varchar(20),s_contact integer)"""
#
# cur.execute(ab)
# conn.commit()


