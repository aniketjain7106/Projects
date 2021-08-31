import mysql.connector as connector
db= connector.connect(
  host="localhost",
  user="root",
  password="password",
  port='3306',
  database='splitwise'
)
cur=db.cursor()
print("Welcome To Splitwise")
n=1
while n:
  n=int(input("Welcome... \n1: create a group \n2: login group id \n0: exit\n"))
  if n==0:
    pass
  elif n==1:
    x=1
    while x:
      t=input("Enter group id ")
      p=input("Enter password ")
      p1=input("Renenter Password ")
      if p1==p:
        s="insert into groupid (id,password) values (%s,%s)"
        b=(t,p)
        try:
          cur.execute(s,b)
          db.commit()
          print("groupid Succesfully created")
          s1="Create table %s (name varchar(20))"
          b1=(t+"es")
          cur.execute(s1,b1)
          np=int(input("enter no of persons in the group "))
          for i in range(np):
            x1=1
            while x1:
              t1=input("Enter mail id of person "+str(i+1)+" ")
              ps1=input("Enter password ")
              ps2=input("Renter Password ")
              s1="insert into %s (name) values (%s)"
              b4=(b1,t1)
              cur.execute(s1,b4)
              db.commit()
              if ps1==ps1:
                s1="insert into personid (id,password,groupid) values (%s,%s,%s)"
                b1=(t1,ps1,t)
                try:
                  cur.execute(s1,b1)
                  db.commit()
                  for i in range (np):
                    s1="ALTER TABLE %s ADD %s varchar(20) default 0"
                    b3=(b1,t1)
                    cur.execute(s1,b1)
                    db.commit()
                  x1=0
                except:
                  print("Id already exists")
                  print("Please renter id again")
          x=0
        except:
          print("Groupid already exists")
          x=int(input("0.Login  1.Renter Group id "))
      else:
        print("Password doesn't match")
  elif n==2:
    x2=1
    while x2:
      em1=input("Enter group id ")
      psd1=input("Enter password ")
      s1="select id from groupid where id=%s"
      cur.execute(s1,(em1,))
      re=cur.fetchone()
      if re==None:
        print("Enter Valid Groupid")
      elif re[0]==em1:
        s1="select * from groupid where id=%s and password=%s"
        cur.execute(s1,(em1,psd1,))
        re=cur.fetchone()
        if re==None:
          print("Enter correct password")
        elif re[0]==em1 and re[1]==psd1:
          x3=1
          while x3:
            id1=input("Enter email ")
            pse1=input("Enter Password ")
            s1="select id from personid where id=%s"
            cur.execute(s1,(id1,))
            re=cur.fetchone()
            if re==None:
              print("Enter Valid Email")
            elif re[0]==id1:
              s1="select * from personid where id=%s and password=%s"
              cur.execute(s1,(id1,pse1,))
              re=cur.fetchone()
              if re==None:
                print("Enter Correct Password") 
              elif re[0]==id1 and re[1]==pse1:
                x2=0
                print("welcome "+str(id1)) 
                x3=0               
    print("Hola")
    n1=input("1.split a bill \n2. view balance \n3.Add a member \n4.exit ")
    if n1==1:
      pass