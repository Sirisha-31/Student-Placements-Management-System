from tkinter import *
import sqlite3

def open_reports():

    window = Toplevel()
    window.title("Reports")
    window.geometry("400x300")

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    # Total Students
    cursor.execute("SELECT COUNT(*) FROM students")
    students = cursor.fetchone()[0]

    # Total Companies
    cursor.execute("SELECT COUNT(*) FROM companies")
    companies = cursor.fetchone()[0]

    # Total Placement Drives
    cursor.execute("SELECT COUNT(*) FROM placement_drives")
    drives = cursor.fetchone()[0]

    conn.close()

    Label(window, text="Placement Reports",
          font=("Arial",18,"bold")).pack(pady=20)

    Label(window,
          text=f"Total Students : {students}",
          font=("Arial",12)).pack(pady=5)

    Label(window,
          text=f"Total Companies : {companies}",
          font=("Arial",12)).pack(pady=5)

    Label(window,
          text=f"Total Placement Drives : {drives}",
          font=("Arial",12)).pack(pady=5)