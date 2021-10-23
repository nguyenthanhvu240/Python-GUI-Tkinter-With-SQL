from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox

import mysql.connector


class CourseClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()     #<<< ko move dc window

        #=====TITLE=====
        title = Label(self.root,text="Manage Course Details",font=("goudy old  style",20,"bold"),bg="#033054",fg="lightyellow").place(x=10,y=15,width=1180,height=35)

        #=====Varibles=====
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()


        #=====WIDGETS=====
        lbl_courseName = Label(self.root,text="Course Name:",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_duration = Label(self.root,text="Duration:",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_charges = Label(self.root,text="Charges:",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_description = Label(self.root,text="Description:",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)

        #=====ENTRY=====
        self.txt_courseName = Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_courseName.place(x=150,y=60,width=200)
        txt_duration = Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        txt_charges = Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_description = Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_description.place(x=150,y=180,width=500,height=100)

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
        lbl_search_courseName = Label(self.root,text="Course Name:",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_courseName = Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        self.btn_search = Button(self.root,text="Search:",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        self.btn_search.place(x=1070,y=60,width=120,height=28)

        #=====CONTENT=====
        self.c_frame = Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=470,height=340)

        #=====SCROLL BARS=====
        scrolly = Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx = Scrollbar(self.c_frame,orient=HORIZONTAL)


        #=====COURSE TABLE=====
        self.courseTable = ttk.Treeview(self.c_frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        #=====SCROLL BARS PACK and CONFIG VIEW=====
        scrollx.pack(side=BOTTOM,fill=X)
        scrollx.config(command=self.courseTable.xview)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("cid",text="Course ID")
        self.courseTable.heading("name",text="Name")
        self.courseTable.heading("duration",text="Duration")
        self.courseTable.heading("charges",text="Charges")
        self.courseTable.heading("description",text="Description")

        self.courseTable['show'] = 'headings'

        self.courseTable.column("cid",width=100)
        self.courseTable.column("name",width=100)
        self.courseTable.column("duration",width=100)
        self.courseTable.column("charges",width=100)
        self.courseTable.column("description",width=150)

        self.courseTable.pack(fill=BOTH,expand=1)
        self.courseTable.bind("<ButtonRelease-1>",self.get_date)
        self.show()


    #=====SEARCH COURSE======
    def search(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:    
            mycursor.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")   
            #f{}<< must have this to format '{%%}'
            myrow = mycursor.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in myrow:
                self.courseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")            


    #=====UPDATE=====
    def update(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                mycursor.execute("select * from course where name=%s",(self.var_course.get(),))                
                #@param name = %s,not = ?
                myrow = mycursor.fetchone()
                if myrow==None:
                    messagebox.showerror("Error","Select Course From List",parent=self.root)
                else:
                    mycursor.execute("update course set duration=%s,charges=%s,description=%s where name=%s",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),    # <<<<<< co dong nay moi add dc
                        self.var_course.get(),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Course Update Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    #======DELETE=====
    def delete(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                mycursor.execute("select * from course where name=%s",(self.var_course.get(),))                
                #@param name = %s,not = ?
                myrow = mycursor.fetchone()
                if myrow==None:
                    messagebox.showerror("Error","Select Course From The List",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want delete this Course?",parent=self.root)
                    if op == TRUE:
                        mycursor.execute("delete from course where name=%s",(self.var_course.get(),))
                        conn.commit()
                        messagebox.showinfo("Deleted","Course Delete Successfulle",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

    #=====CLICK TO SHOW=====
    def get_date(self,ev):
        self.txt_courseName.config(state="readonly")
        r=self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content['values']
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete("1.0",END)
        self.txt_description.insert(END,row[4])

    #======ADD COURSE========
    def add(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                mycursor.execute("select * from course where name=%s",(self.var_course.get(),))                
                #@param name = %s,not = ?
                myrow = mycursor.fetchone()
                if myrow!=None:
                    messagebox.showerror("Error","Course Name already present",parent=self.root)
                else:
                    mycursor.execute("insert into course (name,duration,charges,description) values(%s,%s,%s,%s)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),    # <<<<<< co dong nay moi add dc
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    #=====SHOW COURSE======
    def show (self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:    
            mycursor.execute("select * from course")
            myrow = mycursor.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in myrow:
                self.courseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")            

    #=====CLEAR======
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0",END)
        self.txt_courseName.config(state=NORMAL)

if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()