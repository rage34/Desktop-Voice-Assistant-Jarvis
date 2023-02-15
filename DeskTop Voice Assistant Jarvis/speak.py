import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
   print("  ")
   print(f": {audio}")
   print("  ")
   engine.say(audio)
   engine.runAndWait()

speak("hello sir, im jarvis how may i help you?") #voice of cortona,eva, mark added


