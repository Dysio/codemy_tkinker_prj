import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Codemy.com")
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x400")

my_menu = tk.Menu(root)
root.config(menu=my_menu)

#click command
def our_command():
    myLabel = tk.Label(root, text="You clicked a dropdown menu.").pack()

def file_new():
    """File new fuction"""
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    myLabel = tk.Label(file_new_frame, text="You Clicked the File >> New Menu.").pack()

def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    myLabel = tk.Label(edit_cut_frame, text="You Clicked the Edit >> Cut Menu.").pack()


def hide_all_frames():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()

# Create a menu item
file_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu item
edit_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=our_command)

# Create an Options menu item
option_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find Next", command=our_command)

# Create some frames
file_new_frame = tk.Frame(root, width=400, height=400, bg="red")
edit_cut_frame = tk.Frame(root, width=400, height=400, bg="blue")


root.mainloop()