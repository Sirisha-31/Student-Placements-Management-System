from tkinter import *
from tkinter import messagebox
import sqlite3

def save_company():
    name = company_name.get()
    role = job_role.get()
    cgpa = min_cgpa.get()

    if name == "" or role == "" or cgpa == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS companies(
        company_id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        job_role TEXT,
        min_cgpa REAL
    )
    """)

    cursor.execute("""
    INSERT INTO companies(company_name, job_role, min_cgpa)
    VALUES (?, ?, ?)
    """, (name, role, cgpa))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Company Added Successfully")

    company_name.delete(0, END)
    job_role.delete(0, END)
    min_cgpa.delete(0, END)


def open_company():
    global company_name, job_role, min_cgpa

    window = Toplevel()
    window.title("Manage Companies")
    window.geometry("400x300")

    Label(window, text="Company Name").pack(pady=5)
    company_name = Entry(window, width=35)
    company_name.pack()

    Label(window, text="Job Role").pack(pady=5)
    job_role = Entry(window, width=35)
    job_role.pack()

    Label(window, text="Minimum CGPA").pack(pady=5)
    min_cgpa = Entry(window, width=35)
    min_cgpa.pack()

    Button(window, text="Save Company", command=save_company).pack(pady=20)