# main.py — Tkinter Weather App using OpenWeatherMap API
import tkinter as tk
from tkinter import messagebox
from weather_api import fetch_weather  # External module to call weather API
import os

# --------------------- Helper Functions ---------------------

def save_to_history(city, temperature):
    """Append city and temperature to history.txt"""
    with open("history.txt", "a") as file:
        file.write(f"{city} - {temperature}°C\n")

def open_history():
    """Display previous search history in a new window"""
    history_window = tk.Toplevel(app)
    history_window.title("Search History")
    history_window.geometry("300x300")

    tk.Label(history_window, text="Previous Searches:", font=("Arial", 12)).pack(pady=10)

    if os.path.exists("history.txt"):
        with open("history.txt", "r") as file:
            for line in file:
                tk.Label(history_window, text=line.strip(), font=("Arial", 10)).pack()
    else:
        tk.Label(history_window, text="No history yet.", font=("Arial", 10)).pack()

def open_about():
    """Display app info in a popup window"""
    about_window = tk.Toplevel(app)
    about_window.title("About")
    about_window.geometry("300x200")

    tk.Label(about_window, text="Weather App", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(about_window, text="Built with Tkinter + OpenWeatherMap API").pack()
    tk.Label(about_window, text="\nMade by Your Group Name\nVersion 1.0").pack()

def get_weather():
    """Fetch weather info and update the UI"""
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name")
        return

    weather, error = fetch_weather(city)
    if error:
        result_label.config(text=f" Error: {error}")
    else:
        result_text = (
            f"City: {weather['city']}\n"
            f" Condition: {weather['description']}\n"
            f" Temperature: {weather['temperature']} °C\n"
            f" Humidity: {weather['humidity']} %\n"
            f" Wind Speed: {weather['wind']} m/s"
        )
        result_label.config(text=result_text)
        save_to_history(weather['city'], weather['temperature'])

# --------------------- UI Setup ---------------------

app = tk.Tk()
app.title("Weather App")
app.geometry("350x350")
app.resizable(False, False)

# Navigation buttons
tk.Button(app, text="View History", font=("Arial", 10), command=open_history).pack(pady=5)
tk.Button(app, text="About", font=("Arial", 10), command=open_about).pack(pady=5)

# Input field
tk.Label(app, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(app, font=("Arial", 12))
city_entry.pack(pady=5)

# Get weather button
tk.Button(app, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

# Weather result display
result_label = tk.Label(app, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

# Run the application
app.mainloop()
