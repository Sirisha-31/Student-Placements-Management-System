from tkinter import *
from tkinter import messagebox
import sqlite3

def delete_student():
    sid = id_entry.get()

    if sid == "":
        messagebox.showerror("Error", "Enter Student ID")
        return

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE student_id=?", (sid,))
    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Student Deleted Successfully!")
    else:
        messagebox.showerror("Error", "Student ID Not Found")

    conn.close()
    id_entry.delete(0, END)

def open_delete():
    global id_entry

    window = Toplevel()
    window.title("Delete Student")
    window.geometry("350x200")

    Label(window, text="Student ID", font=("Arial", 12)).pack(pady=10)

    id_entry = Entry(window, width=30)
    id_entry.pack()

    Button(window, text="Delete Student", command=delete_student).pack(pady=20)