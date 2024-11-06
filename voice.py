# Import the required module for text 
# to speech conversion
from gtts import gTTS

# Import pygame for playing the converted audio
import pygame
import time

# The text that you want to convert to audio
mytext = 'Nomor Antrian C S R 0 0 1. Silahkan menuju ke konter A 1'

# Language in which you want to convert
language = 'id'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")

# Initialize the mixer module
pygame.mixer.init()

# Load the mp3 file
pygame.mixer.music.load("welcome.mp3")

# Play the loaded mp3 file
pygame.mixer.music.play()
time.sleep(10)
