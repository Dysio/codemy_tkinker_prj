import tkinter as tk

root = tk.Tk()

def myClick():
    myLabel = tk.Label(root, text="Look I clicked a Button!")
    myLabel.pack()

# myLabel1 = tk.Label(root, text="Hello World!")
# myLabel2 = tk.Label(root, text="My name is John Elder")
#
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)

myButton = tk.Button(root, text="Click Me", padx=10, pady=10, bg="green", command=myClick)
myButton.pack()

root.mainloop()