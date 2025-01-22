import tkinter as tk
from tkinter import messagebox
import json
import string
import re
import os
import random

# Function to load user data from the JSON file
def load_data():
    if os.path.exists("users.json"):
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}  # In case the JSON is empty or corrupted
    return {}

# Function to save user data to the JSON file
def save_data():
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Initialize the users dictionary from the JSON file
users = load_data()

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

# Function to handle sign in (sign up)
def sign_in():
    firstname = entry_signup_firstname.get()
    lastname = entry_signup_lastname.get()
    email = entry_signup_email.get()
    password = entry_signup_password.get()

    # Check for symbols or spaces in first name and last name
    if any(char in string.punctuation for char in firstname) or any(char in string.punctuation for char in lastname):
        messagebox.showerror("Sign Up Gagal", "First name and Last name cannot contain symbols or punctuation.")
    elif ' ' in firstname or ' ' in lastname:
        messagebox.showerror("Sign Up Gagal", "First name and Last name cannot contain spaces.")
    elif firstname == "" or lastname == "":
        messagebox.showerror("Sign Up Gagal", "First name and Last name cannot be empty")
    elif not is_valid_email(email):
        messagebox.showerror("Sign Up Gagal", "Invalid email format.")
    elif email in users:
        messagebox.showwarning("Sign Up Gagal", "Email already exists!")
    elif password == "":
        messagebox.showerror("Sign Up Gagal", "Password cannot be empty")
    else:
        global current_otp, otp_email
        current_otp = generate_otp()
        otp_email = email
        
        # Simulate sending OTP (In a real scenario, we would send this via email)
        messagebox.showinfo("OTP Sent", f"An OTP has been sent to your email: {current_otp}\nPlease enter the OTP to complete your registration.")
        
        # Hide the sign-up frame and show OTP verification
        button_signup.grid_forget()
        button_to_login.grid_forget()
        otp_window = tk.Toplevel(root)
        show_otp_entry_window(otp_window)

# Function to verify OTP
def verify_otp(otp_window):
    entered_otp = entry_otp.get()
    if entered_otp == current_otp:
        # OTP is correct, save the user data
        users[otp_email] = {'password': entry_signup_password.get(), 'firstname': entry_signup_firstname.get(), 'lastname': entry_signup_lastname.get()}
        save_data()
        messagebox.showinfo("Sign Up Berhasil", f"Email {otp_email} berhasil didaftarkan!")
        entry_signup_password.delete(0, tk.END)
        entry_signup_firstname.delete(0, tk.END)
        entry_signup_lastname.delete(0, tk.END)
        entry_signup_email.delete(0, tk.END)
        entry_otp.delete(0, tk.END)
        show_login_page()
    else:
        messagebox.showerror("OTP Gagal", "Incorrect OTP. Please try again.")
    button_signup.grid(row=4, column=1)
    button_to_login.grid(row=5, column=1)
    otp_window.destroy()
    

# Function to handle login (using email and password)
def log_in():
    email = entry_login_email.get()
    password = entry_login_password.get()

    if email in users:
        if password == users[email]['password']:
            messagebox.showinfo("Login Berhasil", f"Welcome back {users[email]['firstname']} {users[email]['lastname']}!")
            root.quit()
        else:
            messagebox.showerror("Login Gagal", "Incorrect password.")
    else:
        messagebox.showerror("Login Gagal", "No account found with this email.")

    entry_login_password.delete(0, tk.END)
    entry_login_email.delete(0, tk.END)

# Function to handle password reset - Step 1 (Email verification)
def verify_email(reset_password_frame, entry_reset_email):
    email = entry_reset_email.get()

    if email == "":
            messagebox.showerror("Reset Password Gagal","Email Kosong")

    elif email in users:
        # entry_reset_email.grid_forget()  # Hide email entry
        # label_reset_email.grid_forget()  # Hide email label
        # button_verify.grid_forget()  # Hide verify button
        # label_reset_password.grid(row=0, column=0, padx=10, pady=5)  # Show password entry
        # entry_reset_password.grid(row=0, column=1, padx=10, pady=5)
        # button_reset.grid(row=1, column=1, padx=10, pady=10)  # Show reset button
        show_reset_password_form(reset_password_frame, email)
    else:
        messagebox.showerror("Reset Password Gagal", "Email not found.")
        show_verify_email(reset_password_frame)

    entry_reset_email.delete(0, tk.END)

# Function to reset password (Step 2)
def reset_password(reset_password_frame, entry_reset_password, email):
    new_password = entry_reset_password.get()
        
    if new_password == "":
        messagebox.showerror("Reset Password Gagal", "Password cannot be empty.")
        show_reset_password_form(reset_password_frame)
    else:
        users[email]['password'] = new_password
        save_data()
        messagebox.showinfo("Reset Password Berhasil", "Password has been successfully reset!")
        show_login_page()

    entry_reset_password.delete(0, tk.END)

def show_otp_entry_window(otp_window):
    global entry_otp

    # Create a new top-level window for OTP entry
    otp_window.title("Enter OTP")
    otp_window.geometry("300x150")
    
    label_otp = tk.Label(otp_window, text="Enter OTP:")
    label_otp.pack(padx=10, pady=10)

    entry_otp = tk.Entry(otp_window)
    entry_otp.pack(padx=10, pady=5)

    button_verify_otp = tk.Button(otp_window, text="Verify OTP", command=lambda: verify_otp(otp_window))
    button_verify_otp.pack(pady=10)
# Function to show the sign-up page
def show_signup_page():
    login_frame.grid_forget()  # Hide the login frame
    reset_password_frame.grid_forget()  # Hide reset password frame if shown
    signup_frame.grid(row=0, column=0)  # Show the sign-up frame

# Function to show the login page
def show_login_page():
    signup_frame.grid_forget()  # Hide the sign-up frame
    reset_password_frame.grid_forget()  # Hide reset password frame if shown
    login_frame.grid(row=0, column=0)  # Show the login frame

# Function to show the reset password form
def show_reset_password_page():
    login_frame.grid_forget()  # Hide the login frame
    signup_frame.grid_forget()  # Hide the sign-up frame
    reset_password_frame.grid(row=0, column=0)  # Show the reset password form

def show_verify_email(reset_password_frame):
    label_reset_email = tk.Label(reset_password_frame, text="Enter your email:")
    label_reset_email.grid(row=0, column=0, padx=10, pady=5)

    entry_reset_email = tk.Entry(reset_password_frame)
    entry_reset_email.grid(row=0, column=1, padx=10, pady=5)
    
    button_verify = tk.Button(reset_password_frame, text="Verify Email", command=lambda: verify_email(reset_password_frame, entry_reset_email))
    button_verify.grid(row=1, column=1, padx=10, pady=10)

def show_reset_password_form(reset_password_frame, email):
    label_reset_password = tk.Label(reset_password_frame, text="Enter new password:")
    button_reset = tk.Button(reset_password_frame, text="Reset Password", command=lambda: reset_password(reset_password_frame, entry_reset_password, email))
    entry_reset_password = tk.Entry(reset_password_frame, show="*")
    label_reset_password.grid(row=0, column=0, padx=10, pady=5)  # Show password entry
    entry_reset_password.grid(row=0, column=1, padx=10, pady=5)
    button_reset.grid(row=1, column=1, padx=10, pady=10)  # Show reset button

# Initialize the Tkinter root window
root = tk.Tk()
root.title("Sign In or Log In")
root.geometry("300x300")

# Frame for sign-up page
signup_frame = tk.Frame(root)

label_signup_firstname = tk.Label(signup_frame, text="First name:")
label_signup_firstname.grid(row=0, column=0)

label_signup_lastname = tk.Label(signup_frame, text="Last name:")
label_signup_lastname.grid(row=1, column=0)

label_signup_email = tk.Label(signup_frame, text="Email:")
label_signup_email.grid(row=2, column=0)

label_signup_password = tk.Label(signup_frame, text="Password:")
label_signup_password.grid(row=3, column=0)

entry_signup_firstname = tk.Entry(signup_frame)
entry_signup_firstname.grid(row=0, column=1)

entry_signup_lastname = tk.Entry(signup_frame)
entry_signup_lastname.grid(row=1, column=1)

entry_signup_email = tk.Entry(signup_frame)
entry_signup_email.grid(row=2, column=1)

entry_signup_password = tk.Entry(signup_frame, show="*")
entry_signup_password.grid(row=3, column=1)

button_signup = tk.Button(signup_frame, text="Sign Up", command=sign_in)
button_signup.grid(row=4, column=1)

button_to_login = tk.Button(signup_frame, text="Already have an account? Log In", command=show_login_page)
button_to_login.grid(row=5, column=1)

# Frame for login page
login_frame = tk.Frame(root)

label_login_email = tk.Label(login_frame, text="Email:")
label_login_email.grid(row=0, column=0)

label_login_password = tk.Label(login_frame, text="Password:")
label_login_password.grid(row=1, column=0)

entry_login_email = tk.Entry(login_frame)
entry_login_email.grid(row=0, column=1)

entry_login_password = tk.Entry(login_frame, show="*")
entry_login_password.grid(row=1, column=1)

button_login = tk.Button(login_frame, text="Log In", command=log_in)
button_login.grid(row=2, column=1)

button_to_signup = tk.Button(login_frame, text="Don't have an account? Sign Up", command=show_signup_page)
button_to_signup.grid(row=3, column=1)

button_forgot_password = tk.Button(login_frame, text="Forgot Password?", command=show_reset_password_page)
button_forgot_password.grid(row=4, column=1)

# Frame for reset password page
reset_password_frame = tk.Frame(root)

show_verify_email(reset_password_frame)

# Initially show the login page
show_login_page()

# Start the Tkinter event loop
root.mainloop()
