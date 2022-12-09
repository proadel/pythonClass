# show db_mysql.py files
# DATABASE mysql.py
# SQL codes : SHOW DATABASES
#----------------------------------------------------
import mysql.connector
try:
    conn = mysql.connector.connect(
        host = 'localhost' ,
        user = 'root' ,
        passwd = '' ,
        )
    mycur = conn.cursor()
    mycur.excute("SHOW DATABASES")
    for x in mycur:
        print(x)
except mysql.connector.Error as r:
    print (r)
    #------------------------------------------------