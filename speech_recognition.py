import speech_recognition as sr
import os
from pydub import AudioSegment

name = input("file_name:")
AUDIO_FILE = os.path.dirname(__file__)+"/voice_data/"+name+".wav"


sound = AudioSegment.from_wav(AUDIO_FILE)

length = sound.duration_seconds
n = int(length/30)
l = []
print(length)
print(n)
for i in range(n):
    s = sound[30000*i:30000*(i+1)]
    s.export(os.path.dirname(__file__)+"/voice_data/"+name+str(i)+".wav", format="wav")
s = sound[30000*n:]
s.export(os.path.dirname(__file__)+"/voice_data/"+name+str(n)+".wav", format="wav")

text = ""
for i in range(n+1):
    print(i)
    try:
        r = sr.Recognizer()
        with sr.AudioFile(os.path.dirname(__file__)+"/voice_data/"+name+str(i)+".wav") as source:
            audio = r.record(source)
        text += r.recognize_google(audio, language='ja')
    except:
        print("pass")
data = open(os.path.dirname(__file__)+"/text_data/"+name+".txt", 'w')
data.write(text)
data.close()
