import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Codemy')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x400")

def show():
    myLabel = tk.Label(root, text=var.get()).pack()

# var = tk.IntVar()
var = tk.StringVar()

c = tk.Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myLabel = tk.Label(root, text=var.get()).pack()

myButton = tk.Button(root, text="Show Selection", command=show).pack()

root.mainloop()