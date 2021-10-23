from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import mysql.connector

class reportClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()     #<<< ko move dc window

        #=====TITLE=====
        title = Label(self.root,text="View Student Results",font=("goudy old  style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=35)

        #=====BUTTON=====
        self.var_search = StringVar()
        self.var_id = ""
        
        lbl_select = Label(self.root,text="Search By Roll No:",font=("goudy old style",20,"bold"),bg="white").place(x=280,y=100)
        txt_search = Entry(self.root,textvariable=self.var_search,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=520,y=100,width=150)

        btn_search = Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=680,y=100,width=100,height=35)
        btn_clear = Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=800,y=100,width=100,height=35)
        btn_delete = Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete   ).place(x=500,y=350,width=150,height=35)


        #=====LABEL=====
        lbl_roll = Label(self.root,text="Roll No",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name = Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course = Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks = Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_full = Label(self.root,text="Total Marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per = Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        #=====SHOW=====
        self.roll = Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name = Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course = Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.marks = Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150,height=50)
        self.full = Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.full.place(x=750,y=280,width=150,height=50)
        self.per = Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)


    #=====SEARCH STUDENT======
    def search(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:    
            if self.var_search.get() == "":
                messagebox.showerror("Error","Roll no should be required",parent=self.roll)
            else:
                mycursor.execute("select * from result where roll=%s",(self.var_search.get(),))    #   << co phay
                #f{}<< must have this to format '{%%}'
                myrow = mycursor.fetchone()
                if myrow != None:
                    self.var_id = myrow[0]
                    self.roll.config(text=myrow[1])
                    self.name.config(text=myrow[2])
                    self.course.config(text=myrow[3])
                    self.marks.config(text=myrow[4])
                    self.full.config(text=myrow[5])
                    self.per.config(text=myrow[6])
                else:
                    messagebox.showerror("Error","No Record Founded",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")     

    #======DELETE=====
    def delete(self):
        conn = mysql.connector.connect(host="localhost",user="root",database="res_mana_sys",)
        mycursor = conn.cursor()
        try:
            if self.var_id =="":
                messagebox.showerror("Error","Search Student result first",parent=self.root)
            else:
                mycursor.execute("select * from result where rid=%s",(self.var_id,))                
                #@param name = %s,not = ?
                myrow = mycursor.fetchone()
                if myrow==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want delete this Course?",parent=self.root)
                    if op == TRUE:
                        mycursor.execute("delete from result where rid=%s",(self.var_id,))
                        conn.commit()
                        messagebox.showinfo("Deleted","Result Delete Successfulle",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  



    #=====CLEAR=====
    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")



if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()