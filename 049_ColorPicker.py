import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title('Codemy')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x400")

def color():
    my_color = colorchooser.askcolor()[1]
    my_label = tk.Label(root, text=my_color).pack(pady=10)
    my_label2 = tk.Label(root, text="You picked a Color!", font=("Helveetica", 32), bg=my_color).pack()

my_button = tk.Button(root, text="Pick A Color", command=color).pack()


root.mainloop()