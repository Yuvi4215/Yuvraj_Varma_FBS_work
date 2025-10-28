from tkinter import *
from tkinter import messagebox

def changeTheme():
    val=x.get()
    
    if val==1:
        window.config(background="black")
    elif val==2:
        window.config(background="red")
    elif val==3:
        window.config(background="yellow")
    elif val==4:
        window.config(background="white")
    else:
        messagebox.showwarning("warning", message="please select a choice.")
         


if __name__=="__main__":

    window= Tk()
    window.title("Theme select")
    window.geometry("800x600")

    x=IntVar()

    label1=Label(window, text="Please Select Theme from bellow.")
    radio1=Radiobutton(window, text="black", variable=x, value=1)
    radio2=Radiobutton(window, text="red", variable=x, value=2)
    radio3=Radiobutton(window, text="yellow", variable=x, value=3)
    radio4=Radiobutton(window, text="reset", variable=x, value=4)
    btn= Button(window,text="Submit",command=changeTheme)

    label1.grid(row=1, column=1)
    radio1.grid(row=2,column=1)
    radio2.grid(row=3,column=1)
    radio3.grid(row=4, column=1)
    radio4.grid(row=5,column=1)
    btn.grid(row=6, column=1)


    window.mainloop()