import json
import tkinter as tk
from View_Schedule import view_schedule
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
    """Display the current priority schedule with color coding."""
    priority_schedule = load_priority_schedule()

    if not priority_schedule:
        messagebox.showinfo("No Priorities", "No priorities found. Please set task priorities first.")
        return

    # Create a new Tkinter window to display priorities
    priority_window = tk.Toplevel()
    priority_window.title("Task Priorities")
    priority_window.geometry("500x400")  # Default size of the window

    # Allow minimize, maximize, and close functionality
    priority_window.resizable(True, True)

    # Create a frame to hold the canvas and scrollbar
    frame = tk.Frame(priority_window)
    frame.pack(fill="both", expand=True)

    # Create the canvas and a vertical scrollbar for it
    canvas = tk.Canvas(frame, highlightthickness=0)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    # Bind the scrollable frame to the canvas
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Place the scrollable frame inside the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Configure canvas scrolling
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack canvas and scrollbar into the frame
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Populate the scrollable frame with task priorities
    for day, tasks in priority_schedule.items():
        tk.Label(scrollable_frame, text=day, font=("Arial", 12, "bold"), pady=5).pack(anchor="w")
        for task, priority in tasks.items():
            color_map = {"High": "red", "Medium": "orange", "Low": "green"}
            tk.Label(
                scrollable_frame,
                text=f"Task: {task}, Priority: {priority}",
                font=("Arial", 10),
                fg=color_map.get(priority, "black")
            ).pack(anchor="w", padx=20)

    # Bind mousewheel scrolling
    def on_mousewheel(event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)  # For Windows and macOS
    canvas.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))  # For Linux scroll up
    canvas.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))  # For Linux scroll down



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
            "Choose an option:\n1. View Weekly Schedule\n2. View Task Priorities\n3. Set Task Priorities\n4. Exit"
        )

        if choice == "1":
            view_schedule()
        elif choice == "2":
            view_priority_schedule()
        elif choice == "3":
            input_priority_schedule()
        elif choice == "4":
            messagebox.showinfo("Goodbye", "Goodbye!")
            break
        else:
            messagebox.showwarning("Invalid Choice", "Please select a valid option.")

if __name__ == "__main__":
    main()
    