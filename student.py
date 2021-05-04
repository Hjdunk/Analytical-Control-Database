from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

def success():
	uname= e1.get()
	password=e2.get()

	if(uname == "" and password == ""):
		messagebox.showinfo("", "Please fill all fields")

	elif(uname == "Admin" and password == "12345"):
		messagebox.showinfo("", "Login Success")
		details();
	
	else:
		messagebox.showinfo("", "Incorrect username and password")


def details():

	global e_id,e_name,e_phone,e_course,e_dept,e_advisor

	root = Tk()
	root.title("UNIVERSITY OF NEW HAVEN")
	root.minsize(width=500,height=500)
	root.geometry("700x600")

	ID = Label(root,text="Enter ID").place(x=20,y=30)

	name = Label(root,text="Enter Name").place(x=20,y=60)

	phone = Label(root,text="Enter Mobile No.").place(x=20,y=90)

	course = Label(root,text="Enter Course").place(x=20,y=120)

	department = Label(root,text="Enter Department").place(x=20,y=150)

	Advisor = Label(root,text="Enter Advisor Name").place(x=20,y=180)

	e_id = Entry(root)
	e_id.place(x=150, y=30)

	e_name = Entry(root)
	e_name.place(x=150, y=60)

	e_phone = Entry(root)
	e_phone.place(x=150, y=90)

	e_course = Entry(root)
	e_course.place(x=150, y=120)

	e_dept = Entry(root)
	e_dept.place(x=150, y=150)

	e_advisor = Entry(root)
	e_advisor.place(x=150, y=180)


	Button (root,text= "insert",command=insert).place(x=10, y=240)

	Button (root,text= "delete",command=delete).place(x=80, y=240)

	Button (root,text= "update",command=update).place(x=150, y=240)

	Button (root,text= "get",command=get).place(x=230, y=240)

	#list= Listbox(root)
	#list.place(x=390,y=30)
	#show();

	root.mainloop()


def insert():

				ID =e_id.get()
				name=e_name.get()
				phone=e_phone.get()
				course=e_course.get()
				department=e_dept.get()
				Advisor=e_advisor.get()

				if(ID =="" or name=="" or phone=="" or course==""or department==""or Advisor==""):
								messagebox.showinfo("Insert Status","All fields are required");
				else:
								con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
								cursor= con.cursor()
								cursor.execute("insert into student values('"+ ID +"','"+ name +"', '"+ phone +"','"+ course +"','"+department +"','"+ Advisor +"')")
								cursor.execute("commit")
								con.close()

def update():

	ID =e_id.get()
	name=e_name.get()
	phone=e_phone.get()
	course=e_course.get()
	department=e_dept.get()
	Advisor=e_advisor.get()


	if(ID =="" or name=="" or phone==""):
		messagebox.showinfo("Update Status","All fields are required");
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("update student set name='"+name+"',phone='"+phone+"',course='"+course+"',department='"+department+"',Advisor='"+Advisor+"' where id = '"+ ID +"'")
		cursor.execute("commit")

		e_id.delete(0,'end')
		e_name.delete(0,'end')
		e_phone.delete(0,'end')
		e_course.delete(0,'end')
		e_dept.delete(0,'end')
		e_advisor.delete(0,'end')
		messagebox.showinfo("Update status","Update Successfully")
		con.close()


def get():
	if(e_id.get()==""):
		messagebox.showinfo("Fetch status", "ID is compulsory to fetch details")
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("select * from student where id = '"+ e_id.get() +"'")
		rows = cursor.fetchall()

		for row in rows:
			e_name.insert(0, row[1])
			e_phone.insert(0, row[2])
			e_course.insert(0, row[3])
			e_dept.insert(0, row[4])
			e_advisor.insert(0, row[5])

		con.close()


def delete():
				ID = e_id.get()
				#name=e_name.get()
				#phone=e_phone.get()

				if(ID== ""):
								messagebox.showinfo("Delete Status","ID is required");
				else:
								con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
								cursor= con.cursor()
								cursor.execute("delete from student where id = '"+ ID +"'")
								cursor.execute("commit")
								con.close() 
				
def stud():

	root = Tk()
	root.title("Student Details")
	root.minsize(width=500,height=500)
	root.geometry("700x600")

	global e1,e2

	uname = Label(root,text="Username").place(x=10,y=10)

	password = Label(root,text="Password").place(x=10,y=40)


	e1 = Entry(root)
	e1.place(x=140, y=10)

	e2 = Entry(root)
	e2.place(x=140, y=40)
	e2.config(show="*")

	Button(root, text="Login", command=success, height =3, width = 13).place(x=10,y=100)


	root.mainloop()