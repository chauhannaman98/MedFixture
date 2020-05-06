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
import os, sys, webbrowser, time
from PIL import Image, ImageTk
from tkinter import ttk

conn = sqlite3.connect('database.db')
c = conn.cursor()

class App:
    def __init__(self, master):
        self.master = master

        # menu bar
        Chooser = Menu()
        itemone = Menu()

        itemone.add_command(label='What is it?', command=self.whatIsIt)
        itemone.add_command(label='About', command=self.aboutMaster)

        Chooser.add_cascade(label='Help', menu=itemone)
        Chooser.add_command(label='Exit', command=lambda: exitRoot(root))

        root.config(menu=Chooser)
        
        self.loginLabel = Label(text="\nEnter login credentials\n", font=('arial 14 bold'), fg='black')
        self.loginLabel.pack()

        # login ID
        self.login_id = Label(text="Login ID*", font=('arial 12'), fg='black')
        self.login_id.place(x=60, y=70)

        # password
        self.password = Label(text="Password*", font=('arial 12'), fg='black')
        self.password.place(x=60, y=120)

        # entries for labels
        self.login_id_ent = Entry(width=20)
        self.login_id_ent.place(x=280, y=72)

        self.password_ent = Entry(width=20, show='*')
        self.password_ent.place(x=280, y=122)

        # button for reset password
        self.reset_password = Button(text="Forgot password", bg='#aed4eb', command=self.reset_pass)
        self.reset_password.place(x=310, y=160)

        # button to login
        self.loginShield = PhotoImage(file = "resources/user-shield-100.png")
        self.buttonImage = self.loginShield.subsample(3, 3)
        self.submit = Button(text = 'Login', image=self.buttonImage, compound=LEFT, width=120, height=40, bg='steelblue', command=self.login)
        self.submit.place(x=170, y=200)

        # button for guest login
        self.guestAvatar = PhotoImage(file = "resources/guest.png")
        self.guestImage = self.guestAvatar.subsample(15, 15)
        self.guestButton = Button(text='Login as Guest',image=self.guestImage, compound=LEFT, width=190, height=40, command=self.guestLogin)
        self.guestButton.place(x=140, y=290)

    # function to login
    def login(self, event):
        self.id = self.login_id_ent.get()
        self.password = self.password_ent.get()
        
        if self.id=="" or self.password=="":
            tkinter.messagebox.showwarning("All credentials required","Please enter all fields. Fields marked (*) are required.")
        else:
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
                self.drawWin()
            else:
                tkinter.messagebox.showerror("Login Unsuccessful", "Invalid credentials! Please login again")
    
    # function for guest login
    def guestLogin(self):
        self.id = "guest"
        self.db_name = "Guest User"
        self.db_designation = "Guest"

        tkinter.messagebox.showinfo("Login Successful", "Hello "+self.db_name+"! You have successfully logged in as " + self.db_designation)
        self.drawWin()

    #function to draw toplevel window
    def drawWin(self):
        # hiding root window
        hide_root()

        # drawing toplevel window
        top = Toplevel() 
        top.geometry("480x320+360+180") 
        top.title("Welcome") 
        
        # menu bar
        Chooser = Menu()
        itemone = Menu()

        if self.db_designation == 'System Administrator' or self.db_designation == 'Doctor':
            itemone.add_command(label='Add Appointment', command=self.appointment)
            itemone.add_command(label='Edit Appointment', command=self.update)
            itemone.add_command(label='Delete Appointment', command=self.update)
        
        itemone.add_command(label='View Appointment', command=self.display)
        itemone.add_separator()
        itemone.add_command(label='Logout', command=lambda: self.logout(top))

        Chooser.add_cascade(label='File', menu=itemone)
        Chooser.add_command(label='View Appointment', command=self.display)
        Chooser.add_command(label='Logout', command=lambda: self.logout(top))

        top.config(menu=Chooser)
        top.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))

        self.left = Frame(top, width=130, height=130, bd=1, relief=RAISED)
        self.left.place(x=5, y=5)

        self.right = Frame(top, width=320, height=150)
        self.right.place(x=150, y=5)

        self.footer = Frame(top, width=480, height=30, bd=1, relief=RAISED, \
            highlightbackground="black", highlightthickness=1)
        self.footer.place(x=0, y=290)

        self.timeLabel = Label(self.footer, text="Logged in at "+time.strftime("%I:%M:%S %p"), font=('arial 10'), fg='black')
        self.timeLabel.place(x=5, y=3)
        
        self.drawImage(top)

        self.userlogin = Label(self.right, text="You are logged in as:", font=('arial 12 bold'), fg='black')
        self.userlogin.place(x=5, y=20)

        self.Name = Label(self.right, text="Name: " + self.db_name, font=('arial 12'), fg='black')
        self.Name.place(x=5, y=50)

        self.Name = Label(self.right, text="Designation: " + self.db_designation, font=('arial 12'), fg='black')
        self.Name.place(x=5, y=80)

    def destroyTop(self, top):
        top.destroy()

    # function to close the top window
    def logout(self, top):
        MsgBox = tk.messagebox.askquestion('Logout Application','Are you sure you want to logout?', icon='warning')
        if MsgBox == 'yes':
            self.path = self.name + ".jpg"
            self.destroyTop(top)
            show_root()

    # function to open the appointment window    
    def appointment(self):
        if sys.platform.startswith('linux'):
            os.system("python3 appointment.py")
        elif sys.platform.startswith('win32'):
            os.system("python appointment.py")

    # function to open the update window  
    def update(self):
        if sys.platform.startswith('linux'):
            os.system("python3 update.py")
        elif sys.platform.startswith('win32'):
            os.system("python update.py")

    # function to open the display window  
    def display(self):
        if sys.platform.startswith('linux'):
            os.system("python3 display.py")
        elif sys.platform.startswith('win32'):
            os.system("python display.py")

    def writeTofile(self):
        # Convert binary data to proper format and write it on Hard Disk
        with open(self.photoPath, 'wb') as file:
            file.write(self.photo)

    def drawImage(self, top):
        # function takes image from database and saves it to disk. Then, it draws it on toplevel window
        sql_fetch_blob_query = "SELECT * from credentials where id = ?"
        c.execute(sql_fetch_blob_query, (self.id,))
        self.record = c.fetchall()
        for row in self.record:
            # print("Id = ", row[0], "Name = ", row[1])
            self.name  = row[1]
            self.photo = row[4]

            self.photoPath = "/home/techmirtz/projects/Python Project Sem 6/MedFixture/" + self.name + ".jpg"
            # print(self.photoPath)

            # save file to directory
            self.writeTofile()
            
            self.fileName = self.name + ".jpg"
            file_name = str(self.fileName)

            # draw image on canvas
            self.canvas = Canvas(self.left, width=120, height=120)  
            self.canvas.pack()
            self.img = ImageTk.PhotoImage(Image.open(file_name)) 
            self.canvas.create_image(0,0, anchor=NW, image=self.img)    
            self.canvas.image = self.img

            # deleteProfilePic(self.fileName)
            os.remove(self.fileName)

    def aboutMaster(self):
        about = Toplevel()
        about.geometry("480x320+360+180") 
        about.title("About")
        about.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))

        self.leftAbout = Frame(about, width=130, height=130)
        self.leftAbout.place(x=5, y=30)

        self.rightAbout = Frame(about, width=120, height=250)
        self.rightAbout.place(x=150, y=25)

        self.imgCanvas = Canvas(self.leftAbout, width=120, height=120)  
        self.imgCanvas.pack()
        self.img = PhotoImage(file="resources/icon.png") 
        self.img_sized = self.img.subsample(5,5)
        self.imgCanvas.create_image(8,8, anchor=NW, image=self.img_sized)    
        self.imgCanvas.image = self.img

        self.loginLabel = Label(self.rightAbout, text="\nThe application has been created using\ntkinter for GUI.\nThe data has been saved and accessed\nusing SQLite3.\n\nMade by:\n\n\n\n\n",\
             font=('arial 11'), fg='black')
        self.loginLabel.pack()

        self.gitProfile = Label(self.rightAbout, text="Naman Chauhan", fg='blue', font=('arial 11 underline'), cursor="hand2")
        self.gitProfile.place(x=75, y=130)
        self.gitProfile.bind("<Button-1>", lambda e: webbrowser.open("https://www.github.com/chauhannaman98"))

        self.photo = PhotoImage(file = "resources/github-100.png")
        self.photoimage = self.photo.subsample(3, 3)
        self.githubButton = Button(about, text = 'Open sourced on GitHub', image=self.photoimage, compound=LEFT, width=220, height=40,\
             bg='black', fg='white', command=lambda : webbrowser.open('https://github.com/chauhannaman98/Hospital-Management-System'))
        self.githubButton.place(x=110, y=250)

    # window to show 'What is it?'
    def whatIsIt(self):
        whatWindow = Toplevel()
        whatWindow.geometry("480x320+360+180")
        whatWindow.title("What is it?")
        whatWindow.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))

        self.imgCanvas = Canvas(whatWindow, width=120, height=120)  
        self.imgCanvas.place(x=180, y=20)
        self.img = PhotoImage(file="resources/icon.png") 
        self.img_sized = self.img.subsample(5,5)
        self.imgCanvas.create_image(8,8, anchor=NW, image=self.img_sized)    
        self.imgCanvas.image = self.img

        self.titleLabel = Label(whatWindow, text="MedFixture v1.0", font=('arial 11 bold'), fg='black')
        self.titleLabel.place(x=180, y=150)

        self.details = Label(whatWindow, text="MedFixture is your interface to book and manage appointments in your hospital's database. You just need to login with proper credentials to get access to the database and manage your appointments with ease.",\
                    font=('arial 11'), fg='black', wraplength=400, justify='center')
        self.details.place(x=40, y=180)

    # function for resetting password
    def reset_pass(self):
        resetWindow = Toplevel()
        resetWindow.geometry("480x320+360+180")
        resetWindow.title("Reset my password")
        resetWindow.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))

        tabControl = ttk.Notebook(resetWindow)        
        secret_ques = ttk.Frame(tabControl) 
        otp = ttk.Frame(tabControl) 
        
        tabControl.add(secret_ques, text ='Secret Question') 
        tabControl.add(otp, text ='Use OTP') 
        tabControl.pack(expand = 1, fill ="both") 

        self.id_label = Label(resetWindow, text="Login ID*", font=('arial 11'))
        self.id_label.place(x=40, y=50)
        self.id_label_ent = Entry(resetWindow,width=20)
        self.id_label_ent.place(x=170, y=52)

        '''''''''###Secret Question tab###'''''''''
        self.ques_label = Label(secret_ques, text="Secret Question*", font=('arial 11'))
        self.ques_label.place(x=40, y=110)

        # list of questions
        OptionList = ["What's name of your first pet dog?",
        "What's your father's middle name?",
        "What's your favorite book?"
        ]

        # OptionMenu
        self.variable = tk.StringVar(secret_ques)
        self.variable.set(OptionList[0])

        self.opt = tk.OptionMenu(secret_ques, self.variable, *OptionList)
        self.opt.config(width=30, font=('arial', 11))
        self.opt.place(x=170, y=103)
        self.ques_num = 0

        # callback method
        def callback(*args):  
            for i in range(len(OptionList)):    # assign question number to for query in the database
                if OptionList[i] == self.variable.get():
                    break

            self.ques_num = i
            print(str(self.ques_num)+": "+OptionList[i])

        self.variable.trace("w", callback)

        self.answer = Label(secret_ques, text="Your Answer*", font=('arial 11'))
        self.answer.place(x=40, y=150)

        self.answer_ent = Entry(secret_ques, width=20)
        self.answer_ent.place(x=170, y=150)

        self.new_pass = Label(secret_ques,text="New Password*", font=('arial 11'), fg='black')
        self.new_pass.place(x=40, y=190)

        self.new_pass_ent = Entry(secret_ques, width=20, show='*')
        self.new_pass_ent.place(x=170, y =190)

        # button to submit the answers
        self.submit_answer = Button(secret_ques, text="Submit", font=('arial 11'), width=12, height=2, command=self.subAnswer)
        self.submit_answer.place(x=150, y=230)

        '''''''''###OTP tab###'''''''''
        # to do:
    
    def subAnswer(self):
        self.forgetID = self.id_label_ent.get()
        self.ans = self.answer_ent.get()

        n = int(self.ques_num)
        sql_fetch_answer_query = "SELECT * FROM credentials where id = ?"
        c.execute(sql_fetch_answer_query, (self.forgetID,))
        self.record = c.fetchall()
        for row in self.record:
            self.secret_status = row[5+n*2]
            self.secret_answer = row[6+n*2]

        if self.secret_status and self.secret_answer == self.ans:
            sql_pass_update_query = "UPDATE credentials SET pass=? where id=?"
            c.execute(sql_pass_update_query, (self.new_pass_ent.get(), self.forgetID, ))
            conn.commit()
        else:
            print("Incorrect secret answer")

# def deleteProfilePic(filepath):
#     print("Deleting: "+filepath)
#     os.remove(filepath)

root = tk.Tk()
b = App(root)
root.geometry("540x380+360+180")
root.resizable(False, False)
root.title("Techmirtz Hospital Appointment Application - Login Window")
root.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))
root.bind('<Return>', b.login)

def hide_root():
    # Hide root window
    root.withdraw()

def show_root():
    # Show root window
    root.deiconify()

def exitRoot(root):
    MsgBox = tk.messagebox.askquestion('Exit Application','Do you really want to exit?', icon='warning')
    if MsgBox == 'yes':
        root.destroy()

if 'TRAVIS' in os.environ:
    root.update_idletasks()
else:
    root.mainloop()
