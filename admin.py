import tkinter as tk
from tkinter import messagebox, ttk
import pymysql

def add_password():
    password_reason = entry_reason.get()
    username = entry_username.get()
    password = entry_password.get()

    if password_reason and username and password:
        cursor.execute("INSERT INTO passwords (password_reason, username, password) VALUES (%s, %s, %s)", (password_reason, username, password))
        conn.commit()
        messagebox.showinfo("Success", "Password added successfully!")
    else:
        messagebox.showerror("Error", "Please fill all the fields.")

def delete_password():
    password_reason = entry_reason.get()
    if password_reason:
        cursor.execute("DELETE FROM passwords WHERE password_reason = %s", (password_reason,))
        conn.commit()
        messagebox.showinfo("Success", "Password deleted successfully!")
    else:
        messagebox.showerror("Error", "Please enter the password reason.")

def update_password():
    password_reason = entry_reason.get()
    new_password = entry_new_password.get()
    if password_reason and new_password:
        cursor.execute("UPDATE passwords SET password = %s WHERE password_reason = %s", (new_password, password_reason))
        conn.commit()
        messagebox.showinfo("Success", "Password updated successfully!")
    else:
        messagebox.showerror("Error", "Please enter the password reason and new password.")

def clear_entries():
    entry_reason.delete(0, tk.END)
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_new_password.delete(0, tk.END)

def close_window():
    conn.close()
    root.destroy()

def show_data():
    top = tk.Toplevel()
    top.title("Database Entries")

    tree = ttk.Treeview(top)
    tree["columns"] = ("Password Reason", "Username", "Password")
    tree.heading("#0", text="ID")
    tree.heading("Password Reason", text="Password Reason")
    tree.heading("Username", text="Username")
    tree.heading("Password", text="Password")

    cursor.execute("SELECT * FROM passwords")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3]))

    tree.pack(expand=True, fill="both")

root = tk.Tk()
root.title("Admin Panel")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_reason = tk.Label(frame, text="Password Reason:")
label_reason.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry_reason = tk.Entry(frame, width=30)
entry_reason.grid(row=0, column=1, padx=5, pady=5)

label_username = tk.Label(frame, text="Username:")
label_username.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry_username = tk.Entry(frame, width=30)
entry_username.grid(row=1, column=1, padx=5, pady=5)

label_password = tk.Label(frame, text="Password:")
label_password.grid(row=2, column=0, sticky="w", padx=5, pady=5)

entry_password = tk.Entry(frame, width=30)
entry_password.grid(row=2, column=1, padx=5, pady=5)

label_new_password = tk.Label(frame, text="New Password:")
label_new_password.grid(row=3, column=0, sticky="w", padx=5, pady=5)

entry_new_password = tk.Entry(frame, width=30)
entry_new_password.grid(row=3, column=1, padx=5, pady=5)

button_add = tk.Button(frame, text="Add Password", command=add_password)
button_add.grid(row=4, column=0, padx=5, pady=5)

button_delete = tk.Button(frame, text="Delete Password", command=delete_password)
button_delete.grid(row=4, column=1, padx=5, pady=5)

button_update = tk.Button(frame, text="Update Password", command=update_password)
button_update.grid(row=5, column=0, padx=5, pady=5)

button_clear = tk.Button(frame, text="Clear Entries", command=clear_entries)
button_clear.grid(row=5, column=1, padx=5, pady=5)

button_show_data = tk.Button(frame, text="Show Database Entries", command=show_data)
button_show_data.grid(row=6, columnspan=2, padx=5, pady=5)

button_exit = tk.Button(frame, text="Exit", command=close_window)
button_exit.grid(row=7, columnspan=2, padx=5, pady=5)

# Connect to MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='plmokn@12',
    database='password_manager'
)

cursor = conn.cursor()

root.mainloop()
