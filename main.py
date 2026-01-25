import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "e360618b2e034ff3b96c1a35517d33e9"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
     tts = gTTS(text)
     tts.save('temp.mp3')


# Initialize pygame mixer
     pygame.mixer.init()

    # Load the MP3 file
     pygame.mixer.music.load("temp.mp3")

    # Play the MP3 (loops = 0 means play once, -1 means loop forever)
     pygame.mixer.music.play(loops=0)

    # Keep the program running long enough to hear the music
     while pygame.mixer.music.get_busy():  
        pygame.time.Clock().tick(10)

     pygame.mixer.music.unload()
     os.remove("temp.mp3")
    
    


def aiprocess(command):
    client = OpenAI(api_key="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",)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud.Give short responses please"},
    {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processcommand(c):
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
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles =  data.get('articles' , [])

            for article in articles:
                speak(article['title'])
      
    else:
        output = aiprocess(c)
        speak(output)
        pass
        # let openai handle the request






if __name__ == "__main__":
    speak("Intializing Jarvis....")
    while True:
        #listen for the wake word "Jarvis"
    # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=3,phrase_time_limit=3)
            word = r.recognize_google(audio)
            
            
            if "jarvis" in word.lower():   # More flexible check
                speak("Ya")  
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activate...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

                 
        except Exception as e:
            print("Error; {0}".format(e))

