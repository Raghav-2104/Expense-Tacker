import tkinter as tk
from tkinter import messagebox
import mysql.connector
import pywhatkit
import random
from tkinter.messagebox import showinfo

class ForgetPasswordWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Forget Password")
        self.master.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        # Label for the WhatsApp number
        self.whatsapp_label = tk.Label(self.master, text="WhatsApp Number (with country code):")
        self.whatsapp_label.pack()
        # Entry box for the WhatsApp number
        self.whatsapp_entry = tk.Entry(self.master)
        self.whatsapp_entry.pack()
        # Label for the OTP
        self.otp_label = tk.Label(self.master, text="OTP received on WhatsApp:")
        self.otp_label.pack()
        # Entry box for the OTP
        self.otp_entry = tk.Entry(self.master, show="*")
        self.otp_entry.pack()
        # Button to generate OTP
        self.generate_otp_button = tk.Button(self.master, text="Generate OTP", command=self.generate_otp)
        self.generate_otp_button.pack()
        # Label for the new password
        self.new_password_label = tk.Label(self.master, text="New Password:")
        self.new_password_label.pack()
        # Entry box for the new password
        self.new_password_entry = tk.Entry(self.master, show="*")
        self.new_password_entry.pack()
        # Label for confirming the new password
        self.confirm_password_label = tk.Label(self.master, text="Confirm Password:")
        self.confirm_password_label.pack()
        # Entry box for confirming the new password
        self.confirm_password_entry = tk.Entry(self.master, show="*")
        self.confirm_password_entry.pack()
        # Button to reset password
        self.reset_button = tk.Button(self.master, text="Reset Password", command=self.reset_password)
        self.reset_button.pack()

        self.number = random.randint(0, 9999)
    def reset_password(self):
        whatsapp = self.whatsapp_entry.get()
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
                    conn = mysql.connector.connect(user='root', password='Raghav@2104', host='localhost', database='expense_tracker')
                    cursor = conn.cursor()
                    cursor.execute("UPDATE registration SET password=%s WHERE phone=%s", (new_password, whatsapp))
                    conn.commit()
                    messagebox.showinfo("Success", "Your password has been updated.")
                except mysql.connector.Error as error:
                    print("Failed to update record to database: {}".format(error))
                finally:
                    if conn.is_connected():
                        cursor.close()
                        conn.close()
            else:
                messagebox.showerror("Error", "The OTP entered is incorrect.")

    def verify_otp(self, whatsapp, otp):
        print(int(self.otp_entry.get())==self.number)
        if int(self.otp_entry.get())==self.number:
            return True
        else:
            return False
        
    
    def generate_otp(self):
        whatsapp = self.whatsapp_entry.get()
        if not whatsapp:
            messagebox.showerror("Error", "Please enter your WhatsApp number.")
        else:
            pywhatkit.sendwhatmsg_instantly(whatsapp, message=str(self.number), wait_time=10)
            messagebox.showinfo("OTP", "An OTP has been sent to your WhatsApp number.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ForgetPasswordWindow(master=root)
    app.mainloop()
