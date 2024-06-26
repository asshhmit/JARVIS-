import pyttsx3
import pyaudio
import wikipedia


q = 'sharukh khan from wikipedia'
rpl = q.replace('from wikipedia', '')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#engine.setProperty('voice' , voices[0].id)
engine.setProperty('rate', 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


rs = wikipedia.summary(rpl , sentences = 2)
print(rs)
speak(rs)

