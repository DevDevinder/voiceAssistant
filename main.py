import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import googlesearch
# installs
# pip install SpeechRecognition
# pip install PyAudio
# pip install pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)#what the voice sounds like
listening = True

#says what is written
def talk(text):
    engine.say(text)
    engine.runAndWait()

#recieving commands
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening to you...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
#condition checks if command starts with certain word or name ,
# removes that name from output  and will return the command to  output
            print(command)
            if command.startswith('rose'):
                command = command.replace('rose', '')
                print(command)

                return command

    except:
        pass
    else:
        return take_command()

#commands
def run_alexa():
    try:
        command = take_command()
        print(command)
#brings up youtube video
        if 'play' in command:
            song = command.replace('play', '')#removes play phrase from output
            talk('sweet shing gan.. ama put' + song + 'on the now')
            engine.say('on the now')
            pywhatkit.playonyt(song)
#gives time
        elif 'time' in command:
            time = datetime.datetime.now().strftime(' %I : %M %p')
            talk('its about' + time)
#shares wiki output
        elif 'wiki' in command:
            person = command.replace('wiki', '')
            info = wikipedia.summary(person, 1)# how many lines from the wiki page
            print(info)
            talk(info)

        elif 'date' in command:
            talk('no im married to the game')
#gives a joke
        elif 'joke' in command:
            talk(pyjokes.get_joke())
#gives a google search
        elif 'search' in command:
            pywhatkit.search(command)
            talk('here is what I found')
        elif 'cheng' in command:
            talk('she is a sneaky cheeky girl from the mainland.')
        elif 'which bank' in command:
            talk('any bank is fine dont worry')

        else:
            talk('Please improve your english and say it again. wo de my yaah!')
    except Exception as e:
        print(e)
        pass


while listening is True:
    run_alexa()
    print('here')
