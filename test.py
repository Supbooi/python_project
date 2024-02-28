import tkinter as tk
from tkinter import messagebox
from random import randint

def generate_password():
    password = ''.join(chr(randint(33, 126)) for _ in range(12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def save_password():
    password = password_entry.get()
    if password:
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")
        messagebox.showinfo("Success", "Password saved successfully!")
    else:
        messagebox.showwarning("Error", "Please generate a password first.")

# Create main window
root = tk.Tk()
root.title("Password Manager")

# Frame to hold widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Label for password entry
password_label = tk.Label(frame, text="Password:")
password_label.grid(row=0, column=0, padx=5, pady=5)

# Entry for password
password_entry = tk.Entry(frame, width=30)
password_entry.grid(row=0, column=1, padx=5, pady=5)

# Button to generate password
generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=5)

# Button to save password
save_button = tk.Button(frame, text="Save Password", command=save_password)
save_button.grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()
