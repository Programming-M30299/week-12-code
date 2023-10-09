from tkinter import *


class LoginApp:
    def __init__(self):
        self.win = Tk()
        self.win.title("Employee Login")
        self.win.geometry("250x100")

        self.mainframe = Frame(self.win)
        self.mainframe.grid(column=0, row=0)

        self.username = StringVar()
        self.password = StringVar()
        self.message = StringVar()
        self.message.set("Enter username and password.")

        self.create_widgets()

        self.win.mainloop()

    def create_widgets(self):
        Label(self.mainframe, textvariable=self.message, width=30).grid(
            column=1, row=0, columnspan=2)

        Label(self.mainframe, text="Username:").grid(column=1, row=1)
        Entry(self.mainframe, width=25,
              textvariable=self.username).grid(column=2, row=1)

        Label(self.mainframe, text="Password:").grid(column=1, row=2)
        Entry(self.mainframe, width=25, textvariable=self.password,
              show='*').grid(column=2, row=2)

        Button(self.mainframe, text="Sign in",
               command=self.authenticate).grid(column=1, row=3)
        Button(self.mainframe, text="Cancel",
               command=self.win.quit).grid(column=2, row=3)

    def authenticate(self):
        username = self.username.get()
        password = self.password.get()

        loginDetails = {
            "YousefD": "VenterboSS",
            "SergeiT": "25Operyu",
            "Yemi": "Idec704",
            "WernerS": "IAmMel12"
        }

        if username not in loginDetails:
            self.message.set("Username not found.")
        elif loginDetails[username] != password:
            self.message.set("Incorrect password.")
        else:
            self.message.set("Login successful!")


app = LoginApp()
