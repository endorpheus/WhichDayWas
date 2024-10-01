import tkinter as tk
from tkinter import messagebox

def zeller_congruence(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    
    k = year % 100
    j = year // 100
    
    # Zeller's congruence formula
    day_of_week = (day + (13*(month+1))//5 + k + k//4 + j//4 + 5*j) % 7
    
    # Map day_of_week to actual day names
    weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    return weekdays[day_of_week]

def calculate_day(event=None):
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())
        day = int(day_entry.get())
        
        if month < 1 or month > 12 or day < 1 or day > 31:
            raise ValueError("Month should be between 1-12 and day should be between 1-31.")
        
        weekday = zeller_congruence(year, month, day)
        
        # Update window title with the result
        root.title(f"{month}/{day}/{year} is a {weekday}")
    except ValueError:
        root.title("")  # Set window title to blank on error

# Create the application window
root = tk.Tk()
root.title("")  # Initially set window title to blank

# Create entry fields
year_label = tk.Label(root, text="Enter year:")
year_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
year_entry = tk.Entry(root)
year_entry.grid(row=0, column=1, padx=10, pady=10)
year_entry.bind('<KeyRelease>', calculate_day)  # Bind key release event

month_label = tk.Label(root, text="Enter month (1-12):")
month_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1, padx=10, pady=10)
month_entry.bind('<KeyRelease>', calculate_day)  # Bind key release event

day_label = tk.Label(root, text="Enter day (1-31):")
day_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
day_entry = tk.Entry(root)
day_entry.grid(row=2, column=1, padx=10, pady=10)
day_entry.bind('<KeyRelease>', calculate_day)  # Bind key release event

# Run the main tkinter event loop
root.mainloop()
