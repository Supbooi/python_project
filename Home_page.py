from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Home Page")
root.geometry("1222x701")
root.iconbitmap("1st.ico")
root.resizable(False,False)

image = Image.open('data_protection.png')
image= image.resize((1230,700))

img= ImageTk.PhotoImage(image)

background_label = Label(root, image=img, border=0)
background_label.place(x=0, y=0,relwidth=1,relheight=1)

def save_password():
    root.destroy()
    import password

def generate_password():
    root.destroy() 
    import pwgen


frame = Frame(root, width=600, height=400, bg='#feca91')
frame.place(x=300,y=120)



heading =Label(frame, text='Password Management System', fg='black', bg='#feca91', font=('Arial', 20, 'bold'))
heading.place(x=120, y=5)

b1=Button(frame, width=45, text='Save Password', bg='#1cb4c3', fg='white', font=('Arial', 12, 'bold'), border=3,command=save_password)
b1.place(x=70, y=120)

b2=Button(frame, width=45, text='Generate Password', bg='#1cb4c3', fg='white', font=('Arial', 12, 'bold'), border=3,command=generate_password)
b2.place(x=70, y=220)

root.mainloop()