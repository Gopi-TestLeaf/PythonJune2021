import sqlite3
from Learn_DataBase.TestData import Test_Data


class Data_Base:

    def __init__(self, file_name, table_name):
        self.file_name = file_name
        self.table_name = table_name

    def get_connection(self):
        con = sqlite3.connect(self.file_name)
        print("Create DB")
        return con

    def create_table(self, con):
        con.execute(''' CREATE TABLE IF NOT EXISTS ''' + self.table_name + '''(fName, lName, eMail, pwd)''')
        print('Table Created')

    def insert_record(self, con, obj):
        qr= f''' INSERT INTO {self.table_name}(fName, lName, eMail, pwd) VALUES(?, ?, ?, ?)'''
        con.execute(qr, (obj.fName, obj.lName, obj.eMail, obj.pwd))
        con.commit()
        print('Inserted the Records')

    def close_connection(self, con):
        con.close()
        print("Close DB")

if __name__ == "__main__":
    db_obj = Data_Base('newDataBase.db', 'leafGopi')
    con = db_obj.get_connection()
    db_obj.create_table(con)
    obj = Test_Data(fName="Gopinath", lName="Jayakumar", eMail="g@gmail.com", pwd=54321)
    db_obj.insert_record(con, obj)
    db_obj.close_connection(con)

