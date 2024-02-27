from tkinter import *
from tkinter import messagebox
import pymysql



def login_page():
    register.destroy()
    import login

def clear():
    username_UI.delete(0,END)
    password_UI.delete(0,END)
    confirm_password_UI.delete(0,END)


def database():
    if username_UI.get()=="" or password_UI.get()=="" or confirm_password_UI.get()=="":
        messagebox.showerror("Error","All fields are required")
    elif password_UI.get() != confirm_password_UI.get():
        messagebox.showerror("Error","Password doesnot match")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='plmokn@12')
            mycursor=con.cursor()
        except:
            messagebox.showerror("Error","Database Connectivity Issue, Please Try Again")
            return 
        try:
            query="create database userdata"
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query='insert into data(username,password) values(%s,%s)'
        mycursor.execute(query,(username_UI.get(),password_UI.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Succes',"Registration is Successful")
        
register=Tk()

#######################################
#Adding title on the top
register.title("Register")

#######################################################
# Setting a fixed size for the gui when first opened
register.geometry("920x500+300+200")

#######################################################
#Adding background color for the gui page
register.config(bg="#fff")

#########################################################
# Makes it so that the size of the gui cannot be changed  
register.resizable(False,False)





###################################################################################################
#Adding functions that we can call in the login button so that it connects itself to the database

# def Register_now():
#     username=username_UI.get()
#     password=password_UI.get()
#     confirm_password=confirm_password_UI.get()


#     if password==confirm_password:











##################################
# Adding a image on the gui
img=PhotoImage(file='log.png')
Label(register,image=img,border=0,bg="white").place(x=50,y=90)




# Makes a different workspace that we can write and place stuff on 
frame=Frame(register,width=350,height=390,bg="lavender")
frame.place(x=480,y=50)




# Writting a title in the frame that we just created
Title=Label(frame,text="Register",fg="#57a1f8",bg="white",background="lavender",font=('Microsoft Yahei UI Light',23,'bold'))
Title.place(x=100,y=5)



###############################################################
# Making funcions for animations in the entrybox of Username

def on_enter(e):
    username_UI.delete(0,END)

def on_leave(e):
    if username_UI.get()=='':
        username_UI.insert(0,'Username')


#Creating entryboxes for user input of Username

username_UI=Entry(frame,width=25,fg='black',border=2,bg='white', bd=0,background="lavender",font=('Microsoft Yahei UI Light',11))
username_UI.place(x=30,y=80) 
username_UI.insert(0,"Username")#adds a default entry on entrybox when running the code
username_UI.bind("<FocusIn>",on_enter)
username_UI.bind("<FocusOut>",on_leave)

# Making a line under the username Entrybox of Username
Frame(frame,width=290,height=2,bg='black').place(x=25,y=107)







#####################################################################
# Making funcions for animations in the entrybox of password

def on_enter(e):
    password_UI.delete(0,END)

def on_leave(e):
    if password_UI.get()=='':
        password_UI.insert(0,'Password')





#Creating entryboxes for user input of password

password_UI=Entry(frame,width=25,fg='black',border=2,bg='white', bd=0,background="lavender",font=('Microsoft Yahei UI Light',11))
password_UI.place(x=30,y=150) 
password_UI.insert(0,"Password")#adds a default entry on entrybox when running the code
password_UI.bind("<FocusIn>",on_enter)
password_UI.bind("<FocusOut>",on_leave)




# Making a line under the username Entrybox of password
Frame(frame,width=290,height=2,bg='black').place(x=25,y=177)










#############################################################################
# Making funcions for animations in the entrybox of confirm password

def on_enter(e):
    confirm_password_UI.delete(0,END)

def on_leave(e):
    if confirm_password_UI.get()=='':
        confirm_password_UI.insert(0,'Confirm Password')




#################################################################################
#Creating entryboxes for user input of confirm password

confirm_password_UI=Entry(frame,width=25,fg='black',border=2,bg='white',background="lavender", bd=0,font=('Microsoft Yahei UI Light',11))
confirm_password_UI.place(x=30,y=220) 
confirm_password_UI.insert(0,"Confirm Password")#adds a default entry on entrybox when running the code
confirm_password_UI.bind("<FocusIn>",on_enter)
confirm_password_UI.bind("<FocusOut>",on_leave)



# Making a line under the username Entrybox of confirm password
Frame(frame,width=290,height=2,bg='black').place(x=25,y=247)








##################################################
# Creating a button for logging in 

Button(frame,width=39,pady=7,text="Register",bg="#57a1f8",fg="white",bd=0,command=database).place(x=35,y=280)




#################################################
# adding a lebel for already existing accounts

label=Label(frame,text='Wanna log a into existing account?',fg='black',background="lavender",font=('Microsoft Yahei UI Light',9))
label.place(x=75,y=340)



###################################################################################################################################################################
# adding a login button without a background or anything for it to have only underline and if clicked on will open a login page and destroy the register page

login=Button(frame,width=6,text="Log In",bd=0,bg="lavender",cursor='hand2',fg='#57a1f8',underline=True,command=login_page)
login.place(x=280,y=340)

register.mainloop()