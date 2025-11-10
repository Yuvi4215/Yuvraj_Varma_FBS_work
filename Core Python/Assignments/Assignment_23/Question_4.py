import tkinter as tk
from tkinter import messagebox


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.index = 0
        self.score = 0

        self.questions = [
            ("Capital of India?", ["Delhi", "Mumbai", "Chennai", "Kolkata"], "Delhi"),
            ("5 + 3 = ?", ["5", "8", "10", "7"], "8"),
            ("Largest planet?", ["Mars", "Earth", "Jupiter", "Venus"], "Jupiter"),
        ]

        self.question_label = tk.Label(root, font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.options = []
        self.var = tk.StringVar()

        for i in range(4):
            btn = tk.Radiobutton(
                root, text="", variable=self.var, value="", font=("Arial", 12)
            )
            btn.pack(anchor="w")
            self.options.append(btn)

        tk.Button(root, text="Submit", command=self.check_answer).pack(pady=10)

        self.load_question()

    def load_question(self):
        q, options, _ = self.questions[self.index]
        self.question_label.config(text=q)

        for i, opt in enumerate(options):
            self.options[i].config(text=opt, value=opt)

        self.var.set(None)

    def check_answer(self):
        selected = self.var.get()
        _, _, correct = self.questions[self.index]

        if selected == correct:
            messagebox.showinfo("Correct", "Right answer!")
            self.score += 1
        else:
            messagebox.showerror("Wrong", f"Correct answer: {correct}")

        self.index += 1

        if self.index < len(self.questions):
            self.load_question()
        else:
            messagebox.showinfo(
                "Quiz Finished", f"Your score: {self.score}/{len(self.questions)}"
            )


root = tk.Tk()
QuizGame(root)
root.mainloop()
