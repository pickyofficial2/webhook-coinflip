import tkinter as tk
import random
import requests

webhook_url = "YOUDISCORDWEBHOOKURLHERE" # replace with your webhook url from discord

def play(): # defines the play command, which happens when u press button1
    coinflip = random.randint(0, 1)
    if coinflip > 0:
        winlose = "heads won"
        requests.post(webhook_url, json={"content":winlose})
        
    else:
        winlose = "tails won"
        requests.post(webhook_url, json={"content":winlose})

window = tk.Tk() 
window.geometry("200x200") # sets the window size
window.resizable(width=False, height=False) # makes the window unresizeable
window.title("coinflip") # changes the name of the window
 
button1 = tk.Button(window, text="Heads", font=("Arial", 30, "bold"), fg="green", bg="light green", command=play, height=3, width=8) # defines what button1 is
button1.pack() # makes button1 appear using pack()

button2 = tk.Button(window, text="close", fg="red", bg="dark red", borderwidth=5, command=window.destroy) # defines what button2 is
button2.pack() # makes button2 appear using pack()

window.mainloop() # the window's main loop
