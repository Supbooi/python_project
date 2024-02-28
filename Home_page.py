from tkinter import *
from PIL import Image, ImageTk

def save_password():
    root.destroy()
    import password

def generate_password():
    root.destroy() 
    import pwgen

root = Tk()
root.title("Password Management")
root.geometry("1000x550")
root.iconbitmap("1st.ico")
root.resizable(False,False)

image = Image.open('dashboard.png')
image = image.resize((1000, 550))

img = ImageTk.PhotoImage(image)

label = Label(root, image=img, border=0)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Increase frame size and anchor it to the left side
frame = Frame(root, bg='white', width=300, height=400)
frame.place(x=480, y=70)

# Create a frame for our buttons
button_frame = Frame(frame, bg='white')
button_frame.pack(side=LEFT, padx=20, pady=20)

# Enhance button appearance
save_button = Button(button_frame, text="Save Password", width=15, height=2, command=save_password,borderwidth=2, relief="raised", padx=10, pady=5,fg='#57a1f8', font=('Arial', 10, 'underline'), cursor='hand2')
save_button.pack(pady=10)

generate_button = Button(button_frame, text="Generate Password", width=15, height=2, command=generate_password,borderwidth=2, relief="raised", padx=10, pady=5)
generate_button.pack(pady=10)


root.mainloop()
