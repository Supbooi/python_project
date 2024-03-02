import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  
import pymysql

def homepage():
    root.destroy()
    import Home_page


def add_password(conn, cursor):
    password_reason = entry_reason.get()
    username = entry_username.get()
    password = entry_password.get()

    if password_reason and username and password:
        # Check if the username already exists
        cursor.execute("SELECT * FROM passwords WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            messagebox.showerror("Error", "Username already exists!")
        else:
            # Insert the new entry if the username is unique
            cursor.execute("INSERT INTO passwords (password_reason, username, password) VALUES (%s, %s, %s)", (password_reason, username, password))
            conn.commit()
            messagebox.showinfo("Success", "Password added successfully!")
    else:
        messagebox.showerror("Error", "Please fill all the fields.")

def delete_password(conn, cursor):
    password_reason = entry_reason.get()
    if password_reason:
        cursor.execute("DELETE FROM passwords WHERE password_reason = %s", (password_reason,))
        conn.commit()
        messagebox.showinfo("Success", "Password deleted successfully!")
    else:
        messagebox.showerror("Error", "Please enter the password reason.")

def update_password(conn, cursor):
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

def close_window(conn, root):
    conn.close()
    root.destroy()

# def show_data(conn, cursor):
#     top = tk.Toplevel()
#     top.title("Database Entries")

#     tree = ttk.Treeview(top)
#     tree["columns"] = ("Password Reason", "Username", "Password")
#     tree.heading("#0", text="ID")
#     tree.heading("Password Reason", text="Password Reason")
#     tree.heading("Username", text="Username")
#     tree.heading("Password", text="Password")

#     cursor.execute("SELECT * FROM passwords")
#     rows = cursor.fetchall()
#     for row in rows:
#         tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3]))

#     tree.pack(expand=True, fill="both")

root = tk.Tk()
root.title("Password Manager")
root.geometry("1222x701")
root.iconbitmap("1st.ico")
root.resizable(False,False)

image = Image.open('data_protection.png')
image= image.resize((1230,700))

img= ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=img, border=0)
background_label.place(x=0, y=0,relwidth=1,relheight=1)

# Calculate frame position to keep it centered
frame_width = 1000
frame_height = 600
x_position = (root.winfo_screenwidth() // 2) - (frame_width // 2)
y_position = (root.winfo_screenheight() // 2) - (frame_height // 2)

frame = tk.Frame(root, width=frame_width, height=frame_height, bg='#10303f')
frame.place(x=x_position, y=y_position)

label_reason = tk.Label(frame, text="Password Reason:",fg='white', bg='#10303f', font=('Arial', 20, 'bold'))
label_reason.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry_reason = tk.Entry(frame, width=30, font=("Helvetica", 16), bg='white', fg='black')
entry_reason.grid(row=0, column=1, padx=5, pady=5)

label_username = tk.Label(frame, text="Username:",fg='white', bg='#10303f', font=('Arial', 20, 'bold'))
label_username.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry_username = tk.Entry(frame, width=30, font=("Helvetica", 16), bg='white', fg='black')
entry_username.grid(row=1, column=1, padx=5, pady=5)

label_password = tk.Label(frame, text="Password:",fg='white', bg='#10303f', font=('Arial', 20, 'bold'))
label_password.grid(row=2, column=0, sticky="w", padx=5, pady=5)

entry_password = tk.Entry(frame, width=30, font=("Helvetica", 16), bg='white', fg='black')
entry_password.grid(row=2, column=1, padx=5, pady=5)

label_new_password = tk.Label(frame, text="New Password:",fg='white', bg='#10303f', font=('Arial', 20, 'bold'))
label_new_password.grid(row=3, column=0, sticky="w", padx=5, pady=5)

entry_new_password = tk.Entry(frame, width=30, font=("Helvetica", 16), bg='white', fg='black')
entry_new_password.grid(row=3, column=1, padx=5, pady=5)

button_add = tk.Button(frame, text="Add Password",bg='#1cb4c3', fg='white', font=('Arial', 12, 'bold'), border=1, command=lambda: add_password(conn, cursor))
button_add.grid(row=4, column=0, padx=5, pady=5)

button_delete = tk.Button(frame, text="Delete Password",bg='#1cb4c3', fg='white', font=('Arial', 12, 'bold'), border=1, command=lambda: delete_password(conn, cursor))
button_delete.grid(row=4, column=1, padx=5, pady=5)

button_update = tk.Button(frame, text="Update Password",bg='#1cb4c3', fg='white', font=('Arial', 12, 'bold'), border=1, command=lambda: update_password(conn, cursor))
button_update.grid(row=5, column=0, padx=5, pady=5)

button_clear = tk.Button(frame, text="Clear Entries",bg='#1cb4c3', fg='white', font=('Arial', 12, 'bold'), border=1, command=clear_entries)
button_clear.grid(row=5, column=1, padx=5, pady=5)

# button_show_data = tk.Button(frame, text="Show Database Entries",bg='#1cb4c3', fg='white', font=('Arial', 12, 'bold'), border=1, command=lambda: show_data(conn, cursor))
# button_show_data.grid(row=6, columnspan=2, padx=5, pady=5)

button_exit = tk.Button(frame, text="Exit",bg='#1cb4c3', fg='white', font=('Arial', 12, 'bold'), border=3, command=lambda: close_window(conn, root))
button_exit.grid(row=7, columnspan=2, padx=5, pady=5)

# Connect to MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='plmokn@12',
    database='password_manager'
)

cursor = conn.cursor()

back_to_home_page=tk.Button(text='HOME', fg='white', bg='#1976a8', font=('Arial', 12,'bold'),command=homepage)
back_to_home_page.place(x=70, y=10)

root.mainloop()

