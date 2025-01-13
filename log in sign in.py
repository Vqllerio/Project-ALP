import tkinter as tk  # Import the tkinter library for GUI creation
from tkinter import messagebox  # Import messagebox for displaying pop-up messages
import json  # Import JSON to handle data storage

# Function to load user data from the JSON file
def load_data():
    try:
        with open("users.json", "r") as file:
            return json.load(file)  # Load the user data from the JSON file
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

# Function to save user data to the JSON file
def save_data():
    with open("users.json", "w") as file:
        json.dump(users, file)  # Save the current users dictionary to the JSON file

# Initialize the users dictionary from the JSON file
users = load_data()  # Load the existing users from the JSON file

# Function to handle sign in (sign up)
def sign_in():
    username = entry_username.get()  # Get the username input from the entry field
    password = entry_password.get()  # Get the password input from the entry field
    if username == "":
        messagebox.showerror("sign up gagal","username belum ada")
    if password == "":
        messagebox.showerror("sign up gagal","password belum ada")
    # Check if username already exists in the dictionary
    elif username in users:
        messagebox.showwarning("Sign Up Gagal", "Username sudah ada!")  # Show a warning if username exists
    else:
        users[username] = password  # Add the new username and password to the dictionary
        save_data()  # Save updated user data to the JSON file
        messagebox.showinfo("Sign Up Berhasil ", f"Username {username} berhasil didaftarkan!")  # Show a success message
    entry_password.delete(0, tk.END)  # Clear the password entry field
    entry_username.delete(0, tk.END)  # Clear the username entry field

# Function to handle login
def log_in():
    username = entry_username.get()  # Get the username input from the entry field
    password = entry_password.get()  # Get the password input from the entry field
    
    # Check if the username exists in the users dictionary
    if username in users:
        if password == users[username]:  # Check if the password matches the one in the dictionary
            messagebox.showinfo("Login Berhasil", f"{username} telah masuk")  # Show a success message
            root.quit()  # Close the window after successful login
        else:
            messagebox.showerror("Login Gagal", "Maaf username atau password salah")  # Show an error if the password is incorrect
    else:
        messagebox.showerror("Login Gagal", "Maaf username atau password salah")  # Show an error if the username is not found
    entry_password.delete(0, tk.END)  # Clear the password entry field
    entry_username.delete(0, tk.END)  # Clear the username entry field

# Initialize the Tkinter root window
root = tk.Tk()  # Create the main window
root.title("Sign In or Log In")  # Set the title of the window

root.geometry("300x150")  # Set the size of the window
# Label for username
label_username = tk.Label(root, text="Username:")  # Create a label for the username field
label_username.grid(row=0, column=0)  # Place the label in the grid layout

# Label for password
label_password = tk.Label(root, text="Password:")  # Create a label for the password field
label_password.grid(row=1, column=0)  # Place the label in the grid layout

# Entry field for username
entry_username = tk.Entry(root)  # Create an entry field for the username
entry_username.grid(row=0, column=1)  # Place the entry field in the grid layout

# Entry field for password
entry_password = tk.Entry(root, show="*")  # Create an entry field for the password (with * to hide characters)
entry_password.grid(row=1, column=1)  # Place the entry field in the grid layout

# Buttons for sign-in and login
button_sign_in = tk.Button(root, text="Sign Up", command=sign_in)  # Create a button for the sign-up action
button_sign_in.grid(row=2, column=0)  # Place the button in the grid layout

button_log_in = tk.Button(root, text="Log In", command=log_in)  # Create a button for the log-in action
button_log_in.grid(row=2, column=2)  # Place the button in the grid layout

# Start the Tkinter event loop
root.mainloop()  # Run the Tkinter event loop to keep the window open
