import json
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk

SCHEDULE_FILE = "schedule.json"

def load_schedule():
    """Load the schedule from a JSON file."""
    try:
        with open(SCHEDULE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_schedule(schedule):
    """Save the schedule to a JSON file."""
    with open(SCHEDULE_FILE, "w") as file:
        json.dump(schedule, file, indent=4)

def is_valid_time_input(value):
    """Validate if the input is a valid time format (HH:MM)."""
    try:
        parts = value.split(":")
        if len(parts) == 2 and 0 <= int(parts[0]) < 24 and 0 <= int(parts[1]) < 60:
            return True
    except ValueError:
        pass
    return False

def input_schedule_for_day(day):
    """Collect schedule inputs for a specific day."""
    schedule = {}
    fields = [
        ("Wake up time (e.g., 07:00)", "wake_up_time"),
        ("Stretch start time (e.g., 07:10)", "stretch_start_time"),
        ("Stretch end time (e.g., 07:20)", "stretch_end_time"),
        ("Work start time (e.g., 08:00)", "work_start_time"),
        ("Work end time (e.g., 12:00)", "work_end_time"),
    ]

    for prompt, key in fields:
        while True:
            value = simpledialog.askstring("Input", f"{day}: {prompt}")
            if value is None:  # User canceled
                return None
            if is_valid_time_input(value):
                schedule[key] = value
                break
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid time in HH:MM format.")

    numeric_fields = [
        ("Move notification interval in minutes (e.g., 30)", "move_notification_interval"),
        ("Moving time in minutes (e.g., 2)", "moving_time"),
        ("Break time in minutes (e.g., 5)", "break_time"),
    ]

    for prompt, key in numeric_fields:
        while True:
            value = simpledialog.askstring("Input", f"{day}: {prompt}")
            if value is None:  # User canceled
                return None
            if value.isdigit():
                schedule[key] = value
                break
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid number.")

    return schedule

def input_schedule():
    """Collect schedules for all days of the week."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    schedule = load_schedule()

    while True:
        options = days + ["Finish and Save"]
        choice = simpledialog.askstring("Select Day", "Choose a day to set or update the schedule:\n" + "\n".join(f"{i+1}. {day}" for i, day in enumerate(options)))

        if choice and choice.isdigit() and 1 <= int(choice) <= 7:
            day = days[int(choice) - 1]
            day_schedule = input_schedule_for_day(day)
            if day_schedule is not None:
                schedule[day] = day_schedule
                messagebox.showinfo("Success", f"Schedule for {day} updated successfully.")
            else:
                messagebox.showinfo("Cancelled", f"Skipped schedule for {day}.")
        elif choice == str(len(options)):
            save_schedule(schedule)
            messagebox.showinfo("Saved", "Weekly schedule saved successfully!")
            break
        else:
            messagebox.showwarning("Invalid Choice", "Please select a valid option.")

def view_schedule():
    """Display the current weekly schedule."""
    schedule = load_schedule()
    if not schedule:
        messagebox.showinfo("No Schedule", "No schedule found. Please set your schedule first.")
        return

    display_text = "Your Weekly Schedule:\n"
    for day, day_schedule in schedule.items():
        if isinstance(day_schedule, dict):
            display_text += f"\n{day}:\n"
            for key, value in day_schedule.items():
                display_text += f"  {key.replace('_', ' ').capitalize()}: {value}\n"
        else:
            display_text += f"\n{day}: Invalid schedule format.\n"

    messagebox.showinfo("Weekly Schedule", display_text)

def main():
    """Main function to manage the schedule."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    while True:
        choice = simpledialog.askstring(
            "Weekly Schedule Manager",
            "Choose an option:\n1. View Weekly Schedule\n2. Set Weekly Schedule\n3. Exit"
        )

        if choice == "1":
            view_schedule()
        elif choice == "2":
            input_schedule()
        elif choice == "3":
            messagebox.showinfo("Goodbye", "Goodbye!")
            break
        else:
            messagebox.showwarning("Invalid Choice", "Please select a valid option.")

if __name__ == "__main__":
    main()
