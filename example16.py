# INSERT data mysql.py
# DATABASE mysql.py
# SQL codes : INSERT INTO yourtablename VALUES(int,'')
#-------------------------------------------------------
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
    insert into tablePy1 values(1,'Adel MD')
    """)
    conn.commit()
except mysql.connector.Error as r:
    print (r)
#-------------------------------------------------------
#---B-A-S-I-C---C-O-D-E--------------------------
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