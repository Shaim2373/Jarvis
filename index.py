import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)  
engine.setProperty('voice', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
        
    elif hour>=12 and hour<18:
        speak("good afternoon!")
        
    else:
        speak("good Evening!")
        
    speak("I am jarvis sir. please tell me how can i help you")

def takeCommand():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        
        
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {command}\n")
        speak(f"User said: {command}\n")
        
    except Exception():
        # print(e)
        print("Say that again please...")
        return "None"
    return command



if __name__ == '__main__':
    wishMe()
    # while True:
    if 1:
        command = takeCommand().lower()
        
    
    
    
    
    if 'wikipedia' in command:
        speak('searching wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
        
          
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com/")
        
        
    elif 'open google' in command:
        webbrowser.open("https://www.google.com/")
            
            
    elif 'open facebook' in command:
            webbrowser.open("https://www.facebook.com/")
    
    
    elif 'the time' in command:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print("strTime")
    
    
    elif 'youtube play' in command:
        webbrowser.open("https://www.youtube.com/watch?v=7wtfhZwyrcc")
            
            