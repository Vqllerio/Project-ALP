import json
import tkinter as tk
from Schedule import input_schedule,view_schedule
from tkinter import simpledialog, messagebox

SCHEDULE_FILE = "schedule.json"
PRIORITY_FILE = "priority_schedule.json"

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


def load_priority_schedule():
    """Load the priority schedule from a JSON file."""
    try:
        with open(PRIORITY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_priority_schedule(priority_schedule):
    """Save the priority schedule to a JSON file."""
    with open(PRIORITY_FILE, "w") as file:
        json.dump(priority_schedule, file, indent=4)


def input_priority_for_day(day):
    """Set priority for tasks in a specific day's schedule."""
    schedule = load_schedule()
    priority_schedule = load_priority_schedule()

    if day not in schedule:
        messagebox.showinfo("No Schedule", f"No schedule found for {day}. Please set the schedule first.")
        return

    day_schedule = schedule[day]
    day_priority = priority_schedule.get(day, {})

    for task, _ in day_schedule.items():
        while True:
            priority = simpledialog.askstring(
                "Input", f"Set priority for '{task}' on {day} (1:High, 2:Medium, 3:Low):"
            )
            if priority is None:
                return  # User canceled

            if priority in ["1", "2", "3"]:
                priority_map = {"1": "High", "2": "Medium", "3": "Low"}
                day_priority[task] = priority_map[priority]
                break
            else:
                messagebox.showerror("Invalid Input", "Priority must be 1 (High), 2 (Medium), or 3 (Low).")

    priority_schedule[day] = day_priority
    save_priority_schedule(priority_schedule)
    messagebox.showinfo("Success", f"Priorities for {day} updated successfully!")


def view_priority_schedule():
    """Display the current priority schedule."""
    priority_schedule = load_priority_schedule()

    if not priority_schedule:
        messagebox.showinfo("No Priorities", "No priorities found. Please set task priorities first.")
        return

    display_text = "Your Weekly Task Priorities:\n"
    for day, tasks in priority_schedule.items():
        display_text += f"\n{day}:\n"
        for task, priority in tasks.items():
            display_text += f"  Task: {task}, Priority: {priority}\n"

    messagebox.showinfo("Task Priorities", display_text)


def input_priority_schedule():
    """Set priorities for tasks across the week."""
    schedule = load_schedule()
    if not schedule:
        messagebox.showinfo("No Schedule", "No schedule found. Please set your weekly schedule first.")
        return

    days = list(schedule.keys())

    while True:
        options = days + ["Finish"]
        choice = simpledialog.askstring(
            "Select Day", "Choose a day to set priorities:\n" + "\n".join(f"{i+1}. {day}" for i, day in enumerate(options))
        )

        if choice and choice.isdigit() and 1 <= int(choice) <= len(days):
            day = days[int(choice) - 1]
            input_priority_for_day(day)
        elif choice == str(len(options)):
            messagebox.showinfo("Saved", "Task priorities saved successfully!")
            break
        else:
            messagebox.showwarning("Invalid Choice", "Please select a valid option.")


def main():
    """Main function to manage the schedule and priorities."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    while True:
        choice = simpledialog.askstring(
            "Weekly Schedule Manager",
            "Choose an option:\n1. View Weekly Schedule\n2. Set Weekly Schedule\n3. View Task Priorities\n4. Set Task Priorities\n5. Exit"
        )

        if choice == "1":
            view_schedule()
        elif choice == "2":
            input_schedule()
        elif choice == "3":
            view_priority_schedule()
        elif choice == "4":
            input_priority_schedule()
        elif choice == "5":
            messagebox.showinfo("Goodbye", "Goodbye!")
            break
        else:
            messagebox.showwarning("Invalid Choice", "Please select a valid option.")

if __name__ == "__main__":
    main()
    