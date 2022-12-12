import db_connection as dbConn

class Create:
    def func_CreateData(self):

        # Get the sql connection
        connection = dbConn.getConnection()
                
        stud_id = input('Enter Student ID = ')
        stud_lastname = input('Enter Last Name = ')
        stud_firstname = input('Enter First Name = ')
        stud_section = input('Enter your Section = ')

        try:
           query = "INSERT INTO students(ID, LastName, FirstName, Section) Values(%s,%s,%s,%s)" 
           cursor = connection.cursor()
           # Execute the sql query
           cursor.execute(query, [stud_id, stud_lastname, stud_firstname, stud_section])
           # Commit the data
           connection.commit()
           print('Data Saved Successfully')

        except:
             print('Something went wrong, please check')

        finally:
           # Close the connection
           connection.close()