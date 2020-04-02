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

# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move in the database
c = conn.cursor()

# empty list to later appends the ids from the database
ids = []

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
        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.age.place(x=5, y=140)

        # gender
        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.gender.place(x=5, y=180)

        # location
        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.location.place(x=5, y=220)

        # appointment time
        self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.time.place(x=5, y=260)

        # phone
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.phone.place(x=5, y=300)

        # Enteries for all labels==============================================================
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)

        # button to perform a command
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=340)

        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]

        # displaying the logs in right frame
        self.logs = Label(self.right, text="Appointment Log", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=20, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Appointments till now :  " + str(self.final_id))

    # function to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '':
            tkinter.messagebox.showwarning("Warning","Please fill up all the boxes")
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success","Appointment for "+str(self.val1)+" has been created")
            

            self.box.insert(END, '\nAppointment fixed for ' + str(self.val1) + ' at ' + str(self.val5))


#creating the object
root = tk.Tk()
b = App(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# title of the window
root.title("Techmirtz Hospital Appointment Application")

# icon of the application
root.iconphoto(False, tk.PhotoImage(file='icon.png'))

# end the loop
root.mainloop()