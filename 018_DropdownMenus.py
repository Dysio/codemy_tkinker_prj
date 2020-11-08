import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Codemy')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x400")

# Drop Down Boxes

def show():
    myLabel = tk.Label(root, text=clicked.get()).pack()

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"]

clicked = tk.StringVar()
clicked.set(options[0])

drop = tk.OptionMenu(root, clicked, *options)
drop.pack()

myButton = tk.Button(root, text="Show Selection", command=show).pack()

root.mainloop()