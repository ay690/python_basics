import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import pygame
import requests
import musicLibrary
# import random
import pyautogui
from gtts import gTTS
from groq import Groq


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "5acde251ae4045fb9def38f733735b25"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


def aiCommand(command):
    client = Groq(api_key="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",)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content":"You are a Virtual Assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."
            },
            {
                "role": "user",
                "content": command
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content
       
def terminateJarvis():
    response = "Pleasure helping you sir"
    speak(response)
    exit()


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

    elif "volume up" in c.lower():
        for _ in range(5):
            pyautogui.press("up")
        speak("Volume increased")

    elif "volume down" in c.lower():
        for _ in range(5):
            pyautogui.press("down")

        speak("Volume decreased")
    
    # elif "mute" in c.lower():
    #     pyautogui.hotkey("alt", "tab")
    #     pyautogui.press("m")
    #     speak("Muted")

    # elif "umute" in c.lower():
    #     pyautogui.hotkey("alt", "tab")
    #     pyautogui.press("m")
    #     speak("Umuted")

    elif "news" in c.lower():
        # print(f"{newsapi}")
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
    
    else:
        # Let groq AI handle the request
        output = aiCommand(c)
        speak(output)
     
      

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
             audio = r.listen(source, timeout=5, phrase_time_limit=5)
  

           word = r.recognize_google(audio)
        
           if(word.lower() == "jarvis"):
               speak("Yeah")
               # Listen for word
               with sr.Microphone() as source:
                   print("Jarvis Activated")
                   audio = r.listen(source)
                   command = r.recognize_google(audio)

                   if "thank you jarvis" in command.lower():
                       terminateJarvis()

                   processCommand(command)

                   
        except Exception as e:
            print("Error; {0}".format(e))
    
       