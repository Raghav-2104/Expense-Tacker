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
            'CREATE TABLE IF NOT EXISTS ExpenseTracker (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Date DATETIME, Payee TEXT, Expense TEXT, Amount FLOAT, ModeOfPayment TEXT)'
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
        from piechart import PieChartWindow
        print('Piechart')
        PieChartWindow('Expense Tracker.db')
        self.destroy()

    def list_all_expenses(self):
        connector, self.table

        self.table.delete(*self.table.get_children())

        all_data = connector.execute('SELECT * FROM ExpenseTracker')
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
            connector.execute('DELETE FROM ExpenseTracker WHERE ID=%d' % values_selected[0])
            connector.commit()

            self.list_all_expenses()
            messagebox.showinfo('Record deleted successfully!',
                                'The record you wanted to delete has been deleted successfully')


    def remove_all_expenses(self):
        surety = messagebox.askyesno('Are you sure?','Are you sure that you want to delete all the expense items from the database?',icon='warning')

        if surety:
            self.table.delete(*self.table.get_children())

            connector.execute('DELETE FROM ExpenseTracker')
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
                'INSERT INTO ExpenseTracker (Date, Payee, Expense, Amount, ModeOfPayment) VALUES (?, ?, ?, ?, ?)',
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
if __name__ == '__main__':
    app=Home()
    app.mainloop()