from tkinter import *
from tkinter import messagebox
import sqlite3

def save_student():
    name = name_entry.get()
    branch = branch_entry.get()
    cgpa = cgpa_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if name == "" or branch == "" or cgpa == "" or email == "" or phone == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students(name, branch, cgpa, email, phone)
    VALUES (?, ?, ?, ?, ?)
    """, (name, branch, cgpa, email, phone))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student Added Successfully!")

    name_entry.delete(0, END)
    branch_entry.delete(0, END)
    cgpa_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)


def open_student():
    global root
    global name_entry, branch_entry, cgpa_entry, email_entry, phone_entry

    root = Toplevel()
    root.title("Add Student")
    root.geometry("400x450")
    root.resizable(False, False)

    Label(root, text="Add Student", font=("Arial", 18, "bold")).pack(pady=15)

    Label(root, text="Name").pack()
    name_entry = Entry(root, width=35)
    name_entry.pack()

    Label(root, text="Branch").pack()
    branch_entry = Entry(root, width=35)
    branch_entry.pack()

    Label(root, text="CGPA").pack()
    cgpa_entry = Entry(root, width=35)
    cgpa_entry.pack()

    Label(root, text="Email").pack()
    email_entry = Entry(root, width=35)
    email_entry.pack()

    Label(root, text="Phone").pack()
    phone_entry = Entry(root, width=35)
    phone_entry.pack()

    Button(root, text="Save Student", width=20, command=save_student).pack(pady=20)