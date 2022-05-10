## This project is to convert text to speech
# project prerequisites - 1. tkinter, gTTS(Google Text-to-Speech), PlaySound

"""Lets Start the project"""
## Importing necesarry packages
from tkinter import *
from gtts import  gTTS
from playsound import playsound
import os

# Initializing windows
root = Tk()             # <TK()>to initialized tkinter which will be used for GUI
root.geometry("350x300")  # <geometry>to set the width and height of the windows
root.configure(bg='ghost white') # <configure> to use to access windows attributes
root.title("TEXT TO SPEECH") # <title> set the title of the windows

Label(root, text = "TEXT TO SPEECH", font = "arial 20 bold", bg='white smoke').pack()   
# widget is used ot display one or more than one line of text that users cant to able to modify

Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

# Function to Convert Text to Speech in Python
def Text_to_speech():
    Message = entry_field.get()   # <Message> will be stores the value of entry_field
    speech = gTTS(text = Message) # <text> is the sentences or text ot read
    speech.save("NewSound.mp3")   # <speech> stores the converted voice from the text
    playsound("NewSound.mp3")     # <playsound> used to play sound  
    os.remove("NewSound.mp3")     # <remove> used to remove old sound and replace new one

# Function to EXIT
def Exit():
    root.destroy()                # <Exit> will quit the programm by stopping mainloop()

# Function to RESET
def Reset():
    Msg.set("")                   # <Reset> function sets Msg variable to empty strings


# Defining buttons
#Button() used to display button on the window
Button(root, text="PLAY", font="arial 15 bold", 
        command=Text_to_speech, width = '4', bg = 'green').place(x = 25,y=140)
Button(root, font='arial 15 bold', text = "EXIT", width= '4',
        command=Exit, bg = 'red'). place(x=100, y=140)
Button(root, font='arial 15 bold', text="RESET", bg = 'orange',
        width='6', command=Reset).place(x=175, y = 140)

root.mainloop()  # it is a method that executes when we want to run our programm