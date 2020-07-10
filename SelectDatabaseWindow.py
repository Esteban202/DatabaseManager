import tkinter as tk
import sqlite3
import os

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
	select_database_window.destroy()])
	select_button.place(relx=0.3,rely=0.7,anchor="n",relheight=0.1,relwidth=0.4)

	back2_button = tk.Button(select_database_window,text="Back",font="Times",command=lambda: select_database_window.destroy())
	back2_button.place(relx=0.7,rely=0.7,anchor="n",relheight=0.1,relwidth=0.4) 

	select_database_window.mainloop()