import tkinter as tk
from tkinter import messagebox

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("300x200")

        self.accounts = {}

        self.label = tk.Label(self.master, text="Enter Account:")
        self.label.pack()

        self.account_entry = tk.Entry(self.master)
        self.account_entry.pack()

        self.label2 = tk.Label(self.master, text="Enter Password:")
        self.label2.pack()

        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.save_button = tk.Button(self.master, text="Save Password", command=self.save_password)
        self.save_button.pack()

        self.retrieve_button = tk.Button(self.master, text="Retrieve Password", command=self.retrieve_password)
        self.retrieve_button.pack()

    def save_password(self):
        account = self.account_entry.get()
        password = self.password_entry.get()

        if account and password:
            self.accounts[account] = password
            messagebox.showinfo("Success", "Password saved successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter both account and password!")

    def retrieve_password(self):
        account = self.account_entry.get()

        if account in self.accounts:
            password = self.accounts[account]
            messagebox.showinfo("Password", f"Password for {account}: {password}")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"No password found for account: {account}")

    def clear_entries(self):
        self.account_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    password_manager = PasswordManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
