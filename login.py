from tkinter import*
from tkinter import messagebox
import pymysql

def register_page():
    root.destroy()
    import sign_in

def database():
    if user.get()=="" or password.get()=="":
        messagebox.showerror("Error","All fields are requried")

root=Tk()
root.title('LOGIN')
root.geometry('925x500+300+200') #size of background
root.iconbitmap("1st.ico")
root.configure(bg='#fff') #background
root.resizable(False,False) #resize horizontal ways or vertical ways




# def signin():
#     Username=user.get()
#     Password=password.get()

   
#     if Username=='@dmin' and Password=='6969':
#         screen=Toplevel(root)
#         screen.title('App')
#         screen.geometry('925x500+300+200')
#         screen.config(bg='light grey')

#         Label(screen,text="Secure Your Password",bg='light grey',font=('Calibri(Body)',20,'bold'))
#         label.place(x=10,y=5)


#         screen.mainloop()

#         # print('Logged in succesfully')
    
#     elif Username!='@dmin' and Password!='6969':
#         messagebox.showerror("Error","Username or password is incorrect")
    
#     elif password!='6969':
#         messagebox.showerror("Error","Invalid Password!")

#     elif Username!='@dmin':
#         messagebox.showerror("Error","Invalid Username!")


img=PhotoImage(file='log.png') #add image at side
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='#d9d9d9') #background frame for login work
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#c69512',bg='#d9d9d9',font=('Microsoft YaHei UI Light',24,'bold')) #styling heading
heading.place(x=130,y=5)

#....................
def on_enter(e):
    user.delete(0,'end') #making function for animation in entry box of username

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=26,fg='black',border=0,bg='lavender',font=('Microsoft YaHei UI Light',11)) #add entry box
user.place(x=30,y=80)
user.insert(0,'Username') #adds a default input in entrybox when running the code
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107) #adds line under entry
#....................

def on_enter(e):
    password.delete(0,'end') #making function for animation in entry box of password

def on_leave(e):
    name=password.get()
    if name=='':
        password.insert(0,'Password')



password=Entry(frame,width=26,fg='black',border=0,bg='lavender',font=('Microsoft YaHei UI Light',11)) #add entry box
password.place(x=30,y=150)
password.insert(0,'Password') #adds a default input in entrybox when running the code
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177) #adds line under entry
#....................

Button(frame,width=39,pady=10,text='Sign in',bg='white',cursor='hand2',fg='chocolate',border=0,command=database).place(x=35,y=204) #adding signin button
label=Label(frame,text='Create Account ?',fg='black',bg='lavender',font=('Microsoft YaHei UI Light',9)) #adding label
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='lavender',cursor='hand2',fg='#57a1f8',command=register_page) #add button for new signup ones
sign_up.place(x=215,y=270)

root.mainloop()

