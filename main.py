import tkinter as tk
import sqlite3
import os
from IncludeDatabase import include_database
from AddDatabaseWindow import add_database_window

current_database = ""

def exit(root):
	root.destroy()

def select_database_window():
	
	def get_name_files():
		name_files = []
		for filename in os.listdir("./"):
			if filename.endswith(".db"):
				name_files.append(filename)
		return name_files

	def set_listbox(ListBox,NameFiles):
		for filename in name_files:
			ListBox.insert("end",filename)

	def define_current_database(Database):
		global current_database 
		current_database = Database
		return current_database

	def show_current_database(Database):
		mainlabel["text"] = f"Current Database is {Database}"

	select_database_window = tk.Tk()
	select_database_window.title("Select a Database")
	select_database_window.resizable(False,False)
	
	canvas = tk.Canvas(select_database_window, height=300, width=300, bg="#367800")
	canvas.pack()

	select_listbox = tk.Listbox(select_database_window,selectmode="single")
	name_files = get_name_files()
	set_listbox(select_listbox,name_files)
	select_listbox.place(relx=0.5,rely=0.1,anchor="n")

	select_button = tk.Button(select_database_window,text="Select",font="Times",command=lambda: [define_current_database(select_listbox.get(first=select_listbox.curselection(),last=None)),
	show_current_database(current_database),select_database_window.destroy()])
	select_button.place(relx=0.3,rely=0.7,anchor="n",relheight=0.1,relwidth=0.4)

	back2_button = tk.Button(select_database_window,text="Back",font="Times",command=lambda: select_database_window.destroy())
	back2_button.place(relx=0.7,rely=0.7,anchor="n",relheight=0.1,relwidth=0.4) 

	select_database_window.mainloop()

def search_database_window(currentDatabase):
	
	def search_by_name(Name,currentDatabase):
		selection = []
		conn = sqlite3.connect(f"{currentDatabase}")
		c = conn.cursor()
		with conn:
			c.execute("SELECT * FROM users WHERE first=?",(Name,))
		selection = c.fetchall()
		userlist = []
		for user in selection:
			userlist.append(list(user))
		
		search_result = tk.Tk()
		search_result.resizable(False,False)

		search_result_canvas = tk.Canvas(search_result,height=300,width=200)
		search_result_canvas.pack()
		search_listbox = tk.Listbox(search_result,selectmode="single")
		for user in userlist:
			search_listbox.insert("end",user)
		search_listbox.place(relx=0.5,rely=0.1,anchor="n")

		back4_button = tk.Button(search_result_canvas,text="Back",font="Times",command=lambda: search_result.destroy())
		back4_button.place(relx=0.5,rely=0.875,anchor="n",relheight=0.1,relwidth=0.4)

		search_result.mainloop()

	def search_by_last(Last,currentDatabase):
		selection = []
		conn = sqlite3.connect(f"{currentDatabase}")
		c = conn.cursor()
		with conn:
			c.execute("SELECT * FROM users WHERE last=?",(Last,))
		selection = c.fetchall()
		userlist = []
		for user in selection:
			userlist.append(list(user))
		
		search_result = tk.Tk()
		search_result.resizable(False,False)

		search_result_canvas = tk.Canvas(search_result,height=300,width=200)
		search_result_canvas.pack()
		search_listbox = tk.Listbox(search_result,selectmode="single")
		for user in userlist:
			search_listbox.insert("end",user)
		search_listbox.place(relx=0.5,rely=0.1,anchor="n")

		back5_button = tk.Button(search_result_canvas,text="Back",font="Times",command=lambda: search_result.destroy())
		back5_button.place(relx=0.5,rely=0.875,anchor="n",relheight=0.1,relwidth=0.4)

		search_result.mainloop()

	def search_by_email(EMail,currentDatabase):
		selection = []
		conn = sqlite3.connect(f"{currentDatabase}")
		c = conn.cursor()
		with conn:
			c.execute("SELECT * FROM users WHERE email=?",(EMail,))
		selection = c.fetchall()
		userlist = []
		for user in selection:
			userlist.append(list(user))
		
		search_result = tk.Tk()
		search_result.resizable(False,False)

		search_result_canvas = tk.Canvas(search_result,height=300,width=200)
		search_result_canvas.pack()
		search_listbox = tk.Listbox(search_result,selectmode="single")
		for user in userlist:
			search_listbox.insert("end",user)
		search_listbox.place(relx=0.5,rely=0.1,anchor="n")

		back6_button = tk.Button(search_result_canvas,text="Back",font="Times",command=lambda: search_result.destroy())
		back6_button.place(relx=0.5,rely=0.875,anchor="n",relheight=0.1,relwidth=0.4)

		search_result.mainloop()


	if currentDatabase == "":
		mainlabel["text"] = "No Database is selected"

	else:
		search_database_window = tk.Tk()
		search_database_window.title("Search Data")
		search_database_window.resizable(False,False)

		search_database_canvas = tk.Canvas(search_database_window, height=300, width=300, bg="#367800")
		search_database_canvas.pack()

		current_database_label = tk.Label(search_database_window,text=f"Current Database is {currentDatabase}",font="Times")
		current_database_label.place(relx=0.5,rely=0.1,anchor="n",relheight=0.1,relwidth=0.8)

		search_by_name_entry = tk.Entry(search_database_window, font="Times")
		search_by_name_entry.place(relx=0.325,rely=0.3,anchor="n",relheight=0.1,relwidth=0.6)

		search_by_name_button = tk.Button(search_database_window, font=["Times",10], text="By Name",command=lambda: search_by_name(search_by_name_entry.get(),current_database))
		search_by_name_button.place(relx=0.8,rely=0.3,anchor="n",relheight=0.1,relwidth=0.3)

		search_by_last_entry = tk.Entry(search_database_window, font="Times")
		search_by_last_entry.place(relx=0.325,rely=0.5,anchor="n",relheight=0.1,relwidth=0.6)

		search_by_last_button = tk.Button(search_database_window, font=["Times",10],text="By Last Name",command=lambda: search_by_last(search_by_last_entry.get(),current_database))
		search_by_last_button.place(relx=0.8,rely=0.5,anchor="n",relheight=0.1,relwidth=0.3)

		search_by_email_entry = tk.Entry(search_database_window, font="Times")
		search_by_email_entry.place(relx=0.325,rely=0.7,anchor="n",relheight=0.1,relwidth=0.6)

		search_by_email_button = tk.Button(search_database_window, font=["Times",10],text="By Email",command=lambda: search_by_email(search_by_email_entry.get(),current_database))
		search_by_email_button.place(relx=0.8,rely=0.7,anchor="n",relheight=0.1,relwidth=0.3)

		back3_button = tk.Button(search_database_window,text="Back",font="Times",command=lambda: [search_database_window.destroy(),searchdatabutton.config(state="normal")])
		back3_button.place(relx=0.5,rely=0.875,anchor="n",relheight=0.1,relwidth=0.4)

		search_database_window.mainloop()

def delete_data_window(currentDatabase):
	
	def delete_data(option):
		conn = sqlite3.connect(f"{currentDatabase}")
		c = conn.cursor()
		with conn:
			c.execute("DELETE FROM users WHERE email=?",(option[2],))

	def accept_data_deleted():
		accept = tk.Tk()
		accept.title("Delete Data")
		accept.resizable(False,False)
		accept_canvas = tk.Canvas(accept,height=100,width=200)
		accept_canvas.pack()
		accept_frame = tk.Frame(accept)
		accept_frame.place(relheight=1,relwidth=1)
		accept_label = tk.Label(accept_frame,text="Data has been Deleted")
		accept_label.place(relx=0.5,rely=0.3,relheight=0.2,relwidth=1,anchor="n")
		accept_button = tk.Button(accept_frame,text="OK",command=lambda: exit(accept))
		accept_button.place(relx=0.5,rely=0.7,relheight=0.2,relwidth=0.3,anchor="n")
		accept.mainloop()
		


	if currentDatabase == "":
		mainlabel["text"] = "No Database is Selected"

	else:
		delete_data_window = tk.Tk()
		delete_data_window.title("Delete Data")
		delete_data_window.resizable(False,False)

		delete_data_canvas = tk.Canvas(delete_data_window,height=300,width=400)
		delete_data_canvas.pack()

		selection = []
		conn = sqlite3.connect(f"{currentDatabase}")
		c = conn.cursor()
		with conn:
			c.execute("SELECT * FROM users")
		selection = c.fetchall()
		userlist = []
		for user in selection:
			userlist.append(list(user))

		delete_listbox = tk.Listbox(delete_data_canvas,selectmode="single")
		for user in userlist:
			delete_listbox.insert("end",user)
		delete_listbox.place(relx=0.5,rely=0.1,anchor="n",relwidth=0.8)

		back7_button = tk.Button(delete_data_canvas,text="Back",font="Times",command=lambda: delete_data_window.destroy())
		back7_button.place(relx=0.7,rely=0.875,anchor="n",relheight=0.1,relwidth=0.4)

		delete_button = tk.Button(delete_data_canvas,text="Delete",font="Times",command=lambda: [delete_data(delete_listbox.get(delete_listbox.curselection())),accept_data_deleted()])
		delete_button.place(relx=0.3,rely=0.875,anchor="n",relheight=0.1,relwidth=0.4)

		delete_data_window.mainloop()



HEIGHT = 600
WIDTH = 600

root = tk.Tk()
root.title("Database Manager")
root.resizable(False,False)

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH,bg="black")
canvas.pack()

frame = tk.Frame(root,bg="#367800",bd=3)
frame.place(relx=0.5,rely=0.1,relheight=0.175,relwidth=0.9,anchor="n")

frame_bottom = tk.Frame(root,bg="#367800",bd=6)
frame_bottom.place(relx=0.5,rely=0.3,relheight=0.6,relwidth=0.9,anchor="n")

frame_exit = tk.Frame(root,bg="#367800")
frame_exit.place(relx=0.5,rely=0.93,relheight=0.05,relwidth=0.2,anchor="n")

firstentry = tk.Entry(frame,font="Times")
firstentry.place(relx=0.2,rely=0.1,relheight=0.2,relwidth=0.2)

firstlabel = tk.Label(frame,text="Name",font="Times",bg="#367800",fg="white")
firstlabel.place(relx=0.01,rely=0.1,relheight=0.2,relwidth=0.175)

lastentry = tk.Entry(frame,font="Times")
lastentry.place(relx=0.2,rely=0.4,relheight=0.2,relwidth=0.2)

lastlabel = tk.Label(frame,text="Last Name",font="Times",bg="#367800",fg="white")
lastlabel.place(relx=0.01,rely=0.4,relheight=0.2,relwidth=0.175)

emailentry = tk.Entry(frame,font="Times")
emailentry.place(relx=0.2,rely=0.7,relheight=0.2,relwidth=0.3)

emaillabel = tk.Label(frame,text="Email",font="Times",bg="#367800",fg="white")
emaillabel.place(relx=0.01,rely=0.7,relheight=0.2,relwidth=0.175)

includebutton = tk.Button(frame, text="Include Data", font=["Times",10], command=lambda: include_database(firstentry.get(),
lastentry.get(),emailentry.get(),current_database))
includebutton.place(relx=0.9,rely=0.2,relheight=0.2,relwidth=0.3,anchor="e")

searchdatabutton = tk.Button(frame, text="Search Data", font=["Times",10], command= lambda: search_database_window(current_database))
searchdatabutton.place(relx=0.9,rely=0.4,relheight=0.2,relwidth=0.3,anchor="e")

erasedatabutton = tk.Button(frame, text="Delete Data", font=["Times",10], command= lambda: delete_data_window(current_database))
erasedatabutton.place(relx=0.9,rely=0.6,relheight=0.2,relwidth=0.3,anchor="e")

createdatabutton = tk.Button(frame, text="Create Database", font=["Times",10], command= lambda: add_database_window())
createdatabutton.place(relx=0.75,rely=0.9,relheight=0.2,relwidth=0.2,anchor="e")

selectdatabutton = tk.Button(frame, text="Select Database", font=["Times",10], command= lambda: select_database_window())
selectdatabutton.place(relx=0.975,rely=0.9,relheight=0.2,relwidth=0.2,anchor="e")

mainlabel = tk.Label(frame_bottom,text="",font=["Times",15])
mainlabel.place(relwidth=1,relheight=1)

exitbutton = tk.Button(frame_exit,text="Exit",font=["Times",10],command=lambda: exit(root))
exitbutton.place(relheight=1,relwidth=1)

root.mainloop()