from tkinter import *
from tkinter import messagebox
import sqlite3

def login():
    email = email_entry.get()

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE email=?", (email,))
    row = cursor.fetchone()

    conn.close()

    if row:
        messagebox.showinfo("Success", f"Welcome {row[1]}")
    else:
        messagebox.showerror("Error", "Student Not Found")

def open_student_login():
    window = Toplevel()
    window.title("Student Login")
    window.geometry("350x200")

    Label(window, text="Student Login",
          font=("Arial", 16, "bold")).pack(pady=15)

    Label(window, text="Email").pack()

    global email_entry
    email_entry = Entry(window, width=30)
    email_entry.pack()

    Button(window,
           text="Login",
           command=login).pack(pady=20)