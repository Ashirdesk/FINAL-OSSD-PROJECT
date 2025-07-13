# main.py
import tkinter as tk
from tkinter import messagebox
from weather_api import fetch_weather
import os

# Save history to a text file
def save_to_history(city, temperature):
    with open("history.txt", "a") as file:
        file.write(f"{city} - {temperature}°C\n")

# Show search history window
def open_history():
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

# Show about window
def open_about():
    about_window = tk.Toplevel(app)
    about_window.title("About")
    about_window.geometry("300x200")

    tk.Label(about_window, text="Weather App", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(about_window, text="Built with Tkinter + OpenWeatherMap API").pack()
    tk.Label(about_window, text="\nMade by Your Group Name\nVersion 1.0").pack()

# Get weather and update main window
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name")
        return

    weather, error = fetch_weather(city)
    if error:
        result_label.config(text=f"Error: {error}")
    else:
        result_text = (
            f"City: {weather['city']}\n"
            f"Condition: {weather['description']}\n"
            f"Temperature: {weather['temperature']} °C\n"
            f"Humidity: {weather['humidity']} %\n"
            f"Wind Speed: {weather['wind']} m/s"
        )
        result_label.config(text=result_text)
        save_to_history(weather['city'], weather['temperature'])

# GUI Setup
app = tk.Tk()
app.title("Weather App")
app.geometry("350x350")
app.resizable(False, False)

# Navigation buttons
tk.Button(app, text="View History", font=("Arial", 10), command=open_history).pack(pady=5)
tk.Button(app, text="About", font=("Arial", 10), command=open_about).pack(pady=5)

tk.Label(app, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(app, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(app, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

app.mainloop()
