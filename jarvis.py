import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0])
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        print("Say that again")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ajaymayani96@gmail.com','asth@0883')
    server.sendmail('ajaymayani96@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    # speak('ajay is a good boy')
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir);
            # print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%HH:%M:%S')
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'ajay' in query:
            try:
                speak("what should I say,")
                content = takeCommand()
                to = "ajmayani7@gmail.com"
                sendEmail(to,content)
                speak("email has been sent ")
            except Exception as e:
                print(e)
                print('Sorry I am not able to send this email right now......!')