import pyttsx3
import speech_recognition as sr
import os
import webbrowser as w
import wikipedia
import subprocess
import datetime
import pyautogui
import time
import requests
import pywhatkit as wk
import google.generativeai as genai
import cv2
import random
import operator
import sys
from dotenv import load_dotenv





engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
engine.setProperty('rate', 150)

# engine.say("Hello, I am your assistant. How can I help you today?")
# engine.runAndWait()  # Waits for the speech to finish


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
     
      r = sr.Recognizer()
      with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            # r.pause_threshold = 1
            print("Listening...")
            audio = r.listen(source)
            try:

                print("recogonizing....")
                query = r.recognize_google(audio, language="en-hi-in")
                print(f"user said: {query}")
                return query
            except sr.UnknownValueError:
                print("Sorry master, I did not understand that.")
                return ""
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
                return ""

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning master!")
    elif hour>=12 and hour<18:
        speak("good afternoon master!")
    else:
        speak("good evening master!")
    speak("ready to serve. how can i serve you?")


def conf():
    load_dotenv()

def get_weather(city, api_key):
    # Base URL for the OpenWeather API
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    
    # Complete URL
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"  # Using metric for Celsius
    
    # Sending a GET request to the API
    response = requests.get(complete_url)
    
    
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        
        main = data['main']
        weather = data['weather'][0]
        
       
        print(f"City: {data['name']} , Temperature: {main['temp']}°C ,Pressure: {main['pressure']} hPa , Humidity: {main['humidity']}% , Weather Description: {weather['description']}")
        speak(f"City: {data['name']} , Temperature: {main['temp']}°C ,Pressure: {main['pressure']} hPa , Humidity: {main['humidity']}% , Weather Description: {weather['description']}")
    else:
        print("City Not Found!")
        speak("City Not Found")
api_key = os.getenv('W_key')
# api_key = "89c33d140e50f4cb3db591cb528b9094"

def ai(query):
    

    # genai.configure(api_key="AIzaSyDbYFrawCr3lA-Nn2ubnf6sRi77HdJS4CM")
    genai.configure(api_key=os.getenv('ai_key'))

    generation_cofig = {"temperature": 0.9, "top_p":1, "top_k":1, "max_output_tokens": 2048}

    model = genai.GenerativeModel("gemini-pro", generation_config=generation_cofig)

    response = model.generate_content(query)

    ans=response.text
    return ans


def cls():
    pyautogui.keyDown('win')
    pyautogui.press('up')
    pyautogui.keyUp('win')
    time.sleep(1.5)
    pyautogui.moveTo(1883, 11, 1)
    pyautogui.click(x=1883, y=11, interval=0, button='left')



if __name__=="__main__":
    wish_me()
    conf()
    while True:
        # speak("hello sir, how can i help you")
        txt=takecommand().lower()
        sites=[["youtube","https://youtube.com"],["wikipedia",'https://wikipedia.com'],["google","https://google.com"],["browser","https://google.com"],["web browser","https://google.com"]]
        for site in sites:
            if f"open {site[0]}" in txt:
                w.open(site[1])
                speak(f"opening.....{site[0]},master ")
###########################################GENERAL COMMANDS#############################################


        if 'hey joy' in txt:
            print("yes sir")
            speak("yes sir")
        
     

        elif 'the time'  in txt: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"master the time is {strTime}")
        
        elif 'current time'  in txt: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"master the time is {strTime}")
        
        elif 'time now'  in txt: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"master the time is {strTime}")



        elif ('who is this' or 'what is this') in txt:
            print("I am the joy, aakshit sharma's assistance . who are you?")
            speak("I am the joy, akshit sharma's assistance . who are you?")

        elif 'i am akshit' in txt:
            print('hello master! i am ready to serve you. what i can do?')
            speak('hello master! i am ready to serve you. what i can do?')
        
        elif 'shut down the system' in txt:
            print("shutting down master")
            speak("shutting down master")
            os.system("shutdown /s /t 5")
        
        elif'restart the system' in txt:
            print("restarting master")
            speak("restarting master")
            os.system("shutdown /r /t 5")
        
        elif"undo the task" in txt:
            print("undoing the command")
            speak("undoing the command")
            pyautogui.press('backspace')
        
        elif "redo the task" in txt:
            print("redoing the command")
            speak("redoing the command")
            pyautogui.press('ctrl+shift+z')
        
        elif "hibernate the system" in txt:
            print("hibernating master")
            speak("hibernating master")
            os.system("shutdown /h /t 5")

         
        elif'go to sleep' in txt:
            
            speak("alright i am going to sleep")
            sys.exit()

        elif"justify the content" in txt:
            print("justifying the content")
            speak("justifying the content")
            pyautogui.press('ctrl+j')
        
        elif "underline the contant" in txt:
            speak("underlining the content")
            pyautogui.press('ctrl+u')
        
        elif"maximize the window" in txt:
            speak("maximizing the window")
            pyautogui.press('winup')
        
        elif"minimize the window" in txt:
            speak("minimizing the window")
            pyautogui.press('win down')

        elif "weather today".lower() in txt.lower():
            speak("please tell the name of city for weather forcast")
            city =takecommand()
        
            get_weather(city, api_key)
            speak("what else can i do for you master")
            print("what else can i do for you master")
            txt=takecommand()

        elif "temperature today".lower() in txt.lower():
            speak("please tell the name of city for weather forcast")
            city =takecommand()
            
            get_weather(city, api_key)
            speak("what else can i do for you master")
            print("what else can i do for you master")
            txt=takecommand()

        elif "today's temperature".lower() in txt.lower():
            speak("please tell the name of city for weather forcast")
            city =takecommand()
            
            get_weather(city, api_key)
            speak("what else can i do for you master")
            print("what else can i do for you master")
            txt=takecommand()


        elif "today's forecast".lower() in txt.lower():
            speak("please tell the name of city for weather forcast")
            city =takecommand()
            
            get_weather(city, api_key)
            speak("what else can i do for you master")
            print("what else can i do for you master")
            txt=takecommand()
        
        elif "forecast today".lower() in txt.lower():
            speak("please tell the name of city for weather forcast")
            city =takecommand()
            
            get_weather(city, api_key)
            speak("what else can i do for you master")
            print("what else can i do for you master")
            txt=takecommand()

############################# SEARCHIN ON SERVE#######################################################
        elif("what is my ip address") in txt:
            speak("checking..")
            try:
                ip = requests.get('https://api.ipify.org').text
                speak("your ip adress is" + ip)
                print(ip)
            except Exception as e:
                print(e)
                speak(" there is an erorr in checking ip address due to some technical issue. please try again after some time")

        elif 'what is' in  txt:
            speak("searching on wikipedia..")
            txt=txt.replace("what is", "")
            result = wikipedia.summary(txt, sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif 'news' in txt:
            speak("news are being read...")
            url = "https://news.google.com/topstories?hl=en-IN&gl=IN&"
            w.open(url)
            speak("news are being read master")
        
        elif'open youtube'in txt:
            speak("opening youtube master")
            speak("what you want to search on youtube master?")
            tt=takecommand().lower()
            wk.playonyt(f"{tt}")

        elif"search on Youtube".lower() in txt:
            speak("searching on youtube")
            tt=txt.replace("search on youtube",'')
            w.open(f"www.youtube.com/results?search_query={tt}")

        elif 'search on google' in txt:
            speak("searching...")
            txt = txt.replace("search", "")
            url = "https://google.com/search?q=" + txt
            w.open(url)
            speak("searching done master")

############ for apps open AND CLOSE #####################################
        elif'open paint' in txt:
            npath=""
            os.startfile(npath)
        # elif'close paint' in txt:
        #     os.system("taskkill /f/im mspaint.exe")
        
        elif'open notepad' in txt:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
        

        elif "open VS code" in txt:
            speak("opening..")
            pyautogui.locateCenterOnScreen("vs.jpg")
            time.sleep(1.5)
            pyautogui.doubleClick()
            speak("opened...")

        elif "open github" in txt:
            speak("opening..")
            pyautogui.locateCenterOnScreen("github.png")
            time.sleep(1.5)
            pyautogui.doubleClick()
            speak("opened...")

        elif "open kaggle" in txt:
            speak("opening..")
            pyautogui.locateCenterOnScreen("kaggle.png")
            time.sleep(1.5)
            pyautogui.doubleClick()
            speak("opened...")

        elif"close this" in txt:
            speak("closing..")
            pyautogui.keyDown('win')
            pyautogui.press('up')
            pyautogui.keyUp('win')
            time.sleep(1.5)
            pyautogui.moveTo(1883, 11, 1)
            pyautogui.click(x=1883, y=11, interval=0, button='left')
        
        # elif'close notepad' in txt:
        #     os.system("taskkill /f/im notepad.exe")


        elif"open camera" in  txt:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(50)==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        
        elif"take a screenshot" in txt:
            speak('tell me te file name:')
            name=takecommand().lower()
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif"volume up" in txt:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        
        elif "volume down" in txt:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        
        elif "mute" in txt:
            pyautogui.press("volumemute")
        
        elif"unmute" in txt:
            pyautogui.press("volumemute")
        


        ############################ OPEN MUSIC #################################
        elif 'play music' in txt:
            print("playing music")
            speak("playing music")
            music_dir = 'C:\\Users\\Joy\\Music\\Songs'# ADRESS
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))# SONGS==RANDOM CHOICE(SONGS)

       ##################### PLAY VIDEO##################################
        elif 'play video' in txt:
            print("playing video")
            speak("playing video")
            video_dir = 'C:\\Users\\Joy\\Videos\\Movies'# ADDRESS
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[0]))# VIDEOS==RANDOM CHO



#####################################################################################################
        elif"close browser" in txt:
            os.system('taskkill /f /im chrome.exe')
            speak("browser is closed master")
        elif"close firefox" in txt:
            os.system('taskkill /f /im firefox.exe')
            speak("browser is closed master")
        elif"close edge" in txt:
            os.system('taskkill /f /im msedge.exe')
            speak("browser is closed master")


            ################################### LEFT ############################################
        
        elif'type' in txt: #10
            txt=txt.replace("type","")
            pyautogui.typewrite(f'{txt}',0.1)

        elif'goodbye' in txt:
            print("goodbye master")
            speak("goodbye master")
            break
        elif  'bye' in txt:
            print("goodbye master")
            speak("goodbye master")
            break
        elif'STOP' in txt:
            print("goodbye master")
            speak("goodbye master")
            break
        elif'' in txt:
            None
        else:
            print(f"what i found is :{ai()}")
            speak(f"what i found is :{ai()}")



        
    
