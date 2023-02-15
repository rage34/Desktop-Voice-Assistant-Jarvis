
import pywhatkit
import wikipedia
from pywikihow import WikiHow , search_wikihow
import os
import webbrowser as web
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

def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")

    writeab = str(query)


    oooooo = open('C:\\project\\complete jarvis series\\data.txt','a')
    oooooo.write(writeab)
    oooooo.close()

    Query = str(term)

    pywhatkit.search(Query)


    if 'how to' in Query:

        max_result = 1

        how_to_func = search_wikihow(query=Query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()
        speak(how_to_func[0].summary)

    

    else:

        search = wikipedia.summary(Query,2)

        speak(f": According To Your Search : {search}")

def YoutubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term

    web.open(result)

    speak("this is what  i found for your search")

    pywhatkit.playonyt(term)

    speak("This may also  help you sir.")

# def Alram(query):

#     TimeHere= open('C:\\project\\complete jarvis series\\data.txt','a')
#     TimeHere.write(query)
#     TimeHere.close()
#     os.startfile("C:\\project\\complete jarvis series\\DataBase\\ExtraPro\\Alram.py")

# Alram('set alarm for 16 and 38')

#YoutubeSearch('kaushik shresth')

#GoogleSearch('what is photosynthesis')





  

