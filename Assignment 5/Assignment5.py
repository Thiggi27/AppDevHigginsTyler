# Program Name: Assignment5.py
# Course: IT3883/Section W02
# Student Name: Tyler Higgins
# Assignment Number: Lab#5
# Due Date: 04/15/2025
# Purpose: This program reads temperature readings from a file, stores them in an SQLite database, and calculates the average temperature for Sunday and Thursday.
# Resources Used: sqlite3 module documentation

import sqlite3

# Connect to SQLite database (if it doesnt already exist that is)
conn = sqlite3.connect('temperature_data.db')
cursor = conn.cursor()

# Step 1: Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Temperature (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    )
''')

# Step 2: Read input file and insert data
with open("Assignment5input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            day = parts[0]
            try:
                temp = float(parts[1])
                cursor.execute("INSERT INTO Temperature (Day_Of_Week, Temperature_Value) VALUES (?, ?)", (day, temp))
            except ValueError:
                print(f"Skipping invalid temperature value: {parts[1]}")

# Step 3: Commit changes
conn.commit()

# Step 4: Query average for Sunday and Thursday
cursor.execute("SELECT AVG(Temperature_Value) FROM Temperature WHERE Day_Of_Week = 'Sunday'")
sunday_avg = cursor.fetchone()[0]

cursor.execute("SELECT AVG(Temperature_Value) FROM Temperature WHERE Day_Of_Week = 'Thursday'")
thursday_avg = cursor.fetchone()[0]

# Step 5: Print results
print(f"Average temperature for Sunday: {sunday_avg:.2f}")
print(f"Average temperature for Thursday: {thursday_avg:.2f}")

# Close connection
conn.close()
