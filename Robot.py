import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

robot=pyttsx3.init() #tao object Robot
voice=robot.getProperty('voices') #lay giong
robot.setProperty('voice',voice[1].id) #chon giong

def speak(audio):
    print("Robot: " + audio)
    robot.say(audio)
    robot.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") #xac dinh thoi gian va sang chieu
    speak(Time)

def welcome():
    hour=datetime.datetime.now().hour #gio
    if hour >= 6 and hour < 12:
        speak("Good Morning Boss")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss")
    elif hour >= 18 and hour < 24:
        speak("Good Night Boss")
    speak('How can i help you')


def command():
    c=sr.Recognizer()
    with sr.Microphone() as source: #giong lay tu microphone
        c.pause_threshold=2 #lenh dung bao nhieu giay truoc khi nghe lenh moi
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Hương: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query=str(input('Your order is: '))
    return query

if __name__ == '__main__':
    welcome()
    while True:
        query=command().lower() #lay lenh chuyen thanh dang khong viet hoa de may de nhan dien
        if "google" in query:
            speak("What should i search Boss?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')

        if "youtube" in query:
            speak("What should i search Boss?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "open video":
            a=r"C:\Users\Huong\Desktop\a.mp4"
            os.startfile(a)

