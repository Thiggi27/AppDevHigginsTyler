# Program Name: Assignment3.py
# Course: IT3883/Section W02
# Student Name: Tyler Higgins
# Assignment Number: 3
# Due Date: 02/23/2025
# Purpose: This program opens a seperate GUI window and automatically updates input of MPG to determine KmPL
# List Specific resources used to complete the assignment: None

import tkinter as tk

# Conversion factor
MPG_TO_KML = 0.425143707

# This function updates the result as the user types
def update_conversion(event):
    try:
        mpg_value = float(entry.get())  # Get the value from the input box
        kml_value = mpg_value * MPG_TO_KML  # Convert mpg to km/l
        result_label.config(text=f"{kml_value:.2f} km/l")  # auto update pdate the result
    except ValueError:
        result_label.config(text="Invalid input")  # Show error message for invalid input

# Create the main window
root = tk.Tk()
root.title("MPG to KM/L Converter")

# Create an input field
entry = tk.Entry(root)
entry.pack()
entry.bind("<KeyRelease>", update_conversion)  # Call update_conversion when a key is released

# Label to display the result
result_label = tk.Label(root, text="Enter MPG value")
result_label.pack()

# run the GUI loop
root.mainloop()
