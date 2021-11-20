import sqlite3 as sql
import random as ra
DBPATH = 'database.db'

con = sql.connect(DBPATH)
cur =  con.cursor()


lower = ['a', 'b',	'c',	'd',	'e',	'f',	'g',	'h',	'i',	'j',	'k',	'l',	'm',	'n',	'o',	'p',	'q',	'r',	's',	't',	'u',	'v',	'w',	'x',	'y',	'z']
upper = ['A',	'B',	'C',	'D',	'E',	'F',	'G',	'H',	'I',	'J',	'K',	'L',	'M',	'N',	'O',	'P',	'Q',	'R',	'S',	'T',	'U',	'V',	'W',	'X',	'Y',	'Z']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


class sqlUtil():
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
        self.SQL_COMMAND_INSERT = ''
    def insert(self):
        print(self.filename)
        self.SQL_COMMAND_INSERT  = "INSERT INTO urls(userid, filename, urladdress, haspassword, password, active) VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}')".format(self.userid, self.filename, self.urladdress, self.haspassword, self.password, self.active)
        print(self.SQL_COMMAND_INSERT)
        self.cur.execute(self.SQL_COMMAND_INSERT)
        self.con.commit()
        self.con.close()
    

class GetData():
    def __init__(self):
        self.con = sql.connect('database.db')
        self.cur = self.con.cursor()
    def get(self, url):
        print("***#> GET FILE \n")
        self.SQL_COMMAND_SELECT = "SELECT * FROM urls WHERE urladdress = '{0}'".format(url)
        print("*** #> {0}".format(self.SQL_COMMAND_SELECT))
        self.cur.execute(self.SQL_COMMAND_SELECT)
        row = self.cur.fetchone()
        return row   

class makeUrl():
    def __init__(self):
        self.lower = ['a', 'b',	'c',	'd',	'e',	'f',	'g',	'h',	'i',	'j',	'k',	'l',	'm',	'n',	'o',	'p',	'q',	'r',	's',	't',	'u',	'v',	'w',	'x',	'y',	'z']
        self.upper = ['A',	'B',	'C',	'D',	'E',	'F',	'G',	'H',	'I',	'J',	'K',	'L',	'M',	'N',	'O',	'P',	'Q',	'R',	'S',	'T',	'U',	'V',	'W',	'X',	'Y',	'Z']
        self.number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.db = 'database.db'
        self.SQL_COMMAND = ''
    def make(self):
        while True:
            s = str()
            for i in range(2):
                s = s + self.lower[ra.randint(0,25)]
                s = s + self.upper[ra.randint(0,25)]
                s = s + str(self.number[ra.randint(0,9)])
            con = sql.connect(self.db, timeout=10)
            self.SQL_COMMAND= "SELECT * FROM urls where urladdress = " + "'" + str(s) + "'"
            cur = con.cursor()
            cur.execute(self.SQL_COMMAND)
            result = cur.fetchone()
            print(result)
            if not result:
                break    
        return s
