import json
import time
import winsound
from tkinter import Tk, Label

def load_config():
    default_config = {
        "work_duration": 25,
        "short_break_duration": 5,
        "long_break_duration": 15,
        "play_sound": True,
        "flash_screen": True,
        "order": ["work", "short_break", "work", "long_break"]
    }
    try:
        with open("config.json", "r") as file:
            user_config = json.load(file)
            return {**default_config, **user_config}  # merges config w defaults
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error loading config.json. Using default values.")
        return default_config

def flash_screen(current_phase, next_phase):
    # flash red page with message
    root = Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)  # ENSURES WINDOW IS TOPMOST (can remove pygetwindow)
    root.configure(bg="red")
    message = f"POMODORO {current_phase} ended, next is {next_phase}"
    label = Label(root, text=message, font=("Arial", 24), fg="white", bg="red")
    label.pack(expand=True)
    root.after(1000, root.destroy)
    root.mainloop()

def play_sound():
    # Melody: E E E B A B G~ A~ C* B~~
    notes = {      # in Hz
        "E": 330,  # E
        "B": 494,  # B
        "A": 440,  # A
        "G~": 392, # G (long)
        "A~": 440, # A (long)
        "C*": 523, # C (high)
        "B~~": 494 # B (longer)
    }
    durations = {   # in ms
        "E": 300,   # E
        "B": 300,   # B
        "A": 300,   # A
        "G~": 600,  # G (long)
        "A~": 600,  # A (long)
        "C*": 300,  # C (high)
        "B~~": 900  # B (longer)
    }
    melody = ["E", "E", "E", "B", "A", "B", "G~", "A~", "C*", "B~~"]
    
    for note in melody:
        winsound.Beep(notes[note], durations[note])

def countdown(minutes, message, config, next_phase):
    print(f"{message} for {minutes} minutes.")
    for remaining in range(minutes * 60, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"{mins:02}:{secs:02}", end="\r", flush=True)
        time.sleep(1)
    print("\nTime's up!")
    if config["play_sound"]:
        play_sound()
    if config["flash_screen"]:
        flash_screen(message, next_phase)

def pomodoro_timer():
    config = load_config()
    while True:
        order = config["order"]
        for i, step in enumerate(order):
            next_step = order[(i + 1) % len(order)]  # next phase in the cycle
            if step == "work":
                countdown(config["work_duration"], "Work", config, next_step)
            elif step == "short_break":
                countdown(config["short_break_duration"], "Short Break", config, next_step)
            elif step == "long_break":
                countdown(config["long_break_duration"], "Long Break", config, next_step)

if __name__ == "__main__":
    pomodoro_timer()