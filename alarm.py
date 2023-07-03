
import os
from playsound import playsound

path = os.getcwd()

print(path)

playsound(path + "/alert.mp3")