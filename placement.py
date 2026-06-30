from tkinter import *
from tkinter import messagebox
import sqlite3

def save_drive():
    company = company_entry.get()
    date = date_entry.get()
    venue = venue_entry.get()

    if company == "" or date == "" or venue == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS placement_drives(
        drive_id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        drive_date TEXT,
        venue TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO placement_drives(company_name, drive_date, venue)
    VALUES (?, ?, ?)
    """, (company, date, venue))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Placement Drive Added Successfully!")

    company_entry.delete(0, END)
    date_entry.delete(0, END)
    venue_entry.delete(0, END)


def open_drive():

    global company_entry, date_entry, venue_entry

    window = Toplevel()
    window.title("Placement Drives")
    window.geometry("400x300")

    Label(window, text="Company Name").pack(pady=5)
    company_entry = Entry(window, width=35)
    company_entry.pack()

    Label(window, text="Drive Date").pack(pady=5)
    date_entry = Entry(window, width=35)
    date_entry.pack()

    Label(window, text="Venue").pack(pady=5)
    venue_entry = Entry(window, width=35)
    venue_entry.pack()

    Button(window, text="Save Drive", command=save_drive).pack(pady=20)