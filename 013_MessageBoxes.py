import tkinter as tk
from PIL import ImageTk, Image
from tkinter import  messagebox

root = tk.Tk()
root.title('Codemy')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World!")
    tk.Label(root, text=response).pack()
    if response == 1:
        tk.Label(root, text="You clicked yes!").pack()
    else:
        tk.Label(root, text="You clicked no!").pack()



tk.Button(root, text="Popup", command=popup).pack()

tk.mainloop()