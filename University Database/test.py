from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as mysql
from student import *
from faculty import *
from department import *
from course import *

mypass = "rootroot"
mydatabase="univ_database"

con = mysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("UNIVERSITY OF WEST HAVEN")
root.minsize(width=500,height=500)
root.geometry("700x600")

label = Label(root, text = "Welcome to UWH database",fg = "black").pack()


#icon = PhotoImage(file = "/Users/gokulsd/Desktop/Rogan/Gokul/image.jpeg")
#label = Label(root, image = icon)
#xqlabel.pack()


headingFrame1 = Frame(root,bg="#FFBB04",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n University Database", bg='light blue', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Student Details",bg='red', fg='black',command=stud)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Faculty Details",bg='black', fg='black',command=fac_login)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Department Details",bg='black', fg='black',command=dep_login)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Course Details",bg='black', fg='black',command=course_login)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)



root.mainloop()