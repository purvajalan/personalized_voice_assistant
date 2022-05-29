import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
command = "."


def talk(text):
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    talk('Hi. I am Hazel, your personal voice assistant. What can I do for you?')

def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source,None,10)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'hazel' in command:
            command = command.replace('hazel', '')
            print(command)
    return command


def run_hazel():
    command = take_command()
    print(command)
    if 'what can you do' in command:
        talk('I can tell you jokes, the current time, perform searches and play songs for you')
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        thing = command.replace('what is', '')
        info_thing = wikipedia.summary(thing, 1)
        print(info_thing)
        talk(info_thing)
    elif 'where is' in command:
        place = command.replace('where is', '')
        info_place = wikipedia.summary(place, 1)
        print(info_place)
        talk(info_place)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    try:
        run_hazel()
    except UnboundLocalError:
        print("No command detected! Hazel has stopped working ")
        command = "."
