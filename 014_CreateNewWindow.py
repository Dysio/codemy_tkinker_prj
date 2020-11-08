import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Learn to code at Codemy')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')

def open():
    global my_img
    top = tk.Toplevel()
    top.title('Top Window')
    top.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
    # lbl = tk.Label(top, text="Hello World").pack()
    my_img = ImageTk.PhotoImage(Image.open("images/audi-logo.png"))
    my_label = tk.Label(top, image=my_img).pack()
    btn2 = tk.Button(top, text="Close window", command=top.destroy).pack()

btn = tk.Button(root, text='Open Second Window', command=open).pack()


root.mainloop()