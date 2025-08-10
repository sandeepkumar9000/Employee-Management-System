from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('error','all field are required' )
    elif usernameEntry.get()=='sandy' and passwordEntry.get()=='1234':
          messagebox.showinfo('succes','login is succesful')
          root.destroy()
          import ems
    else:
         messagebox.showerror('error','wrong credentials')
root = CTk()
root.geometry('930x478')
root.resizable(0, 0)
root.title('Login Page')

# Background Image
image = CTkImage(Image.open('cover.jpg'), size=(930, 478))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=0, y=0)

# Heading
headinglabel = CTkLabel(
    root,
    text='Employee Management System',
    fg_color="#000000",    # background for text
    font=('Goudy Old Style', 20, 'bold'),
    text_color='white'
)
headinglabel.place(x=50, y=100)

# Username Entry - Styled
usernameEntry = CTkEntry(
    root,
    placeholder_text='ENTER YOUR NAME',
    width=210,
    height=30,
    corner_radius=0,
    fg_color="#1e1e1e",         # dark transparent background
    text_color="white",
    placeholder_text_color="gray",
    font=('Arial', 14)
)
usernameEntry.place(x=20, y=150)

# Password Entry - Styled
passwordEntry = CTkEntry(
    root,
    placeholder_text='PASSWORD',
    width=250,
    height=40,
    corner_radius=0,
    fg_color="#1e1e1e",
    text_color="white",
    placeholder_text_color="gray",
    font=('Arial', 14),
    show='*'
)
passwordEntry.place(x=20, y=200)

# Login Button - Stylish
loginButton = CTkButton(
    root,
    text='LOGIN',
    width=120,
    height=40,
    corner_radius=0,
    fg_color="#00b4d8",        # cyan color
    hover_color="#0096c7",
    cursor='hand2',
    text_color="black",
    command=login,
    font=('Arial', 14, 'bold')
)
loginButton.place(x=115, y=260)

root.mainloop()

