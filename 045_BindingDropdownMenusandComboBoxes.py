import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Codemy.com")
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x400")

def selected(self):
    if clicked.get() == "Friday":
        myLabel = tk.Label(root, text="It'f Friday night!").pack()
    else:
        myLabbel = tk.Label(root, text=clicked.get()).pack()

def comboclick(event):
    # myLabel = tk.Label(root, text=myCombo.get()).pack()
    if myCombo.get() == "Friday":
        myLabel = tk.Label(root, text="It'f Friday night!").pack()
    else:
        myLabbel = tk.Label(root, text=myCombo.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

clicked = tk.StringVar()
clicked.set(options[0])

drop = tk.OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()

# myButton = tk.Button(root, text="Print", command=selected)
# myButton.pack()

root.mainloop()