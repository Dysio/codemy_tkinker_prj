import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')

frame = tk.LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = tk.Button(frame, text="Don't Click Here")
b2 = tk.Button(frame, text=".... or here")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()