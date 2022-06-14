#Storing the audio in desired format and transcribing it in chunks of 6000 milliseconds
import scipy.io.wavfile
import pandas
import nltk
import numpy
from collections import Counter
import math
import numpy
import speech_recognition as sr
from pydub import AudioSegment
from operator import itemgetter
from translate import Translator
from transformers import pipeline

def transcription(roomname):
    r = sr.Recognizer()
    transcript = ""
    unit = 6000
    room=str(roomname)
    sound = AudioSegment.from_mp3(room+".mp3") 
    last_chunk_length = len(sound) % 6000
    for i in range(0 , len(sound) // unit):
        sound = AudioSegment.from_mp3(room+".mp3") 
        if (i == 0):  
            sound = sound[:unit]
            sound.export(room+".wav", format = "wav")
            audio = sr.AudioFile(room+".wav")
            with audio as source:
                audiodata = r.record(audio)
            query = r.recognize_google(audiodata, language = 'ur-PK')
            transcript = transcript + query
            f = open(room+".docx", "a")
            f.write(query)
            f.close()
        else:
            sound = sound[unit:(unit + 6000)]
            sound.export(room+".wav", format = "wav")
            audio = sr.AudioFile(room+".wav")
            with audio as source:
                audiodata = r.record(audio)
            query = r.recognize_google(audiodata, language = 'ur-PK')
            transcript = transcript + query
            f = open(room+".docx", "a")
            f.write(query)
            f.close()
            unit = unit + 6000
transcription(1)