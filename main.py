import tkinter as tk
from tkinter import messagebox
import string
from log_in_sign_in import is_valid_email, generate_otp, load_data, save_data
from Input_General_Information import GeneralInformationForm
from Input_Related import SedentaryExercisePlanner
from Homepage import create_homepage

# Global variables
users = load_data()
current_otp = None
otp_email = None

# Sign-up functionality
def sign_up():
    firstname = entry_signup_firstname.get()
    lastname = entry_signup_lastname.get()
    email = entry_signup_email.get()
    password = entry_signup_password.get()

    if any(char in string.punctuation for char in firstname) or any(char in string.punctuation for char in lastname):
        messagebox.showerror("Sign Up Error", "First name and Last name cannot contain symbols or punctuation.")
    elif ' ' in firstname or ' ' in lastname:
        messagebox.showerror("Sign Up Error", "First name and Last name cannot contain spaces.")
    elif firstname == "" or lastname == "":
        messagebox.showerror("Sign Up Error", "First name and Last name cannot be empty.")
    elif not is_valid_email(email):
        messagebox.showerror("Sign Up Error", "Invalid email format.")
    elif email in users:
        messagebox.showwarning("Sign Up Error", "Email already exists!")
    elif password == "":
        messagebox.showerror("Sign Up Error", "Password cannot be empty.")
    else:
        global current_otp, otp_email
        current_otp = generate_otp()
        otp_email = email
        
        # Simulate OTP (would normally send via email)
        messagebox.showinfo("OTP Sent", f"An OTP has been sent to your email: {current_otp}")
        
        show_otp_entry_window()

# OTP verification
def verify_otp():
    """Verify OTP and transition to General and Related Information forms."""
    global otp_window
    entered_otp = entry_otp.get()

    if entered_otp == current_otp:
        # Save user data
        users[otp_email] = {
            'password': entry_signup_password.get(),
            'firstname': entry_signup_firstname.get(),
            'lastname': entry_signup_lastname.get()
        }
        save_data(users)
        messagebox.showinfo("Sign Up Success", "You have successfully registered!")

        # Close OTP window
        otp_window.destroy()

        # Go to Input General and Related Information forms
        show_general_and_related_info_forms()
    else:
        messagebox.showerror("OTP Error", "Incorrect OTP. Please try again.")


def show_general_and_related_info_forms():
    """Transition to General Information and Related Information forms."""
    # Destroy login/signup window
    root.destroy()

    # Open General Information form
    GeneralInformationForm()

    # Open Related Information form
    SedentaryExercisePlanner()

    # After completing forms, transition to the homepage
    create_homepage()

def show_login_page():
    """Display the login page frame."""
    signup_frame.grid_forget()
    login_frame.grid(row=0, column=0)

    # Reset login fields
    entry_login_email.delete(0, tk.END)
    entry_login_password.delete(0, tk.END)


# Login functionality
def log_in():
    email = entry_login_email.get()
    password = entry_login_password.get()

    if email in users and password == users[email]['password']:
        messagebox.showinfo("Login Success", f"Welcome back, {users[email]['firstname']}!")
        create_homepage()  # Directly go to homepage
    else:
        messagebox.showerror("Login Error", "Incorrect email or password.")

# Reset password functionality
def reset_password(email, new_password):
    if email in users:
        users[email]['password'] = new_password
        save_data(users)
        messagebox.showinfo("Password Reset", "Your password has been updated successfully!")
        show_login_page()
    else:
        messagebox.showerror("Error", "Email not found.")

# OTP window for verification
def show_otp_entry_window():
    global otp_window, entry_otp
    otp_window = tk.Toplevel(root)
    otp_window.title("Verify OTP")
    otp_window.geometry("300x150")
    
    tk.Label(otp_window, text="Enter OTP:").pack(pady=10)
    entry_otp = tk.Entry(otp_window)
    entry_otp.pack(pady=5)
    tk.Button(otp_window, text="Verify", command=verify_otp).pack(pady=10)

# Show sign-up page
def show_signup_page():
    login_frame.grid_forget()
    signup_frame.grid(row=0, column=0)

# Show login page
def show_login_page():
    signup_frame.grid_forget()
    login_frame.grid(row=0, column=0)

# Tkinter setup
root = tk.Tk()
root.title("Sign In or Sign Up")
root.geometry("300x300")

# Sign-up frame
signup_frame = tk.Frame(root)
tk.Label(signup_frame, text="First name:").grid(row=0, column=0)
entry_signup_firstname = tk.Entry(signup_frame)
entry_signup_firstname.grid(row=0, column=1)

tk.Label(signup_frame, text="Last name:").grid(row=1, column=0)
entry_signup_lastname = tk.Entry(signup_frame)
entry_signup_lastname.grid(row=1, column=1)

tk.Label(signup_frame, text="Email:").grid(row=2, column=0)
entry_signup_email = tk.Entry(signup_frame)
entry_signup_email.grid(row=2, column=1)

tk.Label(signup_frame, text="Password:").grid(row=3, column=0)
entry_signup_password = tk.Entry(signup_frame, show="*")
entry_signup_password.grid(row=3, column=1)

tk.Button(signup_frame, text="Sign Up", command=sign_up).grid(row=4, column=1)
tk.Button(signup_frame, text="Back to Login", command=show_login_page).grid(row=5, column=1)

# Login frame
login_frame = tk.Frame(root)
tk.Label(login_frame, text="Email:").grid(row=0, column=0)
entry_login_email = tk.Entry(login_frame)
entry_login_email.grid(row=0, column=1)

tk.Label(login_frame, text="Password:").grid(row=1, column=0)
entry_login_password = tk.Entry(login_frame, show="*")
entry_login_password.grid(row=1, column=1)

tk.Button(login_frame, text="Log In", command=log_in).grid(row=2, column=1)
tk.Button(login_frame, text="Sign Up", command=show_signup_page).grid(row=3, column=1)

# Start with the login page
show_login_page()

# Start Tkinter loop
root.mainloop()
