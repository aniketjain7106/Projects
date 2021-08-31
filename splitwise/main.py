from tkinter import *
from sys import *
from CreateGroup import *
from LoginGroup import *
from rt import *
import mysql.connector as connector
db= connector.connect(host="localhost",user="root",password="password",port='3306',database='splitwise')
cur=db.cursor(buffered=True)
def exi():
    exit()
win=rt("Splitwise")

label1=Label(win,text="Splitwise\nWelcome to splitwise")
label1.place(x = 50, y = 0)

b = Button(win, text ="Create Group", command = cg)
b.place(x = 50, y = 40, width = 100)
b1 = Button(win, text ="Login Group", command = lg)
b1.place(x = 50, y = 70, width = 100)
b2 = Button(win, text ="Exit", command = exi)
b2.place(x = 50, y = 100, width = 100)
win.mainloop()