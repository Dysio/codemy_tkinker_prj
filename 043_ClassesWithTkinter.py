import tkinter as tk

root = tk.Tk()
root.title("Codemy.com")
root.iconbitmap("")
root.geometry("400x400")

class Elder:
    def __init__(self, master):
        myFrame = tk.Frame(master)
        myFrame.pack()

        self.myButton = tk.Button(master, text="Click me!", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("You clicked a button")

new_window = Elder(root)

root.mainloop()