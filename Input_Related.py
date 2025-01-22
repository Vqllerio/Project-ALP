import tkinter as tk
from tkinter import messagebox
import json

class SedentaryExercisePlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Sedentary Exercise Planner")
        self.root.geometry("400x650")

        self.intensity_var = tk.StringVar(value="")
        self.location_var = tk.StringVar(value="")
        self.goal_var = tk.StringVar(value="")
        self.time_hours_var = tk.StringVar(value="0")
        self.time_minutes_var = tk.StringVar(value="0")
        self.time_seconds_var = tk.StringVar(value="0")

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        # Exercise Intensity Section
        tk.Label(frame, text="What type of exercise do you want to do?", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.intensity_label1 = tk.Label(frame, text="○ Light", anchor="w", font=("Arial", 10))
        self.intensity_label1.grid(row=1, column=0, sticky="w")
        self.intensity_label1.bind("<Button-1>", lambda e: (self.intensity_var.set("light"), self.update_dot_labels()))
        self.intensity_label2 = tk.Label(frame, text="○ Heavy", anchor="w", font=("Arial", 10))
        self.intensity_label2.grid(row=2, column=0, sticky="w")
        self.intensity_label2.bind("<Button-1>", lambda e: (self.intensity_var.set("heavy"), self.update_dot_labels()))

        # Exercise Location Section
        tk.Label(frame, text="Do you prefer to exercise indoors or outdoors?", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", pady=10)
        self.location_label1 = tk.Label(frame, text="○ Indoor", anchor="w", font=("Arial", 10))
        self.location_label1.grid(row=4, column=0, sticky="w")
        self.location_label1.bind("<Button-1>", lambda e: (self.location_var.set("indoor"), self.update_dot_labels()))
        self.location_label2 = tk.Label(frame, text="○ Outdoor", anchor="w", font=("Arial", 10))
        self.location_label2.grid(row=5, column=0, sticky="w")
        self.location_label2.bind("<Button-1>", lambda e: (self.location_var.set("outdoor"), self.update_dot_labels()))

        # Fitness Goal Section
        tk.Label(frame, text="What is your fitness goal?", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", pady=10)
        self.goal_label1 = tk.Label(frame, text="○ Healthy", anchor="w", font=("Arial", 10))
        self.goal_label1.grid(row=7, column=0, sticky="w")
        self.goal_label1.bind("<Button-1>", lambda e: (self.goal_var.set("healthy"), self.update_dot_labels()))
        self.goal_label2 = tk.Label(frame, text="○ Fit", anchor="w", font=("Arial", 10))
        self.goal_label2.grid(row=8, column=0, sticky="w")
        self.goal_label2.bind("<Button-1>", lambda e: (self.goal_var.set("fit"), self.update_dot_labels()))
        self.goal_label3 = tk.Label(frame, text="○ Bodybuild", anchor="w", font=("Arial", 10))
        self.goal_label3.grid(row=9, column=0, sticky="w")
        self.goal_label3.bind("<Button-1>", lambda e: (self.goal_var.set("bodybuild"), self.update_dot_labels()))

        # Time Input Section
        time_frame = tk.Frame(frame)
        time_frame.grid(row=10, column=0, sticky="w", pady=10)

        validate_cmd = self.root.register(self.validate_numeric_input)

        self.time_hours_entry = tk.Entry(time_frame, textvariable=self.time_hours_var, width=5, validate="key", validatecommand=(validate_cmd, "%P"))
        self.time_hours_entry.grid(row=0, column=0, sticky="w", padx=5)
        tk.Label(time_frame, text="H", font=("Arial", 10)).grid(row=0, column=1, sticky="w", padx=5)

        self.time_minutes_entry = tk.Entry(time_frame, textvariable=self.time_minutes_var, width=5, validate="key", validatecommand=(validate_cmd, "%P"))
        self.time_minutes_entry.grid(row=1, column=0, sticky="w", padx=5)
        tk.Label(time_frame, text="M", font=("Arial", 10)).grid(row=1, column=1, sticky="w", padx=5)

        self.time_seconds_entry = tk.Entry(time_frame, textvariable=self.time_seconds_var, width=5, validate="key", validatecommand=(validate_cmd, "%P"))
        self.time_seconds_entry.grid(row=2, column=0, sticky="w", padx=5)
        tk.Label(time_frame, text="S", font=("Arial", 10)).grid(row=2, column=1, sticky="w", padx=5)

        tk.Button(self.root, text="Submit", command=self.submit_preferences, font=("Arial", 12, "bold")).pack(pady=20)

        self.update_dot_labels()

    def update_dot_labels(self):
        # Intensity
        self.intensity_label1.config(text="● Light" if self.intensity_var.get() == "light" else "○ Light")
        self.intensity_label2.config(text="● Heavy" if self.intensity_var.get() == "heavy" else "○ Heavy")
        
        # Location
        self.location_label1.config(text="● Indoor" if self.location_var.get() == "indoor" else "○ Indoor")
        self.location_label2.config(text="● Outdoor" if self.location_var.get() == "outdoor" else "○ Outdoor")
        
        # Goal
        self.goal_label1.config(text="● Healthy" if self.goal_var.get() == "healthy" else "○ Healthy")
        self.goal_label2.config(text="● Fit" if self.goal_var.get() == "fit" else "○ Fit")
        self.goal_label3.config(text="● Bodybuild" if self.goal_var.get() == "bodybuild" else "○ Bodybuild")

    def validate_numeric_input(self, value):
        return value.isdigit() or value == ""

    def submit_preferences(self):
        intensity = self.intensity_var.get()
        location = self.location_var.get()
        goal = self.goal_var.get()
        hours = self.time_hours_var.get()
        minutes = self.time_minutes_var.get()
        seconds = self.time_seconds_var.get()

        if not (intensity and location and goal and hours.isdigit() and minutes.isdigit() and seconds.isdigit()):
            messagebox.showerror("Input Error", "Please fill out all fields with valid inputs.")
            return

        recommendations = {
            ("light", "indoor", "healthy"): "Try yoga, stretching, or light aerobics at home.",
            ("light", "indoor", "fit"): "Consider Pilates or low-intensity resistance training.",
            ("light", "indoor", "bodybuild"): "Focus on beginner weightlifting with light dumbbells.",
            ("light", "outdoor", "healthy"): "Go for a walk in the park or practice Tai Chi.",
            ("light", "outdoor", "fit"): "Try light jogging or cycling in a scenic area.",
            ("light", "outdoor", "bodybuild"): "Engage in bodyweight exercises like push-ups and squats.",
            ("heavy", "indoor", "healthy"): "Do HIIT workouts or indoor cycling.",
            ("heavy", "indoor", "fit"): "Perform weightlifting or resistance band training.",
            ("heavy", "indoor", "bodybuild"): "Engage in a structured bodybuilding program with gym equipment.",
            ("heavy", "outdoor", "healthy"): "Try outdoor boot camp or intense hiking.",
            ("heavy", "outdoor", "fit"): "Do sprint intervals or long-distance running.",
            ("heavy", "outdoor", "bodybuild"): "Practice outdoor calisthenics or use park gym equipment.",
        }

        recommendation = recommendations.get((intensity, location, goal), "No specific recommendation available.")

        data = {
            "intensity": intensity,
            "location": location,
            "goal": goal,
            "time": {
                "hours": hours,
                "minutes": minutes,
                "seconds": seconds
            },
            "recommendation": recommendation
        }

        with open("exercise_preferences.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        summary = (
            f"Here are your preferences:\n\n"
            f"1. Exercise Intensity: {intensity.capitalize()}\n"
            f"2. Location Preference: {location.capitalize()}\n"
            f"3. Fitness Goal: {goal.capitalize()}\n"
            f"4. Exercise Time: {hours} hours, {minutes} minutes, {seconds} seconds\n\n"
            f"Recommended Exercise: {recommendation}"
        )
        messagebox.showinfo("Your Preferences and Recommendation", summary)

        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SedentaryExercisePlanner(root)
    root.mainloop()
