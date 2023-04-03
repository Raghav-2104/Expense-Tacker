import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
import re
import sqlite3
# from avg import temp

conn = sqlite3.connect('expense_tracker.db')
mycursor = conn.cursor()
mycursor.execute('''CREATE TABLE IF NOT EXISTS registration
                (name TEXT, email TEXT UNIQUE, phone TEXT, user TEXT PRIMARY KEY, password TEXT)''')

class register(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='#1b1b1b')

        self.geometry('500x500')
        self.title("Registration Form")

        self.registration = Label(self, text="Registration form", width=20, font=("bold", 20), fg="white", bg='#1b1b1b')
        self.registration.place(x=90, y=53)


        self.Name = Label(self, text="Full Name", width=17, font=("bold", 10), fg="white", bg='#1b1b1b')
        self.Name.place(x=80, y=130)

        self.NameEntry = Entry(self, bg='white')
        self.NameEntry.place(x=240, y=130)

        self.Email = Label(self, text="Email", width=17, font=("bold", 10), fg="white", bg='#1b1b1b')
        self.Email.place(x=80, y=170)

        self.EmailEntry = Entry(self, bg='white')
        self.EmailEntry.place(x=240, y=170)


        self.PhnNo = Label(self, text="Phone number", width=17, font=("bold", 10), fg="white", bg='#1b1b1b')
        self.PhnNo.place(x=80, y=210)

        self.PhnNoEntry = Entry(self, bg='white')
        self.PhnNoEntry.place(x=240, y=210)

        self.Username = Label(self, text="Username", width=17, font=("bold", 10), fg="white", bg='#1b1b1b')
        self.Username.place(x=80, y=260)

        self.UsernameEntry = Entry(self, bg='white')
        self.UsernameEntry.place(x=240, y=260)


        self.Password = Label(self, text="Password", width=17, font=("bold", 10), fg="white", bg='#1b1b1b')
        self.Password.place(x=80, y=310)

        self.PasswordEntry = Entry(self, show='*', bg='white')
        self.PasswordEntry.place(x=240, y=310)
        self.Button = Button(self, text='Submit', width=20, bg='black', fg='white', command=self.combine_funcs)
        self.Button.place(x=100, y=380)
        
        self.Login = Button(self, text='Login', width=20, bg='black', fg='white', command=self.login)
        self.Login.place(x=280, y=380)

    def login(self):
        from login_form import LoginForm
        self.destroy()
        LoginForm()
    def click(self):
        # print("True")
        length = len(self.PasswordEntry.get())
        small = re.search("[a-z]", self.PasswordEntry.get())
        caps = re.search("[A-Z]", self.PasswordEntry.get())
        num = re.search("[0-9]", self.PasswordEntry.get())
        spchar = re.search("[_@$]", self.PasswordEntry.get())

        if length < 8 or small == None or caps == None or num == None or spchar == None:
            showinfo(title="Password", message='''Primary conditions for password validation:
                1.Minimum 8 characters.
                2.The alphabet must be between [a-z]
                3.At least one alphabet should be of Upper Case [A-Z]
                4.At least 1 number or digit between [0-9].
                5.At least 1 character from [ _ or @ or $ ].''')
            return False
        else:
            # print(False)
            return True

    def add_data(self,*args):
        name=self.NameEntry.get()
        email=self.EmailEntry.get()
        phone=self.PhnNoEntry.get()
        user=self.UsernameEntry.get()
        password=self.PasswordEntry.get()
        try:
            mycursor.execute("INSERT INTO registration VALUES (?,?,?,?,?)",(name,email,phone,user,password))
            conn.commit()
            print(mycursor.fetchall)
            showinfo("Registration","Registration Successfully")
        except Exception as err:
            print(err)

    def checkUsername(self):
            # pass
          print("CheckUSername")
          name = self.UsernameEntry.get()
          mycursor.execute("SELECT user from registration")
          rows = mycursor.fetchall()
          ans = True
          for row in rows:
              if row[0] == name:
                  ans = False
                  showinfo(title="Username", message='''Username is already in use!! Please try a different username''')
                  break
          return ans


    def combine_funcs(self):
          if self.checkUsername() and self.click():
            self.add_data()


if __name__ == "__main__":
  app = register()
  app.mainloop()