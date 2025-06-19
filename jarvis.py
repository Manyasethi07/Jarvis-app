import pyttsx3  #pip install pyttsx3  (text to speech recognition)
import datetime
import speech_recognition as sr   #pip install speechrecognition
import wikipedia  #pip install wikipedia
import webbrowser as wb
import os
import pyautogui   #pip install pyautogui
import psutil    #pip install psutil
import pyjokes  #pip install pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    


def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    print("the current time is")
    speak(Time)
    print(Time)
    
def date():
   
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is")
    print("the current date is")
    speak(date) 
    speak(month) 
    speak(year)
    print(date) 
    print(month) 
    print(year)

     
def wishme():
    
    speak("welcome back sir")
    print("welcome back sir")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning sir!")
        print("good morning sir!")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
        print("good afternoon sir")
    elif hour>=18 and hour<24:
        speak("good evening sir")
        print("good evening sir")
    else:
        speak("good night sir")
        
    speak("jarvis at your service please tell me how can i help you?")
    print("jarvis at your service please tell me how can i help you?")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
     print("listening to your command...")
     r.pause_threshold = 1
     audio=r.listen(source)
     
    try:
        print("recognizing your command...")
        query=r.recognize_google(audio,language ='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again")
        print("say that again")
        return "none"
    return query


def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    print('CPU is at' + usage)
    battery=psutil.sensors_battery()
    speak("Battery percent is")
    speak(battery.percent)
    print("Battery percent is")
    print(battery.percent)
    
def jokes():
    speak(pyjokes.get_joke())
    print(pyjokes.get_joke())
    
if __name__=="__main__" :
    wishme()
    while True:
        query=takecommand().lower()
        
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("searching..")
            print("searching..")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'search in chrome' in query:
            speak("what should i search?")
            print("what should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search=takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            
        elif 'logout' in query:
            os.system("shutdown /l 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
       
            
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            jokes()
            
        elif 'offline' in query:
            quit()


        
        