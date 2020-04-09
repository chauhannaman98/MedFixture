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

# import python files
# import appointment

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
        # self.submit.bind('<Return>', self.login)
        # self.grid()
        # self.submit.bind('<Button-1>', self.parse)

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
    
    # menu bar
    Chooser = Menu()
    itemone = Menu()

    itemone.add_command(label='Add Appointment',)
    itemone.add_command(label='Edit Appointment')
    itemone.add_command(label='Delete Appointment')
    itemone.add_separator()
    itemone.add_command(label='Help')
    itemone.add_command(label='Exit')

    Chooser.add_cascade(label='File', menu=itemone)
    Chooser.add_command(label='Add')
    Chooser.add_command(label='Update')
    Chooser.add_command(label='Delete')
    Chooser.add_command(label='Help')
    Chooser.add_command(label='Exit')

    top.config(menu=Chooser)
    top.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))
            

root = tk.Tk()
b = App(root)
root.geometry("540x320+0+0")
root.resizable(False, False)
root.title("Techmirtz Hospital Appointment Application - Login Window")
root.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))
root.mainloop()