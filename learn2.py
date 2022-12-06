#----------------------------------------------------
# PYTHON | Learn variables and Values 
#----------------------------------------------------
#42===Files12========================================
# Exel Files and Python
# to work with exel files should download xlwt lib
#C:\Users\urPC.path> pip install xlwt
'''
import xlwt
from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('sheet1')
#// filename.write(row,column,'value') to -w -r -a 
sheet1.write(3,2,'id')
sheet1.write(3,3,'name')
sheet1.write(3,4,'date')
sheet1.write(3,5,'Phone')
wb.save ('C:\\Users\\..\\..\\..\\fileName.xls')
'''
#----------------------------------------------------
#41===Files11========================================
# javascript = js | .js
#
'''
F = open ('index.html','w')
html = ''''''
<html>
<head>
<title>HTML by PYTHON</title>
<link rel="stylesheet" href="index.css">
<script>src="index.js"<script>
</head>
<body>
<center>
<h1>HTML by Python</h1>
<hr>
<h2 id='para' onmouseover='ok();' onmouseover='ok2();'>Learn 2022</h2>
<p>Developed By Adel MD. | Umbrella Corporation</p>
<p>+967 733477848</p>
</center>
</body>
</html>
''''''
F.write(html)
F.close()
#------js.py-----------------
''''''
F = open ('index.js','w')
js = ''''''
alert ('WELCOME to OUR SITE by Python!!!');
''''''
F.write (js)
F.close()
'''
#----------------------------------------------------
#40===Files10========================================
# HTML files
'''
F = open ('index.html','w')
html = ''''''
<html>
<head>
<title>HTML by PYTHON</title>
<link rel="stylesheet" href="index.css">
</head>
<body>
<center>
<h1>HTML by Python</h1>
<hr>
<h2>Learn 2022</h2>
</center>
</body>
</html>
''''''
F.write(html)
F.close()
'''
'''
F = open ('index.css','w')
css = ''''''
    body{
        background-color: #111;
        color: #fff;
    }
    h1{
        color: blue;
    }
    h2{
        color: red;
    }
''''''
F.write (css)
F.close()
'''
#----------------------------------------------------
#39===Files9=========================================
# w- write | r- read | a- append
# variable = open ('parameter1','parameter2= w-r-a')
# variable = open('file','w') # to write
# variable = open('file','r') # to read
# variable = open('file','a') # to add data without lose
'''
#F = open ('py2022.txt','w') # to creat, also open file
F = open ('py2022.txt','a') # to append, add to file
F.write ("Learn Python !!!\n") # to write inside file
F.write ("Learn Python2 !!!\n") # to write inside file
F.close() # to close file after writing.

'''
#----------------------------------------------------
#38===Files8=========================================
# to deal with folders and files by os lib
'''
import os
#files = os.listdir('folder_name') 
files = os.listdir ('newFolder')
for file in files:
    print (files)
'''
#----------------------------------------------------
#37===Files7=========================================
# DELETE files and folders by using os lib
'''
import os 
#os.remove("") # to remove files ("filename.xxx")
#os.remove("note.txt")

# to rm = remove directory rmdir
#os.rmdir('') # to remove folders ("folder name")
os.rmdir('mkdir1')
'''
#----------------------------------------------------
#36===Files6=========================================
# to ask about folders 
'''
import os
if os.path.exists('mkdir1'):
    print ('YES')
else:
    print ('NO')
'''
#----------------------------------------------------
#35===Files5=========================================
# How to make and create "folders" from python
# when see os , its mean dealling with operating Sys.
'''
import os  # first call the operating system lib
#os.mkdir mk = make , dir = directory
input ("press any key to creat folder ...")
os.mkdir('mkdir1')
input ("press any key to exit programe...")
'''
#----------------------------------------------------
#34===Files4=========================================
# read into -from file
'''
file = open('note.txt','r')
text = file.read()
#input ("press any key to read and display file")
print (text)
#input ("press any key to Exit_file")
'''
#----------------------------------------------------
#33===Files3=========================================
# write into file, and .. ... ......
'''
file = open('note.txt','w')
file.write("1. Learn Python as Self-Study.\n")
file.write("2. new line................\n")
file.write("3. new line................\n")
file.write("4. new line................\n")
input ("press any key to start write into File..")
'''
#----------------------------------------------------
#32===Files2=========================================
# write into file
'''
file = open('note.txt','w')
file.write("Learn Python as Self-Study")
input ("press any key to start write into File..")
'''
#----------------------------------------------------
#31===Files1=========================================
# w r a : open and create any file like this 
#w = write , only writing re-writing new ....
#r = read
#a = append ~ adding ++ side by side the old once
''' 
#file = open('note.txt','w') #--> & to creat file.
file = open('learnPython.txt','w')
input ('press any key.... to creat file')
'''
#----------------------------------------------------
#30===OOP2===========================================
# self | __init__() 
'''
class Home:
    def __init__(self):
        self.kitch()
        self.bedroom()
        #pass
    def kitch(self):
        print ("For Cooking and Eating!!!")
    def bedroom(self):
        print ("For Sleeping, Relaxing and Rest!!!")

x = Home()
#x.bedroom()
#x.kitch()
#---------------

'''
#----------------------------------------------------
#29===OOP1===========================================
# OOP start... CLASS
'''
class Human :
    name = input ("Enter Your Name: ")
    if name == 'adel':
        print ('WELCOME')
    else:
        print ('ERROR!!') 
    def job(self):
        print ('work in Umbrella Company')
x = 3.14
y = 9.8
print (x + y)
x = Human()
#print (x.name)
#x.job () 
'''
#----------------------------------------------------
#28===Condetions19===================================
# Modules useing and import codes from external files
# create tow files named ; one.py, tow.py, Then;
# see files : one.py and tow.py please before run
# tow.py 
'''
# code inside one.py
def color():
    colors = ''''''
    1-red
    2-blue
    3-yellow
    ''''''
    print (colors)

def animal():
    animals = ''''''
    1-rat
    2-cat
    3-wolf
    ''''''
    print (animals)
# codes inside tow.py
import one
one.color()
'''
#----------------------------------------------------
#27===Condetions18===================================
# global usein 
'''
def info ():
    global name
    name = "Class Name: Python"
def on():
    info()
    print (name)
on()
'''
#----------------------------------------------------
#26===Condetions17===================================
#
'''
def math(n1,n2):
    print (n1+n2)
math (5,5)
'''
#----------------------------------------------------
#25===Condetions16===================================
#
'''
def employee(name, job):
    print (name)
    print (job)
employee ('Adel', 'Developer')
'''
#----------------------------------------------------
#24===Condetions15===================================
# pass
'''
def employee ():
    pass
print ("employee")    
'''
#----------------------------------------------------
#23===Condetions14===================================
#
'''
def welcome():
    x = 10
    y = 10
    result = x + y
    print (result)
welcome()    
'''
#----------------------------------------------------
#22===Condetions13===================================
#
'''
def welcome ():
    print ("=======================")
    print ("Welcome To Python Class")
    print ("=======================")
welcome()
'''
#----------------------------------------------------
#21===Condetions12===================================
# try: .... in the End use except : to TShoot= like
'''
try:
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    print (num1 + num2)
except :
    print ("[-] Please The Program Just Take Numbers, Thanks!!")
'''
#----------------------------------------------------
#20===Condetions11===================================
# var = []  ()  {} 
# dictionary  {key:value}
'''
students = {"name":"Adel", "age":43, "developer": True}
print (students.keys())
print (students.values())
print (students.items())
'''
#----------------------------------------------------
#19===Condetions10===================================
#
'''
fname = "Adel"
lname = "mohammed"
print (lname + fname)
'''
#---------------------------------------------------
#18===Condetions9===================================
# string + string 
'''
fname = "Adel"
fname += "Mohammed"
print (fname)
'''
#---------------------------------------------------
#17===Condetions8===================================
# 
'''
names = ('ali', 'hasan', 'khaled', 'shehad', 'rajeh')
numbers = (1,2,3,4,5)
infoIntr = ('level:', 'class :', 'acadNumb :', 'etc..')
infoExtr = ('firstName','lastName', 'address', 'email')
print (infoExtr)
'''
#---------------------------------------------------
#16===Condetions7===================================
# var -- LIST 
'''
#student1 = "adel"
#student2 = "mohammed"
#student3 = "dawood" #.....
#student4 = "Emad"
#student5 = "Bandar"
#student6 = "husam"
students_name = ["adel", "mohammed", "dawood", "Emad", "husam"]
students_degree = [91, 92, 93, 94, 95]
adel = ['Adel DAWOOD', 'Makkah 1979',43, True]
#print (students_degree)
print (adel)
'''
#---------------------------------------------------
#15===Condetions6===================================
# for -range --if --- break =  stop programe
'''
for i in range(0,12):
    print (i)
    if i == 8 :
        print (8, "Update!! needed...")
        #break  # its mean stop if == True.
'''
#---------------------------------------------------
#14===Condetions5===================================
# for ---range1
'''
for x in range(1,10):
    print (x)
'''
#---------------------------------------------------
#14===Condetions5===================================
# for --- alone.
'''
name = "Python Class"
for i in name:
    print (i)
'''
#---------------------------------------------------
#13===Condetions4===================================
# while -loop do not lose the infinity loop magic
'''
start = 0 
while start < 10 : #*
    print ('Start')
    start += 1     #*
'''
#---------------------------------------------------
#12===Condetions3===================================
# range (start, stop)
# 
'''
#print (range(19))
#print (list(range(1,19)))
print (list(range(0,19)))
'''
#---------------------------------------------------
#11===Condetions2===================================
# and  or 
'''
#a = 1000
a = 10 
b = 20
c = 70
#if a == 10 and b == 20 :
#if a == 10 or b == 20 :
if a == 10 or b == 20 or c == 1 :
    print ('OK1')
else :
    print ('NO2')
'''
#---------------------------------------------------
#10===Condetions1===================================
# if ... :  else : ....
# if ... : else if = elif : .... + else in The end. 
'''
x = 10
y = 30
#if x == y :
#if x > y :
if x > y :
    print ('Right1')
elif x < y :
    print ('Right2')
else :  #line_block
    print ('wrong!!')
'''
#---------------------------------------------------
#9===DATA_Entry=====================================
'''
num1 = int (input ('Please Enter First Number:'))
#num2 = input ('Enter Second Number, Dear Sir:')
num2 = int (input ('Enter Second Number, Dear Sir:'))
result = num1 + num2
print (result)
'''
#---------------------------------------------------
#8===DATA_Entry=====================================
'''
print ('=======================')
name = "Python Course1"
name = "Data Entry : input E.g;"
print (name)
print ('=======================')

name = input ("Please Enter Your Name: ")
#print (name)
#print ("Your First Name is :" + name)
print ("Hi Dear, And Welcome Again Mr:" + name)
'''
#---------------------------------------------------
#7==================================================
#
''' 
x = 10
x +=3 # 1-->x=10_OK nextLine 2--> x = 1(10)+3 = 13
x -=2 # = x = 13 - 2 =11
x *=2 # = x = 11 * 2 =22
x /=3 # = x = 22 / 3 = 7.33
print (x)
''' 
#---------------------------------------------------
#6==================================================
# == != > < <= >=
'''
#print (200 > 100)
x , y = 20,20
#print (x==y)
#print (x > y)
#print (x >= y)
#print (x <= y)
print (x != y)
'''
#---------------------------------------------------
#5==================================================
# var = number
'''
x = 10
y = 8
i = 4
# res = (x - o) #WHY ERROR !!!
o = 2
z = 1
res = (x - o)

print (x-y,x-y,x+y-z,x//y,x/y,x%y)
print (res)
'''
#---------------------------------------------------
#4==================================================
# math_matical  - +  * % // ** /
'''
print (1 + 2)
print (2-1)
print (3*2)
print (64 ** 2)
print (64 / 2) 
print (64 // 2)
print (50000*2.5/100)
print (50000*2//100)
'''
#---------------------------------------------------
#3==================================================
'''
print("1-The Name:")
print('2-The Age:')
print('3-Title Job:')
print('4-work_Address')
#exit() 
# to excluded from run = stop program here please... 
print ('5-home_Address:')
print("6-The familyName:")
#exit()
print('7-The parents1Age:')
print('8-Privet_Email')
'''
#---------------------------------------------------
'''
#2==================================================
#this is called THE CLEAN CODE 
name,age,developer = "Adel",43,True 
print (name,age,developer)
'''
#---------------------------------------------------
'''
#1======OLD_SCHOOL==================================
name = "Python Class2" # string
age = 43 #int
weight = 77.5 #float 
have_car = False # or True #bollean "bool" !
print (name)
print (age)
print (weight)
print (have_car)
#===================================================
'''
#---Start_From#1---upword---------------------------