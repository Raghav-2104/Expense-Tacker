import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
import re
import sqlite3

conn = sqlite3.connect('Expense Tracker.db')
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

import tkinter as tk
import sqlite3
from tkinter.messagebox import showinfo
import pywhatkit
from datetime import timedelta
import datetime

conn = sqlite3.connect('Expense Tracker.db')
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

        # self.button_back = tk.Button(self, text='Back', width=15, font=("Helvetica", 12, "bold"), bg='#5c5c5c', fg='white', command=self.back)
        # self.button_back.place(x=50, y=450)


    def submit(self):
        global username
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

    def forget(self):
        ForgetPasswordWindow()
        self.destroy()

import datetime
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import sv_ttk

connector = sqlite3.connect("Expense Tracker.db")
cursor = connector.cursor()

class Home(tk.Tk):
    def __init__(self):
        super().__init__()
        connector.execute(
            f'CREATE TABLE IF NOT EXISTS {username} (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Date DATETIME, Payee TEXT, Expense TEXT, Amount FLOAT, ModeOfPayment TEXT)'
        )
        self.geometry("1130x607") 
        self.title("Expense Tracker")

        sv_ttk.set_theme("dark")

        self.desc = StringVar()
        self.amnt = DoubleVar()
        self.payee = StringVar()
        self.MoP = StringVar(value="Cash")
        self.VoP = StringVar(value="Expense")

        self.sideFrame = Frame(self, background="#1b1b1b", width=250)
        self.buttonFrame = Frame(self, background="#212121", height=60)
        self.buttonFrame.pack(side=TOP, fill=X)
        self.sideFrame.pack(side=LEFT, fill=Y)

        self.date = DateEntry(self.sideFrame,date=datetime.datetime.now())
        Label(self.sideFrame, text="Date: ", background="#1b1b1b").place(x=5, y=15)
        self.date.place(x=60, y=10)

        Label(self.sideFrame, text="Expense: ", background="#1b1b1b").place(x=5, y=80)
        self.expense_list = ttk.OptionMenu(self.sideFrame, self.VoP,
                                    *[ 'Travel','Food', 'Education', 'Entertainment', 'Electricity', 'Household',
                                        'Others'])
        self.expense_list.config(width=15)
        self.expense_list.place(x=70, y=80)

        ttk.Label(self.sideFrame, text="Amount: ", background="#1b1b1b").place(x=5, y=145)
        ttk.Entry(self.sideFrame, text=self.amnt).place(x=70, y=140)

        ttk.Label(self.sideFrame, text="Payee: ", background="#1b1b1b").place(x=5, y=205)
        ttk.Entry(self.sideFrame, text=self.payee).place(x=60, y=205)

        ttk.Label(self.sideFrame, text="Mode Of Pay: ", background="#1b1b1b").place(x=5, y=270)
        self.mode_of_pay = ttk.OptionMenu(self.sideFrame, self.MoP,
                                    *['Cash', 'Cheque', 'Credit Card', 'Debit Card', 'Paytm', 'Google Pay', 'Razorpay',
                                    'BHIM UPI'])
        self.mode_of_pay.config(width=10)
        self.mode_of_pay.place(x=100, y=265)

        ttk.Button(self.sideFrame, text='Add expense', command=self.add_another_expense).place(x=10, y=350)

        #########################################################

        ttk.Button(self.buttonFrame, text='Delete Expense', command=self.remove_expense).place(x=5, y=11)

        ttk.Button(self.buttonFrame, text='Clear Fields in DataEntry', command=self.clear_fields).place(x=130, y=11)

        ttk.Button(self.buttonFrame, text='Delete All Expenses',
                command=self.remove_all_expenses).place(x=310, y=11)

        # ttk.Button(self.buttonFrame, text='Edit Selected Expense', command=self.edit_expense).place(x=465, y=11)

        ttk.Button(self.buttonFrame, text='Convert Expense to a sentence', command=self.selected_expense_to_words).place(x=460, y=11)

        ttk.Button(self.buttonFrame, text='Pie-Chart', command=self.piechart).place(x=680, y=11)

        self.tree_frame = Frame(self, background="#121212")
        self.tree_frame.place(relx=0.202, rely=0.11, relwidth=0.79, relheight=0.86)

        self.table = ttk.Treeview(self.tree_frame, selectmode=BROWSE,columns=('ID', 'Date', 'Payee', 'Expense', 'Amount', 'Mode of Payment'))

        self.X_Scroller = Scrollbar(self.table, orient=HORIZONTAL, command=self.table.xview)
        self.Y_Scroller = Scrollbar(self.table, orient=VERTICAL, command=self.table.yview)
        self.X_Scroller.pack(side=BOTTOM, fill=X)
        self.Y_Scroller.pack(side=RIGHT, fill=Y)

        self.table.config(yscrollcommand=self.Y_Scroller.set, xscrollcommand=self.X_Scroller.set)

        self.table.heading('ID', text='S No.', anchor=CENTER)
        self.table.heading('Date', text='Date', anchor=CENTER)
        self.table.heading('Payee', text='Payee', anchor=CENTER)
        self.table.heading('Expense', text='Expense', anchor=CENTER)
        self.table.heading('Amount', text='Amount', anchor=CENTER)
        self.table.heading('Mode of Payment', text='Mode of Payment', anchor=CENTER)

        self.table.column('#0', width=0, stretch=NO)
        self.table.column('#1', width=50, stretch=NO)
        self.table.column('#2', width=95, stretch=NO)  # Date column
        self.table.column('#3', width=150, stretch=NO)  # Payee column
        self.table.column('#4', width=325, stretch=NO)  # Title column
        self.table.column('#5', width=135, stretch=NO)  # Amount column
        self.table.column('#6', width=125, stretch=NO)  # Mode of Payment column

        self.table.place(relx=0, y=0, relheight=1, relwidth=1.2)
        self.list_all_expenses()
    # Functions

    def piechart(self):
        PieChartWindow()
        self.destroy()

    def list_all_expenses(self):
        connector, self.table

        self.table.delete(*self.table.get_children())

        all_data = connector.execute(f'SELECT * FROM {username}')
        data = all_data.fetchall()

        for values in data:
            self.table.insert('', END, values=values)


    def view_expense_details(self):
        self.table
        self.date, self.payee, self.VoP, self.amnt, self.MoP

        if not self.table.selection():
            messagebox.showerror('No expense selected', 'Please select an expense from the table to view its details')

        current_selected_expense = self.table.item(self.table.focus())
        values = current_selected_expense['values']

        expenditure_date = datetime.date(int(values[1][:4]), int(values[1][5:7]), int(values[1][8:]))

        self.date.set_date(expenditure_date)
        self.payee.set(values[2])
        self.desc.set(values[3])
        self.amnt.set(values[4])
        self.MoP.set(values[5])


    def clear_fields(self):
        self.VoP, self.payee, self.amnt, self.MoP, self.date, self.table

        today_date = datetime.datetime.now().date()

        self.VoP.set('')
        self.payee.set('')
        self.amnt.set(0.0)
        self.MoP.set('Cash'), self.date.set_date(today_date)
        self.table.selection_remove(*self.table.selection())
        self.list_all_expenses()

    def remove_expense(self):
        if not self.table.selection():
            messagebox.showerror('No record selected!', 'Please select a record to delete!')
            return

        current_selected_expense = self.table.item(self.table.focus())
        values_selected = current_selected_expense['values']

        surety = messagebox.askyesno('Are you sure?',f'Are you sure that you want to delete the record of {values_selected[2]}')

        if surety:
            connector.execute(f'DELETE FROM {username} WHERE ID=%d' % values_selected[0])
            connector.commit()

            self.list_all_expenses()
            messagebox.showinfo('Record deleted successfully!',
                                'The record you wanted to delete has been deleted successfully')


    def remove_all_expenses(self):
        surety = messagebox.askyesno('Are you sure?','Are you sure that you want to delete all the expense items from the database?',icon='warning')

        if surety:
            self.table.delete(*self.table.get_children())

            connector.execute(f'DELETE FROM {username}')
            connector.commit()

            self.clear_fields()
            self.list_all_expenses()
            messagebox.showinfo('All Expenses deleted', 'All the expenses were successfully deleted')
        else:
            messagebox.showinfo('Ok then', 'The task was aborted and no expense was deleted!')


    def add_another_expense(self):
        self.date, self.payee, self.VoP, self.amnt, self.MoP

        if not self.date.get() or not self.payee.get() or not self.amnt.get() or not self.MoP.get():
            messagebox.showerror('Fields empty!', "Please fill all the missing fields before pressing the add button!")
        else:
            connector.execute(
                f'INSERT INTO {username} (Date, Payee, Expense, Amount, ModeOfPayment) VALUES (?, ?, ?, ?, ?)',
                (self.date.get_date(), self.payee.get(), self.VoP.get(), self.amnt.get(), self.MoP.get())
            )
            connector.commit()
            self.clear_fields()
            self.list_all_expenses()
            messagebox.showinfo('Expense added','The expense whose details you just entered has been added to the database')

    def selected_expense_to_words(self):
        self.table

        if not self.table.selection():
            messagebox.showerror('No expense selected!', 'Please select an expense from the self.table for us to read')
            return

        current_selected_expense = self.table.item(self.table.focus())
        values = current_selected_expense['values']

        message = f'Your expense can be read like: \n"You paid {values[4]} to {values[2]} for {values[3]} on {values[1]} via {values[5]}"'

        messagebox.showinfo('Here\'s how to read your expense', message)


    def expense_to_words_before_adding(self):
        self.date, self.VoP, self.amnt, self.payee, self.MoP

        if not self.date or not self.VoP or not self.amnt or not self.payee or not self.MoP:
            messagebox.showerror('Incomplete data', 'The data is incomplete, meaning fill all the fields first!')

        message = f'Your expense can be read like: \n"You paid {self.amnt.get()} to {self.payee.get()} for {self.desc.get()} on {self.date.get_date()} via {self.MoP.get()}"'

        add_question = messagebox.askyesno('Read your record like: ', f'{message}\n\nShould I add it to the database?')

        if add_question:
            self.add_another_expense()
        else:
            messagebox.showinfo('Ok', 'Please take your time to add this record')

        self.list_all_expenses()
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import pywhatkit
import random
from tkinter.messagebox import showinfo
import sqlite3

class ForgetPasswordWindow(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.title("Forget Password")
        self.geometry("500x550")
        self.configure(bg="#1b1b1b")
        self.create_widgets()

    def create_widgets(self):
        self.whatsapp_label = tk.Label(self, text="WhatsApp Number (with country code):", fg="white", bg="#1b1b1b")
        self.whatsapp_label.pack(pady=(20, 5))
        
        self.whatsapp_entry = tk.Entry(self)
        self.whatsapp_entry.pack(ipady=5)
        
        self.otp_label = tk.Label(self, text="OTP received on WhatsApp:", fg="white", bg="#1b1b1b")
        self.otp_label.pack(pady=(20, 5))
        
        self.otp_entry = tk.Entry(self, show="*")
        self.otp_entry.pack(ipady=5)
        
        self.generate_otp_button = tk.Button(self, text="Generate OTP", command=self.generate_otp, bg="#3895D3", fg="white")
        self.generate_otp_button.pack(pady=(20, 5))
        
        self.new_password_label = tk.Label(self, text="New Password:", fg="white", bg="#1b1b1b")
        self.new_password_label.pack(pady=(20, 5))
        
        self.new_password_entry = tk.Entry(self, show="*")
        self.new_password_entry.pack(ipady=5)
        
        self.confirm_password_label = tk.Label(self, text="Confirm Password:", fg="white", bg="#1b1b1b")
        self.confirm_password_label.pack(pady=(20, 5))
        
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.pack(ipady=5)
        
        self.reset_button = tk.Button(self, text="Reset Password", command=self.reset_password, bg="#3895D3", fg="white")
        self.reset_button.pack(pady=(20, 5))

        self.back_button = tk.Button(self, text="Back",command=self.back, bg="#3895D3", fg="white")
        self.back_button.pack(pady=(20, 5))

        self.number = random.randint(0, 9999)

    def back(self):
        register()
        self.destroy()
    
    def reset_password(self):
        whatsapp = self.whatsapp_entry.get()
        print(whatsapp[3:])
        otp = self.otp_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        if not whatsapp:
            messagebox.showerror("Error", "Please enter your WhatsApp number.")
        elif not otp:
            messagebox.showerror("Error", "Please enter the OTP received on WhatsApp.")
        elif not new_password or not confirm_password:
            messagebox.showerror("Error", "Please enter a new password and confirm it.")
        elif new_password != confirm_password:
            messagebox.showerror("Error", "The passwords do not match.")
        else:
            # Verify OTP
            if self.verify_otp(whatsapp, otp):
                # Update password in database
                try:
                    conn = sqlite3.connect('Expense Tracker.db')
                    cursor = conn.cursor()
                    cursor.execute("UPDATE registration SET password=? WHERE phone=?", (new_password, whatsapp[3:]))
                    conn.commit()
                    messagebox.showinfo("Success", "Your password has been updated.")
                except sqlite3.Error as error:
                    print("Failed to update record to database: {}".format(error))
                finally:
                    if conn:
                        cursor.close()
                        conn.close()
            else:
                messagebox.showerror("Error", "The OTP entered is incorrect.")

    def verify_otp(self, whatsapp, otp):
        # print(int(self.otp_entry.get())==self.number)
        if int(self.otp_entry.get())==self.number:
            return True
        else:
            return False
        
    
    def generate_otp(self):
        whatsapp = self.whatsapp_entry.get()
        if not whatsapp:
            messagebox.showerror("Error", "Please enter your WhatsApp number.")
        else:
            pywhatkit.sendwhatmsg_instantly(whatsapp, message=str(self.number), wait_time=15)
            messagebox.showinfo("OTP", "An OTP has been sent to your WhatsApp number.")
import tkinter as tk
from tkinter import messagebox
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class PieChartWindow:
    def __init__(self):
        self.conn = None
        self.cursor = None

        self.root = tk.Tk()
        self.root.title("Daily Expense Pie Chart")
        self.root.geometry("700x700")
        self.root.configure(bg="#FFFFFF")
        self.create_widgets()

        self.root.mainloop()
        
    def create_widgets(self):
    # create a frame to hold the pie chart and the button
        chart_frame = tk.Frame(self.root,)
        chart_frame.grid(row=0, column=0, sticky="nsew")

        # connect to the database
        try:
            self.conn = sqlite3.connect('Expense Tracker.db')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error connecting to database: {e}")

        # fetch data from the database
        try:
            self.cursor.execute(f"SELECT Expense, SUM(Amount) as Total_Expenditure FROM {username} GROUP BY Expense")
            data = self.cursor.fetchall()
            print(data)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error fetching data from database: {e}")
            return

        # prepare data for the pie chart
        labels = [row[0] for row in data]
        sizes = [row[1] for row in data]
        # create a figure and a pie chart
        fig = Figure(figsize=(5, 5))
        ax = fig.add_subplot(111)
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")

        # create a canvas to display the pie chart
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.get_tk_widget().grid(row=0, column=0, rowspan=2, sticky="nsew")

        # create a button to go back
        back_button = tk.Button(chart_frame, text="Back", command=self.root.destroy,bg='#1b1b1b',fg='white',font=('Arial', 10, 'bold'))
        back_button.grid(row=1, column=0, sticky="s")

    def __del__(self):
        # close the database connection when the window is closed
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
  app = register()
  app.mainloop()