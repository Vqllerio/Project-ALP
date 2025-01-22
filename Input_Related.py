import tkinter as tk
from tkinter import messagebox
import json

def update_dot_labels():
    """Update the dot labels based on the selected options."""
    # Update intensity dot
    if intensity_var.get() == "light":
        intensity_label1.config(text="● Light")
        intensity_label2.config(text="○ Heavy")
    elif intensity_var.get() == "heavy":
        intensity_label1.config(text="○ Light")
        intensity_label2.config(text="● Heavy")
    else:
        intensity_label1.config(text="○ Light")
        intensity_label2.config(text="○ Heavy")

    # Update location dot
    if location_var.get() == "indoor":
        location_label1.config(text="● Indoor")
        location_label2.config(text="○ Outdoor")
    elif location_var.get() == "outdoor":
        location_label1.config(text="○ Indoor")
        location_label2.config(text="● Outdoor")
    else:
        location_label1.config(text="○ Indoor")
        location_label2.config(text="○ Outdoor")

    # Update goal dot
    if goal_var.get() == "healthy":
        goal_label1.config(text="● Healthy")
        goal_label2.config(text="○ Fit")
        goal_label3.config(text="○ Bodybuild")
    elif goal_var.get() == "fit":
        goal_label1.config(text="○ Healthy")
        goal_label2.config(text="● Fit")
        goal_label3.config(text="○ Bodybuild")
    elif goal_var.get() == "bodybuild":
        goal_label1.config(text="○ Healthy")
        goal_label2.config(text="○ Fit")
        goal_label3.config(text="● Bodybuild")
    else:
        goal_label1.config(text="○ Healthy")
        goal_label2.config(text="○ Fit")
        goal_label3.config(text="○ Bodybuild")

def validate_numeric_input(value):
    """Ensure that only numeric input is allowed."""
    return value.isdigit() or value == ""

def submit_preferences():
    """Submit user preferences and save them to a JSON file."""
    # Get the user inputs
    intensity = intensity_var.get()
    location = location_var.get()
    goal = goal_var.get()
    hours = time_hours_var.get()
    minutes = time_minutes_var.get()
    seconds = time_seconds_var.get()

    # Validate inputs
    if not intensity or not location or not goal or not hours.isdigit() or not minutes.isdigit() or not seconds.isdigit():
        messagebox.showerror("Input Error", "Please fill out all fields with valid numbers.")
        return

    # Provide recommendations based on inputs
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

    # Get the specific recommendation
    recommendation = recommendations.get((intensity, location, goal), "No specific recommendation available.")

    # Save the preferences and recommendation to a JSON file
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

    # Display summary and recommendation
    summary = (
        f"Here are your preferences:\n\n"
        f"1. Exercise Intensity: {intensity.capitalize()}\n"
        f"2. Location Preference: {location.capitalize()}\n"
        f"3. Fitness Goal: {goal.capitalize()}\n"
        f"4. Exercise Time: {hours} hours, {minutes} minutes, {seconds} seconds\n\n"
        f"Recommended Exercise: {recommendation}"
    )
    messagebox.showinfo("Your Preferences and Recommendation", summary)

    # Stop the program after showing the message
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Sedentary Exercise Planner")
root.geometry("400x650")

# Use a frame to group input fields
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Exercise Intensity Section
tk.Label(frame, text="What type of exercise do you want to do?", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", pady=5)
intensity_var = tk.StringVar(value="")
intensity_label1 = tk.Label(frame, text="○ Light", anchor="w", font=("Arial", 10))
intensity_label1.grid(row=1, column=0, sticky="w")
intensity_label1.bind("<Button-1>", lambda e: (intensity_var.set("light"), update_dot_labels()))
intensity_label2 = tk.Label(frame, text="○ Heavy", anchor="w", font=("Arial", 10))
intensity_label2.grid(row=2, column=0, sticky="w")
intensity_label2.bind("<Button-1>", lambda e: (intensity_var.set("heavy"), update_dot_labels()))

# Exercise Location Section
tk.Label(frame, text="Do you prefer to exercise indoors or outdoors?", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", pady=10)
location_var = tk.StringVar(value="")
location_label1 = tk.Label(frame, text="○ Indoor", anchor="w", font=("Arial", 10))
location_label1.grid(row=4, column=0, sticky="w")
location_label1.bind("<Button-1>", lambda e: (location_var.set("indoor"), update_dot_labels()))
location_label2 = tk.Label(frame, text="○ Outdoor", anchor="w", font=("Arial", 10))
location_label2.grid(row=5, column=0, sticky="w")
location_label2.bind("<Button-1>", lambda e: (location_var.set("outdoor"), update_dot_labels()))

# Fitness Goal Section
tk.Label(frame, text="What is your fitness goal?", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", pady=10)
goal_var = tk.StringVar(value="")
goal_label1 = tk.Label(frame, text="○ Healthy", anchor="w", font=("Arial", 10))
goal_label1.grid(row=7, column=0, sticky="w")
goal_label1.bind("<Button-1>", lambda e: (goal_var.set("healthy"), update_dot_labels()))
goal_label2 = tk.Label(frame, text="○ Fit", anchor="w", font=("Arial", 10))
goal_label2.grid(row=8, column=0, sticky="w")
goal_label2.bind("<Button-1>", lambda e: (goal_var.set("fit"), update_dot_labels()))
goal_label3 = tk.Label(frame, text="○ Bodybuild", anchor="w", font=("Arial", 10))
goal_label3.grid(row=9, column=0, sticky="w")
goal_label3.bind("<Button-1>", lambda e: (goal_var.set("bodybuild"), update_dot_labels()))

# Time Input Section inside a frame
time_frame = tk.Frame(frame)  # Create a frame to group time-related entries and labels
time_frame.grid(row=10, column=0, sticky="w", pady=10)

# Time input variables
time_hours_var = tk.StringVar(value="0")
time_minutes_var = tk.StringVar(value="0")
time_seconds_var = tk.StringVar(value="0")

# Validator for numeric input
validate_cmd = root.register(validate_numeric_input)

# Row 1: Hours input and label "h"
time_hours_entry = tk.Entry(time_frame, textvariable=time_hours_var, width=5, validate="key", validatecommand=(validate_cmd, "%P"))
time_hours_entry.grid(row=0, column=0, sticky="w", padx=5)
tk.Label(time_frame, text="H", font=("Arial", 10)).grid(row=0, column=1, sticky="w", padx=5)

# Row 2: Minutes input and label "m"
time_minutes_entry = tk.Entry(time_frame, textvariable=time_minutes_var, width=5, validate="key", validatecommand=(validate_cmd, "%P"))
time_minutes_entry.grid(row=1, column=0, sticky="w", padx=5)
tk.Label(time_frame, text="M", font=("Arial", 10)).grid(row=1, column=1, sticky="w", padx=5)

# Row 3: Seconds input and label "s"
time_seconds_entry = tk.Entry(time_frame, textvariable=time_seconds_var, width=5, validate="key", validatecommand=(validate_cmd, "%P"))
time_seconds_entry.grid(row=2, column=0, sticky="w", padx=5)
tk.Label(time_frame, text="S", font=("Arial", 10)).grid(row=2, column=1, sticky="w", padx=5)

def validate_time_input(value, max_value):
    """Ensure input is a number and within the allowed range, or allow empty input."""
    if value == "":  # Allow empty input for editing
        return True
    return value.isdigit() and 0 <= int(value) <= max_value

def handle_time_input(*args):
    """Update state of time fields based on the hours input."""
    hours = time_hours_var.get()
    if hours.isdigit() and int(hours) == 24:
        # When hours = 24, reset minutes and seconds to 0 and disable them
        time_minutes_var.set("0")
        time_seconds_var.set("0")
        time_minutes_entry.config(state="disabled")
        time_seconds_entry.config(state="disabled")
    else:
        # Enable minutes and seconds when hours is less than 24
        time_minutes_entry.config(state="normal")
        time_seconds_entry.config(state="normal")

# Validator for time inputs
validate_hours_cmd = root.register(lambda value: validate_time_input(value, 24))
validate_minutes_seconds_cmd = root.register(lambda value: validate_time_input(value, 59))

# Add trace for hours to handle state changes
time_hours_var.trace_add("write", handle_time_input)

# Time input entries with updated validators
time_hours_entry.config(validate="key", validatecommand=(validate_hours_cmd, "%P"))
time_minutes_entry.config(validate="key", validatecommand=(validate_minutes_seconds_cmd, "%P"))
time_seconds_entry.config(validate="key", validatecommand=(validate_minutes_seconds_cmd, "%P"))

# Submit Button
tk.Button(root, text="Submit", command=submit_preferences, font=("Arial", 12, "bold")).pack(pady=20)

# Update dots initially
update_dot_labels()

# Start the application
root.mainloop()
