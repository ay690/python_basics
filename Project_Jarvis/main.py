import speech_recognition as sr
import webbrowser
import pyttsx3
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()


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
             audio = r.listen(source, timeout=2, phrase_time_limit=1)
            # print("Sphinx thinks you said" + r.recognize_sphinx(audio))

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
    
        