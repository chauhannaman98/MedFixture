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

# exec(open("./appointment.py").read())

class App:
    def __init__(self, master):
        self.master = master

        # labels for window
        # login ID
        self.login_id = Label(text="Login ID", font=('arial 15 bold'), fg='black')
        self.login_id.place(x=50, y=50)

        # password
        self.password = Label(text="Password", font=('arial 15 bold'), fg='black')
        self.password.place(x=50, y=100)

        # entries for labels
        self.login_id_ent = Entry(width=20)
        self.login_id_ent.place(x=250, y=50)

        self.password_ent = Entry(width=20)
        self.password_ent.place(x=250, y=100)

        # button to login
        self.submit = Button(text="Login", width=20, height=2, bg='steelblue', command=self.login)
        self.submit.place(x=150, y=150)

    # function to login
    def login(self):
        sql = "SELECT pass FROM credentials WHERE id=?"
        self.res = c.execute(sql, (self.login_id_ent,))
        for i in self.res:
            print(i)


root = tk.Tk()
b = App(root)
root.geometry("540x480+0+0")
root.resizable(False, False)
root.title("Techmirtz Hospital Appointment Application - Login Window")
root.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))
root.mainloop()