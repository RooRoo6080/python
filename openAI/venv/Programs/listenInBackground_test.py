import speech_recognition
import time

sr = speech_recognition.Recognizer()


def callback(recognizer, audio):
    print(recognizer.recognize_google(audio))


sr.listen_in_background(speech_recognition.Microphone(), callback)

while True:
    time.sleep(0.1)
