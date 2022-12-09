# DELETE data mysql.py
# DATABASE mysql.py
# SQL codes : DELETE yourtablename where id = int or by name=''
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
    mycur.excute("""
    delete from tablePy1 where id = 1
    """)
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