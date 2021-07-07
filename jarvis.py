import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import smtplib

# from datetime import datetime
import pytz



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoom!")

    else:
        speak("Good Evening!")

    speak("Hello! I am Jarvis. Please tell me how may i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(do, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yash9714457774@gmail.com', 'Yash@1506')
    server.sendmail('yash9714457774@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
   # while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
             speak('Searching Wikipedia...')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("According to Wikipedia")
             print(results)
             speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music ' in query:
            music_dir = 'F:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)

        elif "where is" in query:
            data = query.split(" ")
            location = data[2]
            speak("Hold on, I will show you where " + location + " is.")
            os.system('cmd /k "start chrome https://www.google.nl/maps/place/"'+ location)
        
        
        

        # elif 'open notepad' in query:
        #     codePath = "%windir%\system32\notepad.exe"
        #     os.startfile(codePath)

        elif 'email to yash' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "yash9714457774@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Yash!. Iam not able to send this email")
