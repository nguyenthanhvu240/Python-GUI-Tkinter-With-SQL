import mysql.connector
from tkinter import *

def create_db():
    conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys")
    mycursor = conn.cursor()
    #mycursor.execute("drop table course")
    mycursor.execute("create table if not exists course(cid INTEGER auto_increment,PRIMARY KEY(cid),name text,duration text,charges text,description text)")
    conn.commit()

    mycursor.execute("create table if not exists student(roll integer primary key auto_increment,name text,email text,gender text,dob text,contact text,addmission text,course text,state text,city text,pin text,address text)")
    conn.commit()

    mycursor.execute("create table if not exists result(rid integer primary key auto_increment,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    conn.commit()

create_db()

