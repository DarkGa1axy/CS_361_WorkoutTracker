import os
import sys
from tkinter import *
import tkinter.filedialog
# from tkinter import ttk

root = Tk()
root.geometry("300x300")
root.title("Audio Visualizer")

filename = "" # song file

def import_song():
    global filename

    top = tkinter.Tk()
    top.withdraw()  # hide window

    filename = tkinter.filedialog.askopenfilename(parent=top)
    filename = os.path.basename(filename)

    # clear text
    song = Label(root, text = "                                                                                   ")
    song.place(x = 110, y = 22)

    # print song name
    song = Label(root, text = filename)
    song.place(x = 110, y = 22)
    
    # Cover up previous error text with spaces
    err_text = Label(root, text = "                                                                                   ")
    err_text.place(x = 125, y = 62)
    
    top.destroy()

def open_vis():
    a = "python3.10 vis.py"
    b = str(filename)
    end = ".wav"

    if b == "": # no file selected
        err_text = Label(root, text = "Error: No file selected")
        err_text.place(x = 125, y = 62)
    elif b.endswith(end) == False: # not .wav file
        err_text = Label(root, text = "Error: File is not .wav format")
        err_text.place(x = 125, y = 62)
    else:
        a = a + " " + b
        print(a)
        os.system(a)

def main():
    b1 = Button(root, text = "Import Song", command = import_song)
    b1.place(x = 30, y = 20)

    b2 = Button(root, text = "Open Visualizer", command = open_vis)
    b2.place(x = 30, y = 60)

    b3 = Button(root, text = "Get Song Recommendation")
    b3.place(x = 30, y = 120)

    t1 = Label(root, wraplength = 200, justify = LEFT, text = "In order for song recommendation to work, filename must be the name of the song. Spaces should be replaced by underscores. \nExample: Without Me by Eminem would be without_me.wav")
    t1.place(x = 30, y = 150)


    root.mainloop()

main()