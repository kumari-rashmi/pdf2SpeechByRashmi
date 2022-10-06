from gtts import gTTS
import os

myText = "Hi I am Rashmi , Hi I am Rajiv"
Language = 'en'

myObj = gTTS(text=myText, lang=Language, slow=False)
myObj.save("welcome.mp3")
os.system("mpyg321 welcome.mp3")
