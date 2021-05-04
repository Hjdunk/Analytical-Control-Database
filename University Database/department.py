from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql


def identity():
	uname= e1.get()
	password=e2.get()

	if(uname == "" and password == ""):
		messagebox.showinfo("", "Please fill all fields")

	elif(uname == "Admin" and password == "1234"):
		messagebox.showinfo("", "Login Success")
		details();
	
	else:
		messagebox.showinfo("", "Incorrect username and password")


def dep_login():

	root = Tk()
	root.title("Department Details")
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

	global d_deptid, d_name, d_email

	root = Tk()
	root.title("UNIVERSITY OF NEW HAVEN")
	root.minsize(width=500,height=500)
	root.geometry("700x600")

	d_deptid = Label(root,text="Enter Department ID").place(x=20,y=30)

	d_name = Label(root,text="Enter Department Name").place(x=20,y=60)

	d_email = Label(root,text="Enter Department Email").place(x=20,y=90)


	d_deptid = Entry(root)
	d_deptid.place(x=150, y=30)

	d_name = Entry(root)
	d_name.place(x=180, y=60)

	d_email = Entry(root)
	d_email.place(x=180, y=90)


	Button (root,text= "insert",command=insert).place(x=10, y=240)

	Button (root,text= "delete",command=delete).place(x=80, y=240)

	Button (root,text= "update",command=update).place(x=150, y=240)

	Button (root,text= "get",command=get).place(x=230, y=240)

	#list= Listbox(root)
	#list.place(x=390,y=30)
	#show();

	root.mainloop()

def insert():
	dept_id = d_deptid.get()
	dept_name = d_name.get()
	dept_email = d_email.get()

	if(dept_id == "" or dept_name == "" or dept_email==""):
		messagebox.showinfo("Insert Status","All fields are required")
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("insert into department values('"+ dept_id +"','"+ dept_name +"','"+dept_email +"')")
		cursor.execute("commit")
		con.close()

def update():

	dept_id = d_deptid.get()
	dept_name = d_name.get()
	dept_email = d_email.get()


	if(dept_id =="" or dept_name =="" or dept_email==""):
		messagebox.showinfo("Update Status","All fields are required");
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("update department set dept_id='"+dept_id+"',dept_name='"+dept_name+"',dept_email='"+dept_email+"' where dept_id = '"+ dept_id+"'")
		cursor.execute("commit")

		dept_id.delete(0,'end')
		dept_name.delete(0,'end')
		dept_email.delete(0,'end')
		
		messagebox.showinfo("Update status","Update Successfully")
		con.close()

def delete():
	dept_id = d_deptid.get()
	if(dept_id== ""):
		messagebox.showinfo("Delete Status","ID is required");
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("delete from department where dept_id = '"+ dept_id +"'")
		cursor.execute("commit")
		con.close() 


def get():
	if(d_deptid.get()==""):
		messagebox.showinfo("Fetch status", "ID is compulsory to fetch details")
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("select * from department where dept_id = '"+ d_deptid.get() +"'")
		rows = cursor.fetchall()

		for row in rows:
			d_name.insert(0, row[1])
			d_email.insert(0, row[2])
		
		con.close()



