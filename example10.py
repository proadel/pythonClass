# Input-Text playsound.py
#-----------------------------------------------------
from gtts import gTTS
from playsound import playsound
import os
yourText = input('Please Enter Your TEXT to Play: ')
myJob = gTTS(text = yourText)
myJob.save('audio.mp3')
myJob = os.path.dirname(__file__) + '\audio.mp3'
playsound('audio.mp3')
input ('press ENTER to EXIT!')
#------------------------------------------------------

