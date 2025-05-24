import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import pytz
import smtplib
import email_dict
import email_details
import os
import random
import pyautogui
import time

r = sr.Recognizer()
eng = pyttsx3.init()

def speak(txt):
    eng.say(txt)
    eng.runAndWait()

def takecommand():
      with sr.Microphone() as src2:
             r.adjust_for_ambient_noise(src2,duration=0.5)
             r.pause_threshold = 0.5
             print("Listning....")
             aud2 = r.listen(src2)
             print("Recognizing...")
             txt1 = r.recognize_google(aud2)
             return txt1

def wish():
    utc = datetime.datetime.now()
    india_time = utc.astimezone(pytz.timezone('Asia/Kolkata'))
    hr = india_time.hour
    if hr>=0 and hr<5:
        x1="Good Night Sir!!How may I help you?"
        print(x1)
        speak(x1)
    elif hr>=5 and hr<12:
        x2="Good Morning sir!!How may I help you?"
        print(x2)
        speak(x2)
    elif hr==12:
        x3="Good Noon Sir!!How may I help you?"
        print(x3)
        speak(x3)
    elif hr>12 and hr<18:
        x4="Good Afternoon Sir!!How may I help you?"
        print(x4)
        speak(x4)
    elif hr>=18 and hr<=23:
        x5="Good Evening Sir!!How may I help you?"
        print(x5)
        speak(x5)
        
def search(query):
    res = wikipedia.page(query)
    link=res.url
    webbrowser.open(link)

def open(query):
    webbrowser.open(query)

def show(query):
     result = wikipedia.summary(query,sentences = 2)
     return result

def get_random(length):
    rand=random.randint(0,length)
    return rand

def send_email(to,content):
    a= email_details.details.get("email_id")
    b= email_details.details.get("password")
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(a,b)
    server.sendmail(a,to,content)
    server.close()

if __name__ == "__main__":
    wish()
    while(1):
        try:
            txt2 = takecommand().strip().lower()
            print("User: "+txt2)
            if "good morning" in txt2:
                t1="Good Morning to you also sir!!"
                print(t1)
                speak(t1)   
            elif "good evening" in txt2:
                t2="Good Evening to you also sir!!"
                print(t2)
                speak(t2)
            elif "good night" in txt2:
                t3="Good night to you also sir!!"
                print(t3)
                speak(t3)
            elif "how are you" in txt2:
                t4="I'm doing great, thanks for asking! How can I assist you today?"
                print(t4)
                speak(t4)
            elif "open youtube" in txt2:
                t5="Opening Youtube"
                print(t5)
                speak(t5)
                open("youtube.com")
            elif "open google" in txt2:
                t6="Opening Google"
                print(t6)
                speak(t6)
                open("google.com")
            elif "wikipedia" in txt2:
                t7="Searching from Wikipedia"
                print(t7)
                speak(t7)
                x=txt2.replace("wikipedia","")
                search(x)
            elif "show details of" in txt2:
                t8="Searching details..."
                print(t8)
                speak(t8)
                x=txt2.replace("show details of","")
                details=show(x)
                print(details)
                speak(details)
            elif "on google" in txt2:
                t9="Searching on Google..."
                print(t9)
                speak(t9)
                x=txt2.replace("search ","")
                y=x.replace(" on google","")
                url = f"https://www.google.com/search?q={y}"
                open(url)
            elif "open chat gpt" in txt2:
                t10="Opening chatgpt..."
                print(t10)
                speak(t10)
                open("chatgpt.com")
            elif "on youtube" in txt2:
                t11="Searching on youtube..."
                print(t11)
                speak(t11)
                x=txt2.replace("search ","")
                y=x.replace(" on youtube","")
                url = f"https://www.youtube.com/search?q={y}"
                open(url)
            elif "time" in txt2:
                utc = datetime.datetime.now().strftime("%H:%M:%S:%p") 
                t12="the time is "+ utc
                print (t12)
                speak (t12)
            elif "send email" in txt2:
                x=txt2.replace("send email to ","")
                try:
                    for i in email_dict.email:
                        if x == i:
                            to=email_dict.email[i]
                            t13="What should I say?"
                            print(t13)
                            speak(t13)
                            content=takecommand().strip().lower()
                            print("User: "+content)
                            send_email(to,content)
                            t14="Email has been sent successfully!"
                            print(t14)
                            speak(t14)
                except:
                    err2="email can`t be sent"
                    print(err2)
                    speak(err2)
            elif "date" in txt2:
                date=datetime.date.today().strftime("%d-%B-%Y-%A")
                t15="Today is, "+date
                print(t15)
                speak(t15)
            elif "open vs code" in txt2:
                path="C:\\Users\\PRATIK SAHA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                t16="Opening VS code..."
                print(t16)
                speak(t16)
                os.startfile(path)
            elif "play a song" in txt2 or "play music" in txt2:
                path="C:\\Users\\PRATIK SAHA\\OneDrive\\Desktop\\project1\\Successful proj\\FRIDAY AI\\songs.mp3" 
                t17="Playing songs..."
                print(t17)
                speak(t17)
                songs=os.listdir(path)
                x=get_random(len(songs)-1)
                os.startfile(os.path.join(path,songs[x]))
            elif "spotify" in txt2:
                t18="Playing spotify..."
                print(t18)
                speak(t18)
                url = f"https://open.Spotify.com"
                webbrowser.open(url)
                time.sleep(7)
                pyautogui.press("space")
            elif "chrome"in txt2:
                t19="Opening Google Chrome..."
                print(t19)
                speak(t19)
                open("google chrome.com")
            elif "stop" in txt2  or "bye" in txt2:
                t0="Stopping the program!! Good bye Sir!! Thank you for your Time."
                print(t0)
                speak(t0)
                exit()
            elif "thank you" in txt2 or "thanks" in txt2:
                t00="You`re welcome, Let me know if I can assist you further."
                print(t00)
                speak(t00)
                exit() 
            else:
                err0="Did you say something ?"
                print(err0)
                speak(err0)
        except sr.RequestError:
             err1="Speech Convertion not Possible! Check your Internet Connection!"
             print(err1)
             speak(err1)
        except sr.UnknownValueError:
             err2="Audio is not clear!!"
             print(err2)
             speak(err2) 