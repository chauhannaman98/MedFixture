# import modules
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
import sqlite3

# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move in the database
c = conn.cursor()


# tkinter window
class App:
    def __init__(self, master):
        self.master = master

        # creating the format in master
        self.left = Frame(master, width=800, height=720, bg='lightblue')
        self.left.pack(side = LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side = RIGHT)

        # labels for the window
        self.heading = Label(self.left, text="Techmirtz Hospital Appointment Application", font=('arial 25 bold'), fg='black', bg='lightblue')
        self.heading.place(x=5, y=0)

        # patient's name
        self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.name.place(x=5, y=100)

        # age
        self.name = Label(self.left, text=" Age", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.name.place(x=5, y=140)


#creating the object
root = Tk()
b = App(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()