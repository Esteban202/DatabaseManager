import tkinter as tk
import sqlite3
import os


def include_database(first,last,email,currentDatabase):
	def error_include():
		error_include = tk.Tk()
		error_include.title("Error")
		error_include.resizable(False,False)
		error_include_canvas = tk.Canvas(error_include,height=100,width=300)
		error_include_canvas.pack()
		error_include_frame = tk.Frame(error_include)
		error_include_frame.place(relheight=1,relwidth=1)
		error_include_label = tk.Label(error_include_frame,text="Please enter values for all the fields")
		error_include_label.place(relx=0.5,rely=0.3,relheight=0.2,relwidth=1,anchor="n")
		error_include_button = tk.Button(error_include_frame,text="OK",command=lambda: error_include.destroy())
		error_include_button.place(relx=0.5,rely=0.7,relheight=0.2,relwidth=0.3,anchor="n")
		error_include.mainloop()

	def data_updated(currentDatabase):
		data_updated = tk.Tk()
		data_updated.title("Updated Data")
		data_updated.resizable(False,False)
		data_updated_canvas = tk.Canvas(data_updated,height=100,width=300)
		data_updated_canvas.pack()
		data_updated_frame = tk.Frame(data_updated)
		data_updated_frame.place(relheight=1,relwidth=1)
		data_updated_label = tk.Label(data_updated_frame,text=f"Data in {currentDatabase} has been added")
		data_updated_label.place(relx=0.5,rely=0.3,relheight=0.2,relwidth=1,anchor="n")
		data_updated_button = tk.Button(data_updated_frame,text="OK",command=lambda: data_updated.destroy())
		data_updated_button.place(relx=0.5,rely=0.7,relheight=0.2,relwidth=0.3,anchor="n")
		data_updated.mainloop()

	def no_database():
		no_database = tk.Tk()
		no_database.title("Error")
		no_database.resizable(False,False)
		no_database_canvas = tk.Canvas(no_database,height=100,width=300)
		no_database_canvas.pack()
		no_database_frame = tk.Frame(no_database)
		no_database_frame.place(relheight=1,relwidth=1)
		no_database_label = tk.Label(no_database_frame,text=f"Please select a Database")
		no_database_label.place(relx=0.5,rely=0.3,relheight=0.2,relwidth=1,anchor="n")
		no_database_button = tk.Button(no_database_frame,text="OK",command=lambda: exit(no_database))
		no_database_button.place(relx=0.5,rely=0.7,relheight=0.2,relwidth=0.3,anchor="n")
		no_database.mainloop()

	if first != "" and last != "" and email != "":
		if currentDatabase != "":
			conn = sqlite3.connect(f"{currentDatabase}")
			c = conn.cursor()
			with conn:
				c.execute("INSERT INTO users VALUES(?,?,?)",(first,last,email))
			data_updated(currentDatabase)
		else:
			no_database()
	else:
		error_include()