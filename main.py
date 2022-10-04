import tkinter.messagebox
from tkinter import *
from Tracker import Tracker

def start_tracker(event):
    global t
    text = userEntry.get()
    if(len(text) == 0):
        print("Please input a valid user id")
    else:
        print(text)
        userEntry.config(state = "disable")
        start_button.destroy()
        endButton.pack(pady=20)
        endButton.bind('<Button-1>', stop_tracker)
        t = Tracker(text)



def stop_tracker(event):
    global t
    t.stop_listening()
    endButton.config(state = "disable")

def on_closing():
    global t
    if t is not None:
        t.stop_listening()
    root.destroy()

global t
global stu_ID
t = None
root = Tk()
root.title("Joanna Project")
root.geometry("200x200")

# User id input field
Label(text = "User ID", font = ("Montserrat", 13), fg = '#868686',
      pady = 8, padx=35).pack(anchor="nw")
userEntry = Entry(root, width=60)
userEntry.pack(anchor="nw", padx=20)

# Start Button
start_button = Button(root, text='start')
start_button.pack(pady=20)
start_button.bind('<Button-1>', start_tracker)

# End Button
endButton = Button(root, text = "End")

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
