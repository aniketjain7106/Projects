from tkinter import *
from functools import partial
from tkinter import messagebox
from LoginGroup import *
from CreateGroup import *
import mysql.connector as connector
db= connector.connect(host="localhost",user="root",password="password",port='3306',database='splitwise')
cur=db.cursor(buffered=True)
def cg2():
    print("asnigej")
    global t
    root2 = rt("Enter no of memebers")

    lblfrstrow = Label(root2, text ="Enter no of users")
    lblfrstrow.place(x = 50, y = 20)
    
    nu = Entry(root2, width = 35)
    nu.place(x = 150, y = 20, width = 100)
    t=nu.get()
    nu.focus()
    nu.bind("<Return>",lambda func1:nou())
    print(t)
    
    submitbtn = Button(root2, text ="Submit",bg ='blue',command=nou)
    submitbtn.place(x = 150, y = 135, width = 55)
    root2.destroy()
def login2(user,passw):
    try:
        s1="insert into "+str(userg)+" (name) values ('"+str(user)+"')"
        cur.execute(s1)
        print(s1)
        s1="insert into personid (id,password,groupid) values (%s,%s,%s)"
        b1=(user,passw,userg)
        cur.execute(s1,b1)
        s1="ALTER TABLE "+str(userg)+" ADD "+str(user)+" varchar(20) default 0"
        cur.execute(s1)
        x=1
        db.commit()
        messagebox.showinfo("showinfo", "Person id Created")
    except:
        messagebox.showerror("showerror", "Person id already exist")
        personid.delete(0,END)
        pas.delete(0,END)
        pas2.delete(0,END)
        x=0
        root3.destroy()
def nou():
    global i,x
    x=0
    i=0
    def sub2():
        if pas.get()==pas2.get():
            login2(personid.get(),pas.get())
        else:
            messagebox.showerror("showerror", "Password Doesn't Match")
            personid.delete(0,END)
            pas.delete(0,END)
            pas2.delete(0,END)
            x=0
            root3.destroy()
    
    while(i!=t):
        global personid,pas,pas2,root3
        root3=rt("Enter no of persons")
        lblfrstrow = Label(root3, text ="Username -")
        lblfrstrow.place(x = 50, y = 20)
        
        personid = Entry(root3, width = 35)
        personid.place(x = 150, y = 20, width = 100)
        personid.focus()
        personid.bind("<Return>",lambda func1:password.focus())
        
        lblsecrow = Label(root3, text ="Password -")
        lblsecrow.place(x = 50, y = 50)
        
        pas = Entry(root3, width = 35,show="*")
        pas.place(x = 150, y = 50, width = 100)
        pas.bind("<Return>",lambda func1:password2.focus())

        lblthirdrow = Label(root3, text ="Renter Password-")
        lblthirdrow.place(x = 50, y = 80)
        
        pas2 = Entry(root3, width = 35,show="*")
        pas2.place(x = 150, y = 80, width = 100)
        pas2.bind("<Return>",lambda func1:sub2)
        
        submitbtn = Button(root3, text ="Submit",bg ='blue', command = sub2)
        submitbtn.place(x = 150, y = 135, width = 55)

        if x==1:
            i+=1
    root3.destroy()