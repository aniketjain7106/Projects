from re import I
from tkinter import *
from rt import *
from functools import partial
from tkinter import messagebox
from LoginGroup import *
import mysql.connector as connector
db= connector.connect(host="localhost",user="root",password="password",port='3306',database='splitwise')
cur=db.cursor(buffered=True)


def login1(user,passw):
    try:
        s="insert into groupid (id,password) values ('"+str(user)+"','"+str(passw)+"')"
        print(s)
        cur.execute(s)
        db.commit()
        s1="Create table "+str(user)+" (name varchar(20) unique)"
        print(s1)
        cur.execute(s1)
        db.commit()
        root1.destroy()
        messagebox.showinfo("showinfo", "Group id Created")
        cg2()
    except:
        messagebox.showerror("showerror", "Group id already exist")
        Username.delete(0,END)
        password.delete(0,END)
        password2.delete(0,END)
        root1.destroy()
        cg()

def cg():
    def submitact():
        global userg
        userg = Username.get()
        passw = password.get()
        passw2=password2.get()
        if passw==passw2:
            login1(userg,passw)
        else:
            messagebox.showerror("showerror", "Password Doesn't Match")
            Username.delete(0,END)
            password.delete(0,END)
            password2.delete(0,END)
            root1.destroy()
            cg()

    global root1,Username,password,password2
    root1 = rt("Create Page")
    
    lblfrstrow = Label(root1, text ="Username -", )
    lblfrstrow.place(x = 50, y = 20)
    
    Username = Entry(root1, width = 35)
    Username.place(x = 150, y = 20, width = 100)
    Username.icursor(0)
    Username.bind("<Return>",lambda func1:password.focus())
    
    lblsecrow = Label(root1, text ="Password -")
    lblsecrow.place(x = 50, y = 50)
    
    password = Entry(root1, width = 35,show="*")
    password.place(x = 150, y = 50, width = 100)
    password.bind("<Return>",lambda func1:password2.focus())

    lblthirdrow = Label(root1, text ="Renter Password-")
    lblthirdrow.place(x = 50, y = 80)
    
    password2 = Entry(root1, width = 35,show="*")
    password2.place(x = 150, y = 80, width = 100)
    password2.bind("<Return>",lambda func1:submitact())
    
    submitbtn = Button(root1, text ="Submit",bg ='blue', command = submitact)
    submitbtn.place(x = 150, y = 135, width = 55)
    
    root1.mainloop()

def cg2():
    global nu,root2
    
    root2 = rt("Enter no of memebers")

    lblfrstrow = Label(root2, text ="Enter no of users")
    lblfrstrow.place(x = 50, y = 20)
    
    nu = Entry(root2, width = 35)
    nu.focus()
    nu.place(x = 150, y = 20, width = 100)
    
    nu.focus()
    nu.bind("<Return>",lambda func1:nou())
    
    submitbtn = Button(root2, text ="Submit",bg ='blue',command=nou)
    submitbtn.place(x = 150, y = 135, width = 55)
    root2.mainloop()

def nou():
    global cnt
    global t
    t=nu.get()
    t=int(t)
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
            db.commit()
            messagebox.showinfo("showinfo", "Person id Created")
            personid.delete(0,END)
            pas.delete(0,END)
            pas2.delete(0,END)
            root3.cnt+=1
            personid.focus()
            root3.lift()
            if t==root3.cnt:
                messagebox.showinfo("showinfo", "All id Created please login")
                root3.destroy()
        except:
            messagebox.showerror("showerror", "Person id already exist")
            personid.delete(0,END)
            pas.delete(0,END)
            pas2.delete(0,END)
            personid.focus()
            root3.lift()
    def sub2():
        if pas.get()==pas2.get():
            login2(personid.get(),pas.get())
        else:
            messagebox.showerror("showerror", "Password Doesn't Match")
            personid.delete(0,END)
            pas.delete(0,END)
            pas2.delete(0,END)
            personid.focus()
            root3.lift()
        return
    
    global personid,pas,pas2,root3
    root3=rt("Enter personid and password")
    root3.cnt=0
    lblfrstrow = Label(root3, text ="Username -"+str(root3.cnt+1))
    lblfrstrow.place(x = 50, y = 20)
    
    personid = Entry(root3, width = 35)
    personid.place(x = 150, y = 20, width = 100)
    personid.focus_set()
    personid.bind("<Return>",lambda func1:pas.focus())
    
    lblsecrow = Label(root3, text ="Password -")
    lblsecrow.place(x = 50, y = 50)
    
    pas = Entry(root3, width = 35,show="*")
    pas.place(x = 150, y = 50, width = 100)
    pas.bind("<Return>",lambda func1:pas2.focus())

    lblthirdrow = Label(root3, text ="Renter Password-")
    lblthirdrow.place(x = 50, y = 80)
    
    pas2 = Entry(root3, width = 35,show="*")
    pas2.place(x = 150, y = 80, width = 100)
    pas2.bind("<Return>",lambda func1:sub2())
    
    submitbtn = Button(root3, text ="Submit",bg ='blue', command = sub2)
    submitbtn.place(x = 150, y = 135, width = 55)

    root3.mainloop()
    