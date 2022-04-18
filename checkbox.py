from tkinter import *
import sqlite3
root = Tk()    

array = ['a', 'b', 'c', 'd']
vars = []

conn = sqlite3.connect("test1.db")
c = conn.cursor()
# c.execute("""CREATE TABLE dish(
#     add_dish text,
#     add_description text
#     )
# """)


c.execute("SELECT *,oid FROM dish")
records = c.fetchall()
print(records)
j=0
print_records = ""
da = 0
vard = []
for record in records:
    j=j+1
    vars.append(StringVar())
    var = StringVar(value=record[0])
    vars[-1].set(0)
    print(vars[-1].set(0))
    d = vars[-1]
    # c = Checkbutton(root, text=record[0], variable=var, command=lambda i=record[1]:printSelection(i,vars[-1].get()), onvalue=1, offvalue=0)
    c = Checkbutton(root, text=record[0], variable=var, onvalue=1, offvalue=0)
    c.grid(row=j+2,column=0)
    vard.append(var)
    # print_records = print_records + str(record[0]) +" "+ str(record[1]) + "\n" 

query_label = Label(root,text=print_records)
query_label.grid(row=10,column=0,columnspan=2)

# def printSelection(i,d):
#     print(i,d)
        # print(vars[i].get())
def submits():
    # extract roll numbers for checked checkbuttons
    result = [var.get() for var in vard if var.get()]
    print(result)
    for i in vard:
        if(i.get()=="1"):
            print(i.get())

def submit():
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()   

    c.execute("INSERT INTO dish VALUES (:add_dish,:add_description)",
    {
        'add_dish':add_dish.get(),
        'add_description':add_description.get(),
        
    })

    add_dish.delete(0,END)
    add_description.delete(0,END)
    conn.commit()
    conn.close()
    return

add_dish = Entry(root,width=30)
add_dish.grid(row=0,column=1,padx=20)

add_description = Entry(root,width=30)
add_description.grid(row=1,column=1,padx=20)

add_dish_label = Label(root,text="Enter Dish Name")
add_dish_label.grid(row=0,column=0)

add_description_label = Label(root,text="Enter Dish")
add_description_label.grid(row=1,column=0)

submit_button = Button(root,text="Add record to db",command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)



# for i in range(len(array)):
#     vars.append(StringVar())
#     vars[-1].set(0)
#     c = Checkbutton(root, text=array[i], variable=vars[-1], command=lambda i=i:printSelection(i), onvalue=1, offvalue=0)
#     c.grid(row=i+2,column=0)


root.mainloop()