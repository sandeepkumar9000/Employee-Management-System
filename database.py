import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor,conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='Sandeep@rchi')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error', 'something went wrong, please open MySQL app before running again')
        return

    mycursor.execute('create database if not exists employee_data')
    mycursor.execute('use employee_data')
    mycursor.execute('create table if not exists data (id varchar(20), name varchar(50), phone varchar(15), role varchar(50), gender varchar(20), salary varchar(20))')

def insert(id, name, phone, role, gender, salary):
   mycursor.execute('insert into data values(%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
   conn.commit()
def id_exists(id):
    mycursor.execute('select count(*) from data where id=%s',id)
    result=mycursor.fetchone()
    print(result)
    return result[0]>0
def fetch_employees():
    mycursor.execute('select * from data')
    result=mycursor.fetchall()
    return result
def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('update data set name=%s,phone=%s,role=%s,gender=%s,salary=%s where id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()

def delete(emp_id):
    mycursor.execute("DELETE FROM data WHERE id = %s", (emp_id,))
    conn.commit()
    messagebox.showinfo("Deleted", f"Employee with ID {emp_id} deleted successfully!")

def search(option, value):
    query = f"SELECT * FROM data WHERE {option} = %s"
    mycursor.execute(query, (value,))
    return mycursor.fetchall()

def deleteall_records():
    mycursor.execute('truncate table data')
    conn.commit()





connect_database()