from tkinter import *
from tkinter import messagebox

def submit():
    val1=x.get()
    val2=y.get()
    val3=z.get()
    data=""

    if val1:
        data+="Python\n"
    if val2:
        data+="Java\n"
    if val3:
        data+="Testing\n"
    
    if data:
        messagebox.showinfo("Selection",data)
    else:
        messagebox.showwarning("Warning", "Select at least one course")



if __name__=="__main__":
    window=Tk()
    window.geometry("800x600")
    window.title("Course Selection")
    window.config(background="grey")
    
    x=IntVar()
    y=IntVar()
    z=IntVar()

    frame1=Frame(window)
    frame2=Frame(window)
    frame3=Frame(window)

    label1=Label(frame1, text="Select the courses....")
    label1.pack()
    frame1.pack()

    check1=Checkbutton(frame2, text="Python", variable=x)
    check2=Checkbutton(frame2, text="Java", variable=y)
    check3=Checkbutton(frame2, text="Testing", variable=z)
    check1.pack(side=LEFT)
    check2.pack(side=LEFT)
    check3.pack(side=LEFT)
    frame2.pack()

    btn= Button(frame3, text="Submit", command=submit)
    

    
    btn.pack()
    frame3.pack()



    window.mainloop()