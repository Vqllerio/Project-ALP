import tkinter as tk
from tkinter import messagebox
from Schedule_utils import load_schedule

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
    """Main function to view the schedule."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    view_schedule()

if __name__ == "__main__":
    main()
