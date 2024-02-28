import tkinter as tk
from tkinter import messagebox

def save_password():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    with open("passwords.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    messagebox.showinfo("Success", "Password saved successfully.")

def retrieve_password():
    username = username_entry.get()

    if not username:
        messagebox.showerror("Error", "Please enter the username to retrieve password.")
        return

    found = False
    with open("passwords.txt", "r") as file:
        for line in file:
            if line.startswith(username + ":"):
                password = line.split(":")[1].strip()
                messagebox.showinfo("Success", f"Retrieved Password: {password}")
                found = True
                break
    if not found:
        messagebox.showerror("Error", "Password not found.")

# Initialize Tkinter
root = tk.Tk()
root.title("Password Manager")

# Create GUI components
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.grid(row=2, column=0, columnspan=2, pady=10)

retrieve_button = tk.Button(root, text="Retrieve Password", command=retrieve_password)
retrieve_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()