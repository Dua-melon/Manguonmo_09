import pyttsx3 #(thu vien dung de noi, pip install pyttsx3)
import speech_recognition as sr #thu vien dung de voice to text, phai tai speechrecognition, pyaudio 
# sau do se co loi voi pyaudio, nhap 2 dong nay vao cmd 
#pip install pipwin
#pipwin install pyaudio
from datetime import datetime # phan de lay ngay thang nam
import webbrowser
# ListenBox
def virtual_ear():
    ear = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Emma: I'm listening...")
        audio = ear.listen(mic)
        you = ""
        try:
            you = ear.recognize_bing(audio)
        except Exception as e:
            you = ".........."
    print(you) 
# SpeakBox
# se co loi no module named 'pythoncom', de sua thi pip install pywin32
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 140)
def speak_voice(Emma_brain):
    engine = pyttsx3.init()
    engine.say(Emma_brain)
    engine.runAndWait()
def note(text_note):
    date = datetime.now()
    file_name = str(date).replace(":","-") + "-note.txt"
    with open(file_name,'w') as f:
        f.write(text_note)
    subprocess.Popen(['notepad.exe',file_name])

text = virtual_ear()
# VirtualBox
Note_key = ['make a note','write this down', 'remember this','open notepad']
if 'hello' in text:
    Emma_brain = "Hi, How are you today?"
elif 'time' in text:
    Emma_brain ='Date: '+ datetime.today().strftime('%m-%d-%Y')+'\n'+ 'Time : '+ datetime.today().strftime('%H-%M-%S')
elif 'google' in text:
    webbrowser.open_new_tab('https://www.google.com/')
    Emma_brain = "Opening Google"
elif 'youtube' in text:
    webbrowser.open_new_tab('https://www.youtube.com/')
    Emma_brain = "Opening Youtube"
elif 'facebook' in text:
    webbrowser.open_new_tab('https://www.facebook.com/')
    Emma_brain = "Opening Facebook"
elif 'humg' in text:
    webbrowser.open_new_tab('http://humg.edu.vn/Pages/home.aspx')
    Emma_brain = "Opening your University's home page"
for phrase in Note_key:
    if phrase in text:
        print('Emma: Ok, what do you want me to member?')
        Emma_brain = "Ok, what do you want me to member?"
        speak_voice(Emma_brain)
        note = virtual_ear()
        note(note)
print('Emma: '+Emma_brain)

speak_voice(Emma_brain)