import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Codemy Image Viewer")
root.iconbitmap("codemy.ico")

my_img1 = ImageTk.PhotoImage(Image.open("images/archangel.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/audi-logo.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/AudiRS7.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/DaftPunk.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/nissan_gtr_nismo.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = tk.Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=tk.SUNKEN, anchor=tk.E)

image_number = 0
my_label = tk.Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward():
    global my_label
    global button_forward
    global button_back
    global image_number

    if image_number < len(image_list) - 2:
        image_number += 1

    else:
        image_number = len(image_list) - 1
        button_forward = tk.Button(root, text=">>", state=tk.DISABLED)

    my_label.grid_forget()
    my_label = tk.Label(image=image_list[image_number])
    button_back = tk.Button(root, text="<<", command=lambda: back())

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1, column=2)

    status = tk.Label(root, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1,
                      relief=tk.SUNKEN, anchor=tk.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)


def back():
    global my_label
    global button_forward
    global button_back
    global image_number

    if image_number > 1:
        image_number -= 1

    else:
        image_number = 0
        button_back = tk.Button(root, text="<<", state=tk.DISABLED)

    my_label.grid_forget()
    my_label = tk.Label(image=image_list[image_number])
    button_forward = tk.Button(root, text=">>", command=lambda: forward())

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = tk.Label(root, text="Image " + str(image_number + 1) + " of " + str(len(image_list)), bd=1,
                      relief=tk.SUNKEN, anchor=tk.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)


button_back = tk.Button(root, text="<<", state=tk.DISABLED)
button_exit = tk.Button(root, text="Exit Program", command=root.quit)
button_forward = tk.Button(root, text=">>", command=lambda: forward())

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)


root.mainloop()