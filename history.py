# history.py
import tkinter as tk
import json
import os

def show_history_window():
    top = tk.Toplevel()
    top.title("Search History")
    top.geometry("300x250")
    
    tk.Label(top, text="Previously Searched Cities:", font=("Arial", 12)).pack(pady=10)

    if os.path.exists("history.json"):
        with open("history.json", "r") as f:
            data = json.load(f)
            for city in data:
                tk.Label(top, text=city, font=("Arial", 10)).pack()
    else:
        tk.Label(top, text="No search history found.", font=("Arial", 10)).pack()
