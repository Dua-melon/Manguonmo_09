from tkinter import*
from tkinter import scrolledtext
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = entry.get()
    w = w.lower()
    if w in data:
        return (w,':',data[w])
    elif w.title() in data: 
        return data[w.title()]
    elif w.upper() in data: 
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        return ("Có phải bạn muốn tìm {}? \n {}:{} ".format(get_close_matches(w, data.keys())[0],get_close_matches(w, data.keys())[0],data[get_close_matches(w, data.keys())[0]]) )
        
    else:
        return "Xin lỗi, không tìm thấy từ trong từ điển!!!"
def out_put():
    output = translate(entry)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    label1 = Label(frame2, text = translate(entry))
    label1.place(x = 10, y = 10)


wd = Tk()
wd.geometry('500x300')
wd.title("HUMG Dictionary")

frame = Frame(wd,bg = '#cce6ff')
frame.place(relwidth = 1, relheight = 1)

entry = Entry(frame,width = 50,bd = 5)
entry.place(x = 60, y = 5)

btn = Button(frame,text = 'Tìm kiếm',padx = 7,pady = 2, command = out_put )
btn.place(x = 375, y = 5)


frame1 = Frame(frame,bg = '#ffe6f2')
frame1.place(x = 60, y = 40, relheight = 0.7, relwidth = 0.78)

frame2 = Frame(frame1, bg = 'white')
frame2.place(x = 10,y = 10, relwidth = 0.945, relheight = 0.9)

wd.mainloop()





import pyttsx3 #(thu vien dung de noi, pip install pyttsx3)
import speech_recognition#thu vien dung de voice to text, phai tai speechrecognition, pyaudio 
# sau do se co loi voi pyaudio, nhap 2 dong nay vao cmd 
#pip install pipwin
#pipwin install pyaudio
from datetime import datetime # phan de lay ngay thang nam


# phan de minh giao tiep voi emma
virtual_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Emma: I'm hearing you")
    print('.........')
    audio = virtual_ear.listen(mic)
try:
    you = virtual_ear.recognize_google(audio)
except:
    you = ''
print("You:"+ you)


# day la phan AI, phan de Emma hieu ban muon gi
if you == 'hello':
    Emma_brain = "xin chao"
elif you == 'today':
    Emma_brain = datetime.today().strftime('%d-%m-%Y')
elif you == 'time':
    Emma_brain = datetime.today().strftime('%H-%M-%S')

print(Emma_brain)



# phan de no noi ra
engine = pyttsx3.init()

# de thay doi giong noi thi dung 2 dong code nay, 0 la giong nam va 1 la giong nu
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say(Emma_brain)
engine.runAndWait() # se co loi no module named 'pythoncom', de sua thi pip install pywin32pip install pywin32