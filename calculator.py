from ast import Lambda
import math
from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    return 

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)
    

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math =="addition":
        e.insert(0,f_num+int(second_number))
    elif math == "sub":
        e.insert(0,f_num-int(second_number))
    elif math == "mul":
        e.insert(0,f_num*int(second_number))
    else:
        e.insert(0,f_num/int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num 
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = "mul"
    f_num = int(first_number)
    e.delete(0,END)

def button_division():
    first_number = e.get()
    global f_num 
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0,END)

myButton1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
myButton2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
myButton3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
myButton4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
myButton5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
myButton6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
myButton7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
myButton8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
myButton9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
myButton0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
myButtonadd = Button(root,text="+",padx=39,pady=20,command=lambda:button_add())
myButtonequal = Button(root,text="=",padx=100,pady=20,command=lambda:button_equal())
myButtonclear = Button(root,text="Clear",padx=93,pady=20,command=lambda:button_clear())

myButtonsub = Button(root,text="-",padx=39,pady=20,command=lambda:button_subtract())
myButtonmul = Button(root,text="*",padx=39,pady=20,command=lambda:button_multiply())
myButtondiv = Button(root,text="/",padx=39,pady=20,command=lambda:button_division())

myButton1.grid(row=3,column=0)
myButton2.grid(row=3,column=1)
myButton3.grid(row=3,column=2)

myButton4.grid(row=2,column=0)
myButton5.grid(row=2,column=1)
myButton6.grid(row=2,column=2)

myButton7.grid(row=1,column=0)
myButton8.grid(row=1,column=1)
myButton9.grid(row=1,column=2)

myButton0.grid(row=4,column=0)

myButtonadd.grid(row=5,column=0)
myButtonequal.grid(row=5,column=1,columnspan=2)
myButtonclear.grid(row=4,column=1,columnspan=2)

myButtonsub.grid(row=6,column=0)
myButtonmul.grid(row=6,column=1)
myButtondiv.grid(row=6,column=2)
root.mainloop()