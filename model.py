import sqlite3 as sql

DBPATH = 'database.db'

con = sql.connect(DBPATH)
cur =  con.cursor()



class sqlutil():
    def __init__(self, userid, filename, urladdress, haspassword, password, active):
        self.userid = userid
        self.filename = filename
        self.urladdress = urladdress
        self.haspassword = haspassword
        self.password = password
        self.active = active
        self.dbpath = 'database.db'
        self.con = sql.connect('database.db')
        self.cur = self.con
    def insert(self):
        SQL_COMMAND_INSERT  = '''INSERT INTO urls (userid, filename, urladdress, haspassword, password, active) 
             VALUES (self.userid, self.filename, self.urladdress, self.haspassword, self.password, self.active)'''
        print(self.SQL_COMMAND_INSERT)
        self.cur.execute(SQL_COMMAND_INSERT)
        self.con.commit()
        self.con.close()

        a = sqlutil(1,'qq.exe', 'ASwwaw', 'false','','true')