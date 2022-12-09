# Smart-Alarm playsound.py
#------------------------------------------------------
from gtts import gTTS
from playsound import playsound
import os
import time
#------------------------------------------------------
alarmTime = "Now is 5:00am, Weakup Please.. You should learn Students"
myJob = gTTS(text = alarmTime)
myJob.save('audio.mp3')
myJob = os.path.dirname(__file__) + '\audio.mp3'
playsound('audio.mp3')
input("press ENTER to Exit!!!")
#------------------------------------------------------

# time.sleep(9) #--> 9sec ... then next alarm