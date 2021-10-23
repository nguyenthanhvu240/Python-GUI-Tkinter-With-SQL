from tkinter import *
import mysql.connector
import math
import random
from tkinter import messagebox
import smtplib

#1.CONNECT TO DATABASE
mydb = mysql.connector.connect(host='localhost',user='root',password='',database='login_otp')
mycursor = mydb.cursor()
mycursor.execute("create table if not exists login_record(id int not null auto_increment primary key,name text,username text,password text,email text)")

#2.CREATE UI
root = Tk()
root.geometry('500x450')
root.title('Login Registration Form')
root.resizable(False,False)

#3.CREATE VARIABLES TO HOLD ENTRY WIDGET DATA
full_name = StringVar()
user_name = StringVar()
pass_word = StringVar()
user_name_lo = StringVar()
pass_word_lo = StringVar()
email = StringVar()
otp = StringVar()

### INSERT RECORD
def insert_record():
    count = 0
    warn = ''
    if full_name.get()=='':
        warn = 'Name can not be empty'
    else:
        count +=1

    if user_name.get()=='':
        warn = 'Username can not be empty'
    else:
        count +=1

    if email.get()=='':
        warn = 'Email can not be empty'
    else:
        count +=1
    
    if pass_word.get()=='':
        warn = 'Password can not be empty'
    else:
        count +=1

    if count == 4:
        try:
            mydb = mysql.connector.connect(host='localhost',user='root',password='',database='login_otp')
            mycursor = mydb.cursor()
            mycursor.execute('insert into login_record(name,username,password,email) values(%s,%s,%s,%s)',(
                full_name.get(),
                user_name.get(),
                pass_word.get(),
                email.get(),
            ))
            mydb.commit()
            otpVerification()
        except:
            messagebox.showerror('Error',warn)

### SELECT DATA FROM DATABASE
def login_response():
    try:
        mydb = mysql.connector.connect(host='localhost',user='root',password='',database='login_otp')
        mycursor = mydb.cursor()
        for row in mycursor.execute('select * from login_record'):
            usern = row[2]
            passwo = row[3]
    except Exception as ep:
        messagebox.showerror('',ep)
    count = 0
    if user_name_lo.get() == '':
        warn = 'Username can not be empty'
    else:
        count +=1
    
    if pass_word_lo.get() == '':
        warn = 'Password can not be empty'
    else:
        count +=1
    
    if count == 2:
        if usern == user_name_lo.get() and passwo == pass_word_lo.get():
            messagebox.showinfo('Login Status','Login Successfully!')
        else:
            messagebox.showerror('Login Status','Invalid username or password')
    else:
        messagebox.showerror('',warn)

### LOGIN
def login():
    f = Frame(root,height=450,width=500,bg='#FFBA41')
    Label(f,text='Login',font=('Helvetica',30,'bold'),bg='#FFBA41').place(x=200,y=120)
    Label(f,text='Fill all form field to go to next step',font=('Helvetica',12,'bold'),fg='#666A6C',bg='#FFBA41',).place(x=140,y=170)

    Label(f,text='Username',font=('Helvetica',12,'bold'),fg='#4C4A49',bg='#FFBA41').place(x=150,y=200)
    user = Entry(f,textvariable=user_name_lo,font=('calibre',10,'normal'),width=30)
    user.place(x=150,y=220)

    Label(f,text='Password',font=('Helvetica',12,'bold'),fg='#4C4A49',bg='#FFBA41').place(x=150,y=250)
    passw = Entry(f,textvariable=pass_word_lo,font=('calibre',10,'normal'),width=30,show='*')
    passw.place(x=150,y=250)

    Button(f,text='Log in',font=('Helvetica',15,'bold'),bg='#00B6FF',command=login_response).place(x=220,y=300)
    Label(f,text='Do not have account',font=('Helvetica',12,'bold'),fg='#666A6C',bg='#FFBA41').place(x=140,y=350)
    Button(f,text='Regist Here',font=('Helvetica',8,'bold'),bg='#FFBA41',command=registration).place(x=300,y=350)

    f.place(x=0,y=0)

### REGISTRATION    
def registration():
    f = Frame(root,height=450,width=500,bg='#FFBA41')
    Label(f,text='Registration',font=('Helvetica',30,'bold'),bg='#FFBA41').place(x=140,y=60)

    Label(f,text='Full Name :',font=('Helvetica',12,'bold'),fg='#4C4A49',bg='#FFBA41').place(x=150,y=120)
    Entry(f,textvariable=full_name,font=('calibre',10,'normal'),width=30).place(x=150,y=140)

    Label(f,text='Username :',font=('Helvetica',12,'bold'),fg='#4C4A49',bg='#FFBA41').place(x=150,y=170)
    Entry(f,textvariable=user_name,font=('calibre',10,'normal'),width=30).place(x=150,y=190)

    Label(f,text='Email :',font=('Helvetica',12,'bold'),fg='#4C4A49',bg='#FFBA41').place(x=150,y=220)
    Entry(f,textvariable=email,font=('calibre',10,'normal'),width=30).place(x=150,y=240)

    Label(f,text='Password :',font=('Helvetica',12,'bold'),fg='#4C4A49',bg='#FFBA41').place(x=150,y=270)
    Entry(f,textvariable=pass_word,font=('calibre',10,'normal'),width=30).place(x=150,y=290)

    Button(f,text='Register',font=('Helvetica',15,'bold'),fg='#00B6FF',command=insert_record).place(x=200,y=330)

    Label(f,text='I Already Have Account',font=('Helvetica',12,'bold'),fg='#4C4A49',bg='#FFBA41').place(x=120,y=380)
    Entry(f,textvariable=email,font=('calibre',10,'normal'),width=30).place(x=150,y=240)

    Button(f,text='Login Here',font=('Helvetica',8,'bold'),fg='#FFBA41',command=login).place(x=300,y=380)

    f.place(x=0,y=0)




### OTP VERIFICATION
def otpVerification():
    global OTP 
    digits = '0123456789'
    OTP = ''

    for i in range(4):
        OTP += digits[math.floor(random.random()*10)]
    print(OTP)

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('naduny123@gmail.com','naduny456@gmail.com')   #This is jsut my test mail
    subject = ' Your OTP is: '
    body = OTP

    msg = f'Subject : {subject} \n\n {body}'

    server.sendmail('naduny123@gmail.com','dung26762@gmail.com',msg)
    print('Mail has been sent')

    f = Frame(root,height=450,width=500,bg='#FFBA41')
    Label(f,text='OTP Verification',font=('Helvetica',30,'bold'),bg='#FFBA41').place(x=100,y=120)

    Label(f,text='OTP have sent,please check your email.',font=('Helvetica',12,'bold'),fg='#666A6C',bg='#FFBA41').place(x=120,y=170)

    Label(f,text='Verifi Code:',font=('Helvetica',12,'bold'),fg='#4C4A49',bg='#FFBA41').place(x=150,y=200)
    Entry(f,textvariable=otp,font=('calibre',10,'normal'),width=30).place(x=150,y=230)
    
    Button(f,text='Verify',font=('Helvetica',12,'bold'),bg='#00B6FF',command=lambda : verify(otp.get())).place(x=150,y=260)
    Button(f,text='Resend',font=('Helvetica',12,'bold'),bg='#00B6FF',command=lambda : verify(otp.get())).place(x=230,y=260)

    f.place(x=0,y=0)

### VERIFI
def verify(entryotp):
    global OTP
    if entryotp == OTP:
        messagebox.showinfo('confirmation','Record Saved')
    else :
        messagebox.showerror('Wrong','Please Enter Valid OTP')

login()


root.mainloop()

