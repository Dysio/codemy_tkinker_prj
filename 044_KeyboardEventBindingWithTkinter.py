import tkinter as tk

root = tk.Tk()
root.title("Codemy.com")
root.iconbitmap("")
root.geometry("400x400")

def clicker(event):
    # myLabel = tk.Label(root, text="You clicked a button" + str(event.x) + " " + str(event.y))
    # myLabel = tk.Label(root, text="You clicked a button: " + str(event.char))
    myLabel = tk.Label(root, text="You clicked a button: " + event.keysym)
    myLabel.pack()

myButton = tk.Button(root, text="Click me!", command=clicker)
# myButton.bind("<Button-3>", clicker)
# myButton.bind("<Enter>", clicker)
# myButton.bind("<Leave>", clicker)
# myButton.bind("<FocusIn>", clicker)
# myButton.bind("<Return>", clicker)
myButton.bind("<Key>", clicker)
myButton.pack(pady=20)

root.mainloop()