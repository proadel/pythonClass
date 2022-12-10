# SELECT * data mysql.py
# DATABASE mysql.py
# SQL codes : SELECT * FROM yourtablename
#--------------------------------------------------------------
import mysql.connector
try:
    conn = mysql.connector.connect(
        host = 'localhost' ,
        user = 'root' ,
        passwd = '' ,
        database = 'db1py'
        )      
    mycur = conn.cursor()
    mycur.excute("SELECT * FROM tablePy1")
    for x in mycur:
        print(x)
    conn.commit()
except mysql.connector.Error as r:
    print (r)
#--------------------------------------------------------------
#---B-A-S-I-C---C-O-D-E-------------------------------
'''
import mysql.connector
try:
    conn = mysql.connector.connect(
        host = 'localhost' ,
        user = 'root' ,
        passwd = '' ,
        database = ''
        )
    mycur = conn.cursor()
    mycur.excute()
    conn.commit()
except mysql.connector.Error as r:
    print (r)
'''
#------------------------------------------------