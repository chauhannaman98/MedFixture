# update the appointments
# import modules
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    import tkinter as tk
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect('database.db')
c = conn.cursor()

class App:
    def __init__(self, master):
        self.master = master
        self.heading = Label(master, text="Update Appointments", fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0) 

        # search criteria
        self.name = Label(master, text="Enter Patient's Name", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        # entry for the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=300, y=62)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=102)

    # function to search
    def search_db(self):
        self.input = self.namenet.get()
        
        # execute sql
        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input))
        for self.row in self.res:
            print(self.row)

#creating the object
root = tk.Tk()
b = App(root)
root.geometry("1200x720+0+0")
root.resizable(False, False)
root.title("Techmirtz Hospital Appointment Application - Update Appointment")
root.iconphoto(False, tk.PhotoImage(file='icon.png'))

# end the loop
root.mainloop()