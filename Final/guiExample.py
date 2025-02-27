import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x300")
root.title("Signup Form")


def submitHandle():
    name = nameEntry.get()
    email = emailEntry.get()
    password = passEntry.get()

    if name == "" or email == "" or password == "":
        messagebox.showerror("Form Validation" , "All fields are Required!")
    else :
        if len(password) < 6:
            messagebox.showwarning("Password Validation" , "Password must be 6 digits.")
        else :
            messagebox.showinfo("Submission" , "Form Submit")

tk.Label(text="Signup Form").pack()

tk.Label(root , text="Enter your name : ").pack()
nameEntry = tk.Entry(root)
nameEntry.pack()

tk.Label(root , text="Enter your email : ").pack()
emailEntry = tk.Entry(root)
emailEntry.pack()

tk.Label(root , text="Enter your password : ").pack()
passEntry = tk.Entry(root , show="*")
passEntry.pack()

tk.Button(root , text="Submit" , command=submitHandle ).pack()


root.mainloop()