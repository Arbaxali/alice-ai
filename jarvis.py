import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=(datetime.datetime.now().hour)
    if hour>=0 and hour<=1:
        speak("Good morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<=24:
        speak("Good Evening!")
    speak("Im Alice your personal AI,Please tell me how may i help you !")
def Intro():
    speak('im alice an artificial intelligence,created by arbaaz ali')
    speak('alice is an character which was originally inspired from anime sword art online,')
    speak('i love learning new things')
    speak('here is infromation about myself')
    webbrowser.open('https://hero.fandom.com/wiki/Alice_Zuberg')




def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.phrase_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query =r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:

        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
   wishme()
   while True:
       query = takeCommand().lower()
       if 'quit' in query:
           break
       elif 'wikipedia' in query:
           speak("Searching wikipedia....")
           query = query.replace('Wikipedia', "")
           results = wikipedia.summary(query, sentences=2)
           speak('According to wikipedia')
           print(results)
           speak(results)

       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'open google' in query:
           webbrowser.open("google.com")
       elif 'open whatsapp' in query:
           webbrowser.open("whatsapp.com")
       elif 'open Github' in query:
           webbrowser.open("github.com")
       elif 'play music' in query:
           music_dir = 'D:\\arbaz\\music\\mp3'
           songs = os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir, songs[0]))
       elif 'open pycharm' in query:
           codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
           os.startfile(codePath)
       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir,the time is {strTime}")

       elif 'tell me about yourself' in query:
           Intro()
       elif 'what is alice' in query:
           Intro()
       elif 'introduce yourself' in query:
           Intro()
       elif 'power off' in query:
           speak("do you want to shut down the computer say yes or no")
           if 'yes' in query:
               os.system("shutdown /s /t 1")
           else:
               continue










