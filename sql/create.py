# import mysql.connecter 
# #  while connecting third party resource deffenetly we have to write 
# #  how to use error handling in python ?
# #  these are the commands for  error handling in python:   try , except , finally, raise 
# #  in java /js:  try catch , finally , throw ,throws

# '''



#                                                        














import mysql.connector
dbconnector=None
mycursor = None
try:
    dbconnector=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="33am")
    mycursor=dbconnector.cursor()
    name='''
            create table harish (
            name varchar(32),
            id int,
            loc varchar(32));
         '''

    mycursor.execute(name)
    dbconnector.commit()
    print("table created")
except mysql.connector.DatabaseError as err:
    print (err)
    
finally:
    dbconnector.close()
    mycursor.close()





