from gtts import gTTS
import os

enter_text = ""

language = 'en'

voice = gTTS(text= enter_text, lang= language, slow= False)
voice.save("File.mp3")
os.system("start file.mp3")



