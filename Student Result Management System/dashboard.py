from tkinter import *
from PIL import ImageTk,Image
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass

class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        
        self.root.config(bg="white")

        #=====icon======
        self.logo_dash = ImageTk.PhotoImage(file="images/logo (1).png")
        #=====title=====
        title = Label(self.root,text="Student Result Management System",compound=LEFT,image=self.logo_dash,font=("goudy old  style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #=====MENU=====
        m_frame = LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
        m_frame.place(x=10,y=70,width=1340,height=80)

        btn_course = Button(m_frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student = Button(m_frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result = Button(m_frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view = Button(m_frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout = Button(m_frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=40)
        btn_exit = Button(m_frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=quit).place(x=1120,y=5,width=200,height=40)

        #=====CONTENT_WINDOW======
        self.bg_img = Image.open("images/logo.png")
        self.bg_img = self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #=====UPDATE LABEL=====
        self.ltl_course = Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.ltl_course.place(x=400,y=535,width=300,height=100)
        self.ltl_student = Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.ltl_student.place(x=710,y=535,width=300,height=100)
        self.ltl_result = Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#036874",fg="white")
        self.ltl_result.place(x=1020,y=535,width=300,height=100)


        #=====FOTTER=====
        footer = Label(self.root,text="SRMS-Student Result Management System\nContact us for any Technical Issue: 0947970xxx",font=("goudy old  style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)


    #=====ADD COURSE=====
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)
    
    #=====ADD STUDENT=====
    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    #======ADD RESULT STUDENT======
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)
    
    #=====VIEW STUDENT=====
    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    #root.resizable(width=False,height=False)
    #root.resizable(width=True,height=True)
    #root.resizable(width=False,height=True)
    #Grid.grid_configure()
    root.mainloop()