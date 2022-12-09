# DATABASE mysql.py
#---------------------------------------------------
import mysql.connector
try:
    conn = mysql.connector.connect(
        host = 'localhost' ,
        user = 'root' ,
        passwd = '' ,
        )
    mycur = conn.cursor()
    mycur.excute("CREAT DATABASE db1py DAFAULT CHARCTER SET utf8 DAFAULT COLLATE utf8_general_ci")
except mysql.connector.Error as r:
    print (r)
#---N-O-T-E-----------------------------------------
# #//mycur.excute("CREAT DATABASE db1py") 
#this code "not -support, -including ARABIC lang."
#---------------------------------------------------