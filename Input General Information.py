from tkinter import *

# Initialize the root window
root = Tk()
root.title("General Information Form")
Information = []
# Set a minimum window size
root.geometry("300x200")
root.resizable(False, False)

def Submit():
    Info = [str(Name_Input.get()), int(Age_Input.get()), int(Height_Input.get())]
    print(Info)

# Create and place widgets with padding
Label(root, text="General Information", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

Label(root, text="Name:", anchor="w").grid(row=1, column=0, sticky="w", padx=10)
Name_Input = Entry(root, width=30)
Name_Input.grid(row=1, column=1, pady=5, padx=10)

Label(root, text="Age:", anchor="w").grid(row=2, column=0, sticky="w", padx=10)
Age_Input = Entry(root, width=30)
Age_Input.grid(row=2, column=1, pady=5, padx=10)

Label(root, text="Height (cm):", anchor="w").grid(row=3, column=0, sticky="w", padx=10)
Height_Input = Entry(root, width=30)
Height_Input.grid(row=3, column=1, pady=5, padx=10)

# Add a Submit button
Submit_Button = Button(root, text="Submit", width=10, command=Submit)
Submit_Button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
