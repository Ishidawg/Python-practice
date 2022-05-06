#Tkinter app practice with new widgtes "ttk"
import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

main = Tk(className = "Practice app")
main.geometry("400x400")
main.resizable(False, False)

def helloWorld():
    print("Hello World!")
    messagebox.showinfo(title = "Information", message = "Simple text", icon = "info")

def nameInput():
    pass
    
def quitButton():
    result = messagebox.askquestion(title = "Quit", message = "You really want to quit?", icon = "question")
    if result == 'yes':
        main.destroy()
    else:
        pass

ttk.Label(text = "Practice two").pack(pady = 2)
ttk.Label (text = "It's an app to learn Tkinter Library").pack()    
ttk.Button(text = "Information Button", command = helloWorld).pack(pady = 10)
ttk.Button(text = "Quit", command = quitButton).pack(pady = 140)
    
    
main.mainloop()