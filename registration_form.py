import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
import re
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Raghav@2104",
    database="expense_tracker"
)
mycursor = mydb.cursor()
base = Tk()
base.geometry('500x500')
base.title("Registration Form")

bg = PhotoImage(file = "ExpenseTracker.png")
label6 = Label(base, image = bg)
label6.place(x = 0, y = 0)


registration = Label(base, text="Registration form",width=20, font=("bold", 20))
registration.place(x=90, y=53)


Name = Label(base, text="FullName", width=17, font=("bold", 10))
Name.place(x=80, y=130)

NameEntry = Entry(base)
NameEntry.place(x=240, y=130)

Email = Label(base, text="Email", width=17, font=("bold", 10))
Email.place(x=68, y=170)

EmailEntry = Entry(base)
EmailEntry.place(x=240, y=170)


PhnNo = Label(base, text="Phone number", width=17, font=("bold", 10))
PhnNo.place(x=70, y=220)

PhnNoEntry = Entry(base)
PhnNoEntry.place(x=240, y=220)

Username = Label(base, text="Username", width=17, font=("bold", 10))
Username.place(x=80, y=270)

UsernameEntry = Entry(base)
UsernameEntry.place(x=240, y=270)


Password = Label(base, text="Password:", width=17, font=("bold", 10))
Password.place(x=70, y=320)

PasswordEntry = Entry(base, show='*')
PasswordEntry.place(x=240, y=320)


def click():
    # print("True")
    length = len(PasswordEntry.get())
    small = re.search("[a-z]", PasswordEntry.get())
    caps = re.search("[A-Z]", PasswordEntry.get())
    num = re.search("[0-9]", PasswordEntry.get())
    spchar = re.search("[_@$]", PasswordEntry.get())

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


def checkUsername():
    # pass
    name = UsernameEntry.get()
    mycursor.execute("SHOW TABLES")
    ans=False
    for x in mycursor:
        if x[0] == name:
            ans=False
            showinfo(title="Username", message='''Username is already in use!! Please try a different username''')
            break;
        else:
            ans=True
    return ans


def combine_funcs():
    if checkUsername()and click():
        print("Next")


Button(base, text='Submit', width=20, bg='black', fg='white',command=combine_funcs).place(x=180, y=380)

base.mainloop()

