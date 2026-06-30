from tkinter import *
from tkinter import messagebox
import sqlite3

def save_selected():
    name = name_entry.get()
    company = company_entry.get()
    role = role_entry.get()
    package = package_entry.get()

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS selected_students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        company_name TEXT,
        job_role TEXT,
        package TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO selected_students(student_name, company_name, job_role, package)
    VALUES (?, ?, ?, ?)
    """, (name, company, role, package))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student Selected Successfully!")

    name_entry.delete(0, END)
    company_entry.delete(0, END)
    role_entry.delete(0, END)
    package_entry.delete(0, END)

def open_selected():
    global name_entry, company_entry, role_entry, package_entry

    window = Toplevel()
    window.title("Selected Students")
    window.geometry("400x350")

    Label(window, text="Student Name").pack(pady=5)
    name_entry = Entry(window, width=30)
    name_entry.pack()

    Label(window, text="Company Name").pack(pady=5)
    company_entry = Entry(window, width=30)
    company_entry.pack()

    Label(window, text="Job Role").pack(pady=5)
    role_entry = Entry(window, width=30)
    role_entry.pack()

    Label(window, text="Package (LPA)").pack(pady=5)
    package_entry = Entry(window, width=30)
    package_entry.pack()
    Button(window, text="Save", command=save_selected).pack(pady=20)
