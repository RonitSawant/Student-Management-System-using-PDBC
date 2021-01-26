from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import cx_Oracle
import numpy as np
from matplotlib import pyplot as plt
	
root = Tk()
root.title(" S M S ")
root.geometry("500x580+250+150")
root.configure(background='AntiqueWhite2')

def f1():
	root.withdraw()
	addst.deiconify()

def f3():
	root.withdraw()
	viewst.deiconify()
	
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/Password")
		cursor = con.cursor()
		sql = "select * from kstudent"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		
		for d in data:
			msg = msg + "Rno : " + str(d[0]) + " Name : " + d[1] + " Marks : " + str(d[2]) +"\n"
		stData.insert(INSERT , msg)
		stData.delete('1.0' , END)
		stData.insert(INSERT , msg)	
		
	except cx_Oracle.DatabaseError as e:
		print("Some issue" , e)

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()


def f6():
	root.withdraw()
	updst.deiconify()	
	
def f8():
	root.withdraw()
	delst.deiconify()

def f18():
	
	con=None	
	cursor=None
	try:
		con = cx_Oracle.connect("system/Password")
		cursor=con.cursor()
		sql="select NAME from kstudent"
		cursor.execute(sql)
		gp = list(cursor.fetchall())
		for i,row in enumerate(cursor.fetchall()):
			gp.append(row[i])
			list(gp[i])

		#for getting name in list
		names = [item for t in gp for item in t] 
		sql1 ="select MARKS from kstudent"
		cursor.execute(sql1)
		gp1 = list(cursor.fetchall())
		for i,row in enumerate(cursor.fetchall()):

			gp1.append(row[i])
			list(gp1[i])

		marks = [item for t in gp1 for item in t] 
		a=np.arange(len(names))
		plt.bar(a,marks,width=0.25,label="Marks")
		plt.title("PERFORMANCE")
		plt.ylabel("Marks")
		plt.xlabel("Name")
		plt.xticks(a,names)
		plt.legend()
		plt.grid()
		plt.show()
			
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

lbltitle = Label(root , text = "Student Management System" , font=("castellar",14,"bold"))
btnAdd = Button(root , text = "Add" , width = 12 , font=("ink free",15,"bold") , 
command = f1)
btnView = Button(root , text = "View" , width = 12 , font=("ink free",15,"bold") , 
command = f3)
btnUp = Button(root , text = "Update" , width = 12 , font=("ink free",15,"bold") ,
command = f6)
btnDel = Button(root , text = "Delete" , width = 12 , font=("ink free",15,"bold") ,
command = f8)
btnGrp = Button(root , text = "Graph" , width = 12 , font=("ink free",15,"bold"),
command=f18)

lblQotd = Label(root , text = "Quote of the day :  " , font = ('ink free' , 14 , 'italic'))
txtQotd = Label(root , text = "" , width = 24 ,height = 5, bd = 5 , 
relief = RAISED , wraplength = 255 ,anchor = "w" ,justify = LEFT,  font = ('inkfree' , 14 , 'italic') )


lbltitle.pack(pady = 5)
btnAdd.pack(pady = 5)
btnView.pack(pady = 5)
btnUp.pack(pady = 5)
btnDel.pack(pady = 5)
btnGrp.pack(pady = 5)

lblQotd.pack(pady = 10)
txtQotd.pack()

import bs4
import requests

res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")

soup = bs4.BeautifulSoup(res.text , 'lxml')
quote = soup.find('img' , {"class":"p-qotd"})

ans = quote['alt']
txtQotd.config(text = ans)


import socket
import requests

try:
		socket.create_connection(("www.google.com" , 80))
		a1 = "http://api.openweathermap.org/data/2.5/weather?q=Mumbai"
		a2 = "&units=metric"
		a3 = "&appid=your app id from site"
		api_address = a1 + a2 + a3 

		res1 = requests.get(api_address)
		data = res1.json()
		#print(data)
		main = data['main']
		temp = main['temp']
		temp = str(temp)
		city = "Mumbai"
		lblTemp = Label(root,text = "Temperature : " +temp+"\u00B0" + "\n" +
		"City : "+city,font=("inkfree",16,"bold"))
		lblTemp.place(x=210,y=580)
		lblTemp.pack(pady = 5)	

except OSError :	
	print("Check Network")

####################ADD WINDOW#######################
addst = Toplevel(root)
addst.title("Add Student")
addst.geometry("400x450+250+150")
addst.configure(background='AntiqueWhite2')
addst.withdraw()

def f2():
	addst.withdraw()
	root.deiconify()

def f5():
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/Password")
		rno = (entaddrno.get())
		name = (entaddname.get())
		marks = (entaddmarks.get())

		if len(rno) == 0 or len(name) == 0 or len(marks) == 0:
			messagebox.showwarning("Warning","Plz fill the empty field")
		
		elif rno.isalpha():
			messagebox.showerror("Error","Roll no must be integer")
			entaddrno.delete(0, END)
			entaddrno.focus()

		elif name.isdigit():
			messagebox.showerror("Error","Only strings allowed")
			entaddname.delete(0 , END)
			entaddname.focus()	
						
		elif len(name) < 2:
			msg = "Name cannot be less than 2 characters"
			messagebox.showerror("Error",msg)	
			entaddname.delete(0 , END)
			entaddname.focus()	

		elif marks.isalpha() or int(marks) > 100:
			msg = "Integer less than 100 allowed"
			messagebox.showerror("Error",msg)
			entaddmarks.delete(0,END)
			entaddmarks.focus()

		elif rno.isdigit() and name.isalpha() and int(rno) > 0 and marks.isdigit() and int(marks) > 0 and int(marks) <= 100:
			rno=int(rno)
			marks=int(marks)
			cursor = con.cursor()
			sql = "select rno from kstudent where rno='%d'"
			args = (rno)
			cursor.execute(sql%args)
			data = cursor.fetchall()
			if len(data)==0:
				cursor = con.cursor()
				sql = "insert into kstudent values('%d','%s','%d' )"
				args = (rno , name , marks)
				cursor.execute(sql % args)
				con.commit()
				msg = str(cursor.rowcount) + " records inserted "
				messagebox.showinfo("Success" , msg)
				entaddrno.delete(0 , END)
				entaddname.delete(0 , END)
				entaddmarks.delete(0 , END)
				entaddrno.focus()
			else:
				messagebox.showinfo("Info" , "Record already exists")
				entaddrno.delete(0 , END)
				entaddname.delete(0 , END)
				entaddmarks.delete(0 , END)
				entaddrno.focus()

		
		else:
			messagebox.showerror("Error","Invalid input")
			entaddrno.delete(0 , END)
			entaddname.delete(0 , END)
			entaddmarks.delete(0 , END)
			entaddrno.focus()


	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("Galat Kiya Re" , e)
		con.rollback()

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()	


lbladdrno = Label(addst , text = "Enter Rno" , font = ('inkfree' , 14 , 'italic'))
entaddrno = Entry(addst , bd = 5 , font = ('inkfree' , 14 , 'italic'))
lbladdname = Label(addst , text = "Enter Name" , font = ('inkfree' , 14 , 'italic'))
entaddname = Entry(addst , bd = 5 , font = ('inkfree' , 14 , 'italic'))
lbladdmarks = Label(addst , text = "Enter Marks" , font = ('inkfree' , 14 , 'italic'))
entaddmarks = Entry(addst , bd = 5 , font = ('inkfree' , 14 , 'italic'))

btnAddSave = Button(addst , text = "Save" , font = ('inkfree' , 14 , 'italic') , 
command = f5)
btnAddBack = Button(addst , text = "Back" , font = ('inkfree' , 14 , 'italic') , 
command = f2)

lbladdrno.pack(pady = 5)
entaddrno.pack(pady = 5)
lbladdname.pack(pady = 5)
entaddname.pack(pady = 5)
lbladdmarks.pack(pady=5)
entaddmarks.pack(pady=5)
btnAddSave.pack(pady = 5)
btnAddBack.pack(pady = 5)

#####################VIEW WINDOW######################

viewst = Toplevel(root)
viewst.title("View Student")
viewst.geometry("400x400+200+200")
viewst.configure(background='AntiqueWhite2')
viewst.withdraw()


def f4():
	viewst.withdraw()
	root.deiconify()


stData = scrolledtext.ScrolledText(viewst , width = 40 , height = 10)
btnViewBack = Button(viewst , text = "Back" , font = ('inkfree' , 14 , 'italic') , command = f4)

stData.pack(pady = 5)
btnViewBack.pack()

#######################UPDATE WINDOW#######################

updst = Toplevel(root)
updst.title("Update Student")
updst.geometry("400x300+300+200")
updst.configure(background='AntiqueWhite2')
updst.withdraw()

def f11():
	updnm.deiconify()
	updst.withdraw()

def f12():
	updmrk.deiconify()
	updst.withdraw()

def f13():
	updst.withdraw()
	root.deiconify()

btnUpdname = Button(updst,text="Update Name",font=("ink free",15,"bold"),width=12,command=f11)
btnUpdmarks = Button(updst,text="Update Marks",font=("ink free",15,"bold"),width=12,command=f12)
btnUpdback = Button(updst,text="Back",font=("ink free",15,"bold"),width=12,command=f13)

btnUpdname.pack(pady=10)
btnUpdmarks.pack(pady=10)
btnUpdback.pack(pady=10)

#UPDATE NAME WINDOW
updnm = Toplevel(root)
updnm.title("Update Student's Name")
updnm.geometry("400x400+200+200")
updnm.configure(background='AntiqueWhite2')
updnm.withdraw()

def f7():
	
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/Password")
		rno = (entupdnmrno.get())
		name = (entupdnmname.get())
		
		if len(rno) == 0 or len(name) == 0:
			messagebox.showwarning("Warning","Plz fill the empty field")
		
		elif rno.isalpha():
			messagebox.showerror("Error","Roll no must be integer")
			entupdnmrno.delete(0, END)
			entupdnmrno.focus()
		
		elif int(rno) < 0:
			messagebox.showerror("Error","Roll no must be positive")
			entupdnmrno.delete(0, END)
			entupdnmrno.focus()

		elif name.isdigit():
			messagebox.showerror("Error","Only strings allowed")
			entupdnmname.delete(0 , END)
			entupdnmname.focus()	
						
		elif len(name) < 2:
			msg = "Name cannot be less than 2 characters"
			messagebox.showerror("Error",msg)	
			entupdnmname.delete(0 , END)
			entupdnmname.focus()	

		elif rno.isdigit() and int(rno) > 0 and name.isalpha():
			rno=int(rno)
			cursor = con.cursor()
			sql = "select rno from kstudent where rno='%d'"
			args = (rno)
			cursor.execute(sql%args)
			data = cursor.fetchall()
			if len(data)==0:
				messagebox.showwarning("Info" , "Record does not exist")
				entupdnmrno.delete(0 , END)
				entupdnmname.delete(0 , END)
				entupdnmrno.focus()

			else:
				cursor = con.cursor()
				sql = "update kstudent set name = '%s' where rno = '%d' "
				args = ( name , rno)
				cursor.execute(sql % args)
				con.commit()
				msg = str(cursor.rowcount) + " records updated "
				messagebox.showinfo("Successsful" , msg)
				entupdnmrno.delete(0 , END)
				entupdnmname.delete(0 , END)
				entupdnmrno.focus()

		else:
			messagebox.showerror('Error','Invalid input')
			entupdnmrno.delete(0 , END)
			entupdnmname.delete(0 , END)
			entupdnmrno.focus()

	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("Galat Kiya Re" , e)
		con.rollback()

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def f14():
	updst.deiconify()
	updnm.withdraw()

lblupdnmrno = Label(updnm , text = "Enter Rno" , font = ('inkfree' , 14 , 'italic'))
entupdnmrno = Entry(updnm , bd = 5 , font = ('inkfree' , 14 , 'italic'))
lblupdnmname = Label(updnm , text = "Enter New Name" , font = ('inkfree' , 14 , 'italic'))
entupdnmname = Entry(updnm , bd = 5 , font = ('inkfree' , 14 , 'italic'))

btnUpdSave = Button(updnm , text = "Save" , font = ('inkfree' , 14 , 'italic') , 
command = f7)
btnUpdBack = Button(updnm , text = "Back" , font = ('inkfree' , 14 , 'italic') , 
command = f14)

lblupdnmrno.pack(pady = 5)
entupdnmrno.pack(pady = 5)
lblupdnmname.pack(pady = 5)
entupdnmname.pack(pady = 5)
btnUpdSave.pack(pady = 5)
btnUpdBack.pack(pady = 5)

#####################UPDATE MARKS WINDOW######################
updmrk = Toplevel(root)
updmrk.title("Update Student's Marks")
updmrk.geometry("400x400+200+200")
updmrk.configure(background='AntiqueWhite2')
updmrk.withdraw()

def f15():
	
	con=None
	cursor=None
	try:
		con = cx_Oracle.connect("system/Password")
		rno = (entupdmrkrno.get())
		marks = (entupdmrkmark.get())

		if len(rno) == 0 or len(marks) == 0:
			messagebox.showwarning("Warning","Plz fill the empty field")
		
		elif rno.isalpha():
			messagebox.showerror("Error","Roll no must be integer")
			entupdmrkrno.delete(0, END)
			entupdmrkrno.focus()

		elif marks.isalpha() or int(marks) > 100:
			msg = "Integer less than 100 allowed"
			messagebox.showerror("Error",msg)
			entupdmrkmarks.delete(0,END)
			entupdmrkmarks.focus()

		elif rno.isdigit() and int(rno) > 0 and marks.isdigit() and int(marks)>0 and int(marks)<=100:
			rno=int(rno)
			marks=int(marks)
			cursor = con.cursor()
			sql = "select rno from kstudent where rno='%d'"
			args = (rno)
			cursor.execute(sql%args)
			data = cursor.fetchall()
			if len(data)==0:
				messagebox.showwarning("Info" , "Record does not exist")
				entupdmrkrno.delete(0,END)
				entupdmrkmark.delete(0,END)
				entupdmrkrno.focus()

			else:
				cursor = con.cursor()
				sql = "update kstudent set marks=('%d') where rno='%d'"			
				args = (marks,rno)
				cursor.execute(sql%args)
				con.commit()
				msg= str(cursor.rowcount)+" Row Updated"
				messagebox.showinfo("Success",msg)
				entupdmrkrno.delete(0,END)
				entupdmrkmark.delete(0,END)
				entupdmrkrno.focus()	
		else:
			messagebox.showerror('Error','Invalid input')
			entupdmrkrno.delete(0,END)
			entupdmrkmark.delete(0,END)
			entupdmrkrno.focus()	


	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Error",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()	

def f16():
	updst.deiconify()
	updmrk.withdraw()

lblupdmrkrno = Label(updmrk,text="Enter Rno",font=("arial",12,"bold"))
entupdmrkrno = Entry(updmrk,bd=5)
lblupdmrkmark = Label(updmrk,text="Enter New Marks",font=("arial",12,"bold"))
entupdmrkmark = Entry(updmrk,bd=5)
btnupdmrksave = Button(updmrk,text="Save",font=("ink free",12,"italic"),width=12,command=f15)
btnupdmrkback = Button(updmrk,text="Back",font=("ink free",12,"italic"),width=12,command=f16)


lblupdmrkrno.pack(pady=5)
entupdmrkrno.pack(pady=5)
lblupdmrkmark.pack(pady=5)
entupdmrkmark.pack(pady=5)
btnupdmrksave.pack(pady=5)
btnupdmrkback.pack(pady=5)

######################DELETE WINDOW##########################

delst = Toplevel(root)
delst.title("Delete Student")
delst.geometry("400x400+200+200")
delst.configure(background='AntiqueWhite2')
delst.withdraw()
lblRno = Label(delst , text = "Enter Rno" , font = ('inkfree' , 14 , 'italic'))
entRno = Entry(delst , bd = 5 , font = ('inkfree' , 14 , 'italic'))


def f9():
	
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/Password")
		rno = (entRno.get())
		
		if len(rno) == 0:
			messagebox.showwarning("Warning","Plz fill the empty field")
		
		elif rno.isalpha():
			messagebox.showerror("Error","Roll no must be integer")
			entRno.delete(0, END)
			entRno.focus()

		
		elif rno.isdigit() and int(rno) > 0:
			rno =int(rno)
			cursor = con.cursor()
			sql = "select rno from kstudent where rno='%d'"
			args = (rno)
			cursor.execute(sql%args)
			data = cursor.fetchall()
			if len(data)==0:
				messagebox.showwarning("Info" , "Record does not exist")
				entRno.delete(0 , END)
				entRno.focus()
			else:
				cursor = con.cursor()
				sql = "delete from kstudent where rno = '%d' "
				args = (rno)
				cursor.execute(sql % args)
				msg = str(cursor.rowcount) + " records deleted "
				messagebox.showinfo("Successsful" , msg)
				con.commit()
		
				entRno.delete(0 , END)
				entRno.focus()
		else:
			messagebox.showerror("Error","Invalid Input")
			entRno.delete(0,END)
			entRno.focus()

	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("Galat Kiya Re" , e)
		con.rollback()

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()	

def f17():
	delst.withdraw()
	root.deiconify()

btnDelSave = Button(delst , text = "Save" , font = ('inkfree' , 14 , 'italic') , 
command = f9)
btnDelBack = Button(delst , text = "Back" , font = ('inkfree' , 14 , 'italic') , 
command = f17)

lblRno.pack(pady = 5)
entRno.pack(pady = 5)
btnDelSave.pack(pady = 5)
btnDelBack.pack(pady = 5)

####################GRAPH WINDOW######################
gpst = Toplevel(root)
gpst.title("Graph")
gpst.geometry("400x400+200+200")
gpst.configure(background="AntiqueWhite2")
gpst.withdraw()


def f19():
	root.deiconify()
	gpst.withdraw()

btngpback = Button(gpst,text = 'Back' , font=("inkfree",14,"italic"),width = 12,command=f19)	
btngpback.pack(pady=10)		

root.mainloop()
