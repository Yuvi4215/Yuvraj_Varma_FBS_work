from tkinter import *
from tkinter import messagebox

def eraseAll():
    for widget in window.winfo_children():
        widget.destroy()


def empManage():
    eraseAll()

    def loadData():
        mylist.delete(0, END)
        try:
            with open("Core Python/tkinterDemos/caseStudy/empDataFile.txt", "r") as fp:
                for row in fp:
                    mylist.insert(END, row)
        except FileNotFoundError:
            # create file if not exists
            with open("Core Python/tkinterDemos/caseStudy/empDataFile.txt", "w"):
                pass  

    def addData(mylist):
        data = mylist.get(0, 'end')
        data_str = "".join(data)
        with open("Core Python/tkinterDemos/caseStudy/empDataFile.txt", "w") as fp:
            fp.write(data_str)

    def clearEntry():
        emp_id_entry.config(state="normal")
        emp_id_entry.delete(0, END)
        emp_nm_entry.delete(0, END)
        emp_sal_entry.delete(0, END)
        emp_id_entry.focus()

    def addEmp():
        emp_id = emp_id_entry.get().strip()
        emp_nm = emp_nm_entry.get().strip()
        emp_sal = emp_sal_entry.get().strip()

        if not emp_id or not emp_nm or not emp_sal:
            messagebox.showwarning("Warning", "Please fill all fields!")
            return

        # Prevent duplicate IDs
        for i in range(mylist.size()):
            row = mylist.get(i)
            if row.startswith(emp_id + ","):
                messagebox.showerror("Error", f"Employee ID {emp_id} already exists.")
                return

        edata = f"{emp_id}, {emp_nm}, {emp_sal}\n"
        mylist.insert(END, edata)
        addData(mylist)
        clearEntry()

    def selectEmp():
        clearEntry()
        try:
            edata = mylist.get(ACTIVE)
            result = edata.split(", ")
            emp_id_entry.insert(0, result[0])
            emp_id_entry.config(state="readonly")
            emp_nm_entry.insert(0, result[1])
            emp_sal_entry.insert(0, result[2].rstrip("\n"))
        except:
            messagebox.showerror("Error", "Please select a record from the list.")

    def updateEmp():
        selected_index = mylist.curselection()
        # print(selected_index)
        
        if not selected_index:
            messagebox.showwarning("Warning", "Select an employee to update.")
            return

        emp_id = emp_id_entry.get().strip()
        emp_nm = emp_nm_entry.get().strip()
        emp_sal = emp_sal_entry.get().strip()

        if not emp_id or not emp_nm or not emp_sal:
            messagebox.showwarning("Warning", "Please fill all fields.")
            return

        new_data = f"{emp_id}, {emp_nm}, {emp_sal}\n"
        mylist.delete(selected_index)
        mylist.insert(selected_index, new_data)
        addData(mylist)
        clearEntry()
        messagebox.showinfo("Success", "Employee record updated successfully!")

    def deleteEmp():
        selected_index = mylist.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Select an employee to delete.")
            return

        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this record?")
        if confirm:
            mylist.delete(selected_index)
            addData(mylist)
            clearEntry()
            messagebox.showinfo("Deleted", "Employee record deleted successfully!")

    # Layout setup
    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)
    frame4 = Frame(window)

    frame1.pack(pady=10)
    frame2.pack(pady=10)
    frame3.pack(pady=10)
    frame4.pack(pady=10)

    Label(frame1, text="Admin Dashboard", font=("Arial", 16, "bold")).pack()

    Label(frame2, text="Eid: ", font=("Arial", 12)).grid(row=1, column=1, pady=5)
    emp_id_entry = Entry(frame2, width=25, font=("Arial", 12))
    emp_id_entry.grid(row=1, column=2, padx=5)

    Label(frame2, text="Name: ", font=("Arial", 12)).grid(row=2, column=1, pady=5)
    emp_nm_entry = Entry(frame2, width=25, font=("Arial", 12))
    emp_nm_entry.grid(row=2, column=2, padx=5)

    Label(frame2, text="Salary: ", font=("Arial", 12)).grid(row=3, column=1, pady=5)
    emp_sal_entry = Entry(frame2, width=25, font=("Arial", 12))
    emp_sal_entry.grid(row=3, column=2, padx=5)

    Button(frame3, text="ADD", font=("Arial", 12, "bold"), command=addEmp).pack(side=LEFT, padx=5, pady=15)
    Button(frame3, text="SELECT", font=("Arial", 12, "bold"), command=selectEmp).pack(side=LEFT, padx=5)
    Button(frame3, text="UPDATE", font=("Arial", 12, "bold"), command=updateEmp).pack(side=LEFT, padx=5)
    Button(frame3, text="DELETE", font=("Arial", 12, "bold"), command=deleteEmp).pack(side=LEFT, padx=5)

    scrollbar = Scrollbar(frame4)
    scrollbar.pack(side=RIGHT, fill=Y)

    mylist = Listbox(frame4, yscrollcommand=scrollbar.set, height=15, width=50)
    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)

    loadData()


def login():
    user_id = user_id_entry.get()
    password = password_entry.get()

    if user_id and password:
        if user_id == "Admin" and password == "1234":
            empManage()
        else:
            messagebox.showerror("Error", "Invalid credentials.")
    else:
        messagebox.showwarning("Warning", "Please enter all details.")


def main():
    Label(window, text="User Login", font=("Arial", 16, "bold")).pack(pady=10)
    Label(window, text="User ID:", font=("Arial", 12)).pack(pady=5)

    global user_id_entry, password_entry
    user_id_entry = Entry(window, width=25, font=("Arial", 12))
    user_id_entry.pack(pady=5)

    Label(window, text="Password:", font=("Arial", 12)).pack(pady=5)
    password_entry = Entry(window, width=25, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    Button(window, text="Login", font=("Arial", 12, "bold"), padx=10, command=login).pack(pady=15)


if __name__ == "__main__":
    window = Tk()
    window.geometry("400x600")
    main()
    # empManage()
    window.mainloop()
