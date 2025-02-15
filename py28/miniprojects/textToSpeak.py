import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
engine.setProperty('rate' , 150)

while True:
    data = input("Enter your text:")
    if data == "exit":
        engine.say("Ok Bye")
        engine.runAndWait()
        break
    engine.say(data)
    engine.runAndWait() 