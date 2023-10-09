import tkinter as tk


class MultiplicationCalculator:
    def __init__(self, win):
        self.win = win
        self.win.title("Multiplication Calculator")

        self.mainframe = tk.Frame(self.win)
        self.mainframe.grid(column=0, row=0)

        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.result = tk.StringVar()
        self.result.set("Result will be shown here.")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.mainframe, text="Number 1:").grid(column=1, row=1)
        tk.Entry(self.mainframe, width=20,
                 textvariable=self.num1).grid(column=2, row=1)

        tk.Label(self.mainframe, text="Number 2:").grid(column=1, row=2)
        tk.Entry(self.mainframe, width=20,
                 textvariable=self.num2).grid(column=2, row=2)

        tk.Button(self.mainframe, text="Multiply",
                  command=self.multiply).grid(column=1, row=3)
        tk.Button(self.mainframe, text="Clear",
                  command=self.clear).grid(column=2, row=3)

        tk.Label(self.mainframe, textvariable=self.result).grid(
            column=1, row=4, columnspan=2)

    def multiply(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            self.result.set(f"Result: {num1 * num2}")
        except ValueError:
            self.result.set("Invalid input. Please enter numbers.")

    def clear(self):
        self.num1.set("")
        self.num2.set("")
        self.result.set("Result will be shown here.")


def main():
    root = tk.Tk()
    app = MultiplicationCalculator(root)
    root.mainloop()
