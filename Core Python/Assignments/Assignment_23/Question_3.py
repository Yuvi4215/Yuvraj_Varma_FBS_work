import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.input_var = tk.StringVar()

        tk.Entry(root, textvariable=self.input_var, font=("Arial", 18), justify="right").grid(row=0, column=0, columnspan=4)

        buttons = [
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','.','=','+'
        ]

        row, col = 1, 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, command=lambda b=button:self.click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, value):
        if value == "=":
            try:
                result = eval(self.input_var.get())
                self.input_var.set(result)
            except:
                self.input_var.set("Error")
        else:
            self.input_var.set(self.input_var.get() + value)

root = tk.Tk()
Calculator(root)
root.mainloop()
