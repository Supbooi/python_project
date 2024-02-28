from tkinter import *
from tkinter import messagebox
import pymysql

def login_page():
    register.destroy()
    import login

def clear():
    username_UI.delete(0, END)
    password_UI.delete(0, END)
    confirm_password_UI.delete(0, END)

def database():
    if username_UI.get() == "" or password_UI.get() == "" or confirm_password_UI.get() == "":
        messagebox.showerror("Error", "All fields are required")
    elif password_UI.get() != confirm_password_UI.get():
        messagebox.showerror("Error", "Passwords do not match")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='plmokn@12')
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error", "Database connectivity issue. Please try again.")
            return 
        try:
            query = "CREATE DATABASE IF NOT EXISTS userdata"
            mycursor.execute(query)
            query = 'USE userdata'
            mycursor.execute(query)
            query = 'CREATE TABLE IF NOT EXISTS data(id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, username VARCHAR(100), password VARCHAR(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('USE userdata')
            
        query = 'SELECT * FROM data WHERE username=%s'
        mycursor.execute(query, (username_UI.get(),))
        row = mycursor.fetchone()
        if row is not None:
            messagebox.showerror("Error", "Username already exists")
        else:
            query = 'INSERT INTO data(username, password) VALUES(%s, %s)'
            mycursor.execute(query, (username_UI.get(), password_UI.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', "Registration is successful")
            clear()
            register.destroy()
            import login

register = Tk()
register.title("Register")
register.geometry("920x500+300+200")
register.config(bg="#fff")
register.iconbitmap("1st.ico")
register.resizable(False, False)

# Background Image
img = PhotoImage(file='log.png')
Label(register, image=img, border=0, bg="white").place(x=50, y=90)

# Frame for Input
frame = Frame(register, width=350, height=390, bg="lavender")
frame.place(x=480, y=50)

#USername animation
def on_enter(e):
    name=username_UI.delete(0,'end')

def on_leave(e):
    name=username_UI.get()
    if name=="":
        username_UI.insert(0,'Username')


# Username Entry
username_UI = Entry(frame, width=25, fg='black', border=2, bg='white', bd=0, background="lavender", font=('Microsoft Yahei UI Light', 11))
username_UI.place(x=30, y=80) 
username_UI.insert(0, "Username")
username_UI.bind("<FocusIn>",on_enter)
username_UI.bind("<FocusOut>",on_leave)
# Password Animation
def on_enter(e):
    name=password_UI.delete(0,'end')

def on_leave(e):
    name=password_UI.get()
    if name=="":
        password_UI.insert(0,'Password')

# Password Entry
password_UI = Entry(frame, width=25, fg='black', border=2, bg='white', bd=0, background="lavender", font=('Microsoft Yahei UI Light', 11))
password_UI.place(x=30, y=150) 
password_UI.insert(0, "Password")
password_UI.bind("<FocusIn>", on_enter)
password_UI.bind("<FocusOut>", on_leave)

#Confirm Password Animation
def on_enter(e):
    name=confirm_password_UI.delete(0,'end')

def on_leave(e):
    name=confirm_password_UI.get()
    if name=="":
        confirm_password_UI.insert(0,'Confirm Password')


# Confirm Password Entry
confirm_password_UI = Entry(frame, width=25, fg='black', border=2, bg='white', bd=0, background="lavender", font=('Microsoft Yahei UI Light', 11))
confirm_password_UI.place(x=30, y=220) 
confirm_password_UI.insert(0, "Confirm Password")
confirm_password_UI.bind("<FocusIn>", on_enter)
confirm_password_UI.bind("<FocusOut>", on_leave)

# Title
Title = Label(frame, text="Register", fg="#57a1f8", bg="white", font=('Microsoft Yahei UI Light', 23, 'bold'))
Title.place(x=100, y=5)
# Registration Button
Button(frame, width=39, pady=7, text="Register", bg="#57a1f8", fg="white", bd=0, command=database).place(x=35, y=280)

# Label for Login
Label(frame, text='Already have an account?', fg='black', bg="lavender", font=('Microsoft Yahei UI Light', 9)).place(x=75, y=340)

# Login Button
Button(frame, width=6, text="Log In", bd=0, bg="lavender", cursor='hand2', fg='#57a1f8', underline=True, command=login_page).place(x=280, y=340)

register.mainloop()
