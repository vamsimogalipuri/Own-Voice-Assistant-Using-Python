import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import python_weather

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk("Hello there i'm your Alexa")
talk("say what can i do for you.....")


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening........')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
                talk(command)
            else:
                talk("Sorry i didn't get you what you said")
                talk("perhaps you are not talking to me")
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "current time" in command:
        time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print(time)
        talk("the current time is " + time)
    elif "who" or "how" or "when" or "what" or "where" in command:
        google_it = command
        info = wikipedia.summary(google_it, 3)
        print(info)
        talk(info)
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    # elif "weather" in command:


while True:
    run_alexa()
