import random
import pyttsx3
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def printMessage(text):
    print(f"Bot : {text}")

welcomeMsg = ["Hello I am here for you" , "Hello how i assist you today" , "Hello how are you"]

botMessage = random.choice(welcomeMsg)

def getCommand():
    while True:
        userMessage = input("User : ") 
        userMessage = userMessage.lower()

        if "hello" in userMessage:
            botMessage = random.choice(welcomeMsg)
            printMessage(botMessage)
            speak(botMessage)
        elif 'bye' in userMessage or 'exit' in userMessage or 'close' in userMessage :
            botMessage = "Ok Have a good Day"
            printMessage(botMessage)
            speak(botMessage)
            break
        elif 'open google' in userMessage :
            botMessage = "Ok opening Google.."
            printMessage(botMessage)
            speak(botMessage)
            os.startfile("www.google.com")
        elif 'open notepad' in userMessage:
            botMessage = "  Ok opening Notepad.."
            printMessage(botMessage)
            speak(botMessage)
            os.startfile("notepad")
         

if __name__ == '__main__':
    printMessage(botMessage)
    speak(botMessage)
    getCommand()
