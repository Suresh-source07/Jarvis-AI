# 🤖 Jarvis AI - Your Personal Voice Assistant

Jarvis is an AI-powered voice assistant inspired by Iron Man's iconic Jarvis. It can automate tasks, respond to your voice commands, and assist you with daily activities — all using Python.

---

## 🚀 Features

- 🎤 Voice command recognition
- 🌦️ Weather updates
- 😂 Jokes and fun responses
- 🌐 Google and YouTube automation
- 🎵 Music player
- 🖥️ Opens applications
- 🔊 Custom voice responses
- 🙋 Greets you by name (editable in code)
- 📁 And many more smart features!

---

## ⚙️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Suresh-source07/Jarvis-AI.git
   cd Jarvis-AI
2. Install the required Python libraries
   pip install -r requirements.txt
   Run Jarvis

3. python jarvis.py
   Jarvis will start listening — just speak your command!

🛠 Requirements
Python 3.x

Internet connection (for online features like weather, search, etc.)

All required libraries are listed in requirements.txt.

🧠 Customization
You can customize Jarvis’s voice, name, and greeting inside the source code.

Feel free to add your own commands and features to personalize your AI assistant!

👨‍💻 Author
Suresh Suri
GitHub - Suresh-source07

⭐ Show Your Support
If you like this project, give it a ⭐ on GitHub and feel free to fork it or contribute!




# Jarvis AI Voice Commands

This document contains all the voice commands available for the Jarvis AI Assistant.

## Basic Interaction Commands

- **"hello"** - Greets you and introduces Jarvis
- **"who made you"** - Tells you about the creator
- **"kya hal hai"** - Hindi greeting (responds in Hindi)
- **"loving"** - Acknowledgment command
- **"bye"** - Exits the program
- **"wake up"** - Activates Jarvis for help

## Search Commands

- **"youtube search [query]"** - Searches YouTube for the specified query
- **"google search [query]"** - Performs a Google search
- **"wikipedia [query]"** - Searches Wikipedia and reads summary
- **"what is [query]"** - General search with spoken results

## Website Navigation

- **"website [name]"** - Opens a website (e.g., "website facebook")
- **"launch"** - Prompts for website name to open
- **"open instagram"** - Opens Instagram
- **"open youtube"** - Opens YouTube
- **"open whatsapp"** - Opens WhatsApp Web

## Application Control

### Opening Applications
- **"open Chrome"** - Opens Google Chrome
- **"open wo mic client"** - Opens WOMic Client

### Closing Applications
- **"close Chrome"** - Closes Google Chrome
- **"close youtube"** - Closes Chrome (YouTube)
- **"close wo mic client"** - Closes WOMic Client

## Music Commands

- **"music"** - Prompts for song name and plays it
  - If you say "bhull", it plays a local file (Kesariya.mp3)
  - Otherwise, it searches and plays on YouTube

## WhatsApp Messaging

- **"message"** - Initiates WhatsApp message sending
  - For "aadarsh": Sends to +917826888171
  - For "Mummma": Sends to +919971448627
  - For others: Prompts for phone number

## YouTube Control Commands

- **"pause"** - Pauses video
- **"play"** - Plays/resumes video
- **"restart"** - Restarts video
- **"back"** - Rewinds 10 seconds
- **"forward"** - Fast forwards 10 seconds
- **"full screen"** - Toggles full screen
- **"film mode"** - Toggles theater mode
- **"mute"** - Toggles mute
- **"skip"** - Skip ads
- **"fast"** - Increases playback speed
- **"slow"** - Decreases playback speed
- **"search"** - Opens search box
- **"on captions"** - Turns on captions
- **"close captions"** - Turns off captions
- **"next"** - Next video
- **"previous video"** - Previous video
- **"mini player"** - Toggles mini player
- **"activate youtube tools"** - Voice control for YouTube

## Chrome Browser Commands

- **"open a new window"** - Opens new Chrome window
- **"open a new window in incognito"** - Opens incognito window
- **"open a new tab"** - Opens new tab
- **"open a file in browser"** - Opens file dialog
- **"close the current tab"** - Closes current tab
- **"close the current window"** - Closes current window
- **"Reopen the last tab i closed"** - Reopens last closed tab
- **"Reopen the last window i closed"** - Reopens last closed window
- **"go to tab [1-8]"** - Switches to specific tab number
- **"Go to the next tab"** - Switches to next tab
- **"Go to the previous tab"** - Switches to previous tab
- **"Go to previous page in my browsing history"** - Goes back in history
- **"Go to the next page in my browsing history"** - Goes forward in history
- **"maximize window"** - Maximizes window
- **"minimize window"** - Minimizes window
- **"go to bottom of the page"** - Scrolls to bottom
- **"go to top of the page"** - Scrolls to top
- **"go to history"** - Opens browsing history
- **"go to downloads"** - Opens downloads page
- **"activate chrome tools"** - Voice control for Chrome

## Utility Commands

- **"take screenshot"** - Takes and saves a screenshot
- **"tell me a joke"** - Tells a random joke
- **"repeat my words"** - Repeats what you say next
- **"alarm"** - Sets an alarm (prompts for time input)

## Translation and Language

- **"open translator"** - Activates Hindi to English translation
- **"temperature"** - Gets current temperature in Delhi

## Memory Commands

- **"remember that [message]"** - Saves a message to remember
- **"what do you remember"** - Recalls saved message

## E-book Reader

- **"audiobook"** - Starts PDF reader
  - Currently supports "python" book
  - Reads specified page number
  - Can translate to Hindi if requested

## Notes

- Commands are case-insensitive
- Some commands may require additional input after initial voice command
- WhatsApp messaging requires specific timing input (hours and minutes)
- Screenshot files are saved to the desktop screenshots folder
- The assistant responds in both English and Hindi for certain commands

## Prerequisites

Make sure you have all required Python packages installed:
- pyttsx3 (text-to-speech)
- speech_recognition (speech recognition)
- pywhatkit (WhatsApp and YouTube automation)
- wikipedia (Wikipedia search)
- googletrans (translation)
- gtts (Google text-to-speech)
- pyautogui (screenshot)
- keyboard (keyboard automation)
- pyjokes (jokes)
- PyPDF2 (PDF reading)
- requests & BeautifulSoup (web scraping)
- playsound (audio playback)
