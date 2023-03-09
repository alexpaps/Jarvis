from JarvisGoogleSearch import Jarvisdoc,JarvisWebSearch,JarvisInfSearch
from JarvisSongList import GreekSongs,EnglishSongs,Christooulos
from JarvisEngineCommunication import AudioToText,EngineRate,EngineTalk
import time 

def JarvisTime():

    try:
        Clock = list(time.localtime())

        Good ="Good"

        if 6 <= Clock[3] < 12:
            Good += "Morning"
        elif 12 <= Clock[3] < 16:
            Good = "Hello"
        elif 16 <= Clock[3] < 20:
            Good += "Afternoon"
        elif 20 <= Clock[3] < 24 or 0 <= Clock[3] < 6:
            Good += "Evening"
    except:
         Good = "Hello"
         
    return Good

Answer = ''
#Hello Message
Good = JarvisTime()
EngineTalk(Good + "sir")

while (True):
#Jaris ask if i want any help
    EngineTalk("How can I help you?")
    text = AudioToText()
    EngineRate()
    print(text)

#Gia na peksei to Visino.mp3   
    if text == "army song":
        Christooulos()
#Gia na peksei ta ellinika tragoudia
    elif text.find("play Greek songs") != -1:
        GreekSongs()      
#Gia na peksei ta agglika tragoudia
    elif text.find("play English songs") != -1:
        EnglishSongs()
#Gia Google Search
    elif text.find("google search") != -1:
        try:
                text = text.strip("google search") +' '+'Wikipedia'
                url = JarvisWebSearch(text)#Finds the websites for the current information
                JarvisInfSearch(url,text)#Saves the information in a docx file
                Answer = Jarvisdoc(text)#The Answer
                EngineTalk(Answer)
        except :
                EngineTalk("Sorry, I could not process your request.")
#Den katanoise ti eipa
    elif text == "Sorry, I could not understand what you said.":
        EngineTalk(text)
#Jarvis can not answer that question YET
    else:
         EngineTalk("Sorry sir I can not answer this question yet")   

#Jarvis ask if the user needs something else
    EngineTalk("Do you want anything else sir?")
    
    text = AudioToText()
#Exit from the program loop and a goodbye message 
    if text.find("yes") == -1:
        Clock = list(time.localtime())
        if 20 <= Clock[3] < 6:
            EngineTalk("Good night sir")
        else:
            EngineTalk("Bye sir")
        break

