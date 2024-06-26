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
        print("LISTENING....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("___________\n|         |\n|  *   *  |\n|         |\n|         |\n-----------")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")


    except Exception as e:
        print("say that again please")
        return "none"
    return query 

while True:   
 q = takecommand().lower()
 if 'open youtube' in q:
     speak('opening youtube.')
     webbrowser.open('youtube.com')
     
 if 'search for' in q:
     inp_search = q.replace('search for' , '')
     speak(f'searching for {inp_search.strip()}')
     pywhatkit.search(inp_search.strip())
     time.sleep(1)
     speak("here's your result.")

 if 'open trending page' in q:
     speak("opening trending page on youtube.")
     webbrowser.open("https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")

 if 'play sad song' in q:
     speak('okay sir , playing a random sad song on youtube')
     sad = ['neele neele ambar', 'kya hua tere vada tera irada song ', 'pal pal dil ke pass song ', 'likhe jo khat tujhe song ', 'ye shaam mastani song ', 'luka chuppi song ']
     rand_sad = random.choice(sad)
     pywhatkit.playonyt(rand_sad)
     ans = rand_sad.replace('song', '')
     speak(f'playing {ans} on youtube ')
    
 if 'my ip address' in q:
     ip = get('https://api.ipify.org').text
     speak("your ip address is {ip}")

 if 'from wikipedia' in q:
     speak('searching wikipedia')
     rpl = q.replace('from wikipedia', '')
     results = wikipedia.summary(rpl , sentences=2)
     speak("according to wikipedia")
     speak(results)
     print(results)

 if 'where i am' in q:
     speak("wait sir , i am connecting the lock symbol nearest you ")
     os.system('python where_i_am.py')
