import speech_recognition as sr
import pyttsx3

def AudioToText():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio) 
    except:
         text = "Sorry, I could not understand what you said."

    return text

def EngineRate():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)     

def EngineTalk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
