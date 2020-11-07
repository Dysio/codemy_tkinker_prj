import tkinter as tk

root = tk.Tk()
root.title("Codemy")
root.iconbitmap("codemy.ico")


button_quit = tk.Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()