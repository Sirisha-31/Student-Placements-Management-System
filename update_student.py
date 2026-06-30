from tkinter import *
from tkinter import messagebox
import sqlite3

def update_student():
    sid = id_entry.get()
    name = name_entry.get()
    branch = branch_entry.get()
    cgpa = cgpa_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET name=?, branch=?, cgpa=?, email=?, phone=?
    WHERE student_id=?
    """, (name, branch, cgpa, email, phone, sid))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student Updated Successfully!")

def open_update():

    global id_entry, name_entry, branch_entry
    global cgpa_entry, email_entry, phone_entry

    window = Toplevel()
    window.title("Update Student")
    window.geometry("400x450")

    Label(window, text="Student ID").pack()
    id_entry = Entry(window, width=30)
    id_entry.pack()

    Label(window, text="Name").pack()
    name_entry = Entry(window, width=30)
    name_entry.pack()

    Label(window, text="Branch").pack()
    branch_entry = Entry(window, width=30)
    branch_entry.pack()

    Label(window, text="CGPA").pack()
    cgpa_entry = Entry(window, width=30)
    cgpa_entry.pack()

    Label(window, text="Email").pack()
    email_entry = Entry(window, width=30)
    email_entry.pack()

    Label(window, text="Phone").pack()
    phone_entry = Entry(window, width=30)
    phone_entry.pack()

    Button(window, text="Update", command=update_student).pack(pady=20)