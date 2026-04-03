# 🤖 JARVIS AI Chat Bot

A voice-activated AI assistant built with Python, inspired by Iron Man's JARVIS. It listens to your voice, understands natural language commands, and responds with synthesized speech — powered by OpenAI's GPT-4o-mini.

---

## ✨ Features

- 🎙️ *Voice Recognition* — Listens via microphone using Google Speech Recognition
- 🔊 *Text-to-Speech* — Responds out loud using pyttsx3
- 🌐 *Web Automation* — Opens YouTube, Google, and runs custom Google searches
- 💻 *App Launching* — Opens VS Code directly from voice
- 🕐 *Date & Time* — Tells the current time and date on request
- 🔋 *Battery Status* — Reports your device's battery percentage
- 📖 *Wikipedia Search* — Fetches quick summaries for "who is" / "what is" queries
- 🧠 *Memory* — Remembers your name across sessions using a local memory.json file
- 🤖 *AI Fallback* — For anything else, falls back to GPT-4o-mini for a smart response

---

## 📁 Project Structure


mega project1/
├── main.py         # Main application entry point
└── memory.json     # Persistent memory store (auto-created)


---

## 🛠️ Requirements

- Python 3.8+
- An OpenAI API key

### Dependencies

Install all required packages via pip:

bash
pip install SpeechRecognition pyttsx3 wikipedia psutil openai pyaudio


> *Note:* pyaudio may require additional system-level installation:
> - *Windows:* pip install pipwin && pipwin install pyaudio
> - *macOS:* brew install portaudio && pip install pyaudio
> - *Linux:* sudo apt-get install portaudio19-dev && pip install pyaudio

---

## ⚙️ Setup

1. *Clone the repository*
   bash
   git clone https://github.com/jaiyeshw/JARVIS-AI-CHAT-BOT.git
   cd "JARVIS-AI-CHAT-BOT/mega project1"
   

2. *Set your OpenAI API key*

   Set it as an environment variable:
   bash
   # macOS/Linux
   export OPENAI_API_KEY="your-api-key-here"

   # Windows (Command Prompt)
   set OPENAI_API_KEY=your-api-key-here
   

3. *Create the memory file*

   Create an empty memory.json in the project folder:
   bash
   echo "{}" > memory.json
   

4. *Run the assistant*
   bash
   python main.py
   

---

## 🗣️ Example Voice Commands

| What you say | What JARVIS does |
|---|---|
| "Open YouTube" | Opens youtube.com in your browser |
| "Open Google" | Opens google.com in your browser |
| "Open VSCode" | Launches Visual Studio Code |
| "What time is it?" | Speaks the current time |
| "What's today's date?" | Speaks today's date |
| "Battery status" | Reports battery percentage |
| "Who is Elon Musk?" | Fetches a Wikipedia summary |
| "Search Python tutorials" | Googles "Python tutorials" |
| "My name is Alex" | Remembers your name |
| "What is my name?" | Recalls your saved name |
| "Exit" / "Stop" | Shuts down JARVIS |
| Anything else | Asks GPT-4o-mini and speaks the answer |

---

## 🧠 How It Works

1. JARVIS starts and enters a continuous listening loop
2. Your voice is captured via microphone and transcribed by Google Speech Recognition
3. The transcript is matched against known commands (websites, time, battery, etc.)
4. If no command matches, the query is sent to OpenAI's GPT-4o-mini
5. The response is spoken back using the text-to-speech engine

---

## 📝 Notes

- An active internet connection is required for speech recognition and AI responses
- Wikipedia lookups may occasionally fail for ambiguous topics
- Memory is stored locally in memory.json — do not delete this file if you want JARVIS to remember your name
