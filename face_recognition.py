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
# Create a VideoCapture object
cap2 = cv2.VideoCapture('C:\\Users\\pcper\\OneDrive\\Pictures\\img\\ironmangifff.gif')

# Define the main window
root = tk.Tk()

# Create a label to display the video
label = tk.Label(root)
label.pack()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

def homepage():
    subprocess.run('python', 'main_jarvis.py')

if __name__ == '__main__':
    update_frame()
    root.mainloop()
    cap.release()
    cv2.destroyAllWindows()
    os.system('python introduction.py')    
    
