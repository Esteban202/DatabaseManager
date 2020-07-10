import tkinter as tk
import sqlite3
import os

def add_database_window():
	
	def accept_data_created():
		accept = tk.Tk()
		accept.title("Create Database")
		accept.resizable(False,False)
		accept_canvas = tk.Canvas(accept,height=100,width=200)
		accept_canvas.pack()
		accept_frame = tk.Frame(accept)
		accept_frame.place(relheight=1,relwidth=1)
		accept_label = tk.Label(accept_frame,text="Database created succesfully")
		accept_label.place(relx=0.5,rely=0.3,relheight=0.2,relwidth=1,anchor="n")
		accept_button = tk.Button(accept_frame,text="OK",command=lambda: accept.destroy())
		accept_button.place(relx=0.5,rely=0.7,relheight=0.2,relwidth=0.3,anchor="n")
		accept.mainloop()

	def error_data_created():
		error = tk.Tk()
		error.title("Create Database")
		error.resizable(False,False)
		error_canvas = tk.Canvas(error,height=100,width=300)
		error_canvas.pack()
		error_frame = tk.Frame(error)
		error_frame.place(relheight=1,relwidth=1)
		error_label = tk.Label(error_frame,text="Error! There is already a Database with that name.")
		error_label.place(relx=0.5,rely=0.3,relheight=0.2,relwidth=1,anchor="n")
		error_button = tk.Button(error_frame,text="OK",command=lambda: error.destroy())
		error_button.place(relx=0.5,rely=0.7,relheight=0.2,relwidth=0.3,anchor="n")
		error.mainloop()

	def create_database(Name):
		try:
			createdatabutton.config(state="normal")
			conn = sqlite3.connect(f"{Name}.db")
			c = conn.cursor()
			with conn:
				c.execute("""CREATE TABLE users(
							first text,
							last text,
							email text
						)""")
			add_database_window.destroy()
			accept_data_created()
		except sqlite3.OperationalError:
			error_data_created()

	add_database_window = tk.Tk()
	add_database_window.title("Create new Database")
	add_database_window.resizable(False,False)
	
	canvas = tk.Canvas(add_database_window, height=100, width=300, bg="black")
	canvas.pack()

	database_name_entry = tk.Entry(add_database_window,font="Times")
	database_name_entry.place(relx=0.7,rely=0.3,relheight=0.2,relwidth=0.55,anchor="n")

	label = tk.Label(add_database_window,text="Name",font="Times",bg="#367800",fg="white")
	label.place(relx=0.22,rely=0.3,relheight=0.2,relwidth=0.4,anchor="n")

	create_button = tk.Button(add_database_window,text="Create",font="Times",command=lambda: create_database(database_name_entry.get()))
	create_button.place(relx=0.3,rely=0.7,anchor="n",relheight=0.2,relwidth=0.4) 
	back_button = tk.Button(add_database_window,text="Back",font="Times",command=lambda: (add_database_window.destroy()))
	back_button.place(relx=0.7,rely=0.7,anchor="n",relheight=0.2,relwidth=0.4) 

	add_database_window.mainloop()