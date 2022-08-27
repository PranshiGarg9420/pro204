from concurrent.futures import thread
from pickle import GLOBAL
from re import T
import socket
from struct import pack
from threading import Thread
import random
from tkinter import *
from PIL import ImageTk, Image


SERVER= None
IP_ADDRESS=None
PORT=None

screenWidth= None
screenHeight= None

canvas1= None

name_entry= None
player_name= None
name_window= None


def askPlayerName():
    global player_name
    global name_entry
    global name_window
    global canvas1
    global screenHeight
    global screenWidth

    name_window= Tk()
    name_window.title('Tambola Family Fun')
    
    name_window.attributes('-fullscreen',True)

    screenWidth= name_window.winfo_screenwidth()
    screenHeight= name_window.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas1= Canvas(name_window, width=500, height=500)
    canvas1.pack(fill='both', expand=True)

    canvas1.create_image(0,0,image=bg, anchor='nw')
    canvas1.create_text(screenWidth/2, screenHeight/5, text='Enter your name', fill='black', font=('Chalboard SE',100))

    name_entry= Entry(name_window, width=15, justify='center', bg='white', bd=5, font=('Chalboard SE',50))
    name_entry.place(x=screenWidth/2 - 220, y=screenHeight/4 + 100)

    btn= Button(name_window, text='SAVE', width=15, font=('Chalboard SE',30), height=2, bd=3,fg='white', bg='purple',command=saveName)
    btn.place(x=screenWidth/2 - 130, y=screenHeight/2-30)

    name_window.resizable(True, True)
    name_window.mainloop()


def saveName():
    global SERVER
    global player_name
    global name_entry
    global name_window

    player_name= name_entry.get()
    name_entry.delete(0, END)
    name_window.destroy()

    SERVER.send(player_name.encode('utf-8'))


def setup():
    global SERVER
    global IP_ADDRESS
    global PORT

    IP_ADDRESS= '127.0.0.1'
    PORT= 6000

    SERVER= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    askPlayerName()

    
setup()

