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
import os, sys

conn = sqlite3.connect('database.db')
c = conn.cursor()

class App:
    def __init__(self, master):
        self.master = master

        # labels for window
        self.space = Label(text="")
        self.space.pack()
        
        self.loginLabel = Label(text="Enter login credentials", font=('arial 14 bold'), fg='black')
        self.loginLabel.pack()

        self.space2 = Label(text="")
        self.space2.place(x=50, y=100)

        # login ID
        self.login_id = Label(text="Login ID*", font=('arial 12'), fg='black')
        self.login_id.place(x=60, y=70)

        # password
        self.password = Label(text="Password*", font=('arial 12'), fg='black')
        self.password.place(x=60, y=120)

        # entries for labels
        self.login_id_ent = Entry(width=20)
        self.login_id_ent.place(x=260, y=72)

        self.password_ent = Entry(width=20, show='*')
        self.password_ent.place(x=260, y=122)

        # button to login
        self.submit = Button(text="Login", width=20, height=2, bg='steelblue', command=self.login)
        self.submit.place(x=160, y=170)
        self.submit.bind('<Return>', self.login)

    # function to login
    def login(self):
        self.id = self.login_id_ent.get()
        self.password = self.password_ent.get()
        self.login_id_ent.delete(0, END)
        self.password_ent.delete(0, END)
        sql = "SELECT * FROM credentials WHERE id LIKE ?"
        self.input = str(self.id)
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.db_name = self.row[1]
            self.db_pass = self.row[2]
            self.db_designation = self.row[3]

        if self.db_pass == self.password:
            tkinter.messagebox.showinfo("Login Successful", "Hello "+self.db_name+"! You have successfully logged in as " + self.db_designation)
            drawWin()
        else:
            tkinter.messagebox.showerror("Login Unsuccessful", "Invalid credentials! Please login again")
    
def drawWin():
    top = Toplevel() 
    top.geometry("480x320+0+0") 
    top.title("Welcome") 

    # Hide root window
    hide_root()

    # function to close the top window
    def logout():
        MsgBox = tk.messagebox.askquestion('Logout Application','Are you sure you want to logout?', icon='warning')
        if MsgBox == 'yes':
            top.destroy()
            show_root()
    
    # menu bar
    Chooser = Menu()
    itemone = Menu()

    itemone.add_command(label='Add Appointment', command=appointment)
    itemone.add_command(label='Edit Appointment', command=update)
    itemone.add_command(label='Delete Appointment', command=update)
    itemone.add_separator()
    itemone.add_command(label='Help')
    itemone.add_command(label='Logout', command=logout)

    Chooser.add_cascade(label='File', menu=itemone)
    Chooser.add_command(label='Add', command=appointment)
    Chooser.add_command(label='Update', command=update)
    Chooser.add_command(label='Delete', command=update)
    Chooser.add_command(label='Help')
    Chooser.add_command(label='Logout', command=logout)

    top.config(menu=Chooser)
    top.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))

# function to open the appointment window    
def appointment():
    if sys.platform.startswith('linux'):
        print("OS = linux")
        os.system("python3 appointment.py")
    elif sys.platform.startswith('win32'):
        print("OS = win32")
        os.system("python appointment.py")

# function to open the update window  
def update():
    if sys.platform.startswith('linux'):
        print("OS = linux")
        os.system("python3 update.py")
    elif sys.platform.startswith('win32'):
        print("OS = win32")
        os.system("python update.py")

# function to open the display window  
def display():
    if sys.platform.startswith('linux'):
        print("OS = linux")
        os.system("python3 display.py")
    elif sys.platform.startswith('win32'):
        print("OS = win32")
        os.system("python display.py")

root = tk.Tk()
b = App(root)
root.geometry("540x320+0+0")
root.resizable(False, False)
root.title("Techmirtz Hospital Appointment Application - Login Window")
root.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))

def hide_root():
    # Hide root window
    root.withdraw()

def show_root():
    # Show root window
    root.deiconify()

root.mainloop()
