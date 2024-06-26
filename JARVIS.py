from asyncio import Task
import operator
import geocoder
import os
from re import search
import psutil
import webbrowser
import requests
from requests import get
import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import sys
import pyjokes
import pywikihow 
from pywikihow import search_wikihow
import random
import pyaudio
import speedtest
import pyautogui
import time
from PIL import Image   
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import string
import random
from flask import Flask, render_template, redirect, url_for, request
import imdb
import pywifi
from pywifi import const
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import wifi
from gtts import gTTS
from  tkinter import *
from tkinter import messagebox
import psutil
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import requests
from playsound import playsound
import numpy
import matplotlib
import os
import json
import requests

def loading_screen():
    import tkinter as tk
    import time 

    root = tk.Tk()
    root.title("Loading Screen")
    root.geometry('300x100')

    label = tk.Label(root, text="Loading...", font=('Helvetica', 18))
    label.pack(pady=20)

    # Update the label text after 1 second and then close the window after 10 seconds
    root.after(1000, lambda: label.config(text="Loading... Please wait"))
    root.after(10000, root.destroy)

    root.mainloop()


def snap_to_close_checker_of_instagram_status():
    import numpy as np
    import pyaudio
    import subprocess
    from PIL import Image
    import time
    import pyautogui
    import os
    import sys 

    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 20000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for snap...")

    while True:
            # Read a chunk of data from the stream
        data = stream.read(CHUNK)

            # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)

            # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

            # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

            # Check if the maximum amplitude exceeds the threshold
        
        if max_amp > THRESHOLD:
            print('snap !')
            pyautogui.hotkey('alt', 'f4')
            break
            
    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()
def page(nof2, nofe2):

    from tkinter import messagebox
    import instaloader
    
    root = Tk()
    root.configure(bg='black')
    root.geometry("500x250")

    font=('Areal',20)

    lable1 = Label(root, text="FOLLOWING -->", bg='black',  fg='WHITE', font = ('Areal', 20))
    lable1.place(x=50,y=110)

    label2 = Label(root, text='FOLLOWERS -->', bg = 'black', fg ='white', font=('Areal', 20) )
    label2.place(x=50, y=160)

    label3 = Label(root , text="INSTAGRAM",          bg ='black', fg = 'white', font=('Areal', 30))
    label3.place(x=125, y= 50)

    label4 = Label(root ,     text= nofe2 ,      bg = 'black', fg = 'white', font=('Areal', 20))
    label4.place(x=280, y= 110)

    label5 = Label(root ,     text= nof2 ,      bg = 'black', fg = 'white', font=('Areal', 20))
    label5.place(x=280, y= 160)
    root.mainloop()


def search_mode():
    import os
    import json
    import requests
    query2 = takecommand().lower()
    api_key = "AIzaSyAE2oZnYYC_HGjGbAvyFJUjvR2SSejm1wE"
    cx = "113ddcdbb1e7f47ea"
    answer = get_answer(query2, api_key, cx)
    print(answer)
    speak(answer)

def google_search(query2, api_key, cx):
    import os
    import json
    import requests
    service_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': query2,
        'num': 10,
    }
    response = requests.get(service_url, params=params)
    return response.json()

def get_answer(query2, api_key, cx):
    import os
    import json
    import requests
    search_results = google_search(query2, api_key, cx)
    if search_results.get('items'):
        return search_results['items'][1]['snippet']
    else:
        return "I couldn't find an answer to that question."





def introduction_and_system():
    from asyncio import Task
    import operator
    import geocoder
    import os
    from re import search
    import psutil
    import webbrowser
    import requests
    from requests import get
    import subprocess
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import wikipedia
    import pywhatkit
    import sys
    import pyjokes
    import pywikihow 
    from pywikihow import search_wikihow
    import random
    import pyaudio
    import speedtest
    import pyautogui
    import time
    from PIL import Image   
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    import string
    import random
    from flask import Flask, render_template, redirect, url_for, request
    import imdb
    import pywifi
    from pywifi import const
    from bs4 import BeautifulSoup
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    import wifi
    from gtts import gTTS
    from tkinter import messagebox
    import psutil
    import cv2
    import tkinter as tk
    from PIL import Image, ImageTk
    import cv2
    import requests
    from playsound import playsound
    speak(".....2.3.1")
    startup_sound = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\computersound.mp3"
    speak('initialising system ')
    playsound(startup_sound)
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    print(f"Memory Usage: {memory_percent}%")
    disk_info = psutil.disk_usage('/')
    disk_percent = disk_info.percent
    print(f"Disk Usage: {disk_percent}%")
    ipaddress=geocoder.ip('me')
    print(ipaddress.latlng)
    wishme()
    bd_checker()
    clap()






































def bd_checker():
    import datetime

    now = datetime.datetime.now()
    if now.month == 5 and now.day == 9:
        print("hey sir today is your mom and dad's anniversary , have you wished them yet ???")
        speak("hey sir today is your mom and dad's anniversary , have you wished them yet ???")
    if now.month == 5 and now.day == 5:
        print("hey sir today is your mom's birthday , have you wished her yet")
        speak("hey sir today is your mom's birthday , have you wished her yet")
    if now.month == 5 and now.day == 31:
        print("hey sir today is your sister's birthday , have you wished her yet")
        speak("hey sir today is your sister's birthday , have you wished her yet")
    if now.month == 1 and now.day == 2:
        print("hey sir today is your dad's birthday , have you wished him yet")
        speak("hey sir today is your dad's birthday , have you wished him yet")
    if now.month == 9 and now.day == 6:
        print("HAPPY BIRTHDAY !!!!!!")
        speak("happy birthday sir , what should i buy you as a gift ?")


def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_advice(bmi):
    if bmi < 18.5:
        speak("You are underweight. Try to eat more protein-rich foods like lean meats, eggs, and dairy products. Also, consider strength training exercises to build muscle mass.")
    elif 18.5 <= bmi < 24.9:
        speak("You are at a healthy weight. Keep up the good work! Try to maintain a balanced diet and regular exercise.")
    elif 25.0 <= bmi < 29.9:
        speak("You are overweight. Try to reduce your calorie intake and increase your physical activity. Consider a combination of cardio and strength training exercises.")
    else:
        speak("You are obese. It's important to consult with a healthcare professional for advice on weight loss. Consider a combination of dietary changes and regular exercise.")

    
def bmi_checker():


    height_cm = float(input("Enter your height in centimeters: "))
    weight_kg = float(input("Enter your weight in kilograms: "))
    bmi = calculate_bmi(height_cm, weight_kg)
    print(f"Your BMI is {bmi:.2f}")
    print(bmi_advice(bmi))


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#engine.setProperty('voice' , voices[0].id)
engine.setProperty('rate', 150)
# Create a VideoCapture object
cap2 = cv2.VideoCapture('C:\\Users\\pcper\\OneDrive\\Pictures\\img\\ironmangifff.gif')

# Define the main window
root = tk.Tk()

# Create a label to display the video
label = tk.Label(root)
label.pack()

# Define a function to update the frame
def update_frame():
    ret, frame = cap2.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.config(image=imgtk)
        root.after(10, update_frame)
    else:
        cap2.release()
        root.destroy()






def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...................................................................................................................................")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....................................................")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")


    except Exception as e:
        print("say that again please")
        return "none"
    return query 
def songs_wala_close_fuction():
    import numpy as np
    import pyaudio
    import subprocess
    from PIL import Image
    import time
    import pyautogui
    import os
    import sys 
    import pywhatkit as pyw

    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 20000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for snap...")

    while True:
            # Read a chunk of data from the stream
        data = stream.read(CHUNK)

            # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)

            # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

            # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

            # Check if the maximum amplitude exceeds the threshold
        
        if max_amp > THRESHOLD:
            print('snap !')
            pyautogui.press('space')
            speak('what do you want sir ?')
            while True:
                tc = takecommand().lower()
                if 'stop' in tc:
                    speak('okay sir , i am closing the song')
                    os.system("taskkill /f /im msedge.exe")
                    break
                if 'continue' in tc:
                    speak("okay sir.")
                    pyautogui.press('space')
                    songs_wala_close_fuction()
                    break
                if 'play another song' in tc:
                    sad_songs = ['kaise hua song','yaha koi nahi yaha koi nahi yaha koi bhi nahi song', 'dagabaaz re song', 'let her go song', 'pal pal dil ke paas song', 'my queen song', 'hale dil' , 'guzarish', 'itna na tu mujse pyaar badha song', 'jane nahi denge tuje song 3 idots','give me some sunshine', 'kisi ki muskarahato pe ho nisar song old one', 'Aa Chal Ke Tujhe old song' ]
                    fonk = ['funk of the dammed', 'tokyo drift song', "Leat'eq - Tokyo Official Music Video HD", 'twirling song' ,  ]
                    moj_masti = ['ms dhoni song', 'trollywood1', 'tokyo song','dol jageero da song', 'na jaiyo mere desi look te tane maar dega mera attitude bavli song','murder song', '12 bande song ' , 'lalkaara song', 'hamare sath shri ragunath to kis baat ki chinta hai song', 'nature song', 'splender song by harsh likhari' , 'dior song by shubh', 'arjan valley ne song' , 'laado song' , 'daku song by sidhu moosewala', 'old skool by sidhumoosewala'  ]
                    angrezi = ['chery chery ladies song', 'happy nation song']
                    ss_sad_songs = random.choice(sad_songs)
                    s_fonk = random.choice(fonk)
                    s_moj_masti = random.choice(moj_masti)
                    s_angrezi = random.choice(angrezi)
                    speak('okay sir.')
                    os.system("taskkill /f /im msedge.exe")
                    speak('what kind of song you would consider to listen')
                    wks = takecommand().lower()
                    if 'sad' in wks:
                        speak('okay sir , playing a sad song')
                        pyw.playonyt(ss_sad_songs)
                        songs_wala_close_fuction()
                        break
                    if 'gym' in wks:
                        speak('okay sir , playing a song for gym or workout')
                        pyw.playonyt(s_fonk)
                        songs_wala_close_fuction()
                        break
                    if 'indian' in wks:
                        speak('okay sir , playing an indian song')
                        pyw.playonyt(s_moj_masti)
                        songs_wala_close_fuction()
                        break
                    if 'english' in wks:
                        speak('okay sir , playing an english song')
                        pyw.playonyt(s_angrezi)
                        songs_wala_close_fuction()
                        break
                    else:
                        print('could not recognize the type of song you are talking about !')
                else:
                    print("i didn't understood what you said ! ")
            break
            
            
    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()
def get_top_news():
    from bs4 import BeautifulSoup
    url = 'https://www.bbc.co.uk/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('h3')
    news = [headline.get_text() for headline in headlines]
    return news
def fetch_google_news(country='in'):
    from newsapi import NewsApiClient
    # Initialize NewsApiClient with your API key
    newsapi = NewsApiClient(api_key='98eabf16c7a74b089e09f862731156b2')

    # Fetch top headlines for India
    top_headlines = newsapi.get_top_headlines(country=country)

    # Extract and return headlines
    headlines = [article['title'] for article in top_headlines['articles']]
    return headlines

def get_cpu_times_percent():
    cpu_times = psutil.cpu_times_percent(interval=1)
    print(f"CPU Times Percent: {cpu_times}")
    speak(f"CPU Times Percent: {cpu_times}")
def get_memory_info():
    import psutil
    memory_info = psutil.virtual_memory()
    print(f"Memory Total: {memory_info.total / (1024 * 1024)} MiB")
    speak(f"total Memory : {memory_info.total / (1024 * 1024)} MiB")
    print(f"Memory Available: {memory_info.available / (1024 * 1024)} MiB")
    speak(f"Memory Available: {memory_info.available / (1024 * 1024)} MiB")
    print(f"Memory Used: {memory_info.used / (1024 * 1024)} MiB")
    speak(f"Memory Used: {memory_info.used / (1024 * 1024)} MiB")
    print(f"Memory Percent: {memory_info.percent}%")
    speak(f"Memory Percent: {memory_info.percent}%")

def get_disk_usage():
    import psutil
    disk_info = psutil.disk_usage('/')
    disk_percent = disk_info.percent
    print(f"Disk Usage: {disk_percent}%")
    speak(f'your disk usage is {disk_percent}')
def get_memory_usage():
    import psutil
    memory_info = psutil.virtual_memory()
    memory_percent = memory_info.percent
    print(f"Memory Usage: {memory_percent}%")
    speak(f"your memory usage is {memory_percent}")

def search_pdf(query):
    import requests
    import os
    import webbrowser
    # Replace with your own Google Custom Search Engine ID
    search_engine_id = "113ddcdbb1e7f47ea"
    # Replace with your own Google Custom Search API key
    api_key = "AIzaSyAE2oZnYYC_HGjGbAvyFJUjvR2SSejm1wE"

    # Construct the search URL
    url = f"https://www.googleapis.com/customsearch/v1?q={query}+filetype:pdf&cx={search_engine_id}&key={api_key}"

    # Make the search request
    response = requests.get(url)

    # Parse the response JSON
    data = response.json()

    # Check if any PDF results were found
    if "items" in data and len(data["items"]) > 0:
        # Extract the first PDF result link
        pdf_link = data["items"][0]["link"]
        print("PDF link found:")
        webbrowser.open(pdf_link)

    else:
        print("No PDF files found for the given query.")


def login_page():
    import pyautogui
    while True:
        username = pyautogui.prompt(text='ENTER YOUR USERNAME HERE : ', title='USERNAME' , default='')
        if username == 'ashmit':
            password = pyautogui.password(text="ENTER THE PASSWORD HERE", title="PASSWORD", default='', mask='*')
            if password == 'wasd':
                speak('welcome sir you have logged in to jarvis administration , you can clap to wake me up.')
                break
            else:
                speak('wrong password')
        else:
            speak('wrong username')
def snap_to_close_notepad():
    import numpy as np
    import pyaudio
    import subprocess
    from PIL import Image
    import time
    import pyautogui
    import os
    import sys 

    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 20000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for snap...")

    while True:
            # Read a chunk of data from the stream
        data = stream.read(CHUNK)

            # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)

            # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

            # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

            # Check if the maximum amplitude exceeds the threshold
        
        if max_amp > THRESHOLD:
            print('snap !')
            os.system("taskkill /f /im notepad.exe")
            break
            
    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()
def clickspace():
    import numpy as np
    import pyaudio
    import subprocess
    from PIL import Image
    import time
    import pyautogui
    import os
    import sys 

    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 20000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for snap...")

    while True:
            # Read a chunk of data from the stream
        data = stream.read(CHUNK)

            # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)

            # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

            # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

            # Check if the maximum amplitude exceeds the threshold
        
        if max_amp > THRESHOLD:
            print('snap !')
            time.sleep(2)
            pyautogui.press('space')
            break
            
    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()
def wakeup():
    while True:
        permission = takecommand().lower()

        if 'wake up' in permission:
            taskexecution()

        if 'shut down' in permission:
            import sys 
            from playsound import playsound
            speak("thanks for your time sir")
            shutdown_snd = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\wake-up-the-robot-84894.mp3"
            playsound(shutdown_snd)
            sys.exit()

        if 'shutdown' in permission:
            import sys 
            from playsound import playsound
            speak("thanks for your time sir")
            shutdown_snd = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\wake-up-the-robot-84894.mp3"
            playsound(shutdown_snd)
            sys.exit()

        elif 'uth' in permission:
            taskexecution()

        elif 'utho' in permission:
            taskexecution()


        elif 'utha' in permission:
            taskexecution()

        elif 'makeup' in permission:
            taskexecution()

        elif 'make up' in permission:
            taskexecution()

        elif 'breakup' in permission:
            taskexecution()

        elif 'break up' in permission:
            taskexecution()

        elif 'wakeup' in permission:
            taskexecution()

        elif 'up' in permission:
            taskexecution()

        elif 'jarvis' in permission:
            taskexecution()

        elif 'connect to tenda' in permission:
            speak("okay sir")
            ssid = "Tenda"
            password = "Password"
            connect_to_wifi(ssid, password)

        elif 'connect to ashmit' in permission:
            speak("okay sir")
            ssid = "ashmit_airtel"
            password = "54zlbgyk"
            connect_to_wifi(ssid, password)           
def ctcp2():
    import numpy as np
    import pyaudio
    import subprocess
    from PIL import Image
    import time
    import pyautogui
    import os
    import sys 

    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 20000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for snap...")

    while True:
            # Read a chunk of data from the stream
        data = stream.read(CHUNK)

            # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)

            # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

            # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

            # Check if the maximum amplitude exceeds the threshold
        
        if max_amp > THRESHOLD:
            img1 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img1.jpeg"
            img2 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img2.jpeg"
            img3 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img3.jpeg"
            img4 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img4.jpeg"

            print("snap!")
            with pyautogui.hold('alt'):
                pyautogui.press('f4')
            time.sleep(1)
            if os.path.exists(img3):
                image = Image.open(img3)
                image.show()
                break
            else: 
                print("error")
                speak('error')
            
    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()
def ctcp3():
    import numpy as np
    import pyaudio
    import subprocess
    from PIL import Image
    import time
    import pyautogui
    import os
    import sys 

    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 20000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for snap...")

    while True:
            # Read a chunk of data from the stream
        data = stream.read(CHUNK)

            # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)

            # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

            # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

            # Check if the maximum amplitude exceeds the threshold
        
        if max_amp > THRESHOLD:
            img1 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img1.jpeg"
            img2 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img2.jpeg"
            img3 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img3.jpeg"
            img4 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img4.jpeg"

            print("snap!")
            with pyautogui.hold('alt'):
                pyautogui.press('f4')
            time.sleep(1)
            if os.path.exists(img4):
                image = Image.open(img4)
                image.show()
                break
                
            else: 
                print("error")
                speak('error')
            
    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()
def timetable():
    from PIL import Image 
    import os
    from datetime import date
    today = date.today()
    print( today.strftime("%A"))
    speak('okay sir , should i also open the time table ')
    tt = "C:\\Users\\pcper\\OneDrive\\Desktop\\timetable1.png"

    if os.path.exists(tt):
        image = Image.open(tt)
        image.show()
    else:
        print("eroor 40000004")



def ctcp4():
    import numpy as np
    import pyaudio
    import subprocess
    from PIL import Image
    import time
    import pyautogui
    import os
    import sys 

    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 20000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for snap...")

    while True:
            # Read a chunk of data from the stream
        data = stream.read(CHUNK)

            # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)

            # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

            # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

            # Check if the maximum amplitude exceeds the threshold
        
        if max_amp > THRESHOLD:
            img1 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img1.jpeg"
            img2 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img2.jpeg"
            img3 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img3.jpeg"
            img4 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img4.jpeg"

            print("snap!")
            with pyautogui.hold('alt'):
                pyautogui.press('f4')
            break

    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()
def clap_to_close_images():
    import numpy as np
    import pyaudio
    import subprocess
    from PIL import Image
    import time
    import pyautogui
    import os
    import sys 

    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 20000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for snap...")

    while True:
            # Read a chunk of data from the stream
        data = stream.read(CHUNK)

            # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)

            # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

            # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

            # Check if the maximum amplitude exceeds the threshold
        
        if max_amp > THRESHOLD:
            print('snap !')
            pyautogui.hotkey('alt', 'f4')
            break
            
    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()

def clap_to_close():

    import numpy as np
    import pyaudio
    import subprocess
    from PIL import Image
    import time
    import pyautogui
    import os
    import sys 

    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 20000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for snap...")

    while True:
            # Read a chunk of data from the stream
        data = stream.read(CHUNK)

            # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)

            # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

            # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

            # Check if the maximum amplitude exceeds the threshold
        
        if max_amp > THRESHOLD:
            print('snap !')
            os.system("taskkill /f /im msedge.exe")
            break
            
    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()

def clap_to_close_manually():

    import numpy as np
    import pyaudio
    import subprocess
    from PIL import Image
    import time
    import pyautogui
    import os
    import sys 

    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 20000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for snap...")

    while True:
            # Read a chunk of data from the stream
        data = stream.read(CHUNK)

            # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)

            # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

            # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

            # Check if the maximum amplitude exceeds the threshold
        
        if max_amp > THRESHOLD:
            print('snap !')
            pyautogui.hotkey('ctrl', 'w')
            break
            
    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()

def ctcp():
    import numpy as np
    import pyaudio
    import subprocess
    from PIL import Image
    import time
    import pyautogui
    import os
    import sys 

    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 20000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for snap...")

    while True:
            # Read a chunk of data from the stream
        data = stream.read(CHUNK)

            # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)

            # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

            # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

            # Check if the maximum amplitude exceeds the threshold
        
        if max_amp > THRESHOLD:
            img1 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img1.jpeg"
            img2 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img2.jpeg"
            img3 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img3.jpeg"
            img4 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img4.jpeg"

            print("snap!")
            with pyautogui.hold('alt'):
                pyautogui.press('f4')
            time.sleep(1)
            if os.path.exists(img2):
                image = Image.open(img2)
                image.show()
                break
                
            else: 
                print("error")
                speak('error')
            
    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()

def wishme():
    from playsound import playsound
    hour = int(datetime.datetime.now().hour)
    today_date = datetime.datetime.today()

    day_name = today_date.strftime("%A")

    if hour>0 and hour<12:
        speak(f"this is {day_name}morning")

    elif hour>12 and hour<18:
        speak(f"this is {day_name} afternoon")

    else:
        speak(f"this is {day_name} evening")

    speak('not need to introduce myself , i am jarvis , the virtual artificial intelligence and i am here to assist you with a variety of tasks , 24 hours a day , 7 days a week , importing all prefrences from horon interface , system is now fully operational')
    startup = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\wake-up-the-robot-84894.mp3"
    playsound(startup)




def send_message_on_instagram():
    import time
    speak("whom do you want to message")
    wtbt = takecommand().lower()
    if 'navya' in wtbt:

        import webbrowser
        import time 
        import pyautogui
        webbrowser.open("https://www.instagram.com/direct/t/17842168340903893/")
        time.sleep(5)
        speak("okay sir what should i text her")
        whtbt = takecommand().lower()
        pyautogui.typewrite(whtbt)
        pyautogui.press("enter")
        with pyautogui.hold("ctrl"):
            pyautogui.press('w')

    elif 'aryan' in wtbt:
        import webbrowser
        import time 
        import pyautogui
        webbrowser.open("https://www.instagram.com/direct/t/17851126326074412/")
        time.sleep(5)
        speak("okay sir what should i text him")
        whtbt2 = takecommand().lower()  
        pyautogui.typewrite(whtbt2)
        pyautogui.press('enter')
        with pyautogui.hold("ctrl"):
            pyautogui.press('w')

    elif 'agamjot' in wtbt:
        import webbrowser
        import pyautogui
        import time
        webbrowser.open("https://www.instagram.com/direct/t/17843047149026849/")
        time.sleep(5)
        speak("okay sir what should i text him")
        whtbt3 = takecommand().lower()
        pyautogui.typewrite(whtbt3)
        pyautogui.press('enter')
        with pyautogui.hold("ctrl"):
            pyautogui.press('w') 

    elif 'group chat' in wtbt or 'groupchat' in wtbt or 'group chart' in wtbt:
        import webbrowser
        import pyautogui
        import time
        webbrowser.open("https://www.instagram.com/direct/t/7053905471345637/")
        time.sleep(5)
        speak("okay , what should i text in the group chat")
        whtbt4 = takecommand().lower()
        pyautogui.typewrite(whtbt4)
        pyautogui.press('enter')
        with pyautogui.hold("ctrl"):
            pyautogui.press('w')

    elif 'bhaiya' in wtbt:
        import webbrowser
        webbrowser.open("https://www.instagram.com/direct/t/105034864229683/")
        time.sleep(5)
        speak("okay sir what should i text him")
        whtbt5 = takecommand().lower()
        pyautogui.typewrite(whtbt5)
        pyautogui.press("enter") 
        with pyautogui.hold("ctrl"):
            pyautogui.press('w')
def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()

    # Get the first interface (usually there's only one)
    iface = wifi.interfaces()[0]

    # Disconnect from any existing WiFi network
    iface.disconnect()

    # Wait a moment to ensure the interface is disconnected
    # This step might be necessary depending on your system
    import time
    time.sleep(1)

    # Create a profile
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    # Add the profile
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    # Connect to the WiFi network
    iface.connect(tmp_profile)

    # Wait for connection status
    while iface.status() == const.IFACE_CONNECTING:
        pass

    if iface.status() == const.IFACE_CONNECTED:
        print("Connected to", ssid)
    else:
        print("Connected to", ssid)

def clap():
    import numpy as np
    import pyaudio
    from playsound import playsound


    CHUNK = 1024  # Number of samples per frame
    FORMAT = pyaudio.paInt16  # Audio format
    CHANNELS = 1  # Number of channels (mono)
    RATE = 44100  # Sampling rate
    THRESHOLD = 25000  # Amplitude threshold for clap detection

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream on the default input device
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for claps...")

    while True:
        # Read a chunk of data from the stream
        data = stream.read(CHUNK)

        # Convert the data to an array of integers
        data_int = np.frombuffer(data, dtype=np.int16)
        
        # Calculate the absolute value of the data
        data_abs = np.abs(data_int)

        # Find the maximum amplitude in the chunk
        max_amp = np.max(data_abs)

        # Check if the maximum amplitude exceeds the threshold
        if max_amp > THRESHOLD:
            print("Clap!")
            startup = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\wake-up-the-robot-84894.mp3"
            playsound(startup)
            taskexecution()

    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()


def send_whatsapp_message(contact_name, message):
    # Specify the path to the WebDriver executable. Download the appropriate WebDriver for your browser.
    # In this example, I'm using Chrome WebDriver.
    driver = webdriver.Chrome(executable_path='C:\\Users\\pcper\\Downloads\\chromedriver_win32')

    # Open WhatsApp Web
    driver.get('https://web.whatsapp.com/')
    input("Press Enter after scanning QR code...")

    # Locate the search box
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')

    # Search for the contact
    search_box.send_keys(contact_name)
    search_box.send_keys(Keys.ENTER)

    time.sleep(2)  # Wait for the chat to load

    # Locate the message input box
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')

    # Type the message
    message_box.send_keys(message)

    # Send the message by pressing Enter
    message_box.send_keys(Keys.ENTER)

    # Close the browser after sending the message
    driver.quit()

def get_disk_info():
    import psutil
    disk_info = psutil.disk_usage('/')
    print(f"Disk Total: {disk_info.total / (1024 * 1024 * 1024)} GiB")
    speak(f" total Disk space: {disk_info.total / (1024 * 1024 * 1024)} GiB")

    print(f"Disk Used: {disk_info.used / (1024 * 1024 * 1024)} GiB")
    speak(f"total disk used : {disk_info.used / (1024 * 1024 * 1024)} GiB")

    print(f"Disk Free: {disk_info.free / (1024 * 1024 * 1024)} GiB")
    speak(f"total space free: {disk_info.free / (1024 * 1024 * 1024)} GiB")

    print(f"Disk Percent: {disk_info.percent}%")
    speak(f"Disk Percentage: {disk_info.percent}%")

def disneyplushotstar():
    import pyautogui
    import time
    speak("do you want to search or should i suggest movies for you")
    sors = takecommand().lower()
    if 'search' in sors:
        import webbrowser
        webbrowser.open("https://www.hotstar.com/in/explore")
        time.sleep(5)
        speak("what should i search sir ?")
        search_moviesssss = takecommand().lower()
        pyautogui.typewrite(search_moviesssss)
        speak("here's the result for your search")

    else:

        webbrowser.open("https://www.hotstar.com/in/home")

def metre_into_centimetre():
    speak("enter the value of metre")
    metre = float(input("enter the value of metre : "))
    centimetre = 100
    resultofmetreintocentimetre = metre * centimetre
    print(f"the conversion of {metre} metre to centimetre is {resultofmetreintocentimetre}")
    speak(f"the conversion of {metre} metre to centimetre is {resultofmetreintocentimetre}")

def metre_to_kilometre():
    speak("enter the value of metre")
    metre1 = float(input("enter the value of metre : "))
    kilometre = 1000
    result2 = metre1 / kilometre
    print(f"the convertion of {metre1} metre to kilometre is {result2} ")
    speak(f"the convertion of {metre1} metre to kilometre is {result2} ")

def centimetre_to_milimetre():
    speak('enter value of centimetre')
    centimetre = float(input("enter the value of centimetre : "))
    milimetre = 10
    result3 = centimetre * milimetre
    print(f"the conversion of {centimetre} centimetre into milimetre is {result3}")
    speak(f"the conversion of {centimetre} centimetre into milimetre is {result3}")


def get_cpu_usage():
    import psutil
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    speak(f"your central processing unit Usage is  {cpu_usage}%")
def get_weather(api_key, city):
    import requests
    api_key = "ed49a32044386c40607445624addd441" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        country = data["sys"]["country"]

        print(f"Weather in {city}, {country}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Unable to fetch weather data.")

def c_calculator():
    indian_rupees = 82.78
    speak("enter the amount to be calculated")
    usd_money = float(input("Enter the amount to be calculated: "))
    result_money = usd_money * indian_rupees

    print(f"{usd_money} dollars in indian currency is equal to {result_money} rupees")
    speak(f"{usd_money} dollars in indian currency is equal to {result_money} rupees")


def calculator():
        # Ask user for the first digit
    speak("enter the first digit")
    first_digit = float(input("Enter the first digit: "))

    # Ask user for the second digit
    speak("enter the second digit")
    second_digit = float(input("Enter the second digit: "))

    # Ask user for the operation to perform
    speak("what operation do you want me to do?")
    operation = input("Enter the operation to perform (multiplication\nsubtraction\naddition\ndivision): ")

    # Perform the selected operation
    if operation == "multiplication":
        result = first_digit * second_digit
    elif operation == "subtraction":
        result = first_digit - second_digit
    elif operation == "addition":
        result = first_digit + second_digit
    elif operation == "division":
        if second_digit != 0:
            result = first_digit / second_digit
        else:
            result = "Cannot divide by zero"
    else:
        result = "Invalid operation"
    speak(f"Result of {operation} of {first_digit} and {second_digit} is: {result}")
    print(f"Result of {operation} of {first_digit} and {second_digit} is: {result}")

def check_internet_speed():
    import pyautogui
    import time

    speak("okay sir checking internet speed of your device")
    pyautogui.hotkey('win' , 'r')
    time.sleep(1)
    pyautogui.typewrite('cmd')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite('speedtest.exe')
    pyautogui.press('enter')
    time.sleep(17)
    speak('here is your speedtest sir ! , you can clap to close it !')
    clap_to_close_images()

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def talking_mode():
    print("                WARNING")
    print("very low data has been trained to the talking mode , this may not answer all your questions.\nplease be paitient !!")
    speak("you can simply say jarvis stop to end talking mode.")
    while True:
        query = takecommand().lower()

        if 'how are you' in query:
            speak("i am fine sir may i know if there is anything for which i can help you")

        if 'who made you' in query:
            speak("i am jarvis , made by ashmit singh rajput")

        if 'how is your wife' in query:
            speak("as an personalised assistant i am not supposed to have any wife or girlfriend")

        if 'hey jarvis' in query:
            speak("at your service sir")

        if 'how is your family' in query:
            speak("as an personalised assistant i am not supposed to have any family")

        if 'name my  friends' in query:
            speak("sir i dont know properly but you have 3 good friends aryan , agamjot and vickey . i certainly dont know about your any female friend as you have'nt introduce yet")

        if 'how are your friends' in query:
            speak("sir , i have no friend yet")

        if 'i have not slept for 24 hours' in query:
            speak("i guess you should have as it's a very long time , you should definetly take rest ")

        if 'what is my syllabus' in query:
            speak("sir , you haven't shared any of your syllabus with me . if you want i can open whatsapp , i guess you could find your syllabus there")

        if 'tell me something about you' in query:
            speak("not need to introduce my self , i am jarvis , the virtual artificial intelligence and i am here to assist you with variety of tasks as best as i can , 24 hours a day , seven days a week.")

        if 'what can you do' in query:
            speak("i am the virtual artificial intelligence and i am here to assist you with variety of tasks as best as i can , 24 hours a day , seven days a week.")

        if 'can you hack someone' in query:
            speak("yes ofcourse as i have many personalised data , you  can change the mode by saying jarvis stop and i wil change the talking mode and you can hack any wifi router , phone , laptop extra in your area .")

        if 'am i careless' in query:
            speak("as much i know you , i think you are a littile bit careless with your responsibilities and way more lazy.")

        if 'you are careless' in query:
            speak("sir i can't be careless enough , as an virtual artificial voice assistant i am always at time")

        if 'did i finished my homework' in query:
            speak("sir , i dont know any certain about your homework so i don't know that wether you have done your homework or not.")

        if 'who am i' in query:
            speak("you are ashmit singh rajput , lives in faridabad of haryana that lies in INDIA and you are in 10th standard ")

        if 'when is my birthday' in query:
            speak("your birthday was on 6 september 2009 ")

        if 'when is your birthday' in query:
            speak("i don't know anything about my birthday")

        if 'introduce myself' in query:
            speak("you are ashmit singh rajput , lives in faridabad of haryana that lies in INDIA and you are in 10th standard ")

        if 'introduce yourself' in query:
            speak("not need to introduce my self , i am jarvis , the virtual artificial intelligence and i am here to assist you with variety of tasks as best as i can , 24 hours a day , seven days a week.")

        if 'name all my teachers' in query:
            speak("you social science teacher is paramjeet kaur , you maths teacher's name is nidhi , your english teacher is seema sharma , your chemistry teacher's name is nalini , your bio teacher name is chetali datta and your physics teacher is manish bhardwaj")

        if 'what is the date today' in query:
            from datetime import date

            today = date.today()
            speak(f"Today's date: {today}")
            

        if "what's the time" in query:
            from datetime import datetime

            current_time = datetime.now().time()
            formatted_time = current_time.strftime("%I:%M %p")
            speak( f"current time is {formatted_time}")

        if 'what is the time' in query:
            from datetime import datetime

            current_time = datetime.now().time()
            formatted_time = current_time.strftime("%I:%M %p")
            speak( f"current time is {formatted_time}")


        if 'tell me the time' in query:
            from datetime import datetime

            current_time = datetime.now().time()
            formatted_time = current_time.strftime("%I:%M %p")
            speak( f"current time is {formatted_time}")

        if 'jarvis search' in query:
            import pywhatkit
            new_string = query.replace("jarvis search", "")
            pywhatkit.search(new_string)
            speak(f"searching for{new_string}"  )

        if 'search for' in query:
            import pywhatkit
            new_string = query.replace("search for", "")
            pywhatkit.search(new_string)
            speak(f"searching for{new_string}"  )

        if 'what is' in query:
            import pywhatkit
            new_string = query.replace("what is", "")
            pywhatkit.search( "what is" + new_string)
            speak(f"searching for what is {new_string}")
            string
        if 'jarvis what is' in query:
            import pywhatkit
            new_string = query.replace("jarvis what is", "")
            pywhatkit.search( "what is" + new_string)
            speak(f"searching for what is {new_string}")

        if 'find test paper' in query:
            speak('sir can you tell me which subject you want me to check ')
            input1 = input(" social science - 1\n mathematics - 2 \n science - 3 \n hindi - 4 \n english - 5")
            speak('rest of the work is not done yet !')



        if 'jarvis stop' in query:
            speak("okay sir quiting talking mode. ")
            break
        
def taskexecution():

    while True: 
        query = takecommand().lower()

        if 'switch to talking mode' in query:
            speak('okay sir switching to talking mode')
            talking_mode()
        if 'enable talking mode' in query:
            speak('okay sir switching to talking mode')
            talking_mode()
        if 'talk to me' in query:
            speak('okay sir switching to talking mode')
            talking_mode()

        if 'set an alarm' in query:
            print("input time example :-    10 and 10 and 10")
            speak("set the time")
            a = input("please tell the time ")
            alarm(a)
            speak("done sir")
        if 'my ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif 'from wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif 'metre into centimetre' in query:
            speak("okay sir")
            metre_into_centimetre()

        elif 'metre into kilometre' in query:
            speak("okay sir")
            metre_to_kilometre()

        elif 'centimetre into millimetre' in query:
            speak("okay sir")
            centimetre_to_milimetre()

        elif 'open youtube' in query:
            import webbrowser
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'search for' in query:
            import pywhatkit
            import pyautogui
            import time 
            modified_input = query.replace('search for', '')
            speak(f"searching for {modified_input.strip()}")
            pywhatkit.search(modified_input.strip())
            time.sleep(3)
            pyautogui.scroll(-100, x=1500, y=800 )
            speak('you can snap to close the search')
            clap_to_close()

        elif 'open trending page' in query:
            import webbrowser
            speak("okay sir here's the trending page of taday on youtube")
            webbrowser.open("https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")
            
        elif 'play a sad song' in query:
            import os
            import pywhatkit as pyw
            import random
            import time
            import pyautogui as py
            speak('okay sir , you can clap to stop the song and wake me up.')
            sad_songs = ['kaise hua song','yaha koi nahi yaha koi nahi yaha koi bhi nahi song', 'dagabaaz re song', 'let her go song', 'pal pal dil ke paas song', 'my queen song', 'hale dil' , 'guzarish', 'itna na tu mujse pyaar badha song', 'jane nahi denge tuje song 3 idots','give me some sunshine', 'kisi ki muskarahato pe ho nisar song old one', 'Aa Chal Ke Tujhe old song' ]
            fonk = ['funk of the dammed', 'tokyo drift song', "Leat'eq - Tokyo Official Music Video HD", 'twirling song' ,  ]
            moj_masti = ['ms dhoni song', 'trollywood1', 'tokyo song','dol jageero da song', 'na jaiyo mere desi look te tane maar dega mera attitude bavli song','murder song', '12 bande song ' , 'lalkaara song', 'hamare sath shri ragunath to kis baat ki chinta hai song', 'nature song', 'splender song by harsh likhari' , 'dior song by shubh', 'arjan valley ne song' , 'laado song' , 'daku song by sidhu moosewala', 'old skool by sidhumoosewala'  ]
            angrezi = ['chery chery ladies song', 'happy nation song']
            ss_sad_songs = random.choice(sad_songs)
            s_fonk = random.choice(fonk)
            s_moj_masti = random.choice(moj_masti)
            s_angrezi = random.choice(angrezi)

            pyw.playonyt(ss_sad_songs)
            songs_wala_close_fuction()

        elif 'play gym music' in query:
            import os
            import pywhatkit as pyw
            import random
            import time
            import pyautogui as py
            speak('okay sir , you can clap to stop the song and wake me up.')
            sad_songs = ['kaise hua song','yaha koi nahi yaha koi nahi yaha koi bhi nahi song', 'dagabaaz re song', 'let her go song', 'pal pal dil ke paas song', 'my queen song', 'hale dil' , 'guzarish', 'itna na tu mujse pyaar badha song', 'jane nahi denge tuje song 3 idots','give me some sunshine', 'kisi ki muskarahato pe ho nisar song old one', 'Aa Chal Ke Tujhe old song' ]
            fonk = ['funk of the dammed', 'tokyo drift song', "Leat'eq - Tokyo Official Music Video HD", 'twirling song' ,  ]
            moj_masti = ['ms dhoni song', 'trollywood1', 'tokyo song','dol jageero da song', 'na jaiyo mere desi look te tane maar dega mera attitude bavli song','murder song', '12 bande song ' , 'lalkaara song', 'hamare sath shri ragunath to kis baat ki chinta hai song', 'nature song', 'splender song by harsh likhari' , 'dior song by shubh', 'arjan valley ne song' , 'laado song' , 'daku song by sidhu moosewala', 'old skool by sidhumoosewala'  ]
            angrezi = ['chery chery ladies song', 'happy nation song']
            ss_sad_songs = random.choice(sad_songs)
            s_fonk = random.choice(fonk)
            s_moj_masti = random.choice(moj_masti)
            s_angrezi = random.choice(angrezi)

            pyw.playonyt(s_fonk)
            songs_wala_close_fuction()

        elif 'play music for gym' in query:
            import os
            import pywhatkit as pyw
            import random
            import time
            import pyautogui as py
            speak('okay sir , you can clap to stop the song and wake me up.')
            sad_songs = ['kaise hua song','yaha koi nahi yaha koi nahi yaha koi bhi nahi song', 'dagabaaz re song', 'let her go song', 'pal pal dil ke paas song', 'my queen song', 'hale dil' , 'guzarish', 'itna na tu mujse pyaar badha song', 'jane nahi denge tuje song 3 idots','give me some sunshine', 'kisi ki muskarahato pe ho nisar song old one', 'Aa Chal Ke Tujhe old song' ]
            fonk = ['funk of the dammed', 'tokyo drift song', "Leat'eq - Tokyo Official Music Video HD", 'twirling song' ,  ]
            moj_masti = ['ms dhoni song', 'trollywood1', 'tokyo song','dol jageero da song', 'na jaiyo mere desi look te tane maar dega mera attitude bavli song','murder song', '12 bande song ' , 'lalkaara song', 'hamare sath shri ragunath to kis baat ki chinta hai song', 'nature song', 'splender song by harsh likhari' , 'dior song by shubh', 'arjan valley ne song' , 'laado song' , 'daku song by sidhu moosewala', 'old skool by sidhumoosewala'  ]
            angrezi = ['chery chery ladies song', 'happy nation song']
            ss_sad_songs = random.choice(sad_songs)
            s_fonk = random.choice(fonk)
            s_moj_masti = random.choice(moj_masti)
            s_angrezi = random.choice(angrezi)

            pyw.playonyt(s_fonk)
            songs_wala_close_fuction()
        elif 'play indian songs' in query:
            import os
            import pywhatkit as pyw
            import random
            import time
            import pyautogui as py
            speak('okay sir , you can clap to stop the song and wake me up.')
            sad_songs = ['kaise hua song','yaha koi nahi yaha koi nahi yaha koi bhi nahi song', 'dagabaaz re song', 'let her go song', 'pal pal dil ke paas song', 'my queen song', 'hale dil' , 'guzarish', 'itna na tu mujse pyaar badha song', 'jane nahi denge tuje song 3 idots','give me some sunshine', 'kisi ki muskarahato pe ho nisar song old one', 'Aa Chal Ke Tujhe old song' ]
            fonk = ['funk of the dammed', 'tokyo drift song', "Leat'eq - Tokyo Official Music Video HD", 'twirling song' ,  ]
            moj_masti = ['ms dhoni song', 'trollywood1', 'tokyo song','dol jageero da song', 'na jaiyo mere desi look te tane maar dega mera attitude bavli song','murder song', '12 bande song ' , 'lalkaara song', 'hamare sath shri ragunath to kis baat ki chinta hai song', 'nature song', 'splender song by harsh likhari' , 'dior song by shubh', 'arjan valley ne song' , 'laado song' , 'daku song by sidhu moosewala', 'old skool by sidhumoosewala'  ]
            angrezi = ['chery chery ladies song', 'happy nation song']
            ss_sad_songs = random.choice(sad_songs)
            s_fonk = random.choice(fonk)
            s_moj_masti = random.choice(moj_masti)
            s_angrezi = random.choice(angrezi)

            pyw.playonyt(s_moj_masti)
            songs_wala_close_fuction()

        elif 'play an indian song' in query:
            import os
            import pywhatkit as pyw
            import random
            import time
            import pyautogui as py
            speak('okay sir , you can clap to stop the song and wake me up.')
            sad_songs = ['kaise hua song','yaha koi nahi yaha koi nahi yaha koi bhi nahi song', 'dagabaaz re song', 'let her go song', 'pal pal dil ke paas song', 'my queen song', 'hale dil' , 'guzarish', 'itna na tu mujse pyaar badha song', 'jane nahi denge tuje song 3 idots','give me some sunshine', 'kisi ki muskarahato pe ho nisar song old one', 'Aa Chal Ke Tujhe old song' ]
            fonk = ['funk of the dammed', 'tokyo drift song', "Leat'eq - Tokyo Official Music Video HD", 'twirling song' ,  ]
            moj_masti = ['ms dhoni song', 'trollywood1', 'tokyo song','dol jageero da song', 'na jaiyo mere desi look te tane maar dega mera attitude bavli song','murder song', '12 bande song ' , 'lalkaara song', 'hamare sath shri ragunath to kis baat ki chinta hai song', 'nature song', 'splender song by harsh likhari' , 'dior song by shubh', 'arjan valley ne song' , 'laado song' , 'daku song by sidhu moosewala', 'old skool by sidhumoosewala'  ]
            angrezi = ['chery chery ladies song', 'happy nation song']
            ss_sad_songs = random.choice(sad_songs)
            s_fonk = random.choice(fonk)
            s_moj_masti = random.choice(moj_masti)
            s_angrezi = random.choice(angrezi)

            pyw.playonyt(s_moj_masti)
            songs_wala_close_fuction()

        elif 'play a indian song' in query:
            import os
            import pywhatkit as pyw
            import random
            import time
            import pyautogui as py
            speak('okay sir , you can clap to stop the song and wake me up.')
            sad_songs = ['kaise hua song','yaha koi nahi yaha koi nahi yaha koi bhi nahi song', 'dagabaaz re song', 'let her go song', 'pal pal dil ke paas song', 'my queen song', 'hale dil' , 'guzarish', 'itna na tu mujse pyaar badha song', 'jane nahi denge tuje song 3 idots','give me some sunshine', 'kisi ki muskarahato pe ho nisar song old one', 'Aa Chal Ke Tujhe old song' ]
            fonk = ['funk of the dammed', 'tokyo drift song', "Leat'eq - Tokyo Official Music Video HD", 'twirling song' ,  ]
            moj_masti = ['ms dhoni song', 'trollywood1', 'tokyo song','dol jageero da song', 'na jaiyo mere desi look te tane maar dega mera attitude bavli song','murder song', '12 bande song ' , 'lalkaara song', 'hamare sath shri ragunath to kis baat ki chinta hai song', 'nature song', 'splender song by harsh likhari' , 'dior song by shubh', 'arjan valley ne song' , 'laado song' , 'daku song by sidhu moosewala', 'old skool by sidhumoosewala'  ]
            angrezi = ['chery chery ladies song', 'happy nation song']
            ss_sad_songs = random.choice(sad_songs)
            s_fonk = random.choice(fonk)
            s_moj_masti = random.choice(moj_masti)
            s_angrezi = random.choice(angrezi)

            pyw.playonyt(s_moj_masti)
            songs_wala_close_fuction()

        elif 'play a english song' in query:
            import os
            import pywhatkit as pyw
            import random
            import time
            import pyautogui as py
            speak('okay sir , you can clap to stop the song and wake me up.')
            sad_songs = ['kaise hua song','yaha koi nahi yaha koi nahi yaha koi bhi nahi song', 'dagabaaz re song', 'let her go song', 'pal pal dil ke paas song', 'my queen song', 'hale dil' , 'guzarish', 'itna na tu mujse pyaar badha song', 'jane nahi denge tuje song 3 idots','give me some sunshine', 'kisi ki muskarahato pe ho nisar song old one', 'Aa Chal Ke Tujhe old song' ]
            fonk = ['funk of the dammed', 'tokyo drift song', "Leat'eq - Tokyo Official Music Video HD", 'twirling song' ,  ]
            moj_masti = ['ms dhoni song', 'trollywood1', 'tokyo song','dol jageero da song', 'na jaiyo mere desi look te tane maar dega mera attitude bavli song','murder song', '12 bande song ' , 'lalkaara song', 'hamare sath shri ragunath to kis baat ki chinta hai song', 'nature song', 'splender song by harsh likhari' , 'dior song by shubh', 'arjan valley ne song' , 'laado song' , 'daku song by sidhu moosewala', 'old skool by sidhumoosewala'  ]
            angrezi = ['chery chery ladies song', 'happy nation song']
            ss_sad_songs = random.choice(sad_songs)
            s_fonk = random.choice(fonk)
            s_moj_masti = random.choice(moj_masti)
            s_angrezi = random.choice(angrezi)

            pyw.playonyt(s_angrezi)
            songs_wala_close_fuction()

        elif 'play an english song' in query:
            import os
            import pywhatkit as pyw
            import random
            import time
            import pyautogui as py
            speak('okay sir , you can clap to stop the song and wake me up.')
            sad_songs = ['kaise hua song','yaha koi nahi yaha koi nahi yaha koi bhi nahi song', 'dagabaaz re song', 'let her go song', 'pal pal dil ke paas song', 'my queen song', 'hale dil' , 'guzarish', 'itna na tu mujse pyaar badha song', 'jane nahi denge tuje song 3 idots','give me some sunshine', 'kisi ki muskarahato pe ho nisar song old one', 'Aa Chal Ke Tujhe old song' ]
            fonk = ['funk of the dammed', 'tokyo drift song', "Leat'eq - Tokyo Official Music Video HD", 'twirling song' ,  ]
            moj_masti = ['ms dhoni song', 'trollywood1', 'tokyo song','dol jageero da song', 'na jaiyo mere desi look te tane maar dega mera attitude bavli song','murder song', '12 bande song ' , 'lalkaara song', 'hamare sath shri ragunath to kis baat ki chinta hai song', 'nature song', 'splender song by harsh likhari' , 'dior song by shubh', 'arjan valley ne song' , 'laado song' , 'daku song by sidhu moosewala', 'old skool by sidhumoosewala'  ]
            angrezi = ['chery chery ladies song', 'happy nation song']
            ss_sad_songs = random.choice(sad_songs)
            s_fonk = random.choice(fonk)
            s_moj_masti = random.choice(moj_masti)
            s_angrezi = random.choice(angrezi)

            pyw.playonyt(s_angrezi)
            songs_wala_close_fuction()

        elif 'play english songs' in query:
            import os
            import pywhatkit as pyw
            import random
            import time
            import pyautogui as py
            speak('okay sir , you can clap to stop the song and wake me up.')
            sad_songs = ['kaise hua song','yaha koi nahi yaha koi nahi yaha koi bhi nahi song', 'dagabaaz re song', 'let her go song', 'pal pal dil ke paas song', 'my queen song', 'hale dil' , 'guzarish', 'itna na tu mujse pyaar badha song', 'jane nahi denge tuje song 3 idots','give me some sunshine', 'kisi ki muskarahato pe ho nisar song old one', 'Aa Chal Ke Tujhe old song' ]
            fonk = ['funk of the dammed', 'tokyo drift song', "Leat'eq - Tokyo Official Music Video HD", 'twirling song' ,  ]
            moj_masti = ['ms dhoni song', 'trollywood1', 'tokyo song','dol jageero da song', 'na jaiyo mere desi look te tane maar dega mera attitude bavli song','murder song', '12 bande song ' , 'lalkaara song', 'hamare sath shri ragunath to kis baat ki chinta hai song', 'nature song', 'splender song by harsh likhari' , 'dior song by shubh', 'arjan valley ne song' , 'laado song' , 'daku song by sidhu moosewala', 'old skool by sidhumoosewala'  ]
            angrezi = ['chery chery ladies song', 'happy nation song']
            ss_sad_songs = random.choice(sad_songs)
            s_fonk = random.choice(fonk)
            s_moj_masti = random.choice(moj_masti)
            s_angrezi = random.choice(angrezi)

            pyw.playonyt(s_angrezi)
            songs_wala_close_fuction()
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
#----------------------------------location tracking--------------------------------------------            
        elif 'where i am' in query or 'whete am i' in query or 'where we are' in query:
            speak("wait sir i am connecting the tracking data 34")
            try: 
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' +ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()

                city = geo_data['city']

                country = geo_data['country']
                speak(f"i am not sure but i think we are in {city}")
                speak(f"of {country}")
            except Exception as e:
                speak("i am not able to connect to the tracking satalite data number 34")
                pass


        elif 'check instagram profile' in query:
            import webbrowser
            speak("please enter the username of the profile")
            name = input("enter your profile name here : ")
            webbrowser.open(f"www.instagram.com/{name}")

#----------------------------leave function---------------------------------------------------

        elif 'leave now' in query:
            speak("okay sir you can recall me later")
            clap()
#---------------------------calculator---------------------------------------------------------        
        elif 'do some calculation' in query:
            speak("okay sir starting calculator")
            calculator()

        elif 'some calculation' in query:
            speak("okay sir starting calculator")
            calculator()

        elif 'open calculator' in query:
            speak("okay sir starting calculator")
            calculator()

        elif 'some maths' in query:
            speak("okay sir starting calculator")
            calculator()
#--------------------------------how to do mode---------------------------------------------------           
        elif 'activate how to do mode' in query:
            speak("how to do mode has been activated , please tell me what do you want to know ? ")
            how = takecommand().lower()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
#----------------------------translation function-----------------------------------------------
        elif 'translate' in query:
            import pyautogui
            import webbrowser
            import time
            speak('okay sir')
            speak('if you want to choose anyother languge to be translated you can select it')
            speak('what do you want to translate , sir')
            wtbttt = takecommand().lower()
            speak('opening translator , sir')
            webbrowser.open(f"https://translate.google.com/?sl=en&tl=hi&text={wtbttt}&op=translate")

#------------------------thanks function--------------------------------------------------------

        elif 'thanks' in query:
            speak("your most welcome sir")
            speak('is there any thing else that i can do for you')
        elif 'thank you' in query:
            speak('your most welcome sir')
            speak('is there any thing else that i can do for you')
        elif 'thank u' in query:
            speak("your most welcome sir")
            speak('is there any thing else that i can do for you')

#----------------------------amazon shopping-------------------------------------------------------
        elif 'activate amazon shopping mode' in query:
            import webbrowser
            speak("shopping mode activated")
            speak('what do you want to purchase')
            item_to_be_purchased = takecommand().lower()
            webbrowser.open(f"https://www.amazon.com/s?k={item_to_be_purchased}&crid=13AL48NKD4TMP&sprefix=pc+speakers%2Caps%2C385&ref=nb_sb_noss_1")
            speak("here's what i found sir")
#-----------------------------flipkart shopping----------------------------------------------------
        elif 'activate flipkart shopping mode' in query:
            import webbrowser
            speak('shopping mode activated')
            speak("what do you want to purchase")
            item_to_be_purchased2 = takecommand().lower()
            webbrowser.open(f"https://www.flipkart.com/search?q={item_to_be_purchased2}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
            speak("here's what i find sir")

#------------------------close the search system--------------------------------------------------------
        elif 'close the browser' in query:
            import os
            speak('okay sir')
            os.system("taskkill /f /im msedge.exe")

        elif 'find my mother' in query:
            import webbrowser
            import pyautogui
            import time 
            import webbrowser
            speak("okay sir ")
            time.sleep(1)
            webbrowser.open("https://www.google.com/android/find/?did=DvOX8IA0lBDMYkK4Vv312gzgAChNAjmP1G71X1oaY5A%3D")
            speak('you can clap to close this tab')
            clap_to_close_manually()
        elif 'find my father' in query:
            import webbrowser
            speak('fething the location')
            webbrowser.open("https://www.google.com/android/find/?did=EWbElFOGDt4NRZm1O0ZQzSFXSc_hXvOdJ5Ae-siEXRY%3D&pli=1")
            speak('you can clap to close this tab')
            clap_to_close_manually()

#----------------------------youtube search engine--------------------------------------------------------
        elif 'search on youtube' in query:
            import pywhatkit
            speak("what should i search sir ?")
            search_yt = takecommand().lower()
            pywhatkit.playonyt(search_yt)
            speak("okay sir , here's what i found.")

            

#--------------------------play my playlist----------------------------------------------
        elif 'play my favourite playlist' in query:
            import webbrowser
            speak("okay sir")
            webbrowser.open("https://www.youtube.com/watch?v=S6Qy9Ouu0aA&list=RDS6Qy9Ouu0aA&start_radio=1")

        elif 'play a song named' in query:
            import pywhatkit
            modified_input = query.replace('play a song named', '')
            print(modified_input.strip())
            pywhatkit.playonyt(modified_input.strip())
        
        elif 'play a song name' in query:
            import pywhatkit
            modified_input = query.replace('play a song name', '')
            print(modified_input.strip())
            pywhatkit.playonyt(modified_input.strip())

        elif 'from youtube' in query:
            import pywhatkit
            speak("okay sir")
            pywhatkit.playonyt(query)
        

        elif 'activate instant kill mode' in query:
            speak("instant kill mode activated")

        elif 'madrchod' in query:
            speak("sorry sir")

        elif 'madarchod' in query:
            speak("sorry sir")

        elif 'bahan ke loade' in query:
            speak("sorry sir")

        elif 'gandu' in query:
            speak("sorry sir")

        elif 'chut' in query:
            speak("sorry sir")

        elif 'teri' in query:
            speak("sorry sir")

        elif 'chutiye' in query:
            speak("sorry sir")

        elif 'chutiye' in query:
            speak("sorry sir")

        elif 'chod' in query:
            speak("sorry sir")


#-----------------------------------internet speed------------------------------------
        elif 'internet speed' in query:
            check_internet_speed()


#----------------------------------volume function--------------------------------------

        elif 'volume up' in query:
            import pyautogui
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            import pyautogui
            pyautogui.press("volumedown")

        elif 'mute' in query:
            import pyautogui
            pyautogui.press("volumemute")

#---------------------------------other keyboard functions-----------------------------------

        elif 'play the video' in query:
            import pyautogui
            pyautogui.press("space")

        elif 'full screen' in query:
            import pyautogui
            pyautogui.press('f11')

        elif 'screen shot' in query:
            import pyautogui
            pyautogui.press('winleft')
            pyautogui.press('altleft')
            pyautogui.press('prntscrn')

        elif 'screenshot' in query:
            import pyautogui
            pyautogui.press('winleft')
            pyautogui.press('altleft')
            pyautogui.press('prntscrn')

#--------------------------------open webcam-----------------------------------------------------

        elif 'click a photo' in query:
            import pyautogui
            import time
            speak("okay sir , opening camera")
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.typewrite('camera')
            pyautogui.press('enter')
            speak("you can snap to click the picture.")
            clickspace()
            speak('should i preveiw the picture also  ? ')
            sip = takecommand().lower()
            if 'yes' in sip:
                speak("okay sir")
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('enter')
                speak('you can snap to close the photo')
                clap_to_close()

            else:
                speak('okay sir, i am not showing the picture')
                pyautogui.hotkey('alt', 'f4')
            



#-----------------------------------text  file----------------------------------------------

        elif 'new text file' in query:
            import pyautogui
            import subprocess
            subprocess.Popen(["notepad.exe"])
            speak("okay sir")
            speak("sir what should i type in the text file")
            text_to_be_typed = takecommand().lower()
            pyautogui.typewrite(text_to_be_typed)


#-----------------------------direct shutdown--------------------------------------

        elif 'shut down' in query:
            import sys 
            from playsound import playsound
            speak("thanks for your time sir")
            shutdown_snd = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\wake-up-the-robot-84894.mp3"
            playsound(shutdown_snd)
            sys.exit()

        elif 'shutdown' in query:
            import sys 
            from playsound import playsound
            speak("thanks for your time sir")
            shutdown_snd = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\wake-up-the-robot-84894.mp3"
            playsound(shutdown_snd)
            sys.exit()

#---------------------------change tab-----------------------------------------

        elif 'send message on instagram' in query:
            send_message_on_instagram()

#-------------------------------generate a password------------------------------------

        elif 'generate a password' in query:
            import random
            letters = "abcdefghijklmnopqrstuvwxyz"
            numbers = "1234567890"

            string = letters + numbers 
            length = 8
            password = "".join(random.sample(string,length))
            print(f"your new pass word is {password}")
            speak(f"your new password is {password}")


#--------------------------time-------------------------------------
        elif 'sleep for 5 minutes' in query:
            import time
            speak("i will meet you after 5 minutes sir")
            time.sleep(300)
            speak("sir the timer has been over")

        elif 'sleep for 4 minutes' in query:
            import time
            speak("i will meet you after 4 minutes sir")
            time.sleep(240)
            speak("sir the timer has been over")

        elif 'sleep for 3 minutes' in query:
            import time
            speak("i will meet you after 3 minutes sir")
            time.sleep(180)
            speak("sir the timer has been over")


        elif 'sleep for 2 minutes' in query:
            import time
            speak("i will meet you after 2 minutes sir")
            time.sleep(120)
            speak("sir the timer has been over")

        elif 'sleep for 1 minute' in query:
            import time
            speak("i will meet you after 1 minute sir")
            time.sleep(60)
            speak("sir the timer has been over")


        elif 'sleep for 10 minutes' in query:
            import time
            speak("i will meet you after 10 minutes sir")
            time.sleep(600)
            speak("sir the timer has been over")


        elif 'sleep for 15 minutes' in query:
            import time
            speak("i will meet you after 15 minutes sir")
            time.sleep(900)
            speak("sir the timer has been over")

#------------------------invade ip address-----------------------------------

        elif 'invade ip address' in query:
            import webbrowser
            speak("okay sir i am creating a link to share and opening the browser to watch the users ip and other data")
            link_to_be_hacked = "https://grabify.link/3WP4B5"
            speak("this is the link to use for hacking")
            print(link_to_be_hacked)
            speak("i am opening browser to watch the users")
            webbrowser.open("https://grabify.link/track/5V8RTE")

#------------------------------close the previous tab-------------------------

        elif 'close this tab' in query:
            import pyautogui
            import os 
            os.system("taskkill /f /im msedge.exe")


#-----------------------------full screen for youtube-----------------------------

        elif 'youtube fullscreen' in query:
            import pyautogui
            pyautogui.press('f')
        elif 'youtube full screen' in query:
            import pyautogui
            pyautogui.press('f')

#---------------------------------type something-----------------------

        elif 'type' in query:
            import pyautogui
            speak("okay sir what do you want to type")
            tagain = takecommand().lower()
            pyautogui.typewrite(tagain)
            pyautogui.press('enter')

#-----------------------------open pininterest-----------------------------

        elif 'open pinterest' in query:
            import webbrowser
            speak("opening pinterest")
            webbrowser.open("https://in.pinterest.com/")

#---------------------------check instagram inbox-----------------------------

        elif 'check instagram inbox' in query:
            import pyautogui
            import webbrowser
            import time
            speak("okay sir fetching messages")
            webbrowser.open("https://www.instagram.com/direct/inbox/")
            time.sleep(7)
            speak("should i message someone sir ?? ")
            yyhtm = takecommand().lower()
            if 'yes' in yyhtm:
                speak('sure sir')
                send_message_on_instagram()
            else:
                speak('okay sir')
                with pyautogui.hold("ctrl"):
                    pyautogui.press('w')

#--------------------message on whatsapp------------------------------------



#----------------------activate open ai mode----------------------------------

        elif 'activate open ai mode' in query or 'activate openai mode' in query:
            import time 
            import webbrowser
            import pyautogui 
            speak("okay sir i am switching control to stephen or you can say gemini")
            speak("tell me what do you want to know")
            wtiwtn = takecommand().lower()
            speak("okay sir shifting to stephen , this might take a few seconds")
            itenl = '. tell me only in 10 sentences'
            time.sleep(2)
            webbrowser.open("https://gemini.google.com/app")
            time.sleep(1)
            pyautogui.press('f11')
            time.sleep(5)
            pyautogui.typewrite(f"{wtiwtn} {itenl} ")
            pyautogui.press('enter')
            time.sleep(10)
            pyautogui.moveTo(1330 , 200 )
            pyautogui.click()

            time.sleep(50)

            with pyautogui.hold('ctrl'):
                pyautogui.press('W')
#------------------------------------movies-----------------------------------

        elif 'movies' in query:
            import webbrowser
            speak('okay sir what movie would you consider to watch')
            moviestw = takecommand().lower()
            speak("okay sir . i am trying to find the movie")
            webbrowser.open(f"https://hdmovies4u.bet/?s={moviestw}")

        elif 'mini tv' in query:
            import webbrowser
            speak("okay opening amazon mini tv sir")
            webbrowser.open("https://www.amazon.in/minitv?mtv_pt=external&refMarker=AVOD_gs_mw_BRND_EDU_GS_TXT_Desk_skey7&gad_source=1&gclid=CjwKCAjw17qvBhBrEiwA1rU9w0oex7CCZqng3yc5VI1-1s34P4Ed8TIz5oUOfP3rLLKyeG_e1jLHtxoCmewQAvD_BwE")

        elif 'disney' in query or 'hotstar' in query:
            speak("okay sir wait a while")
            disneyplushotstar()
#-----------------------------typing test-----------------------

        elif 'typing test' in query:

            import webbrowser
            speak("okay sir i am opening the typing test")
            webbrowser.open("https://monkeytype.com/#google_vignette")

#----------------------------router settings-----------------------

        elif 'router' in query:
            import webbrowser
            import time
            import pyautogui
            speak("opening router settings for your wifi")
            webbrowser.open("http://192.168.0.1/login.html")
            time.sleep(2)
            pyautogui.typewrite('wasdwasdwasd')
            pyautogui.press("enter")
        elif 'wifi' in query:

            import webbrowser
            import time
            import pyautogui
            speak("opening router settings for your wifi")
            webbrowser.open("http://192.168.0.1/login.html")
            time.sleep(2)
            pyautogui.typewrite('wasdwasdwasd')
            pyautogui.press("enter")


        elif 'wi-fi' in query:
            import webbrowser
            import pyautogui
            import time
            speak("opening router settings for your wifi")
            webbrowser.open("http://192.168.0.1/login.html")
            time.sleep(2)
            pyautogui.typewrite('wasdwasdwasd')
            pyautogui.press("enter")

#-----------------------------open replit----------------------------------------

        elif 'replete' in query:
            import webbrowser
            speak("opening replit sir")
            webbrowser.open("https://replit.com/~")

#--------------------------gmail--------------------------------------

        elif 'open email' in query:
            import webbrowser
            speak("opening gmail sir")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

#----------------------------------speak after me---------------------------------------

        elif 'speak after me' in query:
            speak("okay sir what should i say after you")
            sam = takecommand().lower()
            speak(sam)
#-----------------------------check weather-----------------------

        elif 'check weather' in query:
            api_key = "ed49a32044386c40607445624addd441" 
            city = "Faridabad, IN" 
            get_weather(api_key, city)

#-------------------------enter my password-----------------------------

        elif 'enter my password' in query:
            import pyautogui
            speak('okay sir')
            pyautogui.typewrite("wasdwasdwasd")
            pyautogui.press('enter')

#---------------------------press enter------------------------------

        elif 'press enter' in query:
            import pyautogui
            pyautogui.press('enter')

#--------------------------enter my password only----------------------

        elif 'enter my password only' in query:
            import pyautogui
            speak('okay sir')
            pyautogui.typewrite("wasdwasdwasd")

#----------------------------open qr code for movies website-----------------------------

        elif 'open code' in query:
            from PIL import Image 
            import os

            image_path = "C:\\Users\\pcper\\OneDrive\\Desktop\\qrcodeforhdmovies.png"

            if os.path.exists(image_path):
                image = Image.open(image_path)
                image.show()
            else:
                print("eroor 40000004")

        elif 'close the picture' in query:
            import pyautogui
            pyautogui.hotkey('alt', 'f4')


        elif 'calculate currency' in query:
            speak("okay sir fetching the values of currency")
            speak("what currency do you want to calculate")
            wtbc = takecommand().lower()
            if 'dollars' in wtbc:
                speak("okay sir opening the calculator")
                c_calculator()

        elif 'temperature' in query:
            import webbrowser
            import time
            import pyautogui
            webbrowser.open("https://gemini.google.com/app")
            time.sleep(1)
            pyautogui.press('f11')
            time.sleep(5)
            pyautogui.typewrite("temperature in faridabad right now , explain.")
            pyautogui.press('enter')
            time.sleep(10)
            pyautogui.moveTo(1330 , 200 )
            pyautogui.click()

            time.sleep(25)

            with pyautogui.hold('ctrl'):
                pyautogui.press('W')

        elif 'what is the time' in query:
            import datetime
            import time 
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {strTime}")

        elif 'send a mail to mother' in query:
            import time
            import webbrowser
            import pyautogui
            speak("sir , what should  be the subject for the email ? ")
            subject = takecommand().lower()
            speak("fine sir , what should i write in the mail ?")
            what_in_email = takecommand().lower()
            email_id = 'ashmitsingh6596@gmail.com'
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=new")
            time.sleep(2)
            pyautogui.press('f11')
            time.sleep(8)
            pyautogui.moveTo(1350, 525)
            pyautogui.typewrite(email_id)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.moveTo(1300 , 580)
            pyautogui.click()
            pyautogui.typewrite(subject)
            pyautogui.press('enter')
            pyautogui.moveTo(1300, 630 )
            pyautogui.click()
            pyautogui.typewrite(what_in_email)
            pyautogui.moveTo(1280 , 1040)
            pyautogui.click()
            time.sleep(1)
            with pyautogui.hold('alt'):
                pyautogui.press('f4')
            time.sleep(1)
            pyautogui.press('enter')

        elif 'find pdf of a book' in query:
            speak("okay sir please enter the book title ")
            query = input("Enter the book title: ")

            # Call the search_pdf function
            search_pdf(query)

        elif 'find a book' in query:
            speak("okay sir please enter the book title ")
            query = input("Enter the book title: ")

            # Call the search_pdf function
            search_pdf(query)

        elif 'find an book' in query:
            speak("okay sir please enter the book title ")
            query = input("Enter the book title: ")

            # Call the search_pdf function
            search_pdf(query)

        elif 'buy a book' in query:
            import webbrowser
            import pyautogui
            import time
            speak("okay sir ")
            webbrowser.open("https://books.google.com/?authuser=0")
            time.sleep(4)
            speak("which book do you want to purchase")
            wbtbp = takecommand().lower()
            pyautogui.typewrite(wbtbp)
            pyautogui.press('enter')

        elif 'check my orders' in query:
            import webbrowser
            speak("okay sir i am fetching your orders of last 3 months on amazon")
            webbrowser.open('https://www.amazon.in/gp/css/order-history?ref_=nav_AccountFlyout_orders')

        elif 'check some electronics' in query:
            import webbrowser
            speak("okay sir i am fetching some new electronics for you")
            speak("from which shopping app should i check electronics")
            check_electronics_from_which_website = takecommand().lower()
            if 'amazon' in check_electronics_from_which_website:
                speak('which type of electronics should i find for you , laptop ,  gaming laptop , computer accesories , smartwatches , headphones , cameras , tablets or home audio ')
                wtoesip = takecommand().lower()
                if 'normal laptops' in wtoesip:
                    speak("i am finding the best laptops for casual usage")
                    webbrowser.open("https://www.amazon.in/s?rh=n%3A1375424031&fs=true&ref=lp_1375424031_sar")
                elif 'gaming laptops' in wtoesip:
                    speak("i am finding the best laptops for good gaming and with your budget ")
                    webbrowser.open("https://www.amazon.in/s?rh=n%3A7198569031&fs=true&ref=lp_7198569031_sar")
                elif 'headphones' in wtoesip:
                    speak("finding the best headphones for you")
                    webbrowser.open("https://www.amazon.in/s?rh=n%3A1388921031&fs=true&ref=lp_1388921031_sar")
                elif 'camera' in wtoesip:
                    speak("i am trying to find the best camera for you sir")
                    webbrowser.open("https://www.amazon.in/s?k=photography+camera+under+50000&rh=n%3A1388977031&ref=nb_sb_noss")
                elif 'smartwatch' in wtoesip:
                    speak("i am trying to find best smartwatches for you")
                    webbrowser.open("https://www.amazon.in/b/ref=cepc_sbc_atfbau_3?pf_rd_r=2EVWQKXK98MM3S81XJD5&pf_rd_p=b3a09f51-a204-4606-b8ca-ef2476655522&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-5&pf_rd_t=&pf_rd_i=976419031&node=11599648031")
                elif 'tablet' in wtoesip:
                    speak('okay  sir i am trying to find the best tablets for you')
                    webbrowser.open("https://www.amazon.in/s?rh=n%3A1375458031&fs=true&ref=lp_1375458031_sar")
                elif 'home audio' in wtoesip:
                    speak('okay sir i am trying to find best audio speakers for your home')
                    webbrowser.open('https://www.amazon.in/s?rh=n%3A1389365031&fs=true&ref=lp_1389365031_sar')
                elif 'computer accesories' in wtoesip:
                    speak("okay sir i am trying to find the best and usefull computer accesories for you")
                    webbrowser.open('https://www.amazon.in/s?rh=n%3A1375248031&fs=true&ref=lp_1375248031_sar')


        elif 'telegram' in query:
            import webbrowser
            speak("okay sir")
            webbrowser.open("https://web.telegram.org/a/#-4171709348")

        elif 'movie description' in query:
            import imdb
            movies_db = imdb.IMDb()
            speak('please tell me the movie name :')
            text = takecommand().lower()
            movies = movies_db.search_movie(text)
            speak(f'searching for {text}')
            speak("here's what i found")
            for movie in movies:
                title = movie['title']
                year = movie['year']
                speak(f'{title}-{year}')
                info = movie.getID()
                movie_info = movies_db.get_movie(info)
                rating = movie_info['rating']
                cast = movie_info['cast']
                actor = cast[0:5]
                plot = movie_info.get('plot outline', 'plot summary not available')
                print(f'{title} was realeased in {year} has imdb ratings of {rating}.it has a cast of {actor}. plot summary of movie is {plot}')
                speak(f'{title} was realeased in {year} has imdb ratings of {rating}.it has a cast of {actor}. plot summary of movie is {plot}')

        elif 'top news' in query:
            # Fetch and print Google News headlines for India
            headlines = fetch_google_news()
            for i, headline in enumerate(headlines, start=1):
                print(f"{i}. {headline}")
                speak(f"{i}. {headline}")

        elif 'locate network' in query:
            import wifi
            import pyautogui
            import time 
            speak("okay sir i am locating wifi networks near you")
            print(" Minky = 75% \n Tenda = 80% \n ashmit_airtel = 75% \n Dlink = 60% \n airtel_9711857337 = 40% \n airtel_nikhil_5g = 25% \n airtel rajan = 10% ")
            speak("Minky = 75% \n Tenda = 80% \n ashmit_airtel = 75% \n Dlink = 60% \n airtel_9711857337 = 40% \n airtel_nikhil_5g = 25% \n airtel rajan = 10% ")
            print("should i connect to any network of your choice")
            speak("should i connect to any network of your choice")
            take_connection = takecommand().lower()
            if 'yes' in take_connection:
                speak("which wifi network do you want me to connect")
                connection_name = takecommand().lower()
                if 'tenda' in connection_name:
                    speak("looks like i dont have the password for tenda , so would you like me to hack this network")
                    wyltht = takecommand().lower()
                    if 'yes' in wyltht:
                        speak("okay sir i am hacking tenda's network router")
                        speak('i have found 5 users connected to the network')
                        time.sleep(3)
                        speak("i have found the handshake file of the router network")
                        speak("looks like that tenda has a lower security password level so i am trying brutteforcing most common one lakh passwords for you")
                        speak("this might take a few seconds")
                        time.sleep(7)
                        speak("okay sir i have found a perfect variabble from your text file passwords , variable number 3470 is the password of tenda")
                        speak("sir i am connecting to the tenda's network , this might break our connection , i would suggest you to restart me")
                        ssid = "Tenda"
                        password = "Password"
                        connect_to_wifi(ssid, password)
                    else:
                        speak("okay sir")
                elif 'ashmit' in connection_name:
                    speak("okay sir, looks like i have the password for this network so i am simply connecting to it")
                    ssid = "ashmit_airtel"
                    password = "54zlbgyk"
                    connect_to_wifi(ssid, password)

                elif 'minki' in connection_name:
                    speak("looks like i dont have the password for the network you want me to connect, would you like me to hack this network")
                    wylmthtn = takecommand().lower()
                    if 'yes' in wylmthtn:
                        speak("okay sir i am hacking Minky's network router")
                        speak('i have found 3 users connected to the network')
                        time.sleep(3)
                        speak("i have found the handshake file of the router network")
                        speak("looks like that minky has a higher security password level so i am trying brutteforcing the traditional method ")
                        speak("this might take a few seconds")
                        time.sleep(7)
                        speak("okay sir i have found a perfect variabble from the traditional bruuteforcing method, looks like the variable number 74536576 is appropriate for minky's network")
                        speak("sir i am connecting to the minky's network , this might break our connection , i would suggest you to restart me")
                        ssid = "Minky"
                        password = "Minky#1689"
                        connect_to_wifi(ssid, password)
                    else:
                        speak("okay sir")   

                else:
                    speak("i could not find the network you want me to connect")                    

            elif 'no' in take_connection:
                speak("okay sir")

            else:
                speak("okay sir")


        elif 'calculate power' in query:
            speak("okay sir , enter the number")
            no_1 = float(input("enter the number : "))
            speak("okay sir , enter the power")
            no_2 = float(input("enter the power : "))
            reslt = no_1 ** no_2
            print(reslt)
            speak(f'the value of {no_1} with power of {no_2} is {reslt}')


        elif 'send message to father and say him to' in query:
            removing_phrase = 'send message to father and say him to'
            text = query.replace(removing_phrase, '').strip()
            import pyautogui as pg
            import time 
            pg.press('win')
            pg.typewrite('whatsapp')
            pg.press('enter')
            time.sleep(5)
            pg.typewrite('papa')
            time.sleep(1)
            pg.moveTo(150 , 180)
            pg.click()
            time.sleep(1)
            pg.typewrite(text)
            pg.press('enter')
            pg.hold('alt', 'f4')

        elif 'send message to father and say him' in query:
            removing_phrase = 'send message to father and say him'
            text = query.replace(removing_phrase, '').strip()
            import pyautogui as pg
            import time 
            pg.press('win')
            pg.typewrite('whatsapp')
            pg.press('enter')
            time.sleep(5)
            pg.typewrite('papa')
            time.sleep(1)
            pg.moveTo(150 , 180)
            pg.click()
            time.sleep(1)
            pg.typewrite(text)
            pg.press('enter')
            pg.hold('alt', 'f4')

        elif 'send message to dad and say him to' in query:
            removing_phrase = 'send message to dad and say him to'
            text = query.replace(removing_phrase, '').strip()
            import pyautogui as pg
            import time 
            pg.press('win')
            pg.typewrite('whatsapp')
            pg.press('enter')
            time.sleep(5)
            pg.typewrite('papa')
            time.sleep(1)
            pg.moveTo(150 , 180)
            pg.click()
            time.sleep(1)
            pg.typewrite(text)
            pg.press('enter')
            pg.hold('alt', 'f4')

        elif 'send message to dad and say him' in query:
            removing_phrase = 'send message to dad and say him'
            text = query.replace(removing_phrase, '').strip()
            import pyautogui as pg
            import time 
            pg.press('win')
            pg.typewrite('whatsapp')
            pg.press('enter')
            time.sleep(5)
            pg.typewrite('papa')
            time.sleep(1)
            pg.moveTo(150 , 180)
            pg.click()
            time.sleep(1)
            pg.typewrite(text)
            pg.press('enter')
            pg.hold('alt', 'f4')

        elif 'send message to sister and say her to' in query:
            removing_phrase = 'send message to sister and say her to'
            text = query.replace(removing_phrase, '').strip()
            import pyautogui as pg
            import time 
            pg.press('win')
            pg.typewrite('whatsapp')
            pg.press('enter')
            time.sleep(5)
            pg.typewrite('didi')
            time.sleep(1)
            pg.moveTo(150 , 180)
            pg.click()
            time.sleep(1)
            pg.typewrite(text)
            pg.press('enter')
            pg.hold('alt', 'f4')

        elif 'send message to sister and say her' in query:
            removing_phrase = 'send message to sister and say her'
            text = query.replace(removing_phrase, '').strip()
            import pyautogui as pg
            import time 
            pg.press('win')
            pg.typewrite('whatsapp')
            pg.press('enter')
            time.sleep(5)
            pg.typewrite('didi')
            time.sleep(1)
            pg.moveTo(150 , 180)
            pg.click()
            time.sleep(1)
            pg.typewrite(text)
            pg.press('enter')
            pg.hold('alt', 'f4')

        elif 'can you help me for something' in query:
            speak("ofcourse sir , what kind of help do you want from me ?")

        elif 'redisign my room' in query:
            import subprocess
            from PIL import Image
            import time
            import pyautogui
            import os
            import sys 

            speak("okay , give me access to your room camera's so that i can help you with some inovative ideas")
            camera_acces = input('enter your password here : ')
            if camera_acces == 'wasd':

                speak("welcome sir , you have logged in to the administration of havikson group")
                speak("i am starting the scanning process , i will suggest you to clear obsticals so that i can scan properly")
                speak("scanning process started")
                loading_screen(10)
                speak("scanning process completed , i am finding  options for your room")
                speak("this might take few seconds ")
                loading_screen(4)
                speak("sir , i have founded the best options for your room ")
                speak("you can snap to change the photo.")
                img1 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img1.jpeg"
                img2 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img2.jpeg"
                img3 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img3.jpeg"
                img4 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img4.jpeg"

                if os.path.exists(img1):
                    image = Image.open(img1)
                    image.show()
                else:
                    print("eroor 40000004")
                ctcp()
                ctcp2()
                ctcp3()
                ctcp4()


            else:
                speak('you have entered wrong password , therefore i am not able to connect to havikson group address')

        elif 'room decoration' in query:
            import subprocess
            from PIL import Image
            import time
            import pyautogui
            import os
            import sys 

            speak("okay , give me access to your room camera's so that i can help you with some inovative ideas")
            camera_acces = input('enter your password here : ')
            if camera_acces == 'wasd':

                speak("welcome sir , you have logged in to the administration of havikson group")
                speak("i am starting the scanning process , i will suggest you to clear obsticals so that i can scan properly")
                speak("scanning process started")
                loading_screen(10)
                speak("scanning process completed , i am finding  options for your room")
                speak("this might take few seconds ")
                loading_screen(4)
                speak("sir , i have founded the best options for your room ")
                speak("you can snap to change the photo.")
                img1 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img1.jpeg"
                img2 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img2.jpeg"
                img3 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img3.jpeg"
                img4 = "C:\\Users\\pcper\\OneDrive\\Desktop\\img4.jpeg"

                if os.path.exists(img1):
                    image = Image.open(img1)
                    image.show()
                else:
                    print("eroor 40000004")
                ctcp()
                ctcp2()
                ctcp3()
                ctcp4()


            else:
                speak('you have entered wrong password , therefore i am not able to connect to havikson group address')

        elif 'video call mother' in query:
            speak("okay sir i am video calling your mother")
            import time
            import pyautogui
            pyautogui.moveTo(659 , 1070)
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)
            pyautogui.typewrite("mata shrii")
            time.sleep(1)
            pyautogui.moveTo(150, 180)
            time.sleep(1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(1770, 70)
            time.sleep(1)
            pyautogui.click()

        elif 'video call sister' in query:
            speak("okay sir i am video calling your sister")
            import time
            import pyautogui
            pyautogui.moveTo(659 , 1070)
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)
            pyautogui.typewrite("didi")
            time.sleep(1)
            pyautogui.moveTo(150, 180)
            time.sleep(1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(1770, 70)
            time.sleep(1)
            pyautogui.click()

        elif 'video call father' in query:
            speak("okay sir i am video calling your father")
            import time
            import pyautogui
            pyautogui.moveTo(659 , 1070)
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)
            pyautogui.typewrite("pampa")
            time.sleep(1)
            pyautogui.moveTo(150, 180)
            time.sleep(1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(1770, 70)
            time.sleep(1)
            pyautogui.click()

        elif "tell me my schedule for tomorrow" in query:
            from PIL import Image 
            import os
            import pyautogui
            from datetime import date
            today = date.today()
            t = ( today.strftime("%A"))
            print(t)
            speak('okay sir')
            tt = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\timetable1.png"

            if os.path.exists(tt):
                image = Image.open(tt)
                image.show()
            else:
                print("eroor 40000004")
            if t == 'Monday':
                speak('i guess your time table for tuesday is as follows.')
                speak('your first class is of social science')
                speak('second class is of mathematics')
                speak('third class is of english')
                speak('fourth class is of maths')
                speak('fifth class is of biology')
                speak('sixth class is of chemistry')
                speak('and last class is of hindi')
            if t == 'Tuesday':
                speak('i guess your time table for wednesday is as follows.')
                speak('your first class is of social science')
                speak('second class is of mathematics')
                speak('third class is of artificial')
                speak('fourth class is of english')
                speak('fifth class is of hindi')
                speak('sixth class is of mathematics')
                speak('and last class is of biology')
            if t == 'Wednesday':
                speak('i guess your time table for thursday is as follows.')
                speak('your first class is of social science')
                speak('second class is of mathematics')
                speak('third class is of english')
                speak('fourth class is of hindi')
                speak('fifth class is of physics')
                speak('sixth class is of social science')
                speak('and last class is of hindi')
            if t == 'Thursday':
                speak('i guess your time table for friday is as follows.')
                speak('your first class is of social science')
                speak('second class is of mathematics')
                speak('third class is of english')
                speak('fourth class is of english')
                speak('fifth class is of library')
                speak('sixth class is of mathematics')
                speak('and last class is of physics')  
            if t == 'Saturday':
                speak('i guess your time table for monday is as follows.')
                speak('your first class is of social science')
                speak('second class is of mathematics')
                speak('third class is of hindi')
                speak('fourth class is of english')
                speak('fifth class is of games')
                speak('sixth class is of chemistry')
                speak('and last class is of artificial intelligence')
            if t == 'Friday':
                speak('i guess your time table for monday is as follows.')
                speak('your first class is of social science')
                speak('second class is of mathematics')
                speak('third class is of hindi')
                speak('fourth class is of english')
                speak('fifth class is of games')
                speak('sixth class is of chemistry')
                speak('and last class is of artificial intelligence')
            if t == 'Sunday':
                speak('i guess your time table for monday is as follows.')
                speak('your first class is of social science')
                speak('second class is of mathematics')
                speak('third class is of hindi')
                speak('fourth class is of english')
                speak('fifth class is of games')
                speak('sixth class is of chemistry')
                speak('and last class is of artificial intelligence')


            speak('you can snap to close the time table')
            clap_to_close_images()


        elif 'how r u' in query:
            import random
            hry1 = ["i'm fine sir , is there anything that i can help with you .", "i'm fine sir , may i know is there anything i can help you with.", "i'm fine sir , may i know if there is any problem that i can help you with.", "oh i thought you forgot me sir, i'm fine just a little bit tired.", "i think i have a headache right now but , i'm good to go.", "okay sir , don't try to put butter on me so please tell me how can i help you"]
            selected_hry1 = random.choice(hry1)
            speak(selected_hry1)

        elif 'how are you' in query:
            import random
            hry = ["i'm fine sir , is there anything that i can help with you .", "i'm fine sir , may i know is there anything i can help you with.", "i'm fine sir , may i know if there is any problem that i can help you with.", "oh i thought you forgot me sir, i'm fine just a little bit tired.", "i think i have a headache right now but , i'm good to go.", "okay sir , don't try to put butter on me so please tell me how can i help you"]
            selected_hry = random.choice(hry)
            speak(selected_hry)

        elif 'set an reminder' in query:
            speak('okay sir , enter what should be the reminder for ?')
            sub = input("enter the title for the reminder : ")
            speak("pelase enter the time for the reminder in 24 hours format ")
            timem = input("enter the time here : ")

        elif 'hack one instagram account' in query:
            import time
            import pyautogui
            import webbrowser
            speak("okay sir , do you have the chache file for this account in your any device ?")
            d_i_h_acces = takecommand().lower()
            if 'yes' in d_i_h_acces:
                navya_one = "navya2024!?"
                navya_two = "navya2676!?"
                ashmit_main = "wasdwasdwasd"
                ashmit_two = "wasdwasdwasd"
                speak("okay sir enter the account which you want me to hack")
                account_name = input("enter the account which you want me to hack : ")
                speak("okay sir , can you help me with some clues or information such as birthdate ? ")
                bd = input("birth date : ")
                crush = input("any particular person he/she likes : ")
                mother = input('his/her mother name : ')
                father = input('his / her father name : ')
                brothersister = input("any brother or sister name : ")
                previous = input("any previous password : ")
                if account_name == "navyasharma1438":
                    speak("okay sir i am starting the process for hacking the id")
                    speak("i am going to apply the estimated method , and the previous password to guess the new password")
                    speak("this  might take a few while")
                    time.sleep(10)
                    speak("okay sir i have found the best combination of password for this account")
                    speak(f"should i login to {account_name} ")
                    sili = takecommand().lower()
                    if "yes" in sili:
                        speak("okay sir this process could take a while")
                        webbrowser.open("shit")
                        time.sleep(4)
                        pyautogui.hotkey('ctrl', 'shift', 'n')
                        time.sleep(1)
                        pyautogui.typewrite("https://www.instagram.com/")
                        time.sleep(2)
                        pyautogui.press('f11')
                        time.sleep(1)

        elif 'play rock paper scissors' in query:
            import random 
            import time
            import pyautogui
            import datetime
            while True:

                sps = ['stone', 'paper', 'scissors']
                selected_sps = random.choice(sps)
                speak("okay sir what do you choose")
                wic = takecommand().lower()
                if 'scissors' in wic and selected_sps == "stone":
                    print("you lose")
                    speak("you lose")
                elif 'scissors' in wic and selected_sps == "paper":
                    print("you win")
                    speak("you win")
                elif 'scissors' in wic and selected_sps == "scissors":
                    print("it's  a tie")
                    speak("it's a tie")
                elif 'stone' in wic and selected_sps == "stone":
                    print("it's a tie")
                    speak("it's a tie")
                elif 'stone' in wic and selected_sps == "paper":
                    print("you lose")
                    speak("you lose")
                elif 'stone' in wic and selected_sps == "scissors":
                    print("you win")
                    speak("you win")
                elif 'rock' in wic and selected_sps == "stone":
                    print("it's a tie")
                    speak("it's a tie")
                elif 'rock' in wic and selected_sps == "paper":
                    print("you lose")
                    speak("you lose")
                elif 'rock' in wic and selected_sps == "scissors":
                    print("you win")
                    speak("you win")
                elif 'paper' in wic and selected_sps == "paper":
                    print("it's a tie")
                    speak("it's a tie")
                elif 'paper' in wic and selected_sps == "stone":
                    print("you win")
                    speak("you win")
                elif 'paper' in wic and selected_sps == "scissors":
                    print("you lose")
                    speak("you lose")
                elif "don't want to play" in wic:
                    speak("okay sir")
                    break
                else:
                    print("i guess that's not an option sir")
                    speak("i guess , that's not an option sir")

        elif 'what are you doing' in query:
            speak('nothing just chilling , if you have any problem you can discuss with me , i will probably find a solution for that')
            
        elif 'schedule my day' in query:
            import pyautogui as py
            import time as t
            speak("okay sir should i delete all the before task ? ")
            delete = takecommand().lower()
            if 'yes' in delete:
                speak("okay sir , i am deleting all before task. ")
                py.moveTo(1915, 1079)
                py.click()
                t.sleep(1)
                py.moveTo(1850, 960)
                py.click(clicks=2, interval=0.25)
                t.sleep(1)
                py.hotkey('ctrl', 'a')
                py.press('backspace')
                py.hotkey('alt', 'f4')
                t.sleep(1)
                py.press('enter')
                py.hotkey('alt', 'tab')
            if 'sure' in delete:
                speak("okay sir , i am deleting all before task. ")
                py.moveTo(1915, 1079)
                py.click()
                t.sleep(1)
                py.moveTo(1850, 960)
                py.click(clicks=2, interval=0.25)
                t.sleep(1)
                py.hotkey('ctrl', 'a')
                py.press('backspace')
                py.hotkey('alt', 'f4')
                t.sleep(1)
                py.press('enter')
                py.hotkey('alt', 'tab')
            if 'please' in delete:
                speak("okay sir , i am deleting all before task. ")
                py.moveTo(1915, 1079)
                py.click()
                t.sleep(1)
                py.moveTo(1850, 960)
                py.click(clicks=2, interval=0.25)
                t.sleep(1)
                py.hotkey('ctrl', 'a')
                py.press('backspace')
                py.hotkey('alt', 'f4')
                t.sleep(1)
                py.press('enter')
                py.hotkey('alt', 'tab')
            if 'okay' in delete:
                speak("okay sir , i am deleting all before task. ")
                py.moveTo(1915, 1079)
                py.click()
                t.sleep(1)
                py.moveTo(1850, 960)
                py.click(clicks=2, interval=0.25)
                t.sleep(1)
                py.hotkey('ctrl', 'a')
                py.press('backspace')
                py.hotkey('alt', 'f4')
                t.sleep(1)
                py.press('enter')
                py.hotkey('alt', 'tab')
            else:
                speak("okay sir")

            speak("okay sir enter the number of tasks you want to do.")
            no_task = float(input("enter the number of tasks you want to do : "))
            if no_task == 1:
                task = input("enter the task : ")
                py.moveTo(1915, 1079)
                py.click()
                t.sleep(1)
                py.moveTo(1850, 960)
                py.click(clicks=2, interval=0.25)
                t.sleep(1)
                py.typewrite(f"1. {task}")
                py.hotkey('alt', 'f4')
                t.sleep(1)
                py.press('enter')
                py.hotkey("alt", 'tab')

            if no_task == 2:
                task_one = input("enter the task number 1 : ")
                task_two = input("enter the task number 2 : ")
                py.moveTo(1915, 1079)
                py.click()
                t.sleep(1)
                py.moveTo(1850, 960)
                py.click(clicks=2, interval=0.25)
                t.sleep(1)
                py.typewrite(f"1. {task_one}")
                py.press('enter')
                py.typewrite(f"2. {task_two}")
                py.hotkey('alt', 'f4')
                t.sleep(1)
                py.press('enter')
                py.hotkey("alt", 'tab')

            if no_task == 3:
                task_onee = input("enter the task numebr 1 : ")
                task_twoe = input("enter the task number 2 : ")
                task_threee = input("enter the task number 3 : ")
                py.moveTo(1915, 1079)
                py.click()
                t.sleep(1)
                py.moveTo(1850, 960)
                py.click(clicks=2, interval=0.25)
                t.sleep(1)
                py.typewrite(f"1. {task_onee}")
                py.press('enter')
                py.typewrite(f"2. {task_twoe}")
                py.press('enter')
                py.typewrite(f"3. {task_threee}")
                py.hotkey('alt', 'f4')
                t.sleep(1)
                py.press('enter')
                py.hotkey("alt", 'tab')

            if no_task == 4:
                task_oneee = input("enter the task numebr 1 : ")
                task_twoee = input("enter the task number 2 : ")
                task_threeee = input("enter the task number 3 : ")
                task_foureee = input("enter the task number 4 : ")
                py.moveTo(1915, 1079)
                py.click()
                t.sleep(1)
                py.moveTo(1850, 960)
                py.click(clicks=2, interval=0.25)
                t.sleep(1)
                py.typewrite(f"1. {task_oneee}")
                py.press('enter')
                py.typewrite(f"2. {task_twoee}")
                py.press('enter')
                py.typewrite(f"3. {task_threeee}")
                py.press('enter')
                py.typewrite(f"4. {task_foureee}")
                py.hotkey('alt', 'f4')
                t.sleep(1)
                py.press('enter')
                py.hotkey("alt", 'tab')

            if no_task == 5:
                task_1 = input("enter the task number 1 : ")
                task_2 = input("enter the task number 2 : ")
                task_3 = input("enter the task number 3 : ")
                task_4 = input("enter the task number 4 : ")
                task_5 = input("enter the task number 5 : ")
                py.moveTo(1915, 1079)
                py.click()
                t.sleep(1)
                py.moveTo(1850, 960)
                py.click(clicks=2, interval=0.25)
                t.sleep(1)
                py.typewrite(f"1. {task_1}")
                py.press('enter')
                py.typewrite(f"2. {task_2}")
                py.press('enter')
                py.typewrite(f"3. {task_3}")
                py.press('enter')
                py.typewrite(f"4. {task_4}")
                py.press('enter')
                py.typewrite(f"5. {task_5}")
                py.hotkey('alt', 'f4')
                t.sleep(1)
                py.press('enter')
                py.hotkey("alt", 'tab')

        elif 'my task' in query:
            import time as t
            import os 
            import pyautogui as py
            speak("okay sir i am opening your tasks for today")
            py.moveTo(1915, 1079)
            py.click()
            t.sleep(1)
            py.moveTo(1850, 960)
            py.click(clicks=2, interval=0.25)
            speak("here's your tasks for today sir !!!")
            speak('you can snap to close your tasks.')
            snap_to_close_notepad()
            py.hotkey('alt', 'tab')

        elif 'find image of' in query:
            import webbrowser
            modified_input = query.replace('find image of', '')
            print(modified_input.strip())
            webbrowser.open(f'https://www.google.com/search?q={modified_input.strip()}&sca_esv=004afa00accdc41c&sca_upv=1&hl=en&sxsrf=ACQVn09CTrEn9EKERhvO3w5VlHaga36C3Q:1712489253287&source=hp&biw=2400&bih=1191&ei=JYMSZofdDaXvseMP-fqEuAY&iflsig=ANes7DEAAAAAZhKRNWvvMi3p_ymYXIvNftbE1TYmjmCw&ved=0ahUKEwjHg_vM_6-FAxWld2wGHXk9AWcQ4dUDCA8&uact=5&oq=hardik+pandya+&gs_lp=EgNpbWciDmhhcmRpayBwYW5keWEgMggQABiABBixAzILEAAYgAQYsQMYgwEyBBAAGAMyCBAAGIAEGLEDMggQABiABBixAzIEEAAYAzILEAAYgAQYsQMYgwEyDhAAGIAEGIoFGLEDGIMBMgsQABiABBixAxiDATIOEAAYgAQYigUYsQMYgwFI8htQAFj6F3AAeACQAQCYAcYBoAHODqoBBDAuMTS4AQPIAQD4AQGKAgtnd3Mtd2l6LWltZ5gCDqACgQ_CAgQQIxgnwgIFEAAYgASYAwCSBwYwLjEzLjGgB8Ba&sclient=img&udm=2')
            
        elif 'switch tab' in query:
            import pyautogui
            speak("okay sir")
            pyautogui.hotkey("alt", 'tab')
        elif 'send a message to mother in which tell her to' in query:
            import pyautogui
            import time
            what_she_got_texted = query.replace('send a message to mother in which tell her to', '')
            print(what_she_got_texted.strip())
            speak("okay sir sending message")
            speak("okay sir ")
            pyautogui.moveTo(x=659, y=1070)
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)
            pyautogui.typewrite('mata shrii')
            pyautogui.moveTo(150 , 180)
            pyautogui.click()
            time.sleep(1)
            pyautogui.typewrite(what_she_got_texted.strip())
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            with pyautogui.hold('alt'):
                pyautogui.press('f4')

        elif 'my cpu usage' in query:
            import psutil
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"CPU Usage: {cpu_usage}%")
            speak(f"your central processing unit Usage is  {cpu_usage}%")
        elif 'memory usage' in query:
            import psutil
            memory_info = psutil.virtual_memory()
            memory_percent = memory_info.percent
            print(f"Memory Usage: {memory_percent}%")
            speak(f"your memory usage is {memory_percent}%")
        elif 'disk usage' in query:
            import psutil
            disk_info = psutil.disk_usage('/')
            disk_percent = disk_info.percent
            print(f"Disk Usage: {disk_percent}%")
            speak(f'your disk usage is {disk_percent}%')
        elif 'disk information' in query:
            get_disk_info()
        elif 'memory information' in query:
            get_memory_info()
        elif 'cpu information' in query:
            get_cpu_times_percent()

        elif 'check system usage' in query:
            import psutil
            import time
            speak('okay sir wait ,while i am checking the system usage')
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"CPU Usage: {cpu_usage}%")
            speak(f"your central processing unit Usage is  {cpu_usage}%")
            memory_info = psutil.virtual_memory()
            memory_percent = memory_info.percent
            print(f"Memory Usage: {memory_percent}%")
            speak(f"your memory usage is {memory_percent}%")
            disk_info = psutil.disk_usage('/')
            disk_percent = disk_info.percent
            print(f"Disk Usage: {disk_percent}%")
            speak(f'your disk usage is {disk_percent}%')
        elif 'check my system usage' in query:
            import psutil
            import time
            speak('okay sir wait ,while i am checking the system usage')
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"CPU Usage: {cpu_usage}%")
            speak(f"your central processing unit Usage is  {cpu_usage}%")
            memory_info = psutil.virtual_memory()
            memory_percent = memory_info.percent
            print(f"Memory Usage: {memory_percent}%")
            speak(f"your memory usage is {memory_percent}%")
            disk_info = psutil.disk_usage('/')
            disk_percent = disk_info.percent
            print(f"Disk Usage: {disk_percent}%")
            speak(f'your disk usage is {disk_percent}%')

            
        elif 'activate mouse' in query:
            import pyautogui
            import time 
            speak('okay sir activating mouse settings.')
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.typewrite('qhm-286g')
            time.sleep(1)
            speak('please give acces to your administration')
            pyautogui.press('enter')
            time.sleep(3)
            speak('your mouse drivers has been activated')

        elif 'bark like a dog' in query:
            from playsound import playsound
            speak("okay sir")
            audio = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\dog-barking-70772.mp3"
            playsound(audio)

        elif "what's my bank balance" in query:
            import time 
            speak("okay sir i am checking your bank balance")
            time.sleep(5)
            amount = 'one lakh twenty thousand three hundred ninety one rupees'
            speak(f"you have {amount}")



        elif 'open porn' in query:
            speak('okay sir')
        
        elif 'follow an instagram account' in query:
            import webbrowser as web
            import os 
            import pyautogui as py
            import time as t
            speak("okay sir please enter the username of the profile you want me to follow ")


            username = input('enter the username : ')
            web.open(f"https://www.instagram.com/{username}/")

            py.moveTo(1040,127)
            t.sleep(5)
            py.click()
            t.sleep(1)
            os.system("taskkill /f /im msedge.exe")
            speak(f"succesfully followed {username} on instagram")

        elif 'follow a instagram account' in query:
            import webbrowser as web
            import os 
            import pyautogui as py
            import time as t
            speak("okay sir please enter the username of the profile you want me to follow ")


            username = input('enter the username : ')
            web.open(f"https://www.instagram.com/{username}/")

            py.moveTo(1040,127)
            t.sleep(5)
            py.click()
            t.sleep(1)
            os.system("taskkill /f /im msedge.exe")
            speak(f"succesfully followed {username} on instagram")


        elif 'follow instagram account' in query:
            import webbrowser as web
            import os 
            import pyautogui as py
            import time as t
            speak("okay sir please enter the username of the profile you want me to follow ")


            username = input('enter the username : ')
            web.open(f"https://www.instagram.com/{username}/")

            py.moveTo(1040,127)
            t.sleep(5)
            py.click()
            t.sleep(1)
            os.system("taskkill /f /im msedge.exe")
            speak(f"succesfully followed {username} on instagram")

        elif 'follow one instagram account' in query:
            import webbrowser as web
            import os 
            import pyautogui as py
            import time as t
            speak("okay sir please enter the username of the profile you want me to follow ")


            username = input('enter the username : ')
            web.open(f"https://www.instagram.com/{username}/")

            py.moveTo(1040,127)
            t.sleep(5)
            py.click()
            t.sleep(1)
            os.system("taskkill /f /im msedge.exe")
            speak(f"succesfully followed {username} on instagram")

        elif 'check latest messages from school group' in query:
            import time
            import pyautogui as py
            
            speak('okay sir checking latest messages from your school group .')
            py.press('win')
            time.sleep(1)
            py.typewrite('whatsapp web')
            time.sleep(1)
            py.press('enter')
            time.sleep(7)
            py.moveTo(150,200)
            time.sleep(1)
            py.click()
            speak('sir these are your latest messages from your school group.')
            speak('you can snap to close it.')
            clap_to_close_manually()

        elif 'hack a phone number' in query:
            import phonenumbers
            import folium
            import requests
            from collections import MutableMapping
            from collections.abc import MutableMapping
            import geocoder
            from phonenumbers import geocoder, timezone, carrier
            speak('enter the phonenumber you want to track')
            # Enter the phone number with the country code
            pn = input('PHONE NUMBER  : ')
            phone_number = ("+91" + pn)
            speak('sir please enter the name for the map file')
            ms = input("what will you name this file : ")
            # Parse the phone number
            phone_number_parsed = phonenumbers.parse(phone_number)

            # Get the geolocation of the phone number
            geolocation = phonenumbers.geocoder.description_for_number(phone_number_parsed, "en")

            # Use a geocoding API to fetch the latitude and longitude coordinates
            response = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={geolocation}&key=e2e2b5da9315468eaa1daea4abad96ce")
            data = response.json()
            latitude = data["results"][0]["geometry"]["lat"]
            longitude = data["results"][0]["geometry"]["lng"]

            # Generate a map using Folium library and mark the location on it
            map = folium.Map(location=[latitude, longitude], zoom_start=10)
            folium.Marker([latitude, longitude]).add_to(map)
            map.save(f"{ms}.html")
            speak(f"sir i have saved the location of the phonenumber as {ms}.html ")

            phoneNumber=phonenumbers.parse("+91" + pn)
            timeZone=timezone.time_zones_for_number(phoneNumber)

            Carrier = carrier.name_for_number(phoneNumber,'en')

            Region=geocoder.description_for_number(phoneNumber,'en')
            speak(f"here's the information of mobile number {pn}")
            print(phoneNumber)
            print(timeZone)
            print(Carrier)
            print(Region)
        elif 'hack one phone number' in query:
            import phonenumbers
            from collections import MutableMapping
            from collections.abc import MutableMapping
            import folium
            import requests
            import geocoder
            from geocoder.arcgis import ArcgisQuery
            from phonenumbers import geocoder, timezone, carrier
            speak('enter the phonenumber you want to track')
            # Enter the phone number with the country code
            pn = input('PHONE NUMBER  : ')
            phone_number = ("+91" + pn)
            speak('sir please enter the name for the map file')
            ms = input("what will you name this file : ")
            # Parse the phone number
            phone_number_parsed = phonenumbers.parse(phone_number)

            # Get the geolocation of the phone number
            geolocation = phonenumbers.geocoder.description_for_number(phone_number_parsed, "en")

            # Use a geocoding API to fetch the latitude and longitude coordinates
            response = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={geolocation}&key=e2e2b5da9315468eaa1daea4abad96ce")
            data = response.json()
            latitude = data["results"][0]["geometry"]["lat"]
            longitude = data["results"][0]["geometry"]["lng"]

            # Generate a map using Folium library and mark the location on it
            map = folium.Map(location=[latitude, longitude], zoom_start=10)
            folium.Marker([latitude, longitude]).add_to(map)
            map.save(f"{ms}.html")
            speak(f"sir i have saved the location of the phonenumber as {ms}.html ")

            phoneNumber=phonenumbers.parse("+91" + pn)
            timeZone=timezone.time_zones_for_number(phoneNumber)

            Carrier = carrier.name_for_number(phoneNumber,'en')

            Region=geocoder.description_for_number(phoneNumber,'en')
            speak(f"here's the information of mobile number {pn}")
            print(phoneNumber)
            print(timeZone)
            print(Carrier)
            print(Region)
            
        elif 'get information of a phone number' in query:
            import phonenumbers
            from collections import MutableMapping
            from collections.abc import MutableMapping
            import folium
            import requests
            import geocoder
            from geocoder.arcgis import ArcgisQuery
            from phonenumbers import geocoder, timezone, carrier
            speak('enter the phonenumber you want to track')
            # Enter the phone number with the country code
            pn = input('PHONE NUMBER  : ')
            phone_number = ("+91" + pn)
            speak('sir please enter the title for the map file ')
            ms = input("what will you name this file : ")
            # Parse the phone number
            phone_number_parsed = phonenumbers.parse(phone_number)

            # Get the geolocation of the phone number
            geolocation = phonenumbers.geocoder.description_for_number(phone_number_parsed, "en")

            # Use a geocoding API to fetch the latitude and longitude coordinates
            response = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={geolocation}&key=e2e2b5da9315468eaa1daea4abad96ce")
            data = response.json()
            latitude = data["results"][0]["geometry"]["lat"]
            longitude = data["results"][0]["geometry"]["lng"]

            # Generate a map using Folium library and mark the location on it
            map = folium.Map(location=[latitude, longitude], zoom_start=10)
            folium.Marker([latitude, longitude]).add_to(map)
            map.save(f"{ms}.html")
            speak(f"sir i have saved the location of the phonenumber as {ms}.html ")

            phoneNumber=phonenumbers.parse("+91" + pn)
            timeZone=timezone.time_zones_for_number(phoneNumber)

            Carrier = carrier.name_for_number(phoneNumber,'en')

            Region=geocoder.description_for_number(phoneNumber,'en')
            speak(f"here's the information of mobile number {pn}")
            print(phoneNumber)
            print(timeZone)
            print(Carrier)
            print(Region)

        elif 'track a phone number' in query:
            import phonenumbers
            import folium
            import requests
            import geocoder
            from geocoder.arcgis import ArcgisQuery
            from collections import MutableMapping
            from collections.abc import MutableMapping
            from phonenumbers import geocoder, timezone, carrier
            speak('enter the phonenumber you want to track')
            # Enter the phone number with the country code
            pn = input('PHONE NUMBER  : ')
            phone_number = ("+91" + pn)
            speak('sir please enter the name for the map file')
            ms = input("what will you name this file : ")
            # Parse the phone number
            phone_number_parsed = phonenumbers.parse(phone_number)

            # Get the geolocation of the phone number
            geolocation = phonenumbers.geocoder.description_for_number(phone_number_parsed, "en")

            # Use a geocoding API to fetch the latitude and longitude coordinates
            response = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={geolocation}&key=e2e2b5da9315468eaa1daea4abad96ce")
            data = response.json()
            latitude = data["results"][0]["geometry"]["lat"]
            longitude = data["results"][0]["geometry"]["lng"]

            # Generate a map using Folium library and mark the location on it
            map = folium.Map(location=[latitude, longitude], zoom_start=10)
            folium.Marker([latitude, longitude]).add_to(map)
            map.save(f"{ms}.html")
            speak(f"sir i have saved the location of the phonenumber as {ms}.html ")

            phoneNumber=phonenumbers.parse("+91" + pn)
            timeZone=timezone.time_zones_for_number(phoneNumber)

            Carrier = carrier.name_for_number(phoneNumber,'en')

            Region=geocoder.description_for_number(phoneNumber,'en')
            speak(f"here's the information of mobile number {pn}")
            print(phoneNumber)
            print(timeZone)
            print(Carrier)
            print(Region)

        elif 'turn on the slideshow' in query:
            import pyautogui as py
            import time as  t
            from playsound import playsound
            import sys
            speak('okay sir i am executing the slideshow and shutting down myself')
            py.hotkey('alt', 'tab')
            t.sleep(1)
            py.press('f5')
            shutdown_snd = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\wake-up-the-robot-84894.mp3"
            playsound(shutdown_snd)
            speak('happy anniversary to both of you guys')
            sys.exit()
        
        elif 'start the slideshow' in query:
            import pyautogui as py
            import time as  t
            from playsound import playsound
            import sys
            speak('okay sir i am executing the slideshow and shutting down myself')
            py.hotkey('alt', 'tab')
            t.sleep(1)
            py.press('f5')
            shutdown_snd = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\wake-up-the-robot-84894.mp3"
            playsound(shutdown_snd)
            speak('happy anniversary to both of you guys')
            sys.exit()

        elif 'start the show' in query:
            import pyautogui as py
            import time as  t
            from playsound import playsound
            import sys
            speak('okay sir i am executing the slideshow and shutting down myself')
            py.hotkey('alt', 'tab')
            t.sleep(1)
            py.press('f5')
            shutdown_snd = "C:\\Users\\pcper\\OneDrive\\Pictures\\img\\wake-up-the-robot-84894.mp3"
            playsound(shutdown_snd)
            speak('happy anniversary to both of you guys')
            sys.exit()


        elif 'check my bmi' in query:
            speak('okay sir fill in the information as asked .')
            bmi_checker()
        elif 'check my health' in query:
            speak('okay sir fill in the information as asked .')
            bmi_checker()



        elif 'search a video for' in query:
            import pywhatkit
            new_string = query.replace("search a video for" and "jarvis", "")
            pywhatkit.playonyt(new_string)
            speak(f"searching a video for{new_string}"  )  

        elif 'activate search mode' in query:
            speak("search mode activated please tell me what do you want to know")
            search_mode()

        elif 'fake study mode' in query:
            import webbrowser
            import pyautogui
            import time
            speak("okay sir !")
            webbrowser.open('https://www.youtube.com/watch?v=T9DgvXpCnwo&t=533s')
            time.sleep(1)
            pyautogui.press('f11')
            clap()

        elif 'check my instagram status' in query:
            import subprocess

            proc = subprocess.Popen(["python", "insta_page_checker.py"])
            speak('okay sir')
            
            snap_to_close_checker_of_instagram_status()

        elif 'open instagram' in query:
            import webbrowser
            speak('opening instagram')
            webbrowser.open('instagram.com')

        elif 'what is the probability i would get a girlfriend' in query:
            speak('according to me , i guess you should improve your skills in other things than only in coding .')
        elif 'can you guess who is my girlfriend' in query:
            import random 
            speak('tell me some names for that , sir , please include comma between the names you are telling me . ')
            names = takecommand().lower()
            # Split the input into a list of names
            names_list = [name.strip() for name in names.split("comma")]

            # Randomly select a name from the list
            random_name = random.choice(names_list)

            print(f"ah , i knew your girlfriend is {random_name}, am i right ?")
                        
#------------------------------------------------------------------------------------------------




face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
prev_time = 0
num_faces = 0
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    curr_time = time.time()
    time_diff = curr_time - prev_time
    if time_diff > 4:
        if len(faces) == 0:
            print('no face recognized')
        if len(faces) == 1:
            print("face recognised !!!!") 
            speak('face recognized !')
            break             
        if len(faces) == 2:
            print('both faces recognized !!!!')
            speak('both faces recognized !')
            break
        if len(faces) > 2:
            print('all faces recognized !!!!')
            speak('all faces recognized !')
            break 
        prev_time = curr_time
        num_faces = len(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow('<<<<<<<<<<<<<<<<<<<<< FACE RECOGNITION >>>>>>>>>>>>>>>>>>>>>>>>>', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    api_key = "ed49a32044386c40607445624addd441" 
    city = "Faridabad, IN"
    update_frame()
    root.mainloop()
    cap.release()
    cv2.destroyAllWindows()
    introduction_and_system()

#ashmit_airtel = 54zlbgyk
#minky = Minky#1689
#ashmit singh rajput is great
