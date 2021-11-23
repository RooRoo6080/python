import pyttsx3 as pyVoice

engine = pyVoice.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)

engine.say("Hi, how are you doing? I am OpenAI.")
engine.runAndWait()
