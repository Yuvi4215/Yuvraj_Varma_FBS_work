from tkinter import *

if __name__=="__main__":
    window=Tk()
    window.geometry("800x600")
    window.config(background="black")

    lable=Label(window, text="Hello World!")
    lable.pack()

    window.mainloop()