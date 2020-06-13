# -*- coding: utf-8 -*-
from tkinter import*
from tkinter import scrolledtext
import json
from difflib import get_close_matches

data = open('data.txt','r')

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