import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()
root.title('Codemy')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x400")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 200)
    plt.show()

my_button = tk.Button(root, text="Graph it!", command=graph)
my_button.pack()

root.mainloop()