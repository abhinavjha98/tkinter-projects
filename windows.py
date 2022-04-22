import tkinter as tk
from tkinter import messagebox
import sqlite3
from fpdf import FPDF,HTMLMixin
from pathlib import Path
import time
my_file = Path("test2.db")
if my_file.exists():
    print("db")
    pass
else:
    print("Create")
    conn = sqlite3.connect("test2.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE dish(
        add_dish text,
        add_description text
        )
    """)
    conn.commit()
    conn.close()
class windowclass():
    def __init__(self, master):
        conn = sqlite3.connect("test2.db")
        c = conn.cursor()
        self.master = master
        self.addbtn = tk.Button(master, text="Add Data", command=self.command)
        self.addbtn.grid(row=1,column=1,  sticky=tk.W+tk.E,pady=10)
        self.quitbtn = tk.Button(master, text="Quit", command=self.quit)
        self.quitbtn.grid(row=1,column=2)
        self.container_no_label = tk.Label(master,text="Enter Container no",pady=5,padx=10)
        self.container_no_label.grid(row=2,column=0)
        self.container_no = tk.Entry(master,width=20)
        self.container_no.grid(row=2,column=1)

        self.invoice_label = tk.Label(master,text="Enter Invoice no",pady=5)
        self.invoice_label.grid(row=3,column=0)
        self.invoice = tk.Entry(master,width=20)
        self.invoice.grid(row=3,column=1)

        self.date_label = tk.Label(master,text="Enter Date",pady=5)
        self.date_label.grid(row=4,column=0)
        self.date = tk.Entry(master,width=20)
        self.date.grid(row=4,column=1)

        self.port_discharge_label = tk.Label(master,text="Enter port of discharge",padx=10,pady=5)
        self.port_discharge_label.grid(row=5,column=0)
        self.port_discharge = tk.Entry(master,width=20)
        self.port_discharge.grid(row=5,column=1)

        c.execute("SELECT *,oid FROM dish")
        self.records = c.fetchall()
        print(self.records)
        j=5
        print_records = ""
        da = 0
        self.vard = []
        self.vars=[]
        
        self.punches_list = []
        self.my_label = tk.Label(master,text="Search Dishes")
        self.my_label.grid(row=6,column=0)
        self.my_entry = tk.Entry(master)
        self.my_entry.grid(row=6,column=1)

        self.my_list = tk.Listbox(master)
        self.my_list.grid(row=7,column=1,pady=10)

        self.my_label = tk.Label(master,text="Selected Data")
        self.my_label.grid(row=8,column=0)

        self.data_show = tk.Entry(master)
        self.data_show.grid(row=8,column=1)

        self.toppings=[]

        for record in self.records:
            self.toppings.append(record[0])
        self.update(self.toppings)
        
        self.my_list.bind("<<ListboxSelect>>",self.fillout)

        self.my_entry.bind("<KeyRelease>",self.check)
        # for record in self.records:
        #     j=j+1
        #     self.vars.append(tk.StringVar())
        #     self.var = tk.StringVar(value=record[0])
        #     self.vars[-1].set(0)
        #     print(self.vars[-1].set(0))
        #     d = self.vars[-1]
        #     # c = Checkbutton(root, text=record[0], variable=var, command=lambda i=record[1]:printSelection(i,vars[-1].get()), onvalue=1, offvalue=0)
            
        #     c = tk.Checkbutton(master, text=record[0], variable=self.var, onvalue=1, offvalue=0)
        #     c.grid(row=j+2,column=0)
        #     self.vard.append(self.var)

        self.printbtn = tk.Button(master, text="Save PDF", command=self.print)
        self.printbtn.grid(row=10,column=1,  sticky=tk.W+tk.E)
    
    def fillout(self,e):
        self.my_entry.delete(0,tk.END)
        if(self.my_list.get(tk.ANCHOR)+"," in self.punches_list):
            pass
        else:
            self.punches_list.append(self.my_list.get(tk.ANCHOR)+",")

            self.data_show.delete(0, tk.END)
            for i in self.punches_list:
                self.data_show.insert(tk.END, i)
                
            # self.my_entry.insert(0,self.my_list.get(ANCHOR))
            self.toppings.remove(self.my_list.get(tk.ANCHOR))

    def update(self,data):
        
        self.my_list.delete(0,tk.END)
        for item in data:
            self.my_list.insert(tk.END,item)

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

    def command(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("600x300")
        app = Demo2(toplevel)

    def quit(self):
        self.master.destroy()

    def print(self):
        # result = [var.get() for var in self.vard if var.get()]
        oid_data = []
        oid_data.append(("","",""))
        oid_data.append(("","",""))
        oid_data.append(("","",""))
        oid_data.append(("","",""))
        oid_data.append(("Sr.No","Product", "Ingredients"))
        k=0
        for i in range(len(self.punches_list)):
            k=k+1
            for j in self.records:
                
                if(self.punches_list[i].replace(",","")==j[0]):
                    oid_data.append((str(k),j[0],j[1]))
       
        # for i in self.vard:
        #     j=j+1
        #     if(i.get()=="1"):
        #         k=k+1
        #         print(self.records[j-1])
        #         oid_data.append((str(k),self.records[j-1][0],self.records[j-1][1]))
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", size=10)
        # pdf.set_xy(0.0,0.0)
        # pdf.set_text_color(220, 50, 50)
        # pdf.cell(w=210.0, h=40.0, align='C', txt="LORD OF THE PDFS", border=0)
        line_height = pdf.font_size * 2.5
        col_width = pdf.epw / 3

        lh_list = []
         #list with proper line_height for each row
        use_default_height = 0 #flag
        
        #create lh_list of line_heights which size is equal to num rows of data
        for row in oid_data:
            for datum in row:
                word_list = datum.split()
                number_of_words = len(word_list) #how many words
                if number_of_words>2: #names and cities formed by 2 words like Los Angeles are ok)
                    use_default_height = 1
                    new_line_height = pdf.font_size * (number_of_words/2) #new height change according to data 
            if not use_default_height:
                lh_list.append(line_height)
            else:
                lh_list.append(new_line_height)
                use_default_height = 0
        #create your fpdf table ..passing also max_line_height!
        for j,row in enumerate(oid_data):
            
            if j==0:
                pdf.cell(col_width, line_height,align='L', txt="Container no: "+str(self.container_no.get()), border=0)
            elif j==1:
                pdf.cell(col_width, line_height,align='L', txt="Invoice no: "+str(self.invoice.get()), border=0)
            elif j==2:
                pdf.cell(col_width, line_height,align='L', txt="Date: "+str(self.date.get()), border=0)
            elif j==3:
                pdf.cell(col_width, line_height,align='L', txt="Port of discharge: "+str(self.port_discharge.get()), border=0)
            else:
                for datum in range(len(row)):
                    print(datum)
                    
                    line_height = lh_list[j]
                    #choose right height for current row
                    if(datum==0):
                        pdf.multi_cell(col_width-50, line_height, row[datum], border=1,align='L',ln=3, 
                    max_line_height=pdf.font_size)
                    elif (datum==1):
                        pdf.multi_cell(col_width-20, line_height, row[datum], border=1,align='L',ln=3, 
                    max_line_height=pdf.font_size)
                    else:
                        pdf.multi_cell(col_width+70, line_height, row[datum], border=1,align='L',ln=3, 
                    max_line_height=pdf.font_size)
            pdf.ln(line_height)

        pdf.output(str(self.invoice.get())+'.pdf')
        message = messagebox.askyesno("Disk Reciepe","Are you want to create more")
        print(message)
        if message ==False:
            self.master.destroy()

        

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        # self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        # self.quitButton.pack()
        add_dish = tk.Entry(self.frame,width=40)
        add_dish.grid(row=5,column=1,padx=20,pady=20)

        add_description = tk.Text(self.frame, height = 5, width = 50)
        add_description.grid(row=6,column=1,padx=20)

        add_dish_label = tk.Label(self.frame,text="Enter Dish Name")
        add_dish_label.grid(row=5,column=0)

        add_description_label = tk.Label(self.frame,text="Enter Dish")
        add_description_label.grid(row=6,column=0)

        submit_button = tk.Button(self.frame,text="Add record to db",command=lambda:self.submit(add_dish,add_description))
        submit_button.grid(row=7,column=0,pady=10,padx=10)

        back_button = tk.Button(self.frame,text="Back to screen",command=self.close_windows)
        back_button.grid(row=7,column=1,pady=10,padx=10)

        edit_button = tk.Button(self.frame,text="Edit records",command=self.update_windows)
        edit_button.grid(row=8,column=0,pady=10,padx=10)

        delete_button = tk.Button(self.frame,text="Delete records",command=self.delete_windows)
        delete_button.grid(row=8,column=1,pady=10,padx=10)
        self.frame.pack()

    def submit(self,add_dish,add_description):
        conn = sqlite3.connect("test2.db")
        c = conn.cursor()   
        print(add_dish.get())
        add_dish_data = add_dish.get()
        add_description_data = add_description.get("1.0",tk.END)
        c.execute("INSERT INTO dish VALUES (:add_dish,:add_description)",
        {
            'add_dish':add_dish_data,
            'add_description':add_description_data,
            
        })

        add_dish.delete(0,tk.END)
        add_description.delete('1.0', tk.END)
        conn.commit()
        conn.close()
        return

    def close_windows(self):
        # self.master.destroy()
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("450x550")
        app = windowclass(toplevel)

    def delete_windows(self):
        # self.master.destroy()
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("450x550")
        app = Delete(toplevel)

    def update_windows(self):
        # self.master.destroy()
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("550x550")
        app = Update(toplevel)

class Delete:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        query_label = tk.Label(self.frame,text="Records in DB")
        query_label.grid(row=0,column=0)
        conn = sqlite3.connect("test2.db")
        c = conn.cursor()
        c.execute("SELECT *,oid FROM dish")
        self.showRecord = c.fetchall()
        print(self.showRecord)
        print_records = ''
        k=0
        for record in self.showRecord:
            k=k+1
            print_records += str(record[0]) +" "+str(record[2])  +"\n"

        self.query_label = tk.Label(self.frame,text=print_records)
        self.query_label.grid(row=0,column=1,pady=10)
        self.delete_label = tk.Label(self.frame,text="Enter ID of dish to be deleted")
        self.delete_label.grid(row=k+1,column=0)
        self.delete_box = tk.Entry(self.frame,width=20)
        self.delete_box.grid(row=k+1,column=1)
        self.show_records_button = tk.Button(self.frame,text="Delete records",command=self.deleteRecords)
        self.show_records_button.grid(row=k+2,column=0,pady=10)
        back_button = tk.Button(self.frame,text="Back to screen",command=self.close_windows)
        back_button.grid(row=k+2,column=1,pady=10)
        conn.commit()
        conn.close()
        self.frame.pack()

    def deleteRecords(self):
        conn = sqlite3.connect("test2.db")
        c = conn.cursor()
        c.execute("DELETE FROM dish WHERE oid="+self.delete_box.get())
        self.delete_box.delete(0,tk.END)
        conn.commit()
        conn.close()
        message = messagebox.askyesno("Delete record","Are you want to delete more")
        print(message)
        if message ==False:
            self.close_windows()
        else:
            self.showRecords()
        # self.master.withdraw()
        # toplevel = tk.Toplevel(self.master)
        # toplevel.geometry("450x550")
        # app = Delete(toplevel)
    def close_windows(self):
        # self.master.destroy()
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("600x300")
        app = Demo2(toplevel)

        

    def showRecords(self):
        conn = sqlite3.connect("test2.db")
        c = conn.cursor()
        c.execute("SELECT *,oid FROM dish")
        self.showRecord = c.fetchall()
        print(self.showRecord)
        print_records = ''
        k=0
        for record in self.showRecord:
            k=k+1
            print_records += str(record[0]) +" "+str(record[2])  +"\n"

        self.query_label = tk.Label(self.frame,text=print_records)
        self.query_label.grid(row=1,column=0)

class Update():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        query_label = tk.Label(self.frame,text="Records in DB")
        query_label.grid(row=0,column=0)
        conn = sqlite3.connect("test2.db")
        c = conn.cursor()
        c.execute("SELECT *,oid FROM dish")
        self.showRecord = c.fetchall()
        print_records = ''
        self.k=0
        for record in self.showRecord:
            self.k=self.k+1
            print_records += str(record[0]) +" "+str(record[2])  +"\n"

        self.query_label = tk.Label(self.frame,text=print_records)
        self.query_label.grid(row=0,column=1,pady=10)
        self.delete_label = tk.Label(self.frame,text="Enter ID of dish to be update")
        self.delete_label.grid(row=self.k+1,column=0)
        self.delete_box = tk.Entry(self.frame,width=20)
        self.delete_box.grid(row=self.k+1,column=1)
        self.show_records_button = tk.Button(self.frame,text="Check records",command=self.updateRecords)
        self.show_records_button.grid(row=self.k+2,column=0,pady=10)
        conn.commit()
        conn.close()
        self.frame.pack()

    def updateRecords(self):
        self.add_dish_label = tk.Label(self.frame,text="Dish Name")
        self.add_dish_label.grid(row=self.k+3,column=0)

        self.add_description_label = tk.Label(self.frame,text="Dish description")
        self.add_description_label.grid(row=self.k+4,column=0)

        self.add_dish = tk.Entry(self.frame,width=30)
        self.add_dish.grid(row=self.k+3,column=1,pady=20)

        self.add_description = tk.Text(self.frame, height = 5, width = 40)
        self.add_description.grid(row=self.k+4,column=1)

        self.show_records_button = tk.Button(self.frame,text="Update records",command=self.saveRecords)
        self.show_records_button.grid(row=self.k+5,column=0,pady=10)
        back_button = tk.Button(self.frame,text="Back to screen",command=self.close_windows)
        back_button.grid(row=self.k+5,column=1,pady=10)
        conn = sqlite3.connect("test2.db")
        c = conn.cursor()
        c.execute("SELECT * FROM dish WHERE oid = "+self.delete_box.get())
        self.showRecord = c.fetchall()
        print(self.showRecord)

        for record in self.showRecord:
            self.add_dish.insert(0,record[0])
            self.add_description.insert(1.0,record[1])
        print_records = ''
        conn.commit()
        conn.close()
        # self.master.withdraw()
        # toplevel = tk.Toplevel(self.master)
        # toplevel.geometry("450x550")
        # app = Delete(toplevel)
        
    def saveRecords(self):
        conn = sqlite3.connect("test2.db")
        c = conn.cursor()
        c.execute("""UPDATE dish SET
            add_dish =:add_dish,
            add_description =:add_description
            WHERE oid =:oid
            """,{
                'add_dish':self.add_dish.get(),
                'add_description':self.add_description.get("1.0",tk.END),
                'oid':self.delete_box.get()
                })
        print(c)
        
        message = messagebox.askyesno("Update record","Are you want to upadte more?")
        print(message)
        if message ==False:
            self.close_windows()
        else:
            self.add_dish.delete(0,tk.END)
            self.add_description.delete('1.0', tk.END)
        conn.commit()
        conn.close()

    def close_windows(self):
        # self.master.destroy()
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("600x300")
        app = Demo2(toplevel)
    def showRecords(self):
        conn = sqlite3.connect("test2.db")
        c = conn.cursor()
        c.execute("SELECT *,oid FROM dish")
        self.showRecord = c.fetchall()
        print(self.showRecord)
        print_records = ''
        k=0
        for record in self.showRecord:
            k=k+1
            print_records += str(record[0]) +" "+str(record[2])  +"\n"

        self.query_label = tk.Label(self.frame,text=print_records)
        self.query_label.grid(row=1,column=0)
        conn.commit()
        conn.close()
root = tk.Tk()
root.title("window")

root.geometry("450x550")
cls = windowclass(root)
root.eval('tk::PlaceWindow . center')
root.mainloop()