from tkinter import *

def add():
    print("in add fuction")
    n1=text1.get()
    n2=text2.get()
    result=int(n1)+int(n2)
    result_label.config(text=f"Result: {result}")


    




if __name__=="__main__":

    window= Tk()
    window.title("Addition programm")
    window.geometry("800x600")

    label1=Label(window,text="Enter number 1 :")
    text1=Entry(window)


    label2=Label(window, text="Enter number 2 :")
    text2=Entry(window)

    
    btn=Button(window, text="Addition", command=add)
    
    result_label = Label(window, text=" ")
    

    label1.grid(row=1, column=1)
    text1.grid(row=1,column=2)
    label2.grid(row=2,column=1)
    text2.grid(row=2,column=2)
    btn.grid(row=3, column=1,columnspan=2)
    result_label.grid(row=4,column=1,columnspan=2)


    window.mainloop()