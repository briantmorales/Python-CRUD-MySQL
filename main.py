#pip install pypyodbc
#!pip install mysql-connector

import pypyodbc
import db_connection as dbConn

from read import Read
from create import Create
from update import Update
from delete import Delete

def main():

    print('CRUD MENU:\n C = Create\n R = Read\n U = Update\n D = Delete ')
    choice = input('Choose option: ')

    if choice == 'C' or choice == 'c' :
        createObj=Create()
        createObj.func_CreateData()
    elif choice == 'R'or choice == 'r':
        readObj =  Read()
        readObj.func_ReadData()
    elif choice == 'U' or choice == 'u':
        updateObj = Update()
        updateObj.func_UpdateData()
    elif choice == 'D'or choice == 'd':
        deleteObj = Delete()
        deleteObj.func_DeleteData()
    else:
        print('Wrong option!.')


# Call the main function
main()