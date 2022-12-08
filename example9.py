# Text-playSound 
#---------------------------------------------------
import os
from gtts import gTTS
from playsound import playsound
myText = "Learn Python By YOURSELF"
myJob = gTTS(text = myText)
myJob.save('audio.mp3')
myJob = os.path.dirname(__file__) + '\audio.mp3'
playsound('audio.mp3')
input ('press ENTER to EXIT!')
#===================================================
#using VLC Lib.
#import vlc
#media = vlc.MediaPlayer('audio.mp3)
#media.play()
#=======================================

