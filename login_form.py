import tkinter as tk
import sqlite3
from tkinter.messagebox import showinfo
from Registration import register
import pywhatkit
from datetime import timedelta
import datetime
from forgetPassword import ForgetPasswordWindow
from maincopy import Home
conn = sqlite3.connect('expense_tracker.db')
cursor = conn.cursor()

class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title("Login Form")
        self.configure(background='#1b1b1b')

        self.label_title = tk.Label(self, text="Login Form", width=20, font=("Helvetica", 20, "bold"), fg='white', bg='#1b1b1b')
        self.label_title.place(x=90, y=50)

        self.label_username = tk.Label(self, text="Username", width=17, font=("Helvetica", 12, "bold"), fg='white', bg='#1b1b1b', padx=10, pady=10)
        self.label_username.place(x=60, y=130)

        self.entry_username = tk.Entry(self, font=("Helvetica", 12))
        self.entry_username.place(x=240, y=135)

        self.label_password = tk.Label(self, text="Password", width=17, font=("Helvetica", 12, "bold"), fg='white', bg='#1b1b1b', padx=10, pady=10)
        self.label_password.place(x=60, y=190)

        self.entry_password = tk.Entry(self, show='*', font=("Helvetica", 12))
        self.entry_password.place(x=240, y=195)

        self.button_forgot_password = tk.Button(self, text='Forgot Password?', width=20, font=("Helvetica", 12, "bold"), bg='#5c5c5c', fg='white', command=self.forget)
        self.button_forgot_password.place(x=155, y=250)

        self.button_submit = tk.Button(self, text='Submit', width=20, font=("Helvetica", 12, "bold"), bg='#5c5c5c', fg='white', command=self.submit)
        self.button_submit.place(x=155, y=320)

        self.button_back = tk.Button(self, text='Back', width=15, font=("Helvetica", 12, "bold"), bg='#5c5c5c', fg='white', command=self.back)
        self.button_back.place(x=50, y=450)


    def submit(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        cursor.execute("SELECT password FROM registration WHERE user = ?", (username,))
        result = cursor.fetchone()
        if result and result[0] == password:
            showinfo(title="Login",message="Logged in Successfully")
            self.destroy()
            tracker = Home()
        else:
            showinfo(title="Login",message="Login Failed !! Please check Username and Password")

    def back(self):
        register()
        self.destroy()


    def forget(self):
        ForgetPasswordWindow()
        self.destroy()

    # def main(self):
    #     MAIN()
    #     self.destroy()
if __name__ == "__main__":
    app = LoginForm()
    app.mainloop()
