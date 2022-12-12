import db_connection as dbConn;

class Update:
    def func_UpdateData(self):
        # Ge the sql connection
        connection = dbConn.getConnection()

        id = input('Enter Student ID = ')
    
        try:
           # Fethc the data which needs to be updated
           sql = "Select * From students Where ID = %s" 
           cursor = connection.cursor()
           cursor.execute(sql, [id])
           item = cursor.fetchone()
           print('Data Fetched for ID = ', id)
           print('Student_ID\t\tStudent_LastName\t\tStudent_FirstName\t\t Student_Section')
           print('----------------------------------------------------------------------------------------------------')       
           print(' {}\t\t {} \t\t\t{}  \t\t\t  {} '.format(item[0], item[1], item[2], item[3]))
           print('----------------------------------------------------------------------------------------------------')
           print('Enter New Data To Update Student Record ')

           stud_id = input('Enter New Student ID = ')
           stud_lastname = input('Enter New Last Name = ')
           stud_firstname = input('Enter New First Name = ')
           stud_section = input('Enter New Section = ')

           query = "UPDATE students SET ID = %s, LastName =%s, FirstName =%s, Section =%s WHERE ID =%s" 
           update_cursor = connection.cursor()
           # Execute the update query
           update_cursor.execute(query, [stud_id, stud_lastname, stud_firstname, stud_section, id ])
           connection.commit()
           print('Data Updated Successfully')

        except:
             print('Something went wrong, please check')

        finally:
           # Close the connection
           connection.close()