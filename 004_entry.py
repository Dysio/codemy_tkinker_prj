import tkinter as tk

root = tk.Tk()

e = tk.Entry(root, width=50, bg="white", fg="black", borderwidth=5)
e.pack()
e.insert(0, "Enter your name")

def myClick():
    hello = "Hello " + e.get()
    # myLabel = tk.Label(root, text="Hello " + e.get())
    myLabel = tk.Label(root, text=hello)
    myLabel.pack()


myButton = tk.Button(root, text="Enter Your name", padx=10, pady=10, bg="green", command=myClick)
myButton.pack()

root.mainloop()
