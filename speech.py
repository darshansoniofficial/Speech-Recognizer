import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Sambhdavo ;) ")
    audio_data = r.record(source, duration=5)
    print("Tame Bolya...")
    text = r.recognize_google(audio_data)
    print(text)
