from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from src.gcalendar import get_events, authenticate_calendar
import subprocess
from src.spotify import play_playlist, pause, skip_next, skip_previous, resume, currently_playing, volume, devices

def speak(text):
    tts = gTTS(text=text, lang="pt")
    playsound.playsound('voice.mp3')

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print('fala caralho')
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language='pt-BR')
            print(said)
        except Exception as e:
            #print("Exception" + str(e))
            pass

    return said.lower()

def abrir_spotify():
    os.startfile(r'C:\Users\Vinicius\AppData\Roaming\Spotify\Spotify.exe')

wake = "fala gay"

while True:
    print('Espionando')
    text = get_audio()

    if wake.lower() in text:
        speak('fala caraio')
        text = get_audio()

        if "abrir" in text and "spotify" in text:
            abrir_spotify()

        if "tocar" in text and "playlist" in text:
            play_playlist()

        if "volume" in text:
            print('Quantos %?')
            vp = get_audio()
            volume(vp)

        if "pular" in text and "música" in text:
            skip_next()

        if "voltar" in text and "música" in text:
            skip_previous()

        if "pausar" in text and "música" in text:
            pause()

        if "despausar" in text and "música" in text:
            resume()

        if "encerrar" in text and "programa" in text:
            break
