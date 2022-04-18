from tkinter import *
from tkinter import ttk

class MainClass():
    
    def __init__(self,master):
        self.toppings = ["Abhinav","Abhi","Dhruv","Abc"]
        self.master = master
        self.punches_list = []
        self.my_label = Label(master,text="Start Typing")
        self.my_label.pack(pady=20)

        self.data_show = Entry(master)
        self.data_show.pack()
        self.my_entry = Entry(master)
        self.my_entry.pack()

        self.my_list = Listbox(master)
        self.my_list.pack(pady=40)
        self.update(self.toppings)
        
        self.my_list.bind("<<ListboxSelect>>",self.fillout)

        self.my_entry.bind("<KeyRelease>",self.check)
    
    def update(self,data):
        
        self.my_list.delete(0,END)
        for item in data:
            self.my_list.insert(END,item)
    def fillout(self,e):
        self.my_entry.delete(0,END)
        self.punches_list.append(self.my_list.get(ANCHOR)+",")

        self.data_show.delete(0, END)
        for i in self.punches_list:
            self.data_show.insert(END, i)
            
        # self.my_entry.insert(0,self.my_list.get(ANCHOR))
        self.toppings.remove(self.my_list.get(ANCHOR))

    def check(self,e):
        typed = self.my_entry.get()
        if typed =="":
            data = self.toppings
        else:
            data = []
            for item in self.toppings:
                if typed.lower() in item.lower():
                    data.append(item)

        self.update(data)
    
root = Tk()
MainClass(root)
root.mainloop()