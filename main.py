from tkinter import *
import queue
from tkinter import ttk
from tkinter import messagebox
from db import Database
import collections
from collections import deque


db = Database("cab_service.db")
d=deque(db)
root = Tk()
root.title("Program for a Cab Service")
root.geometry("1000x720")
root.config(bg="#033074")
#root.state("zoomed")

Name = StringVar()
Type = StringVar()
No_Passengers = StringVar()
AC = StringVar()
Size = StringVar()
Load = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#304c77")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Program for a Cab Service", font=("Calibri", 18, "bold"), bg="#304c77", fg="#ffffff")
title.grid(row=0, column = 1, columnspan=3, padx=10, pady=20, sticky="w")


lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#304c77", fg="#ffffff")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
comboName = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=Name, state="readonly")
comboName['values'] = ("Car", "Van", "3 Wheeler", "Truck", "Lorry")
comboName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblType = Label(entries_frame, text="Type", font=("Calibri", 16), bg="#304c77", fg="#ffffff")
lblType.grid(row=1, column=2, padx=10, pady=10, sticky="w")
comboType = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=Type, state="readonly")
comboType['values'] = ("Traveling", "Carry Things")
comboType.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblNo_Passengers = Label(entries_frame, text="Passengers", font=("Calibri", 16), bg="#304c77", fg="#ffffff")
lblNo_Passengers.grid(row=2, column=0, padx=10, pady=10, sticky="w")
comboNo_Passengers = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=No_Passengers, state="readonly")
comboNo_Passengers['values'] = ("-", "3 and 4", "6 and 8", "3")
comboNo_Passengers.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblAC = Label(entries_frame, text="AC/N-AC", font=("Calibri", 16), bg="#304c77", fg="#ffffff")
lblAC.grid(row=2, column=2, padx=10, pady=10, sticky="w")
comboAC = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=AC, state="readonly")
comboAC['values'] = ("-", "AC", "Non - AC")
comboAC.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblSize = Label(entries_frame, text="Size", font=("Calibri", 16), bg="#304c77", fg="#ffffff")
lblSize.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboSize = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=Size, state="readonly")
comboSize['values'] = ("-", "7 ft and 12 ft")
comboSize.grid(row=3, column=1, padx=10, sticky="w")

lblLoad = Label(entries_frame, text="Load", font=("Calibri", 16), bg="#304c77", fg="#ffffff")
lblLoad.grid(row=3, column=2, padx=10, pady=10, sticky="w")
comboLoad = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=Load, state="readonly")
comboLoad['values'] = ("-", "2500kg and 3500kg")
comboLoad.grid(row=3, column=3, padx=10, pady=10, sticky="w")


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    Name.set(row[1])
    Type.set(row[2])
    No_Passengers.set(row[3])
    AC.set(row[4])
    Size.set(row[5])
    Load.set(row[6])

def dispalyAll():
    tv.delete(*tv.get_children())#Delete before delete
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_vehicle():
    if comboName.get() == "" or comboType.get() == "" or comboNo_Passengers.get() == "" or comboAC.get() == "" or comboSize.get() == "" or comboLoad.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(comboName.get(), comboType.get(), comboNo_Passengers.get(), comboAC.get(), comboSize.get(), comboLoad.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()


def delete_vehicle():
    db.remove(row[0])
    clearAll()
    dispalyAll()

def hire_vehicle():
    #db.remove(row[0])
    d.pop(row[0])
    clearAll()
    dispalyAll()
    messagebox.showinfo(f"(Success", "You hierd a  Vehicle{{row[0]}})")



def clearAll():
    Name.set("")
    Type.set("")
    No_Passengers.set("")
    AC.set("")
    Size.set("")
    Load.set("")


btn_frame = Frame(entries_frame, bg="#304c77")

btn_frame.grid(row=6, column=1, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_vehicle, text="Add Details", width=12, font=("Calibri", 16, "bold"), fg="#ffffff", bg="#06a834", bd=0).grid(row=0, column=0, padx=45)

btnDelete = Button(btn_frame, command=delete_vehicle, text="Delete Details", width=12, font=("Calibri", 16, "bold"), fg="#ffffff", bg="#bd1504", bd=0).grid(row=0, column=2, padx=45)

btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=12, font=("Calibri", 16, "bold"), fg="#ffffff", bg="#05bbe8", bd=0).grid(row=0, column=3, padx=45)

btnHire = Button(btn_frame, command=hire_vehicle, text="Hire", width=12, font=("Calibri", 16, "bold"), fg="#ffffff", bg="#05bbe8", bd=0).grid(row=0, column=4, padx=45)
# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x = 0, y = 305, width = 1000, height = 405)
style = ttk.Style()

style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")

tv.heading("1", text="ID")
tv.column("1", width = 50)

tv.heading("2", text="Name")
tv.column("2", width = 100)

tv.heading("3", text="Type")
tv.column("3", width = 100)

tv.heading("4", text="Passengers")
tv.column("4", width = 100)

tv.heading("5", text="AC")
tv.column("5", width = 100)

tv.heading("6", text="Size")
tv.column("6", width = 100)

tv.heading("7", text="Load")
tv.column("7", width = 100)

tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()