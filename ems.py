from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database  # This should have insert, update, delete, id_exists, fetch_employees

def delete_all():
    result=messagebox.askyesno('confirm','do you want to delete all records')
    if result:
        database.deleteall_records()
    else:
        pass


def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('search by')


def search_employee():
    if searchEntry.get() == '':
        messagebox.showerror('error', 'enter value to search')
    elif searchBox.get() == 'search by':
        messagebox.showerror('error', 'please select an option')
    else:
        search_option = searchBox.get()     # get selected column name
        search_value = searchEntry.get()    # get entered value
        searched_data = database.search(search_option, search_value)
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('', END, values=employee)



def delete_employee():
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showerror('Error', 'Select data to delete')
        return
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('error','data is deleted')


def update_employee():
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showerror('Error', 'Select data to update')
    else:
        database.update(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
        treeview_data()
        clear(True)
        messagebox.showinfo('Success', 'Data updated successfully')

def selection(event):
    selected_items = tree.selection()
    if selected_items:
        row = tree.item(selected_items[0])['values']
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    roleBox.set('Manager')
    genderBox.set('Male')
    salaryEntry.delete(0, END)

def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', END, values=employee)

def add_employee():
    if idEntry.get() == '' or phoneEntry.get() == '' or salaryEntry.get() == '' or nameEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error', 'ID already exists')
    else:
        database.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
        treeview_data()
        clear(True)
        messagebox.showinfo('Success', 'Data added')

# Main window
window = CTk()
window.geometry('930x580')
window.resizable(True, True)
window.title('EMPLOYEE MANAGEMENT SYSTEM')
window.configure(fg_color='black')

# Cover image
logo = CTkImage(Image.open('cover.jpg'), size=(930, 158))
logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0, column=0, columnspan=2)

# LEFT FRAME
leftFrame = CTkFrame(window, fg_color="transparent")
leftFrame.grid(row=1, column=0, pady=20, padx=40, sticky="n")

CTkLabel(leftFrame, text='ID', font=('arial', 18, 'bold'), text_color='white').grid(row=0, column=0, padx=20, pady=10, sticky="w")
idEntry = CTkEntry(leftFrame, font=('arial', 15), width=180)
idEntry.grid(row=0, column=1, pady=10)

CTkLabel(leftFrame, text='Name', font=('arial', 18, 'bold'), text_color='white').grid(row=1, column=0, padx=20, pady=10, sticky="w")
nameEntry = CTkEntry(leftFrame, font=('arial', 15), width=180)
nameEntry.grid(row=1, column=1, pady=10)

CTkLabel(leftFrame, text='Phone', font=('arial', 18, 'bold'), text_color='white').grid(row=2, column=0, padx=20, pady=10, sticky="w")
phoneEntry = CTkEntry(leftFrame, font=('arial', 15), width=180)
phoneEntry.grid(row=2, column=1, pady=10)

CTkLabel(leftFrame, text='Role', font=('arial', 18, 'bold'), text_color='white').grid(row=3, column=0, padx=20, pady=10, sticky="w")
role_options = ["Manager", "Developer", "Designer", "HR", "Intern"]
roleBox = CTkComboBox(leftFrame, values=role_options, width=180, font=('arial', 15), state='readonly')
roleBox.grid(row=3, column=1)
roleBox.set(role_options[0])

CTkLabel(leftFrame, text='Gender', font=('arial', 18, 'bold'), text_color='white').grid(row=4, column=0, padx=20, pady=10, sticky="w")
gender_options = ["Male", "Female", "M/F"]
genderBox = CTkComboBox(leftFrame, values=gender_options, width=180, font=('arial', 15), state='readonly')
genderBox.grid(row=4, column=1)
genderBox.set('Male')

CTkLabel(leftFrame, text='Salary', font=('arial', 18, 'bold'), text_color='white').grid(row=5, column=0, padx=20, pady=10, sticky="w")
salaryEntry = CTkEntry(leftFrame, font=('arial', 15), width=180)
salaryEntry.grid(row=5, column=1, pady=10)

# RIGHT FRAME
rightFrame = CTkFrame(window, fg_color="transparent")
rightFrame.grid(row=1, column=1, pady=20, padx=40, sticky="n")

search_options = ['id', 'name', 'phone', 'role', 'gender', 'salary']
searchBox = CTkComboBox(rightFrame, values=search_options, state='readonly')
searchBox.grid(row=0, column=0, padx=5, pady=10, sticky="w")
searchBox.set("search_by")

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

searchButton = CTkButton(rightFrame, text='Search', width=100,command=search_employee)
searchButton.grid(row=0, column=2, padx=5, pady=10, sticky="ew")

showallButton = CTkButton(rightFrame, text='Show All', width=100, command=show_all)
showallButton.grid(row=0, column=3, padx=5, pady=10, sticky="ew")

# TREEVIEW
tree = ttk.Treeview(rightFrame, height=13, columns=('id', 'name', 'phone', 'role', 'gender', 'salary'), show='headings')
tree.grid(row=1, column=0, columnspan=4, pady=10)

tree.heading('id', text='ID')
tree.heading('name', text='NAME')
tree.heading('phone', text='PHONE')
tree.heading('role', text='ROLE')
tree.heading('gender', text='GENDER')
tree.heading('salary', text='SALARY')

tree.column('id', width=60, anchor='center')
tree.column('name', width=150, anchor='center')
tree.column('phone', width=120, anchor='center')
tree.column('role', width=120, anchor='center')
tree.column('gender', width=110, anchor='center')
tree.column('salary', width=120, anchor='center')

style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 18, 'bold'))
style.configure('Treeview', font=('arial', 15, 'bold'), rowheight=30, background='black', foreground='green')

scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL, command=tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns')
tree.configure(yscrollcommand=scrollbar.set)

# BUTTON FRAME
buttonFrame = CTkFrame(window, fg_color="transparent")
buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)

newButton = CTkButton(buttonFrame, text='New Employee', font=('arial', 15, 'bold'), width=120, command=lambda: clear(True))
newButton.grid(row=0, column=0, pady=5, padx=5)

addButton = CTkButton(buttonFrame, text='Add Employee', font=('arial', 15, 'bold'), width=120, command=add_employee)
addButton.grid(row=0, column=1, pady=5, padx=5)

updateButton = CTkButton(buttonFrame, text='Update Employee', font=('arial', 15, 'bold'), width=150, command=update_employee)
updateButton.grid(row=0, column=2, pady=5, padx=5)

deleteButton = CTkButton(buttonFrame, text='Delete Employee', font=('arial', 15, 'bold'), width=150, command=delete_employee)
deleteButton.grid(row=0, column=3, pady=5, padx=5)

deleteAllButton = CTkButton(buttonFrame, text='Delete All Employees', font=('arial', 15, 'bold'), width=180,command=delete_all)
deleteAllButton.grid(row=0, column=4, pady=5, padx=5)

# Load data initially
treeview_data()

window.bind('<ButtonRelease-1>', selection)


window.mainloop()


