#Made the same but explaing
from tkinter import *
from tkinter import ttk

app = Tk(className="app")
app.geometry("340x320")
app.resizable(False, False)

def printxt():
    print("Hello World!")
    

ttk.Button(text="Click", command=printxt).pack(pady=10)



app.mainloop()