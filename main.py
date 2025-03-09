import pyttsx3 as p
import speech_recognition as sr


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()




r = sr.Recognizer()

speak("Hello Madam, I am your voice assistant! How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio, language="en-US")  # Change to your preferred language
    print(text)

if "what" and "about" and "you" in text:
    speak("I am having a good day Miss")

speak("what can I do for you")