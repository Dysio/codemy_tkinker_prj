import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("Codemy")
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x400")

# Databases

# Connect a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses
    first_name text,
    last_name text,
    address test,
    city text,
    state text,
    zipcode integer
""")

# Commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()
