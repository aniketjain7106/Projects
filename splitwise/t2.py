import sys
import os.path
from os import path
import ast
n=1
c=0
c1=0
while (n and c1==0):
    print("Welcome... \n1: create a group \n2: login group id \n3: exit",end="\n")
    n=int(input())
    if (n==3):
        sys.exit()
    elif (n==1):
        while True:
            groupid=input("Enter Group id ")
            password=input("enter password ")
            password1=input("confirm password ")
            if (password==password1):
                if path.exists(groupid+".txt")==True:
                    print("group id exists")
                    c=int(input("enter 1 to Login or enter 2 to Create a new group id"))
                else:
                    file = open(groupid+".txt", "w")
                    file.write(groupid+":"+password+"\n")
                    file2=open(groupid+"data"+".txt", "w")
                    print("Group id created")
                    d={}
                    np=int(input("Enter no of persons in a group "))
                    l1=[[0]*np]*np
                    for i in range (np):
                        while(True):
                            email=input("Please enter email ")
                            pass1=input("Please enter password ")
                            pass2=input("Renter password ")
                            if pass1==pass2:
                                if email not in d:
                                    d[email]=[pass1,i]
                                    break
                                else:
                                    print("email already exists")
                            else:
                                print("password do not match")
                    dat=str(d)
                    dat2=str(l1)
                    file2.write(dat2)
                    file.write(dat)
                    file.close()
                    file2.close()
                    print("Group Created")
                    c=1
                    break
            else:
                print("Passwords do NOT match!")
            if c==1:
                break
    elif (n==2):
        while True:
            c1=0
            login1=input("Please Enter Group id ")
            login2=input("Password:")
            if path.exists(login1+".txt")==True:
                f=open(login1+".txt", "r")
                file=f.readline()
                x=file.rstrip()
                if x==login1+":"+login2:
                    print("Welcome "+login1)
                    d2=f.readline()
                    d2=ast.literal_eval(d2)
                    while True:
                        em=input("Please enter username ")
                        ps=input("please enter password ")
                        if em in d2:
                            if d2[em][0]==ps:
                                print("Welcome "+em)
                                c1=1
                                break
                            else:
                                print("wrong password")
                        else:
                            print("wrong username")
                else:
                    print("Incorrect Group id Password")
                if c1==1:
                    break
            else:
                print("Incorrect Groupid username please create a group or reenter ")
        while(True):
            n1=int(input("1.Split a bill \n2.How much i owe \n3.how much others owe me \n4.Add a member \n5.exit \n"))
            f1=open(login1+"data"+".txt", "r")
            es=f1.readline()
            print(es)
            print(type(es))
            es=list(es)
            print(type(es))
            print(es)
            print(d2)
            print(type(d2[em][1]))
            print(es[d2[em][1]])
            if n1==5:
                break
            elif n1==1:
                pass     