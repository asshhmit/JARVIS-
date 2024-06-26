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

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#engine.setProperty('voice' , voices[0].id)
engine.setProperty('rate', 150)
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
def homepage():
    subprocess.run('python', 'main_jarvis.py')







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
                    frames_per_buffer=1024)

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
            break

    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the PyAudio object
    p.terminate()



if __name__ == '__main__':
    clap()
    os.system('python taskexec.py')