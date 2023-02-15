from Features import GoogleSearch
from click import command
import pyttsx3
from playsound import playsound
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
import pyautogui
import keyboard
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    print("  ")
    engine.say(audio)
    print(f": {audio}")
    print("  ")
    engine.runAndWait()

def TakeCommand():
   r = sr.Recognizer()

   with sr.Microphone() as source:

      print(": listening....")

      r.pause_threshold =1

      audio = r.listen(source)


   try:

       print(": Recognizing...")

       query = r.recognize_google(audio,language='en-in')

       print(f": your command : {query}\n")

   except:
      return ""


   return query.lower()
     
def TakeCommand_Hindi():
   r = sr.Recognizer()

   with sr.Microphone() as source:

      print(": listening....")

      r.pause_threshold =1

      audio = r.listen(source)


   try:

       print(": Recognizing...")

       query = r.recognize_google(audio,language='hi')

       print(f": your command : {query}\n")

   except:
      return ""


   return query.lo


def TaskExe():


   def Music():
      speak("Tell Me The Name Of The Song!")
      musicName = TakeCommand

      if 'heatwaves' in musicName:
         os.startfile('C:\\Users\\abc\\Music\\rocky\\heatwaves.mp3')

      elif 'thegodofhighschool' in musicName:
         os.startfile('C:\\Users\\abc\\Music\\rocky\\thegodofhighschool.mp3')

      else:
         pywhatkit.playonyt(musicName)
      
      speak("your song has been started! . enjoy sir!")

   def WhatsApp():
      speak("Tell Me The Name Of The Person!")
      name = TakeCommand()

      if  'Naresh' in name:
           speak("Tell Me The Message!")
           msg = TakeCommand()
           speak('Tell Me The Time Sir!')
           speak("Time In Hour!")
           hour = int(TakeCommand())
           speak("Time In Minutes!")
           min = int(TakeCommand())
           pywhatkit.sendwhatmsg("+917090513122",msg,hour,min,20)
           speak("Ok,Sir! , Sending Whatsapp Message !")

      elif 'vijay sir' in name:
           speak("Tell Me The Message!")
           msg = TakeCommand()
           speak('Tell Me The Time Sir!')
           speak("Time In Hour!")
           hour = int(TakeCommand())
           speak("Time In Minutes!")
           min = int(TakeCommand())
           pywhatkit.sendwhatmsg("+918095939824",msg,hour,min,20)
           speak("Ok,Sir! , Sending Whatsapp Message !")
          
      else:
           speak("Tell Me The Phone Number!")
           phone = int(TakeCommand())
           ph =  '+91' + phone
           speak("Tell Me The Message!")
           msg = TakeCommand()
           hour = int(TakeCommand())
           speak("Time In Minutes!")
           min = int(TakeCommand())
           pywhatkit.sendwhatmsg("+917090513122",msg,hour,min,20)
           speak("Ok,Sir! , Sending Whatsapp Message !")
 
   def OpenApps():
      speak("Ok Sir , Wait a Second!")
      
      if 'code' in query:
         os.startfile("C:\\Users\\abc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

      elif 'vision' in query:
         os.startfile("C:\\Keil\\UV3\\Uv3.exe")
      
      elif 'chrome' in query:
         os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

      elif 'facebook'in query:
         webbrowser.open('https://www.facebook.com/')

      elif 'instagram' in query:
         webbrowser.open('https://www.instagram.com/?hl=en')

      elif 'maps' in query:
         webbrowser.open('https://www.google.com/maps/@12.9539974,77.6309395,11z')

      elif 'youtube' in query:
         webbrowser.open('https://www.youtube.com/')

      speak("your command as been completed sir")
  
   def CloseApps():
      speak("Ok,sir! , Wait a Second!")
     
      if 'youtube' in query:
         os.system("TASKKILL /F /im chrome.exe")

      elif 'chrome' in query:
         os.system("TASKKILL /F /im chrome.exe")

      elif 'vision' in query:
         os.system("TASKKILL /F /im Uv3.exe")

      elif 'code' in query:
         os.system("TASKKILL /F /im code.exe")

      speak("your command has been completed sir!")
 
   def YoutubeAuto():
      speak("what's your command?")
      com = TakeCommand()
      if 'pause' in com:
         keyboard.press('space bar')

      elif 'restart' in com:
         keyboard.press('0')

      elif 'mute' in com:
         keyboard.press('m')

      elif 'skip' in com:
         keyboard.press('1')

      elif 'back' in com:
         keyboard.press('j')

      elif 'full screen' in com:
         keyboard.press('f')

      elif 'file mode' in com:
         keyboard.press('t')
      speak("done sir")

   def ChromeAuto():
      speak("chrome automation started")

      command = TakeCommand()

      if 'close this tab' in command:
         keyboard.press_and_release('ctri + w')

      elif 'open new tab' in command:
         keyboard.press_and_release('ctri +t ')
      
      elif 'open new window' in command:
         keyboard.press_and_release('ctri +n ')

      elif 'history' in command:
         keyboard.press_and_release('ctri + h')

   def screenshot():
      speak("ok sir , what should i name that file ?")
      path = TakeCommand()
      path1name = path + ".png"
      path1 = "C:\\Users\\abc\\Pictures\\screenshot"+ path1name
      kk = pyautogui.screenshot()
      kk.save(path1)
      os.startfile("C:\\Users\\abc\\Pictures\\screenshot")
      speak("here is your screenshot")
      
       

   while True:


      query = TakeCommand()

      if 'hello' in query:
         speak("hello sir, I am jarvis .")
         speak("your personal assistant!")
         speak("how may i help you?")

      elif 'how are you' in query:
         speak("i Am fine sir")
         speak("what about you?")

      elif 'you need a break' in query:
         speak("ok sir,you can call me Anytime! ")
         break

      

      elif 'youtube search' in query:
         speak("ok sir , this is what i found for your search!")
         Query = query.replace("jarvis","")
         query = Query.replace("youtube search","")
         web = 'https://www.youtube.com/results?search_query=' + query
         webbrowser.open(web)
         speak("done sir!")

      elif 'google search' in query:
         speak("tis is what i found for your search sir!")
         query = query.replace("jarvis","")
         query = query.replace("google sreach","")
         pywhatkit.search(query)
         speak("done sir!")
        
      elif 'website' in query:
         speak("ok sir , Launching .....")
         query = query.replace("jarvis","")
         query = query.replace("website","")
         query = query.replace("  ","")
         web1 = query.replace("open","")
         web2 = 'https://www.' + web1 + '.com'
         webbrowser.open(web2)
         speak("launched sir!")

      elif 'launch' in query:
         speak("tell me the name of the website!")
         name = TakeCommand()
         web = 'https//www.' + name + '.com'
         webbrowser.open(web)
         speak("done sir!")

      elif 'wikipedia' in query:
         speak("searching wikipedia....")
         query = query.replace("jaris","")
         query = query.replace("wikipedia","")
         wiki = wikipedia.summary(query,2)
         speak(f"According to wikipedia : {wiki}")

      elif 'WhatsApp message' in query:
         WhatsApp()

      elif 'screenshot' in query:
         screenshot()

      elif 'open facebook' in query:
         OpenApps()

      elif 'open instagram' in query:
         OpenApps()

      elif 'open code' in query:
         OpenApps()

      elif 'open youtube' in query:
         OpenApps()

      elif 'open vision' in query:
         OpenApps()

      elif 'open chrome' in query:
         OpenApps()

      elif 'open maps' in query:
         OpenApps()

      elif 'close chrome' in query:
         CloseApps()

      elif 'close vision' in query:
         CloseApps()
      
      elif 'close youtube' in query:
         CloseApps()
      
      elif 'close code' in query:
         CloseApps()

      elif 'pause' in query:
         keyboard.press('space bar')

      elif 'restart' in query:
         keyboard.press('0')

      elif 'mute' in query:
         keyboard.press('m')

      elif 'skip' in query:
         keyboard.press('1')

      elif 'back' in query:
         keyboard.press('j')

      elif 'full screen' in query:
         keyboard.press('f')

      elif 'file mode' in query:
         keyboard.press('t')
      
      elif 'youtube tool' in query:
          YoutubeAuto()
      
   
      elif 'close this tab' in query:
         keyboard.press_and_release('ctri + w')

      elif 'open new tab' in query:
         keyboard.press_and_release('ctri +t ')
      
      elif 'open new window' in query:
         keyboard.press_and_release('ctri +n ')

      elif 'history' in query:
         keyboard.press_and_release('ctri + h')

      elif 'chrome automation' in query:
       ChromeAuto()

      elif 'joke' in query:
         get = pyjokes.get_joke()
         speak(get)

      elif 'repeat my words' in query:
         speak("speak sir!")
         jj = TakeCommand()
         speak(f"you said : {jj}")

      
      
   TakeCommand()

TaskExe()
   
   