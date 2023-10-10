from tkinter import *


class Calculator:
    def __init__(self):
        self.win = Tk()
        self.win.title("Multiplication Calculator")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack(padx=10, pady=10)

        self.buttonFrame = Frame(self.mainFrame)  # Frame for buttons
        self.buttonFrame.pack(side="bottom", fill="x", padx=5, pady=5)

        self.num1 = IntVar()
        self.num2 = IntVar()
        self.result = StringVar()
        self.result.set("Result will be here.")

        self.createWidgets()

        self.win.mainloop()

    def createWidgets(self):
        lblNum1 = Label(self.mainFrame, text="Number 1:")
        lblNum1.pack(side="top", anchor="w")

        entryNum1 = Entry(self.mainFrame, width=20, textvariable=self.num1)
        entryNum1.pack(side="top", anchor="w")

        lblNum2 = Label(self.mainFrame, text="Number 2:")
        lblNum2.pack(side="top", anchor="w")

        entryNum2 = Entry(self.mainFrame, width=20, textvariable=self.num2)
        entryNum2.pack(side="top", anchor="w")

        lblResult = Label(self.mainFrame, textvariable=self.result)
        lblResult.pack(side="top", anchor="w")

        btnMultiply = Button(self.buttonFrame, text="Multiply",
                             command=self.multiply)
        btnMultiply.pack(side="left")

        btnClear = Button(self.buttonFrame, text="Clear",
                          command=self.clear)
        btnClear.pack(side="right")

    def multiply(self):
        num1 = self.num1.get()
        num2 = self.num2.get()
        self.result.set(f"Result: {num1 * num2}")

    def clear(self):
        self.num1.set(0)
        self.num2.set(0)
        self.result.set("Result will be here.")


app = Calculator()
