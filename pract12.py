from tkinter import Tk, Frame, Label, Entry, Button, StringVar


class LoginApp:

    def __init__(self, login_details):
        self.login_details = login_details
        self.win = Tk()
        self.win.title("Employee Login")
        self.win.geometry("250x100")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)

        self.user_name = StringVar()
        self.password = StringVar()
        self.message = StringVar()
        self.message.set("Enter username and password.")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_message = Label(
            self.main_frame,
            textvariable=self.message,
            width=30
        )
        label_message.grid(column=0, row=0, columnspan=2)

        label_user_name = Label(
            self.main_frame,
            text="Username:"
        )
        label_user_name.grid(column=0, row=1)

        entry_user_name = Entry(
            self.main_frame,
            width=25,
            textvariable=self.user_name
        )
        entry_user_name.grid(column=1, row=1)

        label_password = Label(
            self.main_frame,
            text="Password:"
        )
        label_password.grid(column=0, row=2)

        entry_password = Entry(
            self.main_frame,
            width=25,
            textvariable=self.password
        )
        entry_password.grid(column=1, row=2)

        button_sign_in = Button(
            self.main_frame,
            text="Sign In",
            command=self.authenticate
        )
        button_sign_in.grid(column=0, row=3)

        button_cancel = Button(
            self.main_frame,
            text="Cancel",
            command=self.win.destroy
        )
        button_cancel.grid(column=1, row=3)

    def authenticate(self):
        username = self.user_name.get()
        password = self.password.get()

        if username not in self.login_details:
            self.message.set("Username not found.")
        elif self.login_details[username] != password:
            self.message.set("Incorrect password.")
        else:
            self.message.set("Login successful!")


def main():
    company_login_details = {
        "YousefD": "VenterboSS",
        "SergeiT": "25Operyu",
        "YemiO": "Idec704",
        "WinonaS": "IAmMel12"
    }
    app = LoginApp(company_login_details)
    app.run()


main()
