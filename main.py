import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":    
    
    speak("Initializing Jarvis......")

    # listen for wake 

    while True :
     r = sr.Regognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try :
         print()