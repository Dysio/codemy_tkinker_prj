import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Codemy.com")
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x400")

myLabel = tk.Label(root, text='41' + u'\u00b0', font=("Helvetica", 32)).pack(pady=10)
myLabel = tk.Label(root, text='41' + u'\u00a9', font=("Helvetica", 32)).pack(pady=10)

my_button = tk.Button(root, text=u'\u00BB', font=("Helvetica", 32)).pack(pady=10)

root.mainloop()