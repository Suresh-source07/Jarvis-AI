import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
from googletrans import Translator
from gtts import gTTS
import pyautogui
import keyboard
import pyjokes
import PyPDF2
import datetime
import requests
from bs4 import BeautifulSoup
import pickle
from playsound import playsound

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[1].id)


def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f"You said: {audio}")
    print("   ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        command.pause_threshold = 1
        audio = command.listen(source)
        
        
    try:
        print('Recognizing......')
        query = command.recognize_google(audio,language='en-in')
        print(f'you said: {query}')
            
    except:
            return "none"

    return query.lower()


def taskExe():

    def Music():
        Speak("tell me the name of the song sir")
        musicname = takecommand()

        if 'bhull' in musicname:
            os.startfile('e:\\songs\\Kesariya.mp3')

        else:
            pywhatkit.playonyt(musicname)

        Speak("starting the song")

    def Whatsapp():
        Speak("tell me name of the person!")
        name = takecommand()


        if 'aadarsh' in query:
            Speak("tell me the message sir")
            msg = takecommand()
            Speak("tell the time in hour sir")
            hour = int(takecommand())
            Speak("tell me the time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+917826888171",msg,hour,min,20)
            Speak("Sending whatsapp message")

        
        elif 'Mummma' in query:
            Speak("tell me the message sir")
            msg = takecommand()
            Speak("tell the time in hour sir")
            hour = int(takecommand())
            Speak("tell me the time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919971448627",msg,hour,min,20)
            Speak("Sending whatsapp message")
        else:
            Speak("tell me the phone number")
            phone = takecommand()
            ph = '+91' + phone
            Speak("tell me the message sir")
            msg = takecommand()
            Speak("tell the time in hour sir")
            hour = int(takecommand())
            Speak("tell me the time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            Speak("Sending whatsapp message")

    def Openapps():
        Speak('wait a second!,sir')

        if 'wo mic client' in query:
            os.startfile("C:\Program Files (x86)\WOMic\WOMicClient.exe")

        elif 'Chrome' in query:
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

        
        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')

    def Closeapps():
        Speak('ok sir , wait a second!')
        if 'youtube' in query:
            os.system('TASKKILL /F /im chrome.exe')
        elif 'Chrome' in query:
            os.system('TASKKILL /F /im chrome.exe')
        elif 'wo mic client' in query:
            os.system('TASKKILL /F /im WOMicClient.exe')

    def Takehindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening......')
            command.pause_threshold = 1
            audio = command.listen(source)
        
        try:
            print('Recognizing......')
            query = command.recognize_google(audio,language='hi-in')
            print(f'you said: {query}')
            
        except:
            return "none"

        return query.lower()

    def Trans():
        Speak('tell me the line,sir')
        line = Takehindi()
        tl = Translator()
        result = tl.translate(line)
        Text = result.text
        Speak(Text)

    def temp():
        search = 'temperature in delhi'
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_="BNeawe").text
        Speak(f"the temperature outside is {temperature} celcius")

    def youtubeauto():
        Speak("tell me command,sir")
        comm = takecommand()
        if 'pause' in comm:
            keyboard.press('spacebar')

        elif 'play' in comm:
            keyboard.press('spacebar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'forward' in comm:
            keyboard.press('l')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('z')

        elif 'fast' in comm:
            keyboard.press('>')

        elif 'slow' in comm:
            keyboard.press('<')

        elif 'search' in comm:
            keyboard.press('/')

        elif 'on captions' in comm:
            keyboard.press('c')

        elif 'close captions' in comm:
            keyboard.press('c')

        elif 'next' in comm:
            keyboard.press_and_release('shift+N')

        elif 'previous video' in comm:
            keyboard.press_and_release('shift+P')

        elif 'miniplayer' in comm:
            keyboard.press('i')

    def chromeauto():
        Speak('tell me command,sir')
        com = takecommand()

        if 'open a new window' in com:
            keyboard.press_and_release('ctrl+n')

        elif 'open a new window in incognito' in com:
            keyboard.press_and_release('Shift + Ctrl + n')

        elif 'open a new tab' in com:
            keyboard.press_and_release('ctrl+t')

        elif 'open a file in browser' in com:
            keyboard.press_and_release('Ctrl + o')

        elif 'close the current tab' in com:
            keyboard.press_and_release('Ctrl + w')

        elif 'close the current window' in com:
            keyboard.press_and_release('Shift + Ctrl + w')

        elif 'Reopen the last tab i closed' in com:
            keyboard.press_and_release('Shift + Ctrl + t')

        elif 'Reopen the last window i closed' in com:
            keyboard.press_and_release('Shift + Ctrl + t')

        elif 'go to tab 1' in com:
            keyboard.press_and_release('Ctrl + 1')

        elif 'go to tab 2' in com:
            keyboard.press_and_release('Ctrl + 2')

        elif 'go to tab 3' in com:
            keyboard.press_and_release('Ctrl + 3')

        elif 'go to tab 4' in com:
            keyboard.press_and_release('Ctrl + 4')

        elif 'go to tab 5' in com:
            keyboard.press_and_release('Ctrl + 5')

        elif 'go to tab 6' in com:
            keyboard.press_and_release('Ctrl + 6')

        elif 'go to tab 7' in com:
            keyboard.press_and_release('Ctrl + 7')

        elif 'go to tab 8' in com:
            keyboard.press_and_release('Ctrl + 8')

        elif 'Go to the next tab' in com:
            keyboard.press_and_release('ctrl+tab')

        elif 'Go to the previous tab' in com:
            keyboard.press_and_release('Shift + Ctrl + Tab')

        elif 'Go to the previous tab' in com:
            keyboard.press_and_release('Shift + Ctrl + Tab')

        elif 'Go to previous page in my browsing history' in com:
            keyboard.press_and_release('Alt + Left arrow')

        elif 'Go to the next page in my browsing history' in com:
            keyboard.press_and_release('Alt + Right arrow')

        elif 'maximize window' in com:
            keyboard.press_and_release('Alt + =')

        elif 'minimize window' in com:
            keyboard.press_and_release('Alt + -')

        elif 'go to bottom of the page' in com:
            keyboard.press_and_release('Ctrl + Alt + Down arrow')

        elif 'go to top of the page' in com:
            keyboard.press_and_release('Ctrl + Alt + Up arrow ')

        elif 'go to history' in com:
            keyboard.press_and_release('ctrl + h')

        elif 'go to downloads' in com:
            keyboard.press_and_release('ctrl + j')

    def screenshot():
        Speak('ok sir, what should i name the file')
        pathname = takecommand()
        path1 = pathname + ".png"
        kk = pyautogui.screenshot()
        path = 'C:\\Users\\NEW\\Desktop\\jarvis\\screenshots' + path1
        kk.save(path)
        os.startfile('C:\\Users\\NEW\\Desktop\\jarvis\\screenshots')
        Speak('here is your screenshot,sir')
    
    def reader():
        Speak("tell me the name of the book")

        name = takecommand()

        if 'python' in name:

            os.startfile("C:\\Users\\NEW\\Desktop\\jarvis\\ebooks\\python.pdf")
            book = open("C:\\Users\\NEW\\Desktop\\jarvis\\ebooks\\python.pdf","rb")
            pdfreader = PyPDF2.PdfFileReader(book)
            page = pdfreader.getNumPages()
            Speak(f"number of pages in this book is{page}")
            Speak("from where i hv to read,sir?")
            numpage= int(takecommand())
            page = pdfreader.getPage(numpage)
            text = page.extractText()
            Speak("in which language , i hv to read?")
            lang = takecommand()

            if 'hindi' in lang:
                tl = Translator()
                tlhi = tl.translate(text,'hi')
                ttm = tlhi.text
                speech = gTTS(text = ttm)
                
            
            try:
                speech.save('book.mp3')
                playsound('book.mp3')

            except ValueError:
                playsound('book.mp3')


            else:
                Speak(text)
        


    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello sir , my name is jarvis")
            Speak("your personal AI assisstant , how may help you")
            
        
        elif 'who made you' in query:
            Speak("i was made by suresh suri ,  sir")
            

        elif 'kya hal hai' in query:
            Speak("mai thik hu, aap kaise hai")
            

        elif 'loving' in query:
            Speak("thank you , sir")
            

        elif 'bye' in query:
            Speak("ok sir , bye")
            break
        
        elif 'wake up' in query:
            Speak("hello sir , how may i help you")
            

        elif 'youtube search' in query:
            Speak("ok sir ,  this is what i found search")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            
            
        elif 'google search' in query:
            Speak("ok sir ,  this is what i found for your search")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done sir")

        elif 'website' in query:
            Speak("ok sir ,  launching......")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            web1 = query.replace("open","")
            web2 = 'https://www' + web1 + '.com'
            pywhatkit.open(web2)
            Speak("launched sir")

        elif 'launch' in query:
            Speak("tell me the name of the website!")
            name = takecommand()
            web = 'https://.' + name + '.com'
            webbrowser.open(web)
            Speak("Done sir")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("wikipedia","")
            query = query.replace("jarvis","")
            wiki = wikipedia.summary(query,2)
            Speak(f'according to wikipedia: {wiki}')

        elif 'message' in query:
            Whatsapp()

        elif 'take screenshot' in query:
            screenshot()            

        elif 'open instagram' in query:
            query = query.replace("open","")
            query = query.replace("jarvis","")
            Openapps()

        elif ' open wo mic client' in query:
            query = query.replace("open","")
            query = query.replace("jarvis","")
            Openapps()

        elif 'open Chrome' in query:
            query = query.replace("open","")
            query = query.replace("jarvis","")
            Openapps()


        elif 'open youtube' in query:
            query = query.replace("open","")
            query = query.replace("jarvis","")
            Openapps()

        elif 'open whatsapp' in query:
            query = query.replace("open","")
            query = query.replace("jarvis","")
            Openapps()

        elif 'close wo mic client' in query:
            Closeapps()

        elif 'close youtube' in query:
            Closeapps()

        elif 'close Chrome' in query:
            Closeapps()

        elif 'pause' in query:
            keyboard.press('spacebar')

        elif 'play' in query:
            keyboard.press('spacebar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'back' in query:
            keyboard.press('j')

        elif 'forward' in query:
            keyboard.press('l')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('z')

        elif 'fast' in query:
            keyboard.press('>')

        elif 'slow' in query:
            keyboard.press('<')

        elif 'search' in query:
            keyboard.press('/')

        elif 'on captions' in query:
            keyboard.press('c')

        elif 'close captions' in query:
            keyboard.press('c')

        elif 'next' in query:
            keyboard.press_and_release('shift+N')

        elif 'previous video' in query:
            keyboard.press_and_release('shift+P')

        elif 'mini player' in query:
            keyboard.press('i')

        elif 'activate youtube tools' in query:
            youtubeauto()

        elif 'open a new window' in query:
            keyboard.press_and_release('ctrl+n')

        elif 'open a new window in incognito' in query:
            keyboard.press_and_release('Shift + Ctrl + n')

        elif 'open a new tab' in query:
            keyboard.press_and_release('ctrl+t')

        elif 'open a file in browser' in query:
            keyboard.press_and_release('Ctrl + o')

        elif 'close the current tab' in query:
            keyboard.press_and_release('Ctrl + w')

        elif 'close the current window' in query:
            keyboard.press_and_release('Shift + Ctrl + w')

        elif 'Reopen the last tab i closed' in query:
            keyboard.press_and_release('Shift + Ctrl + t')

        elif 'Reopen the last window i closed' in query:
            keyboard.press_and_release('Shift + Ctrl + t')

        elif 'go to tab 1' in query:
            keyboard.press_and_release('Ctrl + 1')

        elif 'go to tab 2' in query:
            keyboard.press_and_release('Ctrl + 2')

        elif 'go to tab 3' in query:
            keyboard.press_and_release('Ctrl + 3')

        elif 'go to tab 4' in query:
            keyboard.press_and_release('Ctrl + 4')

        elif 'go to tab 5' in query:
            keyboard.press_and_release('Ctrl + 5')

        elif 'go to tab 6' in query:
            keyboard.press_and_release('Ctrl + 6')

        elif 'go to tab 7' in query:
            keyboard.press_and_release('Ctrl + 7')

        elif 'go to tab 8' in query:
            keyboard.press_and_release('Ctrl + 8')

        elif 'Go to the next tab' in query:
            keyboard.press_and_release('ctrl+tab')

        elif 'Go to the previous tab' in query:
            keyboard.press_and_release('Shift + Ctrl + Tab')

        elif 'Go to the previous tab' in query:
            keyboard.press_and_release('Shift + Ctrl + Tab')

        elif 'Go to previous page in my browsing history' in query:
            keyboard.press_and_release('Alt + Left arrow')

        elif 'Go to the next page in my browsing history' in query:
            keyboard.press_and_release('Alt + Right arrow')

        elif 'maximize window' in query:
            keyboard.press_and_release('Alt + =')

        elif 'minimize window' in query:
            keyboard.press_and_release('Alt + -')

        elif 'go to bottom of the page' in query:
            keyboard.press_and_release('Ctrl + Alt + Down arrow')

        elif 'go to top of the page' in query:
            keyboard.press_and_release('Ctrl + Alt + Up arrow ')

        elif 'go to history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'go to downloads' in query:
            keyboard.press_and_release('ctrl + j')

        elif 'activate chrome tools' in query:
            chromeauto()

        elif 'tell me a joke' in query:
            query = query.replace("jarvis","")
            j = pyjokes.get_joke()
            Speak(j)

        elif 'repeat my words' in query:
            Speak('ok sir')
            p = takecommand()
            Speak(f" {p}")

        elif 'alarm' in query:
            Speak('tell me the time to set')
            time = input(" :enter the time: ")

            while True:
                time_ac = datetime.datetime.now()
                now = time_ac.strftime("%H:%M:%S")
                
                if now == time:
                    Speak('time to wake up sir')
                    os.startfile('Fed Up Slowed.mp3')
                    

                elif now>time:
                  break

        elif 'open translator' in query:
            Trans()

        elif 'remember that' in query:
            remembermsg = query.replace("remember that","")
            remembermsg = query.replace("jarvis","")
            remembermsg = query.replace("i","you")
            Speak("you tell me to remember" + remembermsg)
            rember = open('data.txt','w')
            rember = rember.write(remembermsg)
            rember.close()

        elif 'what do you remember' in query:
            rember = open('data.txt','r')
            Speak('you tell me that' + rember.read())
      
        elif 'what is' in query:
            import wikipedia as googleScrap
            query = query.replace("google search" , "")
            query = query.replace("google" , "")
            query = query.replace("jarvis","")
            query = query.replace("what is","")
            Speak("this is what i found for your search")
            
            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query,3)
                Speak(result)

            except:
                Speak("no speakable data is avaliable")

        elif 'temperature' in query:
            query =query.replace("tell","")
            query =query.replace("what's","")
            query =query.replace("me the","")
            temp()

        elif 'audiobook' in query:
            reader()        
taskExe()

       


