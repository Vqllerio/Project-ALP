import json

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
