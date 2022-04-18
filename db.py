from tkinter import *
import sqlite3
root = Tk()
root.title("Images")
# root.geometry("400X400")



# c.execute("""CREATE TABLE address(
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
# )
# """)

def submit():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()   

    c.execute("INSERT INTO address VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
    {
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get(),
    })

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect("test.db")
    c = conn.cursor() 

    c.execute("DELETE FROM address WHERE oid="+delete_record.get())
    delete_record.delete(0,END)
    conn.commit()
    conn.close()

def show():
    conn = sqlite3.connect("test.db")
    c = conn.cursor() 

    c.execute("SELECT *,oid FROM address")
    records = c.fetchall()
    print(records)
    print_records = ""
    for record in records:
        print_records = print_records + str(record[0]) +" "+ str(record[6]) + "\n" 

    query_label = Label(root,text=print_records)
    query_label.grid(row=10,column=0,columnspan=2)

    conn.commit()
    conn.close()

    return 

f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)

address = Entry(root,width=30)
address.grid(row=2,column=1)

city = Entry(root,width=30)
city.grid(row=3,column=1)

state = Entry(root,width=30)
state.grid(row=4,column=1)

zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1)

delete_record = Entry(root,width=30)
delete_record.grid(row=8,column=1)


f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0)

l_name_label = Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

address_label = Label(root,text="Address")
address_label.grid(row=2,column=0)

city_label = Label(root,text="City")
city_label.grid(row=3,column=0)

state_label = Label(root,text="State")
state_label.grid(row=4,column=0)

zipcode_label = Label(root,text="ZipCode")
zipcode_label.grid(row=5,column=0)

delete_label = Label(root,text="Delete ID")
delete_label.grid(row=8,column=0)

submit_button = Button(root,text="Add record to db",command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

query_button = Button(root,text="Show record to db",command=show)
query_button.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

delete_button = Button(root,text="Select record to db",command=delete)
delete_button.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

edit_button = Button(root,text="Update record to db",command=delete)
edit_button.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

root.mainloop()