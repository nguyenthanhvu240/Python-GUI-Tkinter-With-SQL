from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import mysql.connector

class resultClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()     #<<< ko move dc window

        
        #=====VARIBLES=====
        self.var_roll =StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()

        #=====TITLE=====
        title = Label(self.root,text="Add Student Results",font=("goudy old  style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=35)

        #=====WIDGETS======
        lbl_select = Label(self.root,text="Select Student:",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
        lbl_name = Label(self.root,text="Name:",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
        lbl_course = Label(self.root,text="Course:",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
        lbl_mark_ob = Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
        lbl_full_marks = Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)

        self.txt_student = ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",25,"bold"),state="readonly",justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200,height=28)
        self.txt_student.set("Select")
    
        #=====BUTTON=====
        self.btn_search = Button(self.root,text="Search:",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        self.btn_search.place(x=500,y=100,width=120,height=28)

        btn_add = Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear = Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)

    
        #=====ENTRY=====
        txt_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow",state="readonly").place(x=280,y=160,width=340)
        txt_course = Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow",state="readonly").place(x=280,y=220,width=340)
        txt_marks = Entry(self.root,textvariable=self.var_marks,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=280,y=280,width=340)
        txt_full_marks = Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=280,y=340,width=340)

        #=====CONTENT_WINDOW======
        self.bg_img = Image.open("images/logo.png")
        self.bg_img = self.bg_img.resize((500,300),Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root,image=self.bg_img).place(x=650,y=100)

        #=====FETCH ROLLE=====
    def fetch_roll(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:    
            mycursor.execute("select roll from student")
            myrow = mycursor.fetchall()
            #v=[]
            if len(myrow) > 0:
                for row in myrow:
                    #v.append(row[0])
                    self.roll_list.append(row[0])
            #print(v)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")   

        #=====SEARCH STUDENT======
    def search(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:    
            mycursor.execute("select name,course from student where roll=%s",(self.var_roll.get(),))    #   << co phay
            #f{}<< must have this to format '{%%}'
            myrow = mycursor.fetchone()
            if myrow != None:
                self.var_name.set(myrow[0])
                self.var_course.set(myrow[1])
            else:
                messagebox.showerror("Error","No Record Founded",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")     


        #======ADD COURSE========
    def add(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please Select Student Record",parent=self.root)
            else:
                mycursor.execute("select * from result where roll=%s and course=%s",(self.var_course.get(),self.var_course.get(),))                
                #@param name = %s,not = ?
                myrow = mycursor.fetchone()
                if myrow!=None:
                    messagebox.showerror("Error","Result already present",parent=self.root)
                else:
                    per = (int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    mycursor.execute("insert into result(roll,name,course,marks_ob,full_marks,per) values(%s,%s,%s,%s,%s,%s)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")          

        #=====CLEAR======
    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set(""),




if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()