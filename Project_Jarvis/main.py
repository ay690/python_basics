import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import requests
import musicLibrary


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "5acde251ae4045fb9def38f733735b25"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    # print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
   
    elif "news" in c.lower():
        print(f"{newsapi}")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            print(data)
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])


        

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    # Listen for the wake word "Jarvis" 
    # Obtain audio from microphone
    while True:
        r = sr.Recognizer()

        print("Recognizing")
        try:
           with sr.Microphone() as source:
             print("Listening....")
             audio = r.listen(source, timeout=10, phrase_time_limit=5)
  

           word = r.recognize_google(audio)
        
           if(word.lower() == "jarvis"):
               speak("Yeah")
               # Listen for word
               with sr.Microphone() as source:
                   print("jarvis active")
                   audio = r.listen(source)
                   command = r.recognize_google(audio)

                   processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
    
        