
import mysql.connector

# Return the sql connection 
def getConnection():

     connection = mysql.connector.connect(
          host = "localhost",
          user = "root123",
          password = "12345",
          database ="studentrecords",
          autocommit=True
     )
     return connection
       