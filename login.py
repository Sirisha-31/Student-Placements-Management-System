from tkinter import *
from tkinter import messagebox
import admin

def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "admin123":
        messagebox.showinfo("Success", "Login Successful")
        root.destroy()
        admin.open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

root = Tk()
root.title("Login")
root.geometry("400x300")

Label(root, text="Admin Login", font=("Arial", 18, "bold")).pack(pady=20)

Label(root, text="Username").pack()
user_entry = Entry(root, width=30)
user_entry.pack()

Label(root, text="Password").pack()
pass_entry = Entry(root, width=30, show="*")
pass_entry.pack()

Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()