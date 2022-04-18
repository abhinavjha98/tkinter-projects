from tkinter import *

root = Tk()

e = Entry(root,width=50)

e.pack()

def myClick():
    myLabel = Label(root,text=e.get())
    myLabel.pack()

myButton = Button(root,text="Enter your name",padx=50,command=myClick)

myButton.pack()

root.mainloop()