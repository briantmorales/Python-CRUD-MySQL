
#!pip install mysql-connector
import mysql.connector
import db_connection as dbConn

mydb = mysql.connector.connect(
  host="localhost",
  user="root123",
  password="12345"
)

mycursor = mydb.cursor()
#create database
mycursor.execute("CREATE DATABASE studentrecords")

#create table students
connection = dbConn.getConnection()
cursor = connection.cursor()
cursor.execute("CREATE TABLE Students(ID int, LastName varchar(255), FirstName varchar(255), Section varchar(255))")

print("Successfully created studentrecords database with students table")

