import tkinter as tk

root = tk.Tk()
root.title('Codemy')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x400")

# Panels
panel_1 = tk.PanedWindow(bd=4, relief="raised", bg="red")
panel_1.pack(fill=tk.BOTH, expand=1)

left_label = tk.Label(panel_1, text="Left Panel")
panel_1.add(left_label)

panel_2 = tk.PanedWindow(panel_1, orient=tk.VERTICAL, bd=4, relief="raised", bg="blue")
panel_1.add(panel_2)

top = tk.Label(panel_2, text="Top Panel")
panel_2.add(top)

bottom = tk.Label(panel_2, text="Bottom Panel")
panel_2.add(bottom)


root.mainloop()