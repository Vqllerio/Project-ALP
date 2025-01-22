import tkinter as tk
import json

class GeneralInformationForm:
    def __init__(self, root, next_step_callback):
        self.root = root
        self.next_step_callback = next_step_callback
        self.root.title("General Information Form")
        self.root.geometry("300x225")
        self.root.resizable(False, False)

        self.age_list = []
        self.height_list = []
        self.weight_list = []

        # UI Components
        self.create_widgets()


    def create_widgets(self):
        # Title
        tk.Label(self.root, text="General Information", font=("Arial", 14, "bold"))\
            .grid(row=0, column=0, columnspan=2, pady=10)

        # Age Input
        tk.Label(self.root, text="Age:", anchor="w")\
            .grid(row=1, column=0, sticky="w", padx=10)
        self.age_input = tk.Entry(self.root, width=30)
        self.age_input.grid(row=1, column=1, pady=5, padx=10)

        # Height Input
        tk.Label(self.root, text="Height (cm):", anchor="w")\
            .grid(row=2, column=0, sticky="w", padx=10)
        self.height_input = tk.Entry(self.root, width=30)
        self.height_input.grid(row=2, column=1, pady=5, padx=10)

        # Weight Input
        tk.Label(self.root, text="Weight (kg):", anchor="w")\
            .grid(row=3, column=0, sticky="w", padx=10)
        self.weight_input = tk.Entry(self.root, width=30)
        self.weight_input.grid(row=3, column=1, pady=5, padx=10)

        # Submit Button
        submit_button = tk.Button(self.root, text="Submit", width=10, command=self.submit)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10)

def submit(self):
    try:
        # Collect the input data
        info = {
            "Age": int(self.age_input.get()),
            "Height": int(self.height_input.get()),
            "Weight": int(self.weight_input.get())
        }

        self.age_list.append(info["Age"])
        self.height_list.append(info["Height"])
        self.weight_list.append(info["Weight"])

        # Write the data to a JSON file
        try:
            with open("general_information.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(info)

        with open("general_information.json", "w") as file:
            json.dump(data, file, indent=4)

        # Clear the input fields
        self.age_input.delete(0, tk.END)
        self.height_input.delete(0, tk.END)
        self.weight_input.delete(0, tk.END)

        print("Data saved:", self.age_list, self.height_list, self.weight_list)

        # Notify the parent application to proceed to the next step
        self.root.destroy()
        if self.next_step_callback:
            self.next_step_callback()

    except ValueError:
        tk.messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneralInformationForm(root)
    root.mainloop()
