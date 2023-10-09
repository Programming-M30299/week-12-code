from tkinter import *


class LoginApp:
    def __init__(self, win):
        self.win = win
        self.win.title("Employee Login")

        self.mainframe = Frame(self.win)
        self.mainframe.grid(column=0, row=0)

        self.username = StringVar()
        self.password = StringVar()
        self.message = StringVar()
        self.message.set(
            "Please enter your username and password then sign in")

        self.create_widgets()

    def create_widgets(self):
        Label(self.mainframe, textvariable=self.message).grid(
            column=1, row=0, columnspan=2)

        Label(self.mainframe, text="Username:").grid(column=1, row=1)
        Entry(self.mainframe, width=20,
              textvariable=self.username).grid(column=2, row=1)

        Label(self.mainframe, text="Password:").grid(column=1, row=2)
        Entry(self.mainframe, width=20, textvariable=self.password,
              show='*').grid(column=2, row=2)

        Button(self.mainframe, text="Sign In",
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
            self.message.set("Username not found")
        elif loginDetails[username] != password:
            self.message.set("Incorrect password")
        else:
            self.message.set("Login successful!")


def main():
    root = Tk()
    app = LoginApp(root)
    root.mainloop()
