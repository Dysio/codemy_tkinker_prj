import tkinter as tk

root = tk.Tk()
root.title("Codemy")
root.iconbitmap("")
root.geometry("470x400")

def myDelete():
    # myLabel.pack_forget()
    myLabel.destroy()
    myButton['state'] = tk.NORMAL
    print(myButton.winfo_exists())

def enter_name_cmd():
    label_text = f"Hello {name_entry_box.get()}"
    name_entry_box.delete(0, 'end')
    global myLabel
    myLabel = tk.Label(root, text=label_text)
    myLabel.pack(pady=10)
    myButton['state'] = tk.DISABLED


name_entry_box = tk.Entry(root, font=("Helvetica", 25), width=25)
name_entry_box.pack(pady=10)

myButton = tk.Button(root, text="Enter Your Name", command=enter_name_cmd)
myButton.pack(pady=10)

deleteButton = tk.Button(root, text="Delete Text", command=myDelete)
deleteButton.pack(pady=10)

root.mainloop()