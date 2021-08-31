from tkinter import *
from CreateGroup import *
from tkinter import messagebox
from rt import *
from main2 import *
import mysql.connector as connector
db= connector.connect(host="localhost",user="root",password="password",port='3306',database='splitwise')
cur=db.cursor(buffered=True)
def lgp():
    s1="select id from groupid where id=%s"
    cur.execute(s1,(userg,))
    re=cur.fetchone()
    if re==None:
        root1.destroy()
        messagebox.showerror("showerror", "Enter Valid Groupid")
        lg()
    elif re[0]==userg:
        s1="select * from groupid where id=%s and password=%s"
        cur.execute(s1,(userg,passw,))
        re=cur.fetchone()
        if re==None:
            root1.destroy()
            messagebox.showerror("showerror", "Enter correct password")
            lg()
        elif re[0]==userg and re[1]==passw:
            root1.destroy()
            lg2()
def lg():
    global root1
    def submitact():
        global userg,passw
        userg = Username.get()
        passw = password.get()
        lgp()
        
    root1=rt("login group")

    lblfrstrow = Label(root1, text ="Group id -", )
    lblfrstrow.place(x = 50, y = 20)
    
    Username = Entry(root1, width = 35)
    lambda func1:Username.focus()
    Username.place(x = 150, y = 20, width = 100)
    Username.bind("<Return>",lambda func1:password.focus())
    
    lblsecrow = Label(root1, text ="Password -")
    lblsecrow.place(x = 50, y = 50)
    
    password = Entry(root1, width = 35,show="*")
    password.place(x = 150, y = 50, width = 100)
    password.bind("<Return>",lambda func1:submitact())

    submitbtn = Button(root1, text ="Submit",bg ='blue', command = submitact)
    submitbtn.place(x = 150, y = 135, width = 55)
    
    root1.mainloop()

def lg2():
    global root2
    def submitact1():
        global userg2,passw2
        userg2 = Username.get()
        passw2 = password.get()
        lgp2()
        
    root2=rt("Login Username")

    lblfrstrow = Label(root2, text ="Username -", )
    lblfrstrow.place(x = 50, y = 20)
    
    Username = Entry(root2, width = 35)
    lambda func1:Username.focus()
    Username.place(x = 150, y = 20, width = 100)
    Username.bind("<Return>",lambda func1:password.focus())
    
    lblsecrow = Label(root2, text ="Password -")
    lblsecrow.place(x = 50, y = 50)
    
    password = Entry(root2, width = 35,show="*")
    password.place(x = 150, y = 50, width = 100)
    password.bind("<Return>",lambda func1:submitact1())

    submitbtn = Button(root2, text ="Submit",bg ='blue', command = submitact1)
    submitbtn.place(x = 150, y = 135, width = 55)
    
    root2.mainloop()

def lgp2():
    s1="select id from personid where id=%s and groupid=%s"
    cur.execute(s1,(userg2,userg,))
    re=cur.fetchone()
    if re==None:
        messagebox.showerror("showerror", "Enter Valid Email")
        root2.destroy()
        lg2()
    elif re[0]==userg2:
        s1="select * from personid where id=%s and password=%s"
        cur.execute(s1,(userg2,passw2,))
        re=cur.fetchone()
        if re==None:
            messagebox.showerror("showerror", "Enter Correct password")
            root2.destroy()
            lg2()
        elif re[0]==userg2 and re[1]==passw2:
            messagebox.showinfo("showinfo", "Successfully login")
            root2.destroy()
            mn(userg,userg2,passw2)