import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import time
import datetime
import wikipedia
import psutil
import json
from openai import OpenAI 

client = OpenAI()


recognizer = sr.Recognizer()


def speak(text):
  engine = pyttsx3.init() 
  engine.say(text)
  engine.runAndWait()
  time.sleep(0.5)

if __name__ == "__main__":
    speak("Jarvis is in standby mode.")  


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    
    except sr.UnknownValueError:
        print("Speech not understood.")
        return "ERROR"

    except sr.RequestError:
        print("API error.")
        return "ERROR"
    
def save_memory(key, value):
    with open("memory.json", "r") as file:
        data = json.load(file)

    data[key] = value

    with open("memory.json", "w") as file:
        json.dump(data, file)


def load_memory(key):
    with open("memory.json", "r") as file:
        data = json.load(file)

    return data.get(key, None)  

def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Jarvis, a smart AI assistant."},
                {"role": "user", "content": question}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("AI Error:", e)
        return "Sorry, I could not process that."  
    

def execute_command(command):
    
#  ----- OPENING WEBSITES------

    if "open youtube" in command:
        speak("Opening YouTube.......")
        webbrowser.open("https://youtube.com")
        return True

    elif "open google" in command:
        speak("Opening Google......")



        webbrowser.open("https://google.com")
        return True

    elif "open vscode" in command:
        speak("Opening Visual Studio Code.....")



        os.system("code")
        return True
    
    # ----- TIME--------
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
        return True

    # ------DATE---------
    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak("Today's date is " + today)
        return True 
    
    # ---- BATTERY ----
    elif "battery" in command:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        speak(f"Your battery is at {percentage} percent.")
        return True
    
      # ---- WIKIPEDIA SEARCH ----
    elif "who is" in command or "what is" in command:
        try:
            topic = command.replace("who is", "").replace("what is", "")
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)
        except:
            speak("I couldn't find information on that.")
        return True
    
     # ---- GOOGLE SEARCH QUERY ----
    elif "search" in command:
        query = command.replace("search", "")
        speak("Searching Google for " + query)
        webbrowser.open("https://www.google.com/search?q=" + query)
        return True
    
    # ---- EXIT ----
    elif "exit" in command or "stop" in command:
        speak("Shutting down. Goodbye.....")
        return False
    
    
    elif "my name is" in command:
      name = command.replace("my name is", "").strip()
      save_memory("name", name)
      speak(f"I will remember that your name is {name}")
      return True
    
    elif "my name" in command:
      name = load_memory("name")
      if name:
        speak(f"Your name is {name}")
      else:
        speak("I don't know your name yet.")
      return True
    

    
    # ---- NORMAL SENTENCES ----
    else:
      response = ask_ai(command)
      speak(response)
      return True


running = True        

            
while running:
        command = listen()

        if command == "ERROR":
            speak("I didn't understand that.")
            continue

        if  command:
           running = execute_command(command)    

      
          
  
