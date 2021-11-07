import openai
import pyttsx3 as pyVoice
import speech_recognition
import playsound
import tkinter
import time

sr = speech_recognition.Recognizer()

openai.organization = "org"
openai.api_key = "OPENAI_API_KEY"

promptElements = [
            "The following is a conversation with an AI assistant. He provides factual information. The assistant is helpful, creative, clever, polite, and very friendly.\n",
            "\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?", "",
            "\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?"]
prevRes = ""

tk = tkinter.Tk()
tk.title("Voice Assistant")
text = tkinter.Text(tk)
text.tag_configure("bold", font="Helvetica 10 bold")
text.pack()


def callback(recognizer, audio):
    global promptElements
    global prevRes

    try:
        speech = recognizer.recognize_google(audio)
    except Exception:
        return

    if "Leo" in speech or "leo" in speech:
        playsound.playsound('voiceAssistantStartSound.wav')

        with speech_recognition.Microphone() as source:
            sr.adjust_for_ambient_noise(source)
            sr.pause_threshold = 0.5
            audio_data = sr.listen(source)
            try:
                newMsg = sr.recognize_google(audio_data)
            except Exception:
                playsound.playsound('voiceAssistantError.wav')
                return
            text.insert("end", newMsg + "\n")

            engine = pyVoice.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.setProperty('rate', 200)
            engine.say(newMsg)
            engine.runAndWait()

        if newMsg == 'quit':
            return

        promptElements[2] = promptElements[3] + prevRes
        promptElements[3] = "\nHuman:" + newMsg + "\nAI:"
        response = openai.Completion.create(
            engine="davinci",
            prompt="".join(promptElements),
            temperature=0.9,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["\n", " Human:", " AI:"]
        )
        prevRes = response.choices[0].text
        text.insert("end", prevRes + "\n", "bold")

        engine = pyVoice.init()
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 140)
        engine.say(prevRes)
        engine.runAndWait()


with speech_recognition.AudioFile('record.wav') as source:
    sr.adjust_for_ambient_noise(source)
    audio_data = sr.record(source)
    newMsg = sr.recognize_google(audio_data)
    playsound.playsound('voiceAssistantBootup.wav')


sr.listen_in_background(speech_recognition.Microphone(), callback)
tk.mainloop()

while True:
    time.sleep(0.1)
