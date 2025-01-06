from tkinter import *

# Initialize the root window
root = Tk()
root.title("General Information Form")
Name = []
Age = []
Height = []
Weight = []

# Set a minimum window size
root.geometry("300x225")
root.resizable(False, False)

def Submit():
    Info = [str(Name_Input.get()), int(Age_Input.get()), int(Height_Input.get()), int(Weight_Input.get())]
    Name.append(Info[0])
    Age.append(Info[1])
    Height.append(Info[2])
    Weight.append(Info[3])
    print(Name, Age, Height, Weight)
    Name_Input.delete(0, END)
    Age_Input.delete(0, END)
    Height_Input.delete(0, END)
    Weight_Input.delete(0, END)

print(Name, Age, Height)

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

Label(root, text="Weight (kg):", anchor="w").grid(row=4, column=0, sticky="w", padx=10)
Weight_Input = Entry(root, width=30)
Weight_Input.grid(row=4, column=1, pady=5, padx=10)

# Add a Submit button
Submit_Button = Button(root, text="Submit", width=10, command=Submit)
Submit_Button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
