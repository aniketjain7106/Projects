import mysql.connector as connector
db= connector.connect(host="localhost",user="root",password="password",port='3306',database='splitwise')
cur=db.cursor(buffered=True)
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
        try:
          s="insert into groupid (id,password) values (%s,%s)"
          b=(t,p)
          cur.execute(s,b)
          db.commit()
          print("groupid Succesfully created")
          s1="Create table "+str(t)+" (name varchar(20) unique)"
          cur.execute(s1)
          np=int(input("enter no of persons in the group "))
          for i in range(np):
            x1=1
            while x1:
              t1=input("Enter mail id of person "+str(i+1)+" ")
              ps1=input("Enter password ")
              ps2=input("Renter Password ")
              if ps1==ps2:
                try:
                  s1="insert into "+str(t)+" (name) values ('"+str(t1)+"')"
                  cur.execute(s1)
                  s1="insert into personid (id,password,groupid) values (%s,%s,%s)"
                  b1=(t1,ps1,t)
                  cur.execute(s1,b1)
                  s1="ALTER TABLE "+str(t)+" ADD "+str(t1)+" varchar(20) default 0"
                  cur.execute(s1)
                  db.commit()
                  x1=0
                except:
                  print("Id already exists")
                  print("Please renter id again")
              else:
                print("Password Doesn't match")
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
            s1="select id from personid where id=%s and groupid=%s"
            cur.execute(s1,(id1,em1,))
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
    c1=1
    while c1:
      n1=int(input("1. Split a bill \n2. View balance \n3. Settle bill\n4. Add a memeber\n5. Take a Loan\n6. Change id and Password\n7. Leave Group\n8. Exit "))
      s1="select name from "+str(em1)
      cur.execute(s1)
      ind=cur.fetchall()
      es=[]
      for k in ind:
        es.append(k[0])
      if n1==1:
        sb=int(input("1. Split bill equally\n2. Split bill among particular persons\n3. Exit "))
        if sb==1:
          c2=1
          while c2:
            am=int(input("Please Enter Total amount "))
            pe=input("Who is paying the bill ")
            am1=am/4
            if pe in es:
              for k in ind:
                if k[0]==pe:
                  s1="update "+(em1)+" set "+(k[0])+"="+(k[0])+"-"+str(am1)+" where name<> '"+str(pe)+"'"
                  cur.execute(s1)
                  db.commit()
                else:
                  s1="update "+(em1)+" set "+(k[0])+"="+(k[0])+"+"+str(am1)+" where name= '"+str(pe)+"'"
                  cur.execute(s1)
                  db.commit()
              c2=0
            else:
              print("Enter right name")
        elif n==3:
          break
      elif n1==2:
        for k in es:
          if k!=id1:
            s1="select "+k+" from "+em1+" where name ='"+id1+"'"
            cur.execute(s1)
            dat=cur.fetchall()
            if float(dat[0][0])<0:
              print("I owe "+k,float(dat[0][0])*-1,"rs")
            else:
              print(k+" owe me ",dat[0][0],"rs")
      elif n1==4:
        n11=int(input("1. Add a Member\n2. Delete a member "))
        if n11==1:
          c3=1
          while c3:
            mem1=input("Enter Name of the member ")
            pas1=input("Please enter password ")
            pas2=input("renter Password ")
            if pas1==pas2:
              if mem1 in es:
                print("id already exist please enter another id")
              else:
                s1="insert into personid (id,password,groupid) values ('"+mem1+"','"+pas1+"','"+em1+"')"
                cur.execute(s1)
                s1="insert into "+em1+" (name) values ('"+mem1+"')"
                cur.execute(s1)
                s1="ALTER TABLE "+em1+" ADD "+mem1+" varchar(20) default 0"
                cur.execute(s1)
                db.commit()
                c3=0
            else:
              print("Password doesnt match")
      elif n1==6:
        n12=int(input("1. Change Id\n2. Change Password "))
        c4=1
        while c4:
          ps34=input("Enter your password ")
          if ps34==pse1:
            if n12==1:
              name1=input("Enter username ")
              s1="update personid set id='"+name1+"' where id='"+id1+"'"
              cur.execute(s1)
              s1="update "+em1+" set name='"+name1+"' where name='"+id1+"'"
              cur.execute(s1)
              s1="alter table "+em1+" rename column "+id1+" to "+name1
              cur.execute(s1)
              db.commit()
              print("Username change successfully")
            elif n12==2:
              name12=input("Enter your new password ")
              s1="update personid set password='"+name12+"' where password='"+ps34+"'"
              print("password change successfully")
              cur.execute(s1)
              db.commit()
            c4=0
          else:
            print("Password incorrect reneter your password")
      elif n1==7:
        s1="select * from "+em1+" where name='"+id1+"'"
        cur.execute(s1)
        dat=cur.fetchall()
        l12=[]
        dat=dat[0][1:]
        flag=0
        for k in dat:
          if float(k)!=0:
            print("Please settle your bill First")
            flag=1
            break
        if flag==0:
          print("removing you")
          s1="alter table "+em1+" drop column "+id1
          cur.execute(s1)
          s1="delete from personid where id='"+id1+"'"
          cur.execute(s1)
          s1="delete from "+em1+" where name ='"+id1+"'"
          cur.execute(s1)
          db.commit()
      elif n1==8:
        c1=0
      elif n1==5:
        nam=input("From whom to take loan")
        amo=float(input("Enter amount of loan"))
          