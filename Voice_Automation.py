import pyttsx3          #
import datetime
import speech_recognition as sr


'''
sapi5 is to use windows inbuilt voice.
Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft
'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)        # Two type of voices we are using first voice(male).


def speak(audio):
    engine.say(audio)
    engine.runAndWait()                         # It will wait till the sentence get finish.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour >= 0 and hour < 12 :
        speak("Good Morning!")
        
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your personal assistant! How may I help you.")
        
def takeCommand():

    ''' It takes microphone input from user and returns string output. '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:

        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n ")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

        

    
if __name__ == '__main__':
    
    wishMe()
    takeCommand()
    while True:
        query = takeCommand().lower()
        ## Logic for executing task  
        if "wikipedia" in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)
        
