from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Password Generator")
root.geometry("1080x720")  # Set window size
root.iconbitmap("1st.ico")

# Load the image
image = Image.open('dashboard.png')
# Resize the image to fit the window
image = image.resize((1080, 720))
# Keep a reference to the image to prevent garbage collection
img = ImageTk.PhotoImage(image)

# Create a label to display the image
label = Label(root, image=img, border=0)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold entry boxes, labels, and buttons
frame = Frame(root, bg='white')
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

my_password = chr(randint(33, 126))  # uses ascii values

# Create Strong password
def new_rand():
    # Clear our entry box
    pw_entry.delete(0, END)

    # Get PW length and convert to integer
    pw_length = int(my_entry.get())

    # create a variable to hold our password
    my_password = ''

    # loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    # output password to the screen
    pw_entry.insert(0, my_password)

# Copy to clipboard
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

# Label for Entry box
label_entry = Label(frame, text="How Many Characters?", )
label_entry.grid(row=0, column=0, pady=10)

# Create Entry box to designate Number of characters
my_entry = Entry(frame,bg='#c69512', fg='white', font=('Helvetica', 24, 'bold'), border=0)
my_entry.grid(row=1, column=0, pady=10)

# Label for Password Entry Box
label_pw = Label(frame, text="Generated Password", font=("Helvetica", 18), bg='white', fg='black')
label_pw.grid(row=2, column=0, pady=10)

# Create Entry Box for our returned Password
pw_entry = Entry(frame, text="", font=("Helvetica", 24), bg='white', fg='black')
pw_entry.grid(row=3, column=0, pady=10)

# Create a frame for our buttons
button_frame = Frame(frame)
button_frame.grid(row=4, column=0, pady=10)

# Create our buttons
my_buttons = Button(button_frame, text="Generate Strong", command=new_rand)
my_buttons.grid(row=0, column=0, padx=10)
clip_buttons = Button(button_frame, text="Copy to Clipboard", command=clipper)
clip_buttons.grid(row=0, column=1, padx=10)

root.mainloop()
