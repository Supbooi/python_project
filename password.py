import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql

def add_password():
    password_reason = entry_reason.get()
    username = entry_username.get()
    password = entry_password.get()

    if password_reason and username and password:
        cursor.execute("INSERT INTO password_manager (password_reason, username, password) VALUES (%s, %s, %s)", (password_reason, username, password))
        conn.commit()
        messagebox.showinfo("Success", "Password added successfully!")
    else:
        messagebox.showerror("Error", "Please fill all the fields.")

def delete_password():
    password_reason = entry_reason.get()
    if password_reason:
        cursor.execute("DELETE FROM password_manager WHERE password_reason = %s", (password_reason,))
        conn.commit()
        messagebox.showinfo("Success", "Password deleted successfully!")
    else:
        messagebox.showerror("Error", "Please enter the password reason.")

def update_password():
    password_reason = entry_reason.get()
    new_password = entry_new_password.get()
    if password_reason and new_password:
        cursor.execute("UPDATE password_manager SET password = %s WHERE password_reason = %s", (new_password, password_reason))
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

root = tk.Tk()
root.title("Password Management System")
root.geometry("1222x701")
root.iconbitmap("1st.ico")
root.resizable(False,False)

image = Image.open('data_protection.png')
image= image.resize((1230,700))

img= ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=img, border=0)
background_label.place(x=0, y=0,relwidth=1,relheight=1)


frame = tk.Frame(root)
frame.pack(padx=10, pady=100)

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

button_exit = tk.Button(frame, text="Exit", command=close_window)
button_exit.grid(row=6, columnspan=2, padx=5, pady=5)

# Connect to MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='plmokn@12',
    database='password_manager'
)

cursor = conn.cursor()

# Create passwords table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS password_manager (
        id INT AUTO_INCREMENT PRIMARY KEY,
        password_reason VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

root.mainloop()
