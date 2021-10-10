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

class makeUrl():
    def __init__(self):
        lower = ['a', 'b',	'c',	'd',	'e',	'f',	'g',	'h',	'i',	'j',	'k',	'l',	'm',	'n',	'o',	'p',	'q',	'r',	's',	't',	'u',	'v',	'w',	'x',	'y',	'z']
        upper = ['A',	'B',	'C',	'D',	'E',	'F',	'G',	'H',	'I',	'J',	'K',	'L',	'M',	'N',	'O',	'P',	'Q',	'R',	'S',	'T',	'U',	'V',	'W',	'X',	'Y',	'Z']
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    def make(self):
        s = str()
        for i in range(2):
            s = s + lower[ra.randint(0,25)]
            s = s + upper[ra.randint(0,25)]
            s = s + str(number[ra.randint(0,9)])
        return s    
