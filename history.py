# history.py
import tkinter as tk
import json
import os

def show_history_window():
    top = tk.Toplevel()
    top.title("Search History")
    top.geometry("300x300")
    top.config(bg="white")

    heading = tk.Label(top, text="Previously Searched Cities:", font=("Arial", 12, "bold"), bg="white")
    heading.pack(pady=10)

    history_frame = tk.Frame(top, bg="white")
    history_frame.pack(fill="both", expand=True)

    if os.path.exists("history.json"):
        try:
            with open("history.json", "r") as f:
                data = json.load(f)

            if data:
                for city in data:
                    tk.Label(history_frame, text=city, font=("Arial", 10), bg="white").pack(anchor="w", padx=10)
            else:
                tk.Label(history_frame, text="No cities found in history.", font=("Arial", 10), bg="white").pack()
        except json.JSONDecodeError:
            tk.Label(history_frame, text="Error reading history data.", font=("Arial", 10), bg="white", fg="red").pack()
    else:
        tk.Label(history_frame, text="No search history file found.", font=("Arial", 10), bg="white").pack()

