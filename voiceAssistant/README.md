This is a voice assistant powered by the OpenAI GPT-3 models.
- Once connected to the Google speech recognition engine, it will play a sound.
- The signal word is 'Leo'
- If it doesn't recognize your input, an error sound will play

***
-- This will not work if you do not have OpenAI access --

Sign up for the waitlist here: [OpenAI GPT-3](https://openai.com/api/)

***
Setting this up requires multiple Python libraries/APIs.
Here are the command line installation steps using pip:

openai:
```pip install openai```

pyttsx3 (text to speech):
```pip install pyttsx3```
 - this one is a bit tricky as it may ask you to download some C++ tools, but a link to the download is given.
 
speech_recognition:
```pip install SpeechRecognition```

playsound:
```pip install playsound```

tkinter:
```pip install tk```
