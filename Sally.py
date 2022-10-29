# Description: this is a virtual assistant program that responds back with hey
# and the files as well as emails for the lecturer

# import the libraries
import smtplib
import speech_recognition as sr
import pyttsx3
import os
import gtts
import datetime
import warnings
import calendar
import random
from email.message import EmailMessage
import webbrowser


# ignore any warning messages

from gtts import gTTS, tokenizer
from pyttsx3 import speak, engine

warnings.filterwarnings('ignore')

engine = pyttsx3.init()
# Record audio and return it as a string
def recordAudio():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-KE')
        print(query)
    except Exception as e:
        print(e)
        speak("Kindly repeat i couldn't hear you...")
        return "None"
    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("hello this is Sally a Virtual Assistant")

    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("Hi im Sally a virtual Assistant for University. how can i help you?")

# A function to get the virtual assistant response
def assistantResponse(text):
    print(text)

    # convert the text to speech
    myobj = gTTS(text=text, lang='en', slow=False)

    # save the converted audio to a file
    # myobj.save('sally_response.mp3')

    # play the converted file
    # os.system('start sally_response.mp3')


text = 'Hi there my name is Sally a University administrator, how can i help?'
assistantResponse(text)
#speak(text)


# a Function for wake word(s) or a phrase
def WakeWord(text):
    WAKE_WORDS = ['hi Sally', 'hello Sally', 'hey']

    text = text.lower()  # converting the text to all lowercase words

    # check to see if the user command/text contains a wake word/phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
        # executed if wake word isn't found n the text from the loop so it returns false
    return False


# A function to get the current date
def getDate():

    # now = datetime.datetime.now()
    # my_date = datetime.datetime.today()
    # weekday = calendar.day_name[my_date.weekday()]
    # monthNum = now.month
    # dayNum = now.day

    # return 'Today is Friday december the 13th'
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    print(date, month, year)
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)
    return date, month, year

# a function to return a random greeting response
def greeting(text):
    # greeting inputs
    GREETING_INPUTS = ['Hi Sally', 'hey Sally', 'Hey']
    GREETING_RESPONSES = ["Hi there my name is Sally a University administrator, how can i help?",
                          "Hi there my name is Sally a University administrator, what can i do for you?",
                          "Hello there my name is Sally a University administrator, what can i do for you?"]

    # if the user input is a greeting, the return a randomly choosen greeting response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    # If no greeting was detected then return an empty string
    return ''


# a function to get a persons fist and last name from text
def getPerson(text):
    wordList = text.split()  # splitting the text into a list of words

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]


def getInformation():
    f = open('StudentInformation.txt', 'r')
    if f.mode == 'r':
        contents = f.read()
        print(contents)

def getTimetable():
    f = open('Timetable.txt', 'r')
    if f.mode == 'r':
        contents = f.read()
        print(contents)


def eLearning():
    speak("Here is ")
    from Scripts import wb
    wb.open('https://elearning.strathmore.edu/')


if __name__ == "__main__":
    getvoices(2)
    step = 0


    while True:
        query = recordAudio()
        print(query)
        # WakeWord(query)

        # getTimetable()

        if len(query) > 0:
            if 'Date' in query:
                getDate()

            elif 'search' in query:
                speak('check E-learning')
                getInformation()
                

            elif 'records' in query:
                speak ('let me open the file')
                assistantResponse('Let me open the file')
                getInformation()

            elif 'timetable' in query:
                speak('let me open the file')
                assistantResponse('file opening')
                getTimetable()






