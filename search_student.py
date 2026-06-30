from tkinter import *
from tkinter import messagebox
import sqlite3

def search_student():
    sid = id_entry.get()

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE student_id=?", (sid,))
    row = cursor.fetchone()

    conn.close()

    if row:
        result.config(
            text=f"""
ID      : {row[0]}
Name    : {row[1]}
Branch  : {row[2]}
CGPA    : {row[3]}
Email   : {row[4]}
Phone   : {row[5]}
"""
        )
    else:
        messagebox.showerror("Error", "Student Not Found")


def open_search():
    global id_entry, result

    window = Toplevel()
    window.title("Search Student")
    window.geometry("400x350")

    Label(window, text="Student ID", font=("Arial", 12)).pack(pady=10)

    id_entry = Entry(window, width=25)
    id_entry.pack()

    Button(window, text="Search", command=search_student).pack(pady=10)

    result = Label(window, text="", justify=LEFT, font=("Arial", 11))
    result.pack(pady=20)