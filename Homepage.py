import tkinter as tk
from tkinter import messagebox
import json

# File paths for the schedule and priority JSON files
SCHEDULE_FILE = "schedule.json"
PRIORITY_FILE = "priority_schedule.json"

# Import your existing functions
from Program_Olahraga import view_recommended_schedule
from View_Schedule import view_schedule
from Edit_Schedule import input_schedule
from Schedule_Priority import input_priority_schedule, view_priority_schedule
from Information import create_exercise_info_app

def load_schedule():
    """Load the schedule from a JSON file."""
    try:
        with open(SCHEDULE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def load_priority_schedule():
    """Load the priority schedule from a JSON file."""
    try:
        with open(PRIORITY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def get_upcoming_tasks():
    """Generate a string for upcoming tasks based on the schedule and priority."""
    schedule = load_schedule()
    priority_schedule = load_priority_schedule()

    tasks = []
    for day, activities in schedule.items():
        if isinstance(activities, dict):
            for task, time in activities.items():
                priority = priority_schedule.get(day, {}).get(task, "No Priority")
                tasks.append(f"{task.replace('_', ' ').capitalize()} - {time} - {priority}")

    if not tasks:
        return "No upcoming tasks available."
    return "\n".join(tasks[:5])  # Display the first 5 tasks

def create_homepage():
    """Create the homepage with navigation buttons."""
    root = tk.Tk()
    root.title("Schedule Manager")
    root.geometry("400x600")  # Set the size of the window

    # Define colors and styles
    bg_color = "#D5F4FF"
    button_color = "#A9E5FF"
    highlight_color = "#6BCFF6"

    root.configure(bg=bg_color)

    # Title
    title_label = tk.Label(
        root, text="Schedule", font=("Arial", 18, "bold"), bg=bg_color, pady=10
    )
    title_label.pack()

    # Frame for Upcoming Tasks
    task_frame = tk.Frame(root, bg=highlight_color, bd=5, relief="ridge")
    task_frame.pack(pady=10, padx=10, fill="x")

    task_label = tk.Label(
        task_frame,
        text="Upcoming Tasks\n" + get_upcoming_tasks(),
        font=("Arial", 12),
        bg=highlight_color,
        justify="left",
    )
    task_label.pack(pady=5, padx=5)

    # Frame for Navigation Buttons
    button_frame = tk.Frame(root, bg=bg_color)
    button_frame.pack(pady=20)

    def open_view_recommended_schedule():
        view_recommended_schedule()

    def open_edit_schedule():
        input_schedule()
        view_schedule()

    def open_set_priority():
        input_priority_schedule()
        view_priority_schedule()

    def open_Information():
        create_exercise_info_app()
        

    # Buttons
    buttons = [
        ("Schedule", open_view_recommended_schedule),
        ("Edit Schedule", open_edit_schedule),
        ("Set Priority", open_set_priority),
        ("Information", open_Information),
    ]

    for text, command in buttons:
        button = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 14),
            bg=button_color,
            relief="raised",
            command=command,
            width=15,
            height=2,
        )
        button.pack(pady=10)

    # Footer Navigation (Optional for aesthetic purposes)
    footer_frame = tk.Frame(root, bg=bg_color)
    footer_frame.pack(side="bottom", fill="x", pady=10)

    for icon_text in ["Home", "Notification", "Settings"]:
        footer_button = tk.Button(
            footer_frame,
            text=icon_text,
            font=("Arial", 10),
            bg=highlight_color,
            width=12,
        )
        footer_button.pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    create_homepage()
