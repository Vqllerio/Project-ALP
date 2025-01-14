from tkinter import *
import json
# Initialize the root window
root = Tk()
root.title("General Information Form")
Age = []
Height = []
Weight = []

# Set a minimum window size
root.geometry("300x225")
root.resizable(False, False)

def Submit():
    # Collect the input data
    Info = {
        "Age": int(Age_Input.get()),
        "Height": int(Height_Input.get()),
        "Weight": int(Weight_Input.get())
    }
    Age.append(Info["Age"])
    Height.append(Info["Height"])
    Weight.append(Info["Weight"])
    
    # Write the data to a JSON file
    try:
        with open("general_information.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    data.append(Info)
    
    with open("general_information.json", "w") as file:
        json.dump(data, file, indent=4)
    
    # Clear the input fields
    Age_Input.delete(0, END)
    Height_Input.delete(0, END)
    Weight_Input.delete(0, END)

print(Age, Height)

# Create and place widgets with padding
Label(root, text="General Information", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

Label(root, text="Age:", anchor="w").grid(row=1, column=0, sticky="w", padx=10)
Age_Input = Entry(root, width=30)
Age_Input.grid(row=1, column=1, pady=5, padx=10)

Label(root, text="Height (cm):", anchor="w").grid(row=2, column=0, sticky="w", padx=10)
Height_Input = Entry(root, width=30)
Height_Input.grid(row=2, column=1, pady=5, padx=10)

Label(root, text="Weight (kg):", anchor="w").grid(row=3, column=0, sticky="w", padx=10)
Weight_Input = Entry(root, width=30)
Weight_Input.grid(row=3, column=1, pady=5, padx=10)

# Add a Submit button
Submit_Button = Button(root, text="Submit", width=10, command=Submit)
Submit_Button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
