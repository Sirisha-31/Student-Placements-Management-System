from tkinter import *

import student
import view_students
import search_student
import update_student
import delete_student
import company
import placement
import reports
import student_login
import selected_students
import view_selected


def open_dashboard():

    dashboard = Tk()
    dashboard.title("Admin Dashboard")
    dashboard.geometry("550x700")
    dashboard.resizable(False, False)

    Label(
        dashboard,
        text="Student Placement Management System",
        font=("Arial", 18, "bold"),
        fg="blue"
    ).pack(pady=20)

    Button(
        dashboard,
        text="Add Student",
        width=30,
        command=student.open_student
    ).pack(pady=5)

    Button(
        dashboard,
        text="View Students",
        width=30,
        command=view_students.open_view_students
    ).pack(pady=5)

    Button(
        dashboard,
        text="Search Student",
        width=30,
        command=search_student.open_search
    ).pack(pady=5)

    Button(
        dashboard,
        text="Update Student",
        width=30,
        command=update_student.open_update
    ).pack(pady=5)

    Button(
        dashboard,
        text="Delete Student",
        width=30,
        command=delete_student.open_delete
    ).pack(pady=5)

    Button(
        dashboard,
        text="Manage Companies",
        width=30,
        command=company.open_company
    ).pack(pady=5)

    Button(
        dashboard,
        text="Placement Drives",
        width=30,
        command=placement.open_drive
    ).pack(pady=5)

    Button(
        dashboard,
        text="Reports",
        width=30,
        command=reports.open_reports
    ).pack(pady=5)

    Button(
        dashboard,
        text="Student Login",
        width=30,
        command=student_login.open_student_login
    ).pack(pady=5)

    Button(
        dashboard,
        text="Selected Students",
        width=30,
        command=selected_students.open_selected
    ).pack(pady=5)

    Button(
        dashboard,
        text="View Selected Students",
        width=30,
        command=view_selected.open_view_selected
    ).pack(pady=5)

    Button(
        dashboard,
        text="Logout",
        width=30,
        bg="red",
        fg="white",
        command=dashboard.destroy
    ).pack(pady=20)

    dashboard.mainloop()


if __name__ == "__main__":
    open_dashboard()