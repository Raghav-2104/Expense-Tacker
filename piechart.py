import tkinter as tk
from tkinter import messagebox
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import datetime as dt


class PieChartWindow:
    def __init__(self):
        
        self.conn = None
        self.cursor = None
        self.ax = None
        self.canvas = None

        self.root = tk.Tk()
        self.root.title("Pie Chart from SQLite Database")
        
        self.root.geometry("700x700")
        self.root.configure(bg="#FFFFFF")
        self.selected_month = tk.StringVar(self.root)
        self.selected_month.set('April')
        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        chart_frame = tk.Frame(self.root,)
        chart_frame.grid(row=0, column=0, sticky="nsew")
        menu_frame = tk.Frame(self.root,)
        menu_frame.grid(row=1, column=0, sticky="s")

        try:
            self.conn = sqlite3.connect("Expense Tracker.db")
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error connecting to database: {e}")

        try:
            self.cursor.execute("SELECT Expense, SUM(Amount) as Total_Expenditure FROM Raghav WHERE strftime('%m', Date) = ? GROUP BY Expense", (dt.datetime.strptime(self.selected_month.get(), '%B').strftime('%m'),))

            data = self.cursor.fetchall()
            print(data)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error fetching data from database: {e}")
            return

        labels = [row[0] for row in data]
        sizes = [row[1] for row in data]

        fig = Figure(figsize=(5, 5))
        self.ax = fig.add_subplot(111)
        self.ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        self.ax.axis("equal")

        self.canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, rowspan=2, sticky="nsew")

        back_button = tk.Button(chart_frame, text="Back", command=self.root.destroy,bg='#1b1b1b',fg='white',font=('Arial', 10, 'bold'))
        back_button.grid(row=1, column=0, sticky="s")


        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month_menu = tk.OptionMenu(menu_frame, self.selected_month, *months, command=self.update_pie_chart)
        month_menu.config(width=10, font=('Arial', 10, 'bold'),bg='#1b1b1b',fg='white')
        month_menu.grid(row=0, column=1)
        
    def update_pie_chart(self, *args):
        month = self.selected_month.get()
        
        try:
            self.cursor.execute("SELECT Expense, SUM(Amount) as Total_Expenditure FROM Raghav WHERE strftime('%m', Date) = ? GROUP BY Expense", (dt.datetime.strptime(month, '%B').strftime('%m'),))
            data = self.cursor.fetchall()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error fetching data from database: {e}")
            return

        labels = [row[0] for row in data]
        sizes = [row[1] for row in data]

        self.ax.clear()
        self.ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        self.ax.axis("equal")

        self.canvas.draw()

    def __del__(self):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    db_file = "Expense Tracker.db"
    app = PieChartWindow()
