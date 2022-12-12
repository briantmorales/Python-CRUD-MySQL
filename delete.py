import db_connection as dbConn;

class Delete:
    def func_DeleteData(self):
        # Get the sql connection
        connection = dbConn.getConnection()

        id = input('Enter Student Id = ')
    
        try:
           # Get record which needs to be deleted
           sql = "Select * From students Where ID = %s" 
           cursor = connection.cursor()
           cursor.execute(sql, [id])
           item = cursor.fetchone()
           print('Data Fetched for ID = ', id)
           print('Student_ID\t\tStudent_LastName\t\tStudent_FirstName\t\t Student_Section')
           print('----------------------------------------------------------------------------------------------------')       
           print(' {}\t\t {} \t\t\t{}  \t\t\t  {} '.format(item[0], item[1], item[2], item[3]))
           print('----------------------------------------------------------------------------------------------------')
           confirm = input('Are you sure to delete this record (Y/N)?')

           # Delete after confirmation
           if confirm == 'Y' or confirm == 'y':
               deleteQuery = "DELETE FROM students WHERE ID= %s"
               cursor.execute(deleteQuery,[id])
               connection.commit()
               print('Data deleted successfully!')
           else:
                print('Wrong Entry')
        except:
            print('Something went wrong, please check')
        finally:
            connection.close()