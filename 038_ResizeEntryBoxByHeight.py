import tkinter as tk

root = tk.Tk()
root.title("Codemy")
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x400")

def myClick():
    hello = "Hello " + e.get()
    myLabel = tk.Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.pack(padx=10, pady=10)

e = tk.Entry(root, width=50, font=('Helvetica', 24))
e.pack(padx=10, pady=10)

myButton = tk.Button(root, text="Enter Your Name", command=myClick)
myButton.pack(pady=10)

root.mainloop()