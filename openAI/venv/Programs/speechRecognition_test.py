import speech_recognition

sr = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    sr.adjust_for_ambient_noise(source)
    sr.pause_threshold = 0.5
    audio_data = sr.listen(source)
    text = sr.recognize_google(audio_data, language="en")
    print(text)
