# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:57:34 2020

@author: Admin001
"""


import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("You may speak now-->\n")
    
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print('Voice Input is: ',text)
    except:
        text = ''
        print("Sorry,could not hear you properly.Try again.")

if text != '':
        
    # Import the required module for text to speech conversion 
    import pyttsx3 
      
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
      
    # say method on the engine that passing input text to be spoken 
    engine.say(text) 
      
    # run and wait method, it processes the voice commands.  
    engine.runAndWait() 
