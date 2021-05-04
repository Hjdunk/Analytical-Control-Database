from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

def identity():
	uname= e1.get()
	password=e2.get()

	if(uname == "" and password == ""):
		messagebox.showinfo("", "Please fill all fields")

	elif(uname == "Admin" and password == "123456"):
		messagebox.showinfo("", "Login Success")
		details();
	
	else:
		messagebox.showinfo("", "Incorrect username and password")


def fac_login():

	root = Tk()
	root.title("Faculty Details")
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

	global f_staffid,f_name,f_ssn,f_dept,f_email

	root = Tk()
	root.title("UNIVERSITY OF NEW HAVEN")
	root.minsize(width=500,height=500)
	root.geometry("700x600")

	staff_id = Label(root,text="Enter Staff ID").place(x=20,y=30)

	name = Label(root,text="Enter Name").place(x=20,y=60)

	ssn = Label(root,text="Enter SSN ").place(x=20,y=90)

	department = Label(root,text="Enter Department").place(x=20,y=120)

	email = Label(root,text="Enter Email").place(x=20,y=150)

	f_staffid = Entry(root)
	f_staffid.place(x=150, y=30)

	f_name = Entry(root)
	f_name.place(x=150, y=60)

	f_ssn = Entry(root)
	f_ssn.place(x=150, y=90)
	f_ssn.config(show="*")

	f_dept = Entry(root)
	f_dept.place(x=150, y=120)

	f_email = Entry(root)
	f_email.place(x=150, y=150)


	Button (root,text= "insert",command=insert).place(x=10, y=240)

	Button (root,text= "delete",command=delete).place(x=80, y=240)

	Button (root,text= "update",command=update).place(x=150, y=240)

	Button (root,text= "get",command=get).place(x=230, y=240)

	#list= Listbox(root)
	#list.place(x=390,y=30)
	#show();

	root.mainloop()


def insert():
	staff_id =f_staffid.get()
	name=f_name.get()
	ssn=f_ssn.get()
	department=f_dept.get()
	email=f_email.get()

	if(staff_id =="" or name=="" or ssn==""or department==""or email==""):
		messagebox.showinfo("Insert Status","All fields are required");
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("insert into faculty values('"+ staff_id +"','"+ name +"', '"+ssn +"','"+ department +"','"+email +"')")
		cursor.execute("commit")
		con.close()

def update():

	staff_id =f_staffid.get()
	name=f_name.get()
	ssn=f_ssn.get()
	department=f_dept.get()
	email=f_email.get()


	if(staff_id =="" or name=="" or ssn=="" or department==""or email==""):
		messagebox.showinfo("Update Status","All fields are required");
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("update faculty set staff_id='"+staff_id+"',name='"+name+"',ssn='"+ssn+"',department='"+department+"',email='"+email+"' where staff_id = '"+ staff_id+"'")
		cursor.execute("commit")

		f_staffid.delete(0,'end')
		f_name.delete(0,'end')
		f_ssn.delete(0,'end')
		f_dept.delete(0,'end')
		f_email.delete(0,'end')
		messagebox.showinfo("Update status","Update Successfully")
		con.close()


def delete():
	staff_id = f_staffid.get()
	if(staff_id== ""):
		messagebox.showinfo("Delete Status","ID is required");
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("delete from faculty where staff_id = '"+ staff_id +"'")
		cursor.execute("commit")
		con.close() 




def get():
	if(f_staffid.get()==""):
		messagebox.showinfo("Fetch status", "ID is compulsory to fetch details")
	else:
		con = mysql.connect(host="localhost", user="root", password="rootroot", database="univ_database")
		cursor= con.cursor()
		cursor.execute("select * from faculty where staff_id = '"+ f_staffid.get() +"'")
		rows = cursor.fetchall()

		for row in rows:
			f_name.insert(0, row[1])
			f_ssn.insert(0, row[2])
			f_dept.insert(0, row[3])
			f_email.insert(0, row[4])

		con.close()

