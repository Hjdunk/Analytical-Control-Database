from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

def identity():
	uname= e1.get()
	password=e2.get()

	if(uname == "" and password == ""):
		messagebox.showinfo("", "Please fill all fields")

	elif(uname == "Admin" and password == "1243"):
		messagebox.showinfo("", "Login Success")
		details();
	
	else:
		messagebox.showinfo("", "Incorrect username and password")


def course_login():

	root = Tk()
	root.title("Course Details")
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

	Button(root, text="Login", command=identity, height =3, width = 13).place(x=10,y=100)


	root.mainloop()


def details():

	global c_cid, c_cname, c_cterm, c_cfaculty, c_ctime

	root = Tk()
	root.title("UNIVERSITY OF NEW HAVEN")
	root.minsize(width=500,height=500)
	root.geometry("700x600")

	c_cid = Label(root,text="Enter Course ID").place(x=20,y=30)

	c_cname = Label(root,text="Enter Course Name").place(x=20,y=60)

	c_cterm = Label(root,text="Enter Course Term ").place(x=20,y=90)

	c_cfaculty = Label(root,text="Enter Faculty Name").place(x=20,y=120)

	c_ctime = Label(root,text="Enter Course Time").place(x=20,y=150)


	c_cid= Entry(root)
	c_cid.place(x=150, y=30)

	c_cname = Entry(root)
	c_cname.place(x=180, y=60)

	c_cterm = Entry(root)
	c_cterm.place(x=180, y=90)

	c_cfaculty = Entry(root)
	c_cfaculty.place(x=180, y=120)

	c_ctime = Entry(root)
	c_ctime.place(x=180, y=150)


	Button (root,text= "insert",command=insert).place(x=10, y=240)

	Button (root,text= "delete",command=delete).place(x=80, y=240)

	Button (root,text= "update",command=update).place(x=150, y=240)

	Button (root,text= "get",command=get).place(x=230, y=240)

	#list= Listbox(root)
	#list.place(x=390,y=30)
	#show();

	root.mainloop()


def insert():
	course_id = c_cid.get()
	course_name = c_cname.get()
	course_term = c_cterm .get()
	course_faculty = c_cfaculty.get()
	course_time = c_ctime.get()

	if(course_id =="" or course_name =="" or course_term ==""or course_faculty ==""or course_time==""):
		messagebox.showinfo("Insert Status","All fields are required");
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("insert into course values('"+ course_id+"','"+ course_name +"', '"+ course_term +"','"+ course_faculty +"','"+course_time+"')")
		cursor.execute("commit")
		con.close()

def update():

	course_id = c_cid.get()
	course_name = c_cname.get()
	course_term = c_cterm .get()
	course_faculty = c_cfaculty.get()
	course_time = c_ctime.get()
	
	if(course_id =="" or course_name =="" or course_term ==""or course_faculty ==""or course_time==""):
		messagebox.showinfo("Update Status","All fields are required");
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("update course set course_id='"+course_id+"',course_name='"+course_name+"',course_term ='"+course_term+"',course_faculty ='"+course_faculty+"',course_time ='"+course_time+"' where course_id = '"+ course_id+"'")
		cursor.execute("commit")

		course_id.delete(0,'end')
		course_name.delete(0,'end')
		course_term.delete(0,'end')
		course_faculty.delete(0,'end')
		course_time.delete(0,'end')
		
		messagebox.showinfo("Update status","Update Successfully")
		con.close()

def delete():
	course_id = c_cid.get()
	if(course_id== ""):
		messagebox.showinfo("Delete Status","ID is required");
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("delete from course where course_id = '"+ course_id +"'")
		cursor.execute("commit")
		con.close() 

def get():
	if(c_cid.get()==""):
		messagebox.showinfo("Fetch status", "ID is compulsory to fetch details")
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("select * from course where course_id = '"+ c_cid.get() +"'")
		rows = cursor.fetchall()

		for row in rows:
			c_cname.insert(0, row[1])
			c_cterm.insert(0, row[2])
			c_cfaculty.insert(0, row[3])
			c_ctime.insert(0, row[4])

		
		con.close()
