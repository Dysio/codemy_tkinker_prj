import tkinter as tk
from tkinter import ttk

import mysql.connector
import csv

root = tk.Tk()
root.title('Codemy.com')
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("400x600")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "tomek710",
    auth_plugin = "mysql_native_password",
    database = "codemy",
)

print(mydb)

# Create a cursor and initialize it
my_cursor = mydb.cursor()

# Create database
# my_cursor.execute("CREATE DATABASE codemy")

# Test if database was created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# Create table
my_cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                  first_name VARCHAR(255),
                  last_name VARCHAR(255),
                  zipcode INT(10),
                  price_paid DECIMAL(10, 2),
                  user_id INT AUTO_INCREMENT PRIMARY KEY)""")

# Alter Table
# my_cursor.execute("""ALTER TABLE customers ADD (
#                     email VARCHAR(255),
#                     address_1 VARCHAR(255),
#                     address_2 VARCHAR(255),
#                     city VARCHAR(50),
#                     state VARCHAR(50),
#                     country VARCHAR(255),
#                     phone VARCHAR(255),
#                     payment_method VARCHAR(50),
#                     discount_code VARCHAR(255)
#                     )""")

# Show table
# my_cursor.execute("SELECT * FROM customers")
#
# for thing in my_cursor.description:
#     print(thing)

# Clear text fields
def clear_fields():
    """Clear Test Fields"""
    first_name_box.delete(0, tk.END)
    last_name_box.delete(0, tk.END)
    address1_box.delete(0, tk.END)
    address2_box.delete(0, tk.END)
    city_box.delete(0, tk.END)
    state_box.delete(0, tk.END)
    zipcode_box.delete(0, tk.END)
    country_box.delete(0, tk.END)
    phone_box.delete(0, tk.END)
    email_box.delete(0, tk.END)
    payment_method_box.delete(0, tk.END)
    discount_box.delete(0, tk.END)
    price_paid_box.delete(0, tk.END)

def add_customer():
    """Add Customer To Database"""
    sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address1_box.get(), address2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_box.get())
    my_cursor.execute(sql_command, values)

    #Commit the changes to database
    mydb.commit()

    clear_fields()

def write_to_csv(result):
    """Write To CSV Excel Function"""
    with open('customers.csv','w', newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)

def search_customers():
    search_customers = tk.Tk()
    search_customers.title("Search Customers")
    search_customers.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
    search_customers.geometry("1000x600")

    def update():
        sql_command = """UPDATE customers SET first_name=%s, last_name=%s, zipcode=%s, price_paid=%s, email=%s, address_1=%s, address_2=%s, city=%s, state=%s, country=%s, phone=%s, payment_method=%s, discount_code=%s WHERE user_id = %s"""

        first_name = first_name_box2.get()
        last_name = last_name_box2.get()
        zipcode = zipcode_box2.get()
        price_paid = price_paid_box2.get()
        email = email_box2.get()
        address1 = address1_box2.get()
        address2 = address2_box2.get()
        city = city_box2.get()
        state = state_box2.get()
        country = country_box2.get()
        phone = phone_box2.get()
        payment_method = payment_method_box2.get()
        discount_code = discount_box2.get()

        id_value = id_box2.get()
        inputs = (first_name, last_name, zipcode, price_paid, email, address1, address2, city, state, country, phone, payment_method, discount_code, id_value)

        my_cursor.execute(sql_command, inputs)
        mydb.commit()

        search_customers.destroy()

    def edit_now(id, index):
        sql2 = "SELECT * FROM customers WHERE user_id = %s"
        name2 = (id,)
        result2 = my_cursor.execute(sql2, name2)
        result2 = my_cursor.fetchall()

        index += 1
        # Create Main Form Top Enter Customer Data
        first_name_label = tk.Label(search_customers, text="First Name").grid(row=index+1, column=0, sticky=tk.W, padx=10, pady=10)
        last_name_label = tk.Label(search_customers, text="Last Name").grid(row=index+2, column=0, sticky=tk.W, padx=10)
        address1_label = tk.Label(search_customers, text="Address 1").grid(row=index+3, column=0, sticky=tk.W, padx=10)
        address2_label = tk.Label(search_customers, text="Address 2").grid(row=index+4, column=0, sticky=tk.W, padx=10)
        city_label = tk.Label(search_customers, text="City").grid(row=index+5, column=0, sticky=tk.W, padx=10)
        state_label = tk.Label(search_customers, text="State").grid(row=index+6, column=0, sticky=tk.W, padx=10)
        zipcode_label = tk.Label(search_customers, text="Zipcode").grid(row=index+7, column=0, sticky=tk.W, padx=10)
        country_label = tk.Label(search_customers, text="Country").grid(row=index+8, column=0, sticky=tk.W, padx=10)
        phone_label = tk.Label(search_customers, text="Phone Number").grid(row=index+9, column=0, sticky=tk.W, padx=10)
        email_label = tk.Label(search_customers, text="Email Address").grid(row=index+10, column=0, sticky=tk.W, padx=10)
        payment_method_label = tk.Label(search_customers, text="Payment Method").grid(row=index+11, column=0, sticky=tk.W, padx=10)
        discount_label = tk.Label(search_customers, text="Discount Code").grid(row=index+12, column=0, sticky=tk.W, padx=10)
        price_paid_label = tk.Label(search_customers, text="Price Paid").grid(row=index+13, column=0, sticky=tk.W, padx=10)
        id_label = tk.Label(search_customers, text="User ID").grid(row=index+14, column=0, sticky=tk.W, padx=10)
        # Create Entry Boxes
        global first_name_box2
        first_name_box2 = tk.Entry(search_customers)
        first_name_box2.grid(row=index+1, column=1, pady=10)
        first_name_box2.insert(0, result2[0][0])
        global last_name_box2
        last_name_box2 = tk.Entry(search_customers)
        last_name_box2.grid(row=index+2, column=1, pady=5)
        last_name_box2.insert(0, result2[0][1])
        global address1_box2
        address1_box2 = tk.Entry(search_customers)
        address1_box2.grid(row=index+3, column=1, pady=5)
        address1_box2.insert(0, result2[0][6])
        global address2_box2
        address2_box2 = tk.Entry(search_customers)
        address2_box2.grid(row=index+4, column=1, pady=5)
        address2_box2.insert(0, result2[0][7])
        global city_box2
        city_box2 = tk.Entry(search_customers)
        city_box2.grid(row=index+5, column=1, pady=5)
        city_box2.insert(0, result2[0][8])
        global state_box2
        state_box2 = tk.Entry(search_customers)
        state_box2.grid(row=index+6, column=1, pady=5)
        state_box2.insert(0, result2[0][9])
        global zipcode_box2
        zipcode_box2 = tk.Entry(search_customers)
        zipcode_box2.grid(row=index+7, column=1, pady=5)
        zipcode_box2.insert(0, result2[0][2])
        global country_box2
        country_box2 = tk.Entry(search_customers)
        country_box2.grid(row=index+8, column=1, pady=5)
        country_box2.insert(0, result2[0][10])
        global phone_box2
        phone_box2 = tk.Entry(search_customers)
        phone_box2.grid(row=index+9, column=1, pady=5)
        phone_box2.insert(0, result2[0][11])
        global email_box2
        email_box2 = tk.Entry(search_customers)
        email_box2.grid(row=index+10, column=1, pady=5)
        email_box2.insert(0, result2[0][5])
        global payment_method_box2
        payment_method_box2 = tk.Entry(search_customers)
        payment_method_box2.grid(row=index+11, column=1, pady=5)
        payment_method_box2.insert(0, result2[0][12])
        global discount_box2
        discount_box2 = tk.Entry(search_customers)
        discount_box2.grid(row=index+12, column=1, pady=5)
        discount_box2.insert(0, result2[0][13])
        global price_paid_box2
        price_paid_box2 = tk.Entry(search_customers)
        price_paid_box2.grid(row=index+13, column=1, pady=5)
        price_paid_box2.insert(0, result2[0][3])
        global id_box2
        id_box2 = tk.Entry(search_customers)
        id_box2.grid(row=index+14, column=1, pady=5)
        id_box2.insert(0, result2[0][4])

        save_record = tk.Button(search_customers, text="Update Record", command=update)
        save_record.grid(row=index+15, column=0, padx=10)


    def search_now():
        selected = drop.get()
        if selected == "Search by...":
            test = tk.Label(search_customers, text="Pick right selection")
            test.grid(row=2, column=0)
        elif selected == "Last name":
            sql = "SELECT * FROM customers WHERE last_name = %s"

        elif selected == "Email address":
            sql = "SELECT * FROM customers WHERE email = %s"

        elif selected == "Customer ID":
            sql = "SELECT * FROM customers WHERE user_id = %s"


        searched = search_box.get()
        # sql = "SELECT * FROM customers WHERE last_name = %s"
        name = (searched, )
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            result = "Record Not Found..."
            searched_label = tk.Label(search_customers, text=result)
            searched_label.grid(row=2, column=0, columnspan=2, padx=10)
        else:
            for index, x in enumerate(result):
                index += 2
                col = 0
                id_reference = str(x[4])
                print(id_reference)
                edit_button = tk.Button(search_customers, text=f"Edit ", command=lambda: edit_now(id_reference, index))
                edit_button.grid(row=index, column=col)
                for item in x:
                    searched_label = tk.Label(search_customers, text=item)
                    searched_label.grid(row=index, column=col+1, padx=10)
                    col += 1
            csv_button = tk.Button(search_customers, text="Save to Excel", command=lambda: write_to_csv(result))
            csv_button.grid(row=index + 1, column=0)


    #Entry box label search for customer
    search_box_label = tk.Label(search_customers, text="Search")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)
    #Entry Box to search for customer
    search_box = tk.Entry(search_customers)
    search_box.grid(row=0, column=1, padx=10, pady=10)
    #Entry box search Button for customer
    search_button = tk.Button(search_customers, text="Search Customers", command=search_now)
    search_button.grid(row=1, column=0, padx=10)
    # Dropdown box
    drop = ttk.Combobox(search_customers, value=["Search by...", "Last name", "Email address", "Customer ID"])
    drop.current(0)
    drop.grid(row=0, column=2)

def list_customers():
    """List of customers"""
    list_customer_query = tk.Toplevel()
    list_customer_query.title("List All Customers")
    list_customer_query.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
    list_customer_query.geometry("800x600")

    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()

    for index, x in enumerate(result):
        column_num = 0
        for y in x:
            lookup_label = tk.Label(list_customer_query, text=y)
            lookup_label.grid(row=index, column=column_num)
            column_num += 1

    csv_button = tk.Button(list_customer_query, text="Save to Excel", command=lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0)


# CREATE LABEL
title_label = tk.Label(root, text="Codemy Customer Database", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady="10")

# Create Main Form Top Enter Customer Data
first_name_label = tk.Label(root, text="First Name").grid(row=1, column=0, sticky=tk.W, padx=10)
last_name_label = tk.Label(root, text="Last Name").grid(row=2, column=0, sticky=tk.W, padx=10)
address1_label = tk.Label(root, text="Address 1").grid(row=3, column=0, sticky=tk.W, padx=10)
address2_label = tk.Label(root, text="Address 2").grid(row=4, column=0, sticky=tk.W, padx=10)
city_label = tk.Label(root, text="City").grid(row=5, column=0, sticky=tk.W, padx=10)
state_label = tk.Label(root, text="State").grid(row=6, column=0, sticky=tk.W, padx=10)
zipcode_label = tk.Label(root, text="Zipcode").grid(row=7, column=0, sticky=tk.W, padx=10)
country_label = tk.Label(root, text="Country").grid(row=8, column=0, sticky=tk.W, padx=10)
phone_label = tk.Label(root, text="Phone Number").grid(row=9, column=0, sticky=tk.W, padx=10)
email_label = tk.Label(root, text="Email Address").grid(row=10, column=0, sticky=tk.W, padx=10)
payment_method_label = tk.Label(root, text="Payment Method").grid(row=11, column=0, sticky=tk.W, padx=10)
discount_label = tk.Label(root, text="Discount Code").grid(row=12, column=0, sticky=tk.W, padx=10)
price_paid_label = tk.Label(root, text="Price Paid").grid(row=13, column=0, sticky=tk.W, padx=10)

first_name_box = tk.Entry(root)
first_name_box.grid(row=1, column=1)
last_name_box = tk.Entry(root)
last_name_box.grid(row=2, column=1, pady=5)
address1_box = tk.Entry(root)
address1_box.grid(row=3, column=1, pady=5)
address2_box = tk.Entry(root)
address2_box.grid(row=4, column=1, pady=5)
city_box = tk.Entry(root)
city_box.grid(row=5, column=1, pady=5)
state_box = tk.Entry(root)
state_box.grid(row=6, column=1, pady=5)
zipcode_box = tk.Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)
country_box = tk.Entry(root)
country_box.grid(row=8, column=1, pady=5)
phone_box = tk.Entry(root)
phone_box.grid(row=9, column=1, pady=5)
email_box = tk.Entry(root)
email_box.grid(row=10, column=1, pady=5)
payment_method_box = tk.Entry(root)
payment_method_box.grid(row=11, column=1, pady=5)
discount_box = tk.Entry(root)
discount_box.grid(row=12, column=1, pady=5)
price_paid_box = tk.Entry(root)
price_paid_box.grid(row=13, column=1, pady=5)


# Create Buttons
add_customer_button = tk.Button(root, text="Add Customer To Database", command=add_customer)
add_customer_button. grid(row=14, column=0, padx=10, pady=10)

clear_fields_button = tk.Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=14, column=1)
#listcustomers button
list_customers_button = tk.Button(root, text="List Customers", command=list_customers)
list_customers_button.grid(row=15, column=0, sticky=tk.W, padx=10)
#search customers
search_customers_button = tk.Button(root, text="Search/Edit Customers", command=search_customers)
search_customers_button.grid(row=15, column=1, sticky=tk.W, padx=10)

# print database records
# my_cursor.execute("SELECT * FROM customers")
# result = my_cursor.fetchall()
# for x in result:
#     print(x)

root.mainloop()