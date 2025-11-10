import tkinter as tk
from tkinter import ttk


class CurrencyConverter:
    rates = {"USD": 1.0, "INR": 83.0, "EUR": 0.93, "GBP": 0.82}

    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("350x200")

        tk.Label(root, text="Enter Amount:").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.from_currency = ttk.Combobox(root, values=list(self.rates.keys()))
        self.from_currency.set("USD")
        self.from_currency.pack(pady=5)

        self.to_currency = ttk.Combobox(root, values=list(self.rates.keys()))
        self.to_currency.set("INR")
        self.to_currency.pack(pady=5)

        tk.Button(root, text="Convert", command=self.convert).pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            source = self.from_currency.get()
            target = self.to_currency.get()

            result = amount * (self.rates[target] / self.rates[source])
            self.result_label.config(text=f"Converted: {result:.2f} {target}")

        except ValueError:
            self.result_label.config(text="Invalid input!")


root = tk.Tk()
CurrencyConverter(root)
root.mainloop()
