import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("300x200")

        # UI widgets
        tk.Label(root, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        tk.Label(root, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        tk.Button(root, text="Login", command=self.authenticate).pack(pady=10)

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "1234":
            messagebox.showinfo("Login", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password.")

root = tk.Tk()
LoginApp(root)
root.mainloop()
