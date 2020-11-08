import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.title('Codemy')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')

# root.filename = filedialog.askopenfilename(initialdir="images", title="Select a file", filetypes=(("png files", "*.png"),("all files","*.*")))

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="images", title="Select a file",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_Label = tk.Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = tk.Label(root, image=my_image).pack()

my_btn = tk.Button(root, text="Open file", command=open).pack()

root.mainloop()