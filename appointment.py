# import modules
from tkinter import *
import sqlite3

# connect to the databse.
conn = sqlite3.connect('database.db')
print("Successfully connected")
print(conn)