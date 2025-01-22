import json

SCHEDULE_FILE = "schedule.json"

def load_schedule():
    """Load the schedule from a JSON file."""
    try:
        with open(SCHEDULE_FILE, "r") as file:
            data = file.read().strip()
            return json.loads(data) if data else {}  # Handle empty file
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return an empty dictionary if file not found or invalid
    except FileNotFoundError:
        return {}

def save_schedule(schedule):
    """Save the schedule to a JSON file."""
    with open(SCHEDULE_FILE, "w") as file:
        json.dump(schedule, file, indent=4)
