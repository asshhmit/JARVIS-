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


