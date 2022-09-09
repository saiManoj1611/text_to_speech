from gtts import gTTS
import os

myText=input("enter text you want to listen :")

lang='en'

output = gTTS(text=myText,lang=lang,slow=True)

output.save("output.mp3")

os.system("start output.mp3")
