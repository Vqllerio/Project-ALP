import tkinter as tk
from tkinter import messagebox

def get_exercise_tips():
    """Provides a list of exercises for people with a sedentary lifestyle."""
    tips = [
        "1. **Walking**: Start with a 10-15 minute walk daily and gradually increase the duration.",
        "2. **Stretching**: Simple stretches can improve flexibility and reduce stiffness.",
        "3. **Chair Exercises**: Perform seated leg lifts, arm raises, or torso twists.",
        "4. **Yoga**: Gentle yoga poses like Cat-Cow or Child's Pose can enhance mobility.",
        "5. **Bodyweight Exercises**: Try wall push-ups, squats, or standing calf raises.",
        "6. **Light Aerobics**: Engage in low-impact aerobics to boost cardiovascular health.",
        "7. **Desk Exercises**: Stretch your neck, wrists, and shoulders during breaks.",
        "8. **Balance Training**: Simple exercises like standing on one foot can improve stability.",
    ]
    return "\n".join(tips)

def create_exercise_info_app():
    """Create a simple GUI to display exercise tips."""
    root = tk.Tk()
    root.title("Exercise Tips")
    root.geometry("500x400")

    # Define colors and styles
    bg_color = "#F0F8FF"
    text_color = "#000080"

    root.configure(bg=bg_color)

    # Title
    title_label = tk.Label(
        root,
        text="Exercises for a Sedentary Lifestyle",
        font=("Arial", 16, "bold"),
        bg=bg_color,
        fg=text_color,
        pady=10,
    )
    title_label.pack()

    # Frame for Tips
    tips_frame = tk.Frame(root, bg=bg_color)
    tips_frame.pack(pady=10, padx=10, fill="both", expand=True)

    tips_label = tk.Label(
        tips_frame,
        text=get_exercise_tips(),
        font=("Arial", 12),
        bg=bg_color,
        fg=text_color,
        justify="left",
        anchor="w",
    )
    tips_label.pack(pady=5, padx=5, fill="both", expand=True)

    # Close Button
    close_button = tk.Button(
        root,
        text="Close",
        font=("Arial", 12),
        bg="#ADD8E6",
        fg="black",
        command=root.destroy,
    )
    close_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_exercise_info_app()
