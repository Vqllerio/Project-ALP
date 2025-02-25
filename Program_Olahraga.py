import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import datetime

SCHEDULE_FILE = "schedule.json"
RECOMMENDED_SCHEDULE_FILE = "recommended_schedule.json"
PRIORITY_FILE = "priority_schedule.json"

def load_schedule():
    """Load the manual schedule from the JSON file."""
    try:
        with open(SCHEDULE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def load_recommended_schedule():
    """Load the recommended schedule from the JSON file."""
    try:
        with open(RECOMMENDED_SCHEDULE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return an empty dictionary if the file is missing or invalid
        return {}


def load_priority_schedule():
    """Load the priority schedule from the JSON file."""
    try:
        with open(PRIORITY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_recommended_schedule(schedule):
    """Save the updated recommended schedule to the JSON file."""
    with open(RECOMMENDED_SCHEDULE_FILE, "w") as file:
        json.dump(schedule, file, indent=4)

def save_priority_schedule(priority_schedule):
    """Save the updated priority schedule to the JSON file."""
    with open(PRIORITY_FILE, "w") as file:
        json.dump(priority_schedule, file, indent=4)

def parse_time(input_time):
    """Convert a time string (HH:MM) to a datetime object."""
    return datetime.datetime.strptime(input_time, "%H:%M")

def format_time(time_obj):
    """Format a datetime object to a time string (HH:MM)."""
    return time_obj.strftime("%H:%M")

def generate_recommended_schedule(wake_up, work_start, work_end):
    """Generate a recommended schedule based on wake-up, work start, and work end times."""
    wake_up_time = parse_time(wake_up)
    work_start_time = parse_time(work_start)
    work_end_time = parse_time(work_end)

    if not (wake_up_time < work_start_time < work_end_time):
        raise ValueError("Ensure wake-up time < work start time < work end time.")

    schedule = {}
    schedule["wake_up_time"] = format_time(wake_up_time)
    schedule["morning_routine"] = format_time(wake_up_time + datetime.timedelta(minutes=30))

    stretch_start = wake_up_time + datetime.timedelta(minutes=30)
    schedule["stretch_start_time"] = format_time(stretch_start)
    schedule["stretch_end_time"] = format_time(stretch_start + datetime.timedelta(minutes=10))

    current_time = work_start_time
    work_blocks = []
    break_blocks = []

    while current_time < work_end_time:
        work_end_block = min(current_time + datetime.timedelta(minutes=90), work_end_time)
        work_blocks.append((current_time, work_end_block))
        current_time = work_end_block

        if current_time < work_end_time:
            break_end = current_time + datetime.timedelta(minutes=10)
            break_blocks.append((current_time, break_end))
            current_time = break_end

    schedule["work_blocks"] = [(format_time(start), format_time(end)) for start, end in work_blocks]
    schedule["break_blocks"] = [(format_time(start), format_time(end)) for start, end in break_blocks]

    return schedule

def input_recommended_schedule():
    """Generate and save a recommended schedule with priorities."""
    schedule = load_schedule()
    priority_schedule = load_priority_schedule()
    recommended_schedule = load_recommended_schedule()

    if not schedule:
        messagebox.showerror("Error", "No manual schedule found. Please create one first.")
        return

    for day, day_schedule in schedule.items():
        wake_up = day_schedule.get("wake_up_time")
        work_start = day_schedule.get("work_start_time")
        work_end = day_schedule.get("work_end_time")

        if not all([wake_up, work_start, work_end]):
            messagebox.showwarning("Incomplete Data", f"Missing data for {day}. Skipping.")
            continue

        # Generate the base recommended schedule
        try:
            generated_schedule = generate_recommended_schedule(wake_up, work_start, work_end)
        except ValueError as e:
            messagebox.showerror("Invalid Time Configuration", str(e))
            continue

        if day not in recommended_schedule:
            recommended_schedule[day] = {}

        for task, time in generated_schedule.items():
            # Handle high/low priority logic
            if day in priority_schedule and task in priority_schedule[day]:
                task_data = priority_schedule[day][task]
                if isinstance(task_data, dict):  # Check if task_data is a dictionary
                    priority = task_data.get("priority", "Low").strip().lower()
                else:
                    priority = task_data.strip().lower()  # If it's not a dictionary, treat it as a string
            else:
                priority = "low"

            # If high priority, keep the original time from the schedule JSON
            if priority == "high":
                recommended_schedule[day][task] = {
                    "time": day_schedule.get(task, time),
                    "priority": "High"
                }
            else:  # Low priority: use generated time
                recommended_schedule[day][task] = {
                    "time": time,
                    "priority": "Low"
                }

    save_recommended_schedule(recommended_schedule)
    messagebox.showinfo("Saved", "Recommended schedule saved successfully!")

def view_recommended_schedule():
    """View the recommended schedule with priorities."""
    recommended_schedule = load_recommended_schedule()

    if not recommended_schedule:
        messagebox.showinfo("No Schedule", "No recommended schedule found. Please generate one first.")
        return

    view_window = tk.Toplevel()
    view_window.title("Recommended Schedule with Priorities")
    view_window.geometry("600x400")

    frame = tk.Frame(view_window)
    frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for day, tasks in recommended_schedule.items():
        tk.Label(scrollable_frame, text=day, font=("Arial", 14, "bold"), pady=5).pack(anchor="w")

        for task, details in tasks.items():
            if isinstance(details, dict):  # Ensure it's a dictionary with time and priority
                time = details.get("time", "N/A")
                priority = details.get("priority", "Low").strip().lower()
            else:
                time = details
                priority = "low"

            # Determine the color based on priority
            color = "red" if priority == "high" else "green"

            # Display the task
            tk.Label(
                scrollable_frame,
                text=f"{task.replace('_', ' ').capitalize()}: {time} (Priority: {priority.capitalize()})",
                font=("Arial", 12),
                fg=color
            ).pack(anchor="w", padx=20)


def format_task_time(task, value):
    """Format task time if applicable and return display values."""
    try:
        # Check if the task is one of the time-related keys
        if task in ["wake_up_time", "work_start_time", "work_end_time"]:
            # Attempt to parse the value as time
            time_obj = datetime.datetime.strptime(value, "%H:%M")
            formatted_time = time_obj.strftime("%I:%M %p")  # Convert to 12-hour format with AM/PM
            return formatted_time, "High"  # Default priority to High for these tasks
    except (ValueError, TypeError):
        pass  # If parsing fails, continue with the default behavior

    # Return the original value and default priority for non-time-related tasks
    return value, "Low" if isinstance(value, str) else None


    for day, tasks in priority_schedule.items():
        tk.Label(scrollable_frame, text=day, font=("Arial", 14, "bold"), pady=5).pack(anchor="w")

        for task, details in tasks.items():
            # Handle time formatting for specific keys
            if isinstance(details, str):  # Direct priority string (e.g., "High" or "Low")
                if task in ["wake_up_time", "work_start_time", "work_end_time"]:
                    formatted_time, priority = format_task_time(task, details)
                    time = formatted_time
                else:
                    priority = details.strip().lower()
                    time = "N/A"
            elif isinstance(details, dict):  # Nested dictionary with priority and time
                time = details.get("time", "N/A")
                priority = details.get("priority", "Low").strip().lower()
            else:
                priority = "low"  # Default to "Low" for unexpected cases
                time = "N/A"

        # Determine the color based on priority
            color = "red" if priority == "high" else "green"

        # Display the task
            tk.Label(
                scrollable_frame,
                text=f"{task.replace('_', ' ').capitalize()}: {time} (Priority: {priority.capitalize()})",
                font=("Arial", 12),
                fg=color
            ).pack(anchor="w", padx=20)
def main():
    """Main function to manage the recommended schedule with priorities."""
    root = tk.Tk()
    root.withdraw()

    while True:
        choice = simpledialog.askstring(
            "Main Menu",
            "Choose an option:\n1. Input Recommended Schedule\n2. View Recommended Schedule\n3. Exit"
        )

        if choice == "1":
            input_recommended_schedule()
        elif choice == "2":
            view_recommended_schedule()
        elif choice == "3":
            messagebox.showinfo("Goodbye", "Exiting the application.")
            break
        else:
            messagebox.showwarning("Invalid Choice", "Please select a valid option.")

if __name__ == "__main__":
    main()
