import sqlite3

conn = sqlite3.connect("placement.db")
cursor = conn.cursor()

# Student Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    branch TEXT NOT NULL,
    cgpa REAL,
    email TEXT UNIQUE,
    phone TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")
from tkinter import *
from tkinter import messagebox

def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "admin123":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

root = Tk()
root.title("Student Placement Management System")
root.geometry("400x300")
root.resizable(False, False)

Label(root, text="Admin Login", font=("Arial", 18, "bold")).pack(pady=20)

Label(root, text="Username").pack()
user_entry = Entry(root, width=30)
user_entry.pack(pady=5)

Label(root, text="Password").pack()
pass_entry = Entry(root, width=30, show="*")
pass_entry.pack(pady=5)

Button(root, text="Login", width=15, command=login).pack(pady=20)

root.mainloop()