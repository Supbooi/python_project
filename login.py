import tkinter as tk
from tkinter import messagebox
import pymysql

def register_page():
    root.destroy()
    import sign_in

def login_user():
    username = user_entry.get()
    user_password = password_entry.get()

    if not username or not user_password:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        connection = pymysql.connect(host='localhost', user='root', password='plmokn@12', database='userdata')
        cursor = connection.cursor()
    except:
        messagebox.showerror("Error","Invalid Connection")
        return

    query = 'SELECT * FROM data WHERE username=%s AND password=%s'
    cursor.execute(query, (username, user_password))
    row = cursor.fetchone()

    if row == None:
        messagebox.showerror("Error","Invalid Username or Password")
    else:
        messagebox.showinfo("Succes","Login in sucessfull")

    root.destroy()
    import Home_page
       
root = tk.Tk()
root.title('LOGIN')
root.geometry('925x500+300+200')
root.configure(bg='#f0f0f0')
root.iconbitmap("1st.ico")
root.resizable(False,False)

# Frame for Login
frame = tk.Frame(root, width=350, height=350, bg='#f0f0f0')
frame.place(x=480, y=70)

# Username animation
def on_enter(e):
    user_entry.delete(0,'end')

def on_leave(e):
    name=user_entry.get()
    if name=="":
        user_entry.insert(0,'Username')
 
# Username Entry
user_entry = tk.Entry(frame, width=30, fg='black', border=0, bg='white', font=('Arial', 12))
user_entry.place(x=40, y=80)
user_entry.insert(0, 'Username')
user_entry.bind('<FocusIn>',on_enter)
user_entry.bind('<FocusOut>',on_leave)

# Password animation
def on_enter(e):
    password_entry.delete(0,'end')

def on_leave(e):
    name=password_entry.get()
    if name=="":
        password_entry.insert(0,'Password')

# Password Entry
password_entry = tk.Entry(frame, width=30, fg='black', border=0, bg='white', font=('Arial', 12), show='*')
password_entry.place(x=40, y=150)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>',on_enter)
password_entry.bind('<FocusOut>',on_leave)

# Background Image
img = tk.PhotoImage(file='log.png')
background_label = tk.Label(root, image=img, bg='#f0f0f0')
background_label.place(x=50, y=50)

# Heading
heading = tk.Label(frame, text='Sign in', fg='#c69512', bg='#f0f0f0', font=('Arial', 24, 'bold'))
heading.place(x=130, y=5)

# Sign In Button
sign_in_button = tk.Button(frame, width=45, pady=10, text='Sign in', bg='#c69512', fg='white', font=('Arial', 12, 'bold'), border=0, command=login_user)
sign_in_button.place(x=10, y=220)

# Create Account Label
create_account_label = tk.Label(frame, text='Create Account ?', fg='black', bg='#f0f0f0', font=('Arial', 10))
create_account_label.place(x=130, y=270)

# Sign Up Button
sign_up_button = tk.Button(frame, width=8, text='Sign up', border=0, bg='#f0f0f0', fg='#57a1f8', font=('Arial', 10, 'underline'), cursor='hand2',command=register_page)
sign_up_button.place(x=265, y=270)

root.mainloop()
