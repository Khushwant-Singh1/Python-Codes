from gtts import gTTS
import os 
print("Welcome to robospeaker")
def robospeaker (text, language = "en" ):
    tts = gTTS(text=text , lang=language , slow = False)
    tts.save("output.mp3")
    os.system("start output.mp3")
while True:
    x = input("Enter the text which you want to say through this program: ")
    if x.lower() == "exit robospeaker":
        print("Exiting Robospeaker")
        break
    robospeaker(x)

