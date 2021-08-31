from tkinter import *
from CreateGroup import *
from tkinter import messagebox
from rt import *
import mysql.connector as connector
db= connector.connect(host="localhost",user="root",password="password",port='3306',database='splitwise')
cur=db.cursor(buffered=True)

def mn(groupid,user,pasw2):
    global root,groupid2,user2,pasw,es
    s1="select name from "+str(groupid)
    cur.execute(s1)
    ind=cur.fetchall()
    es=[]
    groupid2=groupid
    user2=user
    pasw=pasw2
    for k in ind:
        es.append(k[0])
    root=rt("Main Page")
    submitbtn = Button(root, text ="Split a bill",bg ='blue')
    submitbtn.place(x = 50, y = 20, width = 150)
    
    submitbtn = Button(root, text ="View Balance",bg ='blue',command=vb)
    submitbtn.place(x = 50, y = 50, width = 150)

    submitbtn = Button(root, text ="Settla a Bill",bg ='blue')
    submitbtn.place(x = 50, y = 80, width = 150)

    submitbtn = Button(root, text ="Add a member",bg ='blue',command=am)
    submitbtn.place(x = 50, y = 110, width = 150)

    submitbtn = Button(root, text ="Take a loan",bg ='blue')
    submitbtn.place(x = 50, y = 140, width = 150)

    submitbtn = Button(root, text ="Change id and password",bg ='blue',command=cip)
    submitbtn.place(x = 50, y = 170, width = 150)

    submitbtn = Button(root, text ="Leave Group",bg ='blue',command=leave)
    submitbtn.place(x = 50, y = 200, width = 150)

    submitbtn = Button(root, text ="Logout",bg ='blue',command=logout)
    submitbtn.place(x = 50, y = 230, width = 150)
    
    root.mainloop()

def logout():
    root.destroy()

def vb():
    root1=rt("View Balance")
    i=1
    for k in es:
        if k!=user2:
            s1="select "+k+" from "+groupid2+" where name ='"+user2+"'"
            cur.execute(s1)
            dat=cur.fetchall()
            if float(dat[0][0])<0:
                lblfrstrow = Label(root1, text =("I owe "+k+str(float(dat[0][0])*-1)+"rs"), )
                lblfrstrow.place(x = 50, y = i*2*10)
            else:
                lblfrstrow = Label(root1, text =(k+" owe me "+dat[0][0]+"rs"), )
                lblfrstrow.place(x = 50, y = i*2*10)
            i+=1
    
    submitbtn = Button(root1, text ="ok",bg ='blue',command=root1.destroy)
    submitbtn.place(x = 150, y = 135, width = 55)

def leave():
    s1="select * from "+groupid2+" where name='"+user2+"'"
    cur.execute(s1)
    dat=cur.fetchall()
    l12=[]
    dat=dat[0][1:]
    flag=0
    for k in dat:
        if float(k)!=0:
            messagebox.showerror("showerror", "Please settle your bill first")
            root.lift()
            flag=1
            break
    if flag==0:
        messagebox.showinfo("showinfo", "You are removed")
        root.lift()
        s1="alter table "+groupid2+" drop column "+user2
        cur.execute(s1)
        s1="delete from personid where id='"+user2+"'"
        cur.execute(s1)
        s1="delete from "+groupid2+" where name ='"+user2+"'"
        cur.execute(s1)
        db.commit()
        root.destroy()
    
def am():
    def submitact():
        u=Username.get()
        p1=password.get()
        p2=password2.get()
        if p1==p2:
            if u in es:
                messagebox.showerror("showerror", "id already exist please enter another id")
                Username.delete(0,END)
                password2.delete(0,END)
                password.delete(0,END)
                root1.lift()
            else:
                s1="insert into personid (id,password,groupid) values ('"+u+"','"+p1+"','"+groupid2+"')"
                cur.execute(s1)
                s1="insert into "+groupid2+" (name) values ('"+u+"')"
                cur.execute(s1)
                s1="ALTER TABLE "+groupid2+" ADD "+u+" varchar(20) default 0"
                cur.execute(s1)
                db.commit()
                messagebox.showinfo("showinfo", "Memeber added")
                root1.destroy()
                root.lift()
        else:
            messagebox.showerror("showerror", "Password doesn't match")
            Username.delete(0,END)
            password2.delete(0,END)
            password.delete(0,END)
            root1.lift()

    global Username,password,password2
    root1=rt("Add a memeber")
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

def cip():
    def submit1():
        if Username1.get()==Username2.get():
            pass
        else:
            messagebox.showerror("showerror", "Usename doesn't match")
            root4.lift()
            Username1.delete(0,END)
            Username2.delete(0,END)

    def submit2():
        if password21.get()==password22.get():
            s1="update personid set password='"+password22.get()+"' where password='"+user2+"'"
            messagebox.showinfo("showinfo", "password change successfully please login again")
            print(s1)
            cur.execute(s1)
            db.commit()
            pasw=password22.get()
            root5.destroy()
            root3.destroy()
            root.destroy()
        else:
            messagebox.showerror("showerror", "Password doesn't match")
            password21.delete(0,END)
            password22.delete(0,END)
            root5.lift()

    def cu():
        global Username1,Username2,root4
        root4=rt("Change username")
        lblfrstrow1 = Label(root4, text ="Username -", )
        lblfrstrow1.place(x = 50, y = 20)
        
        Username1 = Entry(root4, width = 35)
        Username1.place(x = 150, y = 20, width = 100)
        Username1.icursor(0)
        Username1.bind("<Return>",lambda func1:Username2.focus())

        lblfrstrow2 = Label(root4, text ="Renter Username -", )
        lblfrstrow2.place(x = 50, y = 50)
        
        Username2 = Entry(root4, width = 35)
        Username2.place(x = 150, y = 50, width = 100)
        Username2.icursor(0)
        Username2.bind("<Return>",lambda func1:submit1())

        submitbtn = Button(root4, text ="Submit",bg ='blue', command = submit1)
        submitbtn.place(x = 150, y = 135, width = 55)
        root4.mainloop()

    def cp():
        global password21,password22,root5
        root5=rt("Change password")
        lblthirdrow1 = Label(root5, text ="Enter Password-")
        lblthirdrow1.place(x = 50, y = 50)
        
        password21 = Entry(root5, width = 35,show="*")
        password21.place(x = 150, y = 50, width = 100)
        password21.bind("<Return>",lambda func1:password22.focus())

        lblthirdrow = Label(root5, text ="Renter Password-")
        lblthirdrow.place(x = 50, y = 80)
        
        password22 = Entry(root5, width = 35,show="*")
        password22.place(x = 150, y = 80, width = 100)
        password22.bind("<Return>",lambda func1:submit2())

        submitbtn = Button(root5, text ="Submit",bg ='blue', command = submit2)
        submitbtn.place(x = 150, y = 135, width = 55)

    def check():
        global root3
        pasw22=password.get()
        if pasw22==pasw:
            root2.destroy()
            root3=rt("Change id and password")
            submitbtn1 = Button(root3, text ="Change Username",bg ='blue', command = cu)
            submitbtn1.place(x = 50, y = 135, width = 155)
            submitbtn2 = Button(root3, text ="Change Password",bg ='blue', command = cp)
            submitbtn2.place(x = 50, y = 165, width = 155)
            root3.mainloop()
        else:
            messagebox.showerror("showerror", "Password doesn't match")
            password.delete(0,END)
            root2.lift()

    root2=rt("Enter password")
    lblthirdrow = Label(root2, text ="Enter your userid Password-")
    lblthirdrow.place(x = 50, y = 80)
    password = Entry(root2, width = 35,show="*")
    password.place(x = 150, y = 50, width = 100)
    password.bind("<Return>",lambda func1:check())

    submitbtn = Button(root2, text ="Submit",bg ='blue', command = check)
    submitbtn.place(x = 150, y = 135, width = 55)
    
    root2.mainloop()
    