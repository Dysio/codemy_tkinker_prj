import tkinter as tk

root = tk.Tk()
root.title("Codemy")
root.iconbitmap("")
root.geometry("470x400")
'''
def myDelete():
    # myLabel.pack_forget()
    # myLabel.grid_forget()
    myLabel.destroy()
    # myButton['state'] = tk.NORMAL
    print(myButton.winfo_exists())
'''

# myLabel = tk.Label(root)

def enter_name_cmd():
    global myLabel
    myLabel = tk.Label(root)
    myLabel.destroy()
    label_text = f"Hello {name_entry_box.get()}"
    name_entry_box.delete(0, 'end')
    myLabel = tk.Label(root, text=label_text)
    myLabel.grid(row=3, column=0, pady=10)
    # myButton['state'] = tk.DISABLED


name_entry_box = tk.Entry(root, font=("Helvetica", 25), width=25)
name_entry_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

myButton = tk.Button(root, text="Enter Your Name", command=enter_name_cmd)
myButton.grid(row=1, column=0,pady=10)

# deleteButton = tk.Button(root, text="Delete Text", command=myDelete)
# deleteButton.grid(row=2, column=0, pady=10)

root.mainloop()