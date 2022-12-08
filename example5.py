# Age Calculator
#-------------------------------------------------
import datetime
timeNow = datetime.datetime.now()
age = int (input('Please Enter Your birth Year:'))
year = timeNow.year
ageAnswer = year - age 
print ('your Age is : ', ageAnswer)
input ('press ENTER to EXIT')
#-------------------------------------------------

