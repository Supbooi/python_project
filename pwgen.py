from tkinter import *
from random import randint

root = Tk()
root.title("Password Generator")
root.geometry("500x300")

my_password = chr(randint(33,126))

def new_rand():
    # Clear our entry box
    pw_entry.delete(0,END)

    # Get PW length and convert to integer
    pw_length = int(my_entry.get())

    # create a variable to hold our password
    my_password = ''

    # loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33,126))

    # output password to the screen
        pw_entry.insert(0, my_password)

def clipper():
    pass
# label
l=LabelFrame(root, text="How Many Characters?")
l.pack(pady=20)

# Create Entry box to designate Number of characters
my_entry = Entry(l,font=("Helvetica",24))
my_entry.pack(pady=20,padx=20)

# Create Entry Box for our returned Password
pw_entry = Entry(root,text="",font=("Hevetica",24))
pw_entry.pack(pady=20)

# Create a frame for our buttons
my_frame= Frame(root)
my_frame.pack(pady=20)

# Create our buttons
my_buttons = Button(my_frame,text="Generate Strong",command=new_rand)
my_buttons.grid(row=0, column= 0, padx=10)
clip_buttons = Button(my_frame,text="Copy to Clipboard", command=clipper)
clip_buttons.grid(row=0, column= 1, padx=10)



root.mainloop()