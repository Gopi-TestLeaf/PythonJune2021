# Step01: install sqlite3:- pip install db-sqlite3

import sqlite3

# Create Connection
con = sqlite3.connect("database.db")
print("Create DB")
#*********************************************************************************************************************
# Create Table in DataBase
con.execute(''' CREATE TABLE IF NOT EXISTS python_db(fName, lName, eMail, pwd)''')
print('Table Created')
#*********************************************************************************************************************
# Insert the records
con.execute(''' INSERT INTO python_db(fName, lName, eMail, pwd)
                VALUES('Balaji', 'M', 'Bajaji@gmal.com', 54321)''')
#con.commit()
print('Inserted the Records')
#*********************************************************************************************************************
# Update the Records
qr = ''' UPDATE python_db set lName = "MMM" WHERE fName="Sarath" '''
con.execute(qr)
#con.commit()
print('Updated the records')
#*********************************************************************************************************************
# Fetch all data's
data = con.execute("SELECT * FROM python_db")
for eachRow in data:
    print(eachRow)
#*********************************************************************************************************************
#close the connection
con.close()
print("Close DB")