from tkinter import *
from tkinter import ttk
import sqlite3

def open_view_students():
    window = Toplevel()
    window.title("View Students")
    window.geometry("700x400")

    columns = ("ID", "Name", "Branch", "CGPA", "Email", "Phone")

    tree = ttk.Treeview(window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(fill=BOTH, expand=True)

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)

    conn.close()