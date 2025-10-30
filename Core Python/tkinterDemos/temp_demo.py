import tkinter as tk

def update_entry():
    data_from_backend = "Hello from backend!"
    entry_var.set(data_from_backend)  # Set value dynamically

root = tk.Tk()
root.title("Tkinter Entry Example")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=30)
entry.pack(padx=10, pady=10)

btn = tk.Button(root, text="Load Data", command=update_entry)
btn.pack(pady=5)

root.mainloop()
