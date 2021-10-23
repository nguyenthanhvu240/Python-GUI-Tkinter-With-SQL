from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox

from mysql.connector.fabric.connection import MODE_READONLY
from create_db import create_db
import mysql.connector


class studentClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()     #<<< ko move dc window

        #=====TITLE=====
        title = Label(self.root,text="Manage Student Details",font=("goudy old  style",20,"bold"),bg="#033054",fg="lightyellow").place(x=10,y=15,width=1180,height=35)

        #=====Varibles=====
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        


        #=====WIDGETS=====
            #=====column 1=====
        lbl_roll = Label(self.root,text="Roll No:",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_name = Label(self.root,text="Name:",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_email = Label(self.root,text="Email:",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_gender = Label(self.root,text="Gender:",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

        lbl_state = Label(self.root,text="State:",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        txt_state = Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_state.place(x=150,y=220,width=150)

        lbl_city = Label(self.root,text="City:",font=("goudy old style",15,"bold"),bg="white").place(x=310,y=220)
        txt_city = Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_city.place(x=380,y=220,width=100)

        lbl_pin = Label(self.root,text="Pin:",font=("goudy old style",15,"bold"),bg="white").place(x=490,y=220)
        txt_pin = Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_pin.place(x=570,y=220,width=80)


        lbl_addr = Label(self.root,text="Address:",font=("goudy old style",15,"bold"),bg="white")
        lbl_addr.place(x=10,y=260)
            #=====colum2 =====
        lbl_dob = Label(self.root,text="D.O.B:",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=60)
        lbl_cont = Label(self.root,text="Contact:",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=100)
        lbl_addmission = Label(self.root,text="Addmission:",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=140)
        lbl_course = Label(self.root,text="Course:",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=180)


        #=====ENTRY=====
            #=====entry 1=====
        self.txt_roll = Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_roll.place(x=150,y=60,width=200)
        txt_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        txt_email = Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_gender = ttk.Combobox(self.root,textvariable=self.var_gender,value=["Select","Male","Female","Other"],font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.current(0)

        self.txt_address = Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=150,y=260,width=500,height=100)
            #=====entry 2=====
        txt_dob = Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg="lightyellow")
        txt_dob.place(x=480,y=60,width=170)
        txt_contact = Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=480,y=100,width=170)
        txt_addmission= Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=480,y=140,width=170)
            #=====COURSE LIST=====
        self.course_List = []
        self.fetch_course()
        self.txt_course = ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_List,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_course.place(x=480,y=180,width=170)
        self.txt_course.set("Select")
        
        #=====BUTTON=====
        self.btn_add = Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update = Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete = Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear = Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #=====SEARCH PANEL=====
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root,text="Roll No:",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_roll = Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        self.btn_search = Button(self.root,text="Search:",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        self.btn_search.place(x=1070,y=60,width=120,height=28)

        #=====CONTENT=====
        self.c_frame = Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=470,height=340)

        #=====SCROLL BARS=====
        scrolly = Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx = Scrollbar(self.c_frame,orient=HORIZONTAL)


        #=====COURSE TABLE=====
        self.courseTable = ttk.Treeview(self.c_frame,columns=("roll","name","email","gender","dob","contact","addmission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        #=====SCROLL BARS PACK and CONFIG VIEW=====
        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command=self.courseTable.xview)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("roll",text="Roll No")
        self.courseTable.heading("name",text="Name")
        self.courseTable.heading("email",text="Email")
        self.courseTable.heading("gender",text="Gender")
        self.courseTable.heading("dob",text="DoB")
        self.courseTable.heading("contact",text="Contact")
        self.courseTable.heading("addmission",text="Addmission")
        self.courseTable.heading("course",text="Course")
        self.courseTable.heading("state",text="State")
        self.courseTable.heading("city",text="City")
        self.courseTable.heading("pin",text="Pin")
        self.courseTable.heading("address",text="Address")

        self.courseTable['show'] = 'headings'

        self.courseTable.column("roll",width=100)
        self.courseTable.column("name",width=100)
        self.courseTable.column("email",width=100)
        self.courseTable.column("gender",width=100)
        self.courseTable.column("dob",width=100)
        self.courseTable.column("contact",width=100)
        self.courseTable.column("addmission",width=100)
        self.courseTable.column("course",width=100)
        self.courseTable.column("state",width=100)
        self.courseTable.column("city",width=100)
        self.courseTable.column("pin",width=100)
        self.courseTable.column("address",width=100)


        self.courseTable.pack(fill=BOTH,expand=1)
        self.courseTable.bind("<ButtonRelease-1>",self.get_date)
        self.show()
        #self.fetch_course()


    #=====SEARCH COURSE======
    def search(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:    
            mycursor.execute("select * from student where roll=%s",(self.var_search.get(),))    #   << co phay
            #f{}<< must have this to format '{%%}'
            myrow = mycursor.fetchone()
            if myrow != None:
                self.courseTable.delete(*self.courseTable.get_children())                
                self.courseTable.insert('',END,values=myrow)
            else:
                messagebox.showerror("Error","No Record Founded",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")            


    #=====UPDATE=====
    def update(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No should be required",parent=self.root)
            else:
                mycursor.execute("select * from student where roll=%s",(self.var_roll.get(),))                
                #@param name = %s,not = ?
                myrow = mycursor.fetchone()
                if myrow==None:
                    messagebox.showerror("Error","Select Student From List",parent=self.root)
                else:
                    mycursor.execute("update student set name = %s,email= %s,gender= %s,dob= %s,contact= %s,addmission= %s,course= %s,state= %s,city= %s,pin= %s,address= %s where roll=%s",(                        
                        self.var_name.get(),
                        self.var_email.get(),
                        self.txt_gender.get(),   
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get(),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Student Update Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    #======DELETE=====
    def delete(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No should be required",parent=self.root)
            else:
                mycursor.execute("select * from student where roll=%s",(self.var_roll.get(),))                
                #@param name = %s,not = ?
                myrow = mycursor.fetchone()
                if myrow==None:
                    messagebox.showerror("Error","Select Student From The List",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want delete this Course?",parent=self.root)
                    if op == TRUE:
                        mycursor.execute("delete from student where roll=%s",(self.var_roll.get(),))
                        conn.commit()
                        messagebox.showinfo("Deleted","Student Delete Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

    #=====CLICK TO SHOW=====
    def get_date(self,ev):
        self.txt_roll.config(state="readonly")
        r=self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content['values']
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.txt_gender.set(row[3]),   
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0",END),  
        self.txt_address.insert(END,row[11])     

    ''' self.var_roll.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete("1.0",END)
        self.txt_description.insert(END,row[4])'''

    #=====FETCH COURSE=====
    def fetch_course(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:    
            mycursor.execute("select name from course")
            myrow = mycursor.fetchall()
            #v=[]
            if len(myrow) > 0:
                for row in myrow:
                    #v.append(row[0])
                    self.course_List.append(row[0])
            #print(v)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")            


    #======ADD COURSE========
    def add(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll number should be required",parent=self.root)
            else:
                mycursor.execute("select * from student where roll=%s",(self.var_roll.get(),))                
                #@param name = %s,not = ?
                myrow = mycursor.fetchone()
                if myrow!=None:
                    messagebox.showerror("Error","Roll No already present",parent=self.root)
                else:
                    mycursor.execute("insert into student(roll,name,email,gender,dob,contact,addmission,course,state,city,pin,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.txt_gender.get(),   
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    #=====SHOW COURSE======
    def show (self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:    
            mycursor.execute("select * from student")
            myrow = mycursor.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in myrow:
                self.courseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")            

    #=====CLEAR======
    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.txt_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("Select"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0",END),  
        self.txt_gender.config(state=NORMAL)
        self.var_search.set("")
        
if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()