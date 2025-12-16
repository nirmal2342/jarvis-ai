import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from dotenv import load_dotenv
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

load_dotenv()
newsapi = os.getenv("NEWS_API_KEY")

if not newsapi:
    print("ERROR: NEWS_API_KEY not found. Please set it in .env file.")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif c.startswith("play"):
        song = c.split(" ", 1)[1]
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Sorry, song not found in library")

    elif "news" in c:
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={newsapi}"
        )

        if r.status_code == 200:
            articles = r.json().get("articles", [])
            for article in articles:
                speak(article["title"])
        else:
            speak("Unable to fetch news at the moment")


if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yeah Nirmal")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
