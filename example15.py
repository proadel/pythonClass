# CREATE TABLE mysql.py
# DATABASE mysql.py
# SQL codes : CREATE TABLE
#----------------------------------------------------
import mysql.connector
try:
    conn = mysql.connector.connect(
        host = 'localhost' ,
        user = 'root' ,
        passwd = '' ,
        database = 'db1py' ,
        )      
    mycur = conn.cursor()
    mycur.excute("CREATE TABLE tablePy1 (id int primary key , name varchar(50))")
except mysql.connector.Error as r:
    print (r)
#----------------------------------------------------
#---B-A-S-I-C---C-O-D-E--------------------------
'''
import mysql.connector
try:
    conn = mysql.connector.connect(
        host = 'localhost' ,
        user = 'root' ,
        passwd = '' ,
        database = '' ,
        )
    mycur = conn.cursor()
    mycur.excute()
except mysql.connector.Error as r:
    print (r)
'''
#------------------------------------------------
