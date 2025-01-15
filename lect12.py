from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar


class Calculator:

    def __init__(self):
        self.win = Tk()
        self.win.title("Calculator")
        self.win.geometry("200x150")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.num1 = IntVar()
        self.num2 = IntVar()
        self.result = StringVar()
        self.result.set("Result: 0")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_num1 = Label(self.main_frame, text="Number 1:")
        label_num1.pack()

        entry_num1 = Entry(
            self.main_frame,
            width=20,
            textvariable=self.num1
        )
        entry_num1.pack()

        label_num2 = Label(self.main_frame, text="Number 2:")
        label_num2.pack()

        entry_num2 = Entry(
            self.main_frame,
            width=20,
            textvariable=self.num2
        )
        entry_num2.pack()

        label_result = Label(
            self.main_frame,
            textvariable=self.result
        )
        label_result.pack()

        button_mult = Button(
            self.main_frame,
            text="Multiply",
            command=self.multiply
        )
        button_mult.pack(side="left")

        btn_close = Button(
            self.main_frame,
            text="Close",
            command=self.win.destroy
        )
        btn_close.pack(side="right")

    def multiply(self):
        num1 = self.num1.get()
        num2 = self.num2.get()

        result = num1 * num2
        self.result.set(f"Result: {result}")


def main():
    calc = Calculator()
    calc.run()


main()
