import openai
import pyttsx3 as pyVoice

engine = pyVoice.init()
engine.setProperty('rate', 125)

openai.organization = "org-P6nav9Naj9J0AHIg3Bv9aU9t"
openai.api_key = "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"
promptElements = ["The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, polite, and very friendly.\n", "\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?", "", "\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?"]
prevRes = ""

while True:
    newMsg = input()
    if newMsg.lower() == "quit":
        break
    promptElements[2] = promptElements[3] + prevRes
    promptElements[3] = "\nHuman:" + newMsg + "\nAI:"
    response = openai.Completion.create(
        engine="davinci",
        prompt="".join(promptElements),
        temperature=0.9,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    prevRes = response.choices[0].text
    print(prevRes)
    engine.say(prevRes)
    engine.runAndWait()
