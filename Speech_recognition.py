import speech_recognition as sk
from  AppOpener import *
import pyttsx3,subprocess,os
from  chatterbot import ChatBot
from pywhatkit import *
t=0
while(True):
  try:
    assistent=pyttsx3.init()
    voice=assistent.getProperty('voices')
    assistent.setProperty('voice',voice[1].id)
    if t==0:
     pyttsx3.speak("HII\n I'm Nithish assistent\n")
     pyttsx3.speak("How can i help you")
    '''else:
     pyttsx3.speak("Trying to say")'''
    t=1
    def play(command):
        playonyt(command)
    def talk(command):
        b=info(command,lines=1,return_value=True)
        pyttsx3.speak(b)
    listener=sk.Recognizer()
    with sk.Microphone() as source:
        print("listening..")
        #command="will you shut down my pc"
        voice=listener.listen(source)
        command =listener.recognize_google(voice)
        print(command)
        if "play" in command:
                command=command.replace("play","")
                play(command)
        elif "open" in command:
                command=command.replace("open","")
                app_find=open(command, match_closest=True)
                print(app_find)
                if  app_find==False:
                 search(command)
               
                #open(command)
        elif "search" in command:
             command=command.replace("search","")
             search(command)
        elif "shutdown" in command:
               pyttsx3.speak("System will shutdown your system in a few seconds")
               os.system("shutdown /s /t 2")
        elif "close all" in command:
                cmd='powershell "gps | where {$_.MainWindowTitle} | select Description'
                apps=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
                f=0
                for line in apps.stdout:
                        if line.rstrip() and f>2:
                                temp=line.decode().rstrip().lower()
                                print("apps running--",temp)
                                close(temp,match_closest=True)
                        f+=1
        elif "sleep" in command:
                os.system("shutdown/h")#using command prompt sleeping the sysetem 
        elif "restart" in command:
                os.system("shutdown/r/t 2")#using command prompt restarting the system
                        
        else:
                talk(command)
        pyttsx3.speak("\nFree to ask your question")
  except Exception as e:
      pyttsx3.speak(e)
      pyttsx3.speak("will you try to say again")