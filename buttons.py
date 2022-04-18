from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text="Boom")
    myLabel.pack()

myButton = Button(root,text="Click me",padx=50,command=myClick)

myButton.pack()

root.mainloop()