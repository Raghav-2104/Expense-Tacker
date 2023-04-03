import tkinter as tk
from tkinter import messagebox
import mysql.connector
import pywhatkit
import random
from Registration import register
# from login_form import LoginForm
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
                    conn = sqlite3.connect('expense_tracker.db')
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


if __name__ == "__main__":
    app = ForgetPasswordWindow()
    app.mainloop()
