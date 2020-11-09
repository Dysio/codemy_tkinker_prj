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
# c.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address test,
#     city text,
#     state text,
#     zipcode integer
#     )""")

def submit():
    # Connect a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
              {
                  'f_name':f_name.get(),
                  'l_name':l_name.get(),
                  'address':address.get(),
                  'city':city.get(),
                  'state':state.get(),
                  'zipcode':zipcode.get()
              })

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

    f_name.delete(0, tk.END)
    l_name.delete(0, tk.END)
    address.delete(0, tk.END)
    city.delete(0, tk.END)
    state.delete(0, tk.END)
    zipcode.delete(0, tk.END)


def query():
    # Connect a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    # Loop Thru Results
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()


f_name = tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = tk.Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = tk.Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = tk.Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = tk.Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = tk.Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Create Text Box Labels
label_dict = {
    "f_name_label":"First Name",
    "l_name_label":"Last Name",
    "address_label":"Address",
    "city":"City",
    "state":"State",
    "zipcode":"Zipcode",
}

# f_name_label = tk.Label(root, text="First Name")
# f_name_label.grid()

for r_num, key in enumerate(label_dict):
    key = tk.Label(root, text=label_dict[key])
    key.grid(row=r_num, column=0)


# Create Submit Button
submit_btn = tk.Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create Query Button
query_btn = tk.Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


# Commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()
