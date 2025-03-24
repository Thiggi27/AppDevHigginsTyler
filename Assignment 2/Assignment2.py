# Program Name: Assignment2.py
# Course: IT3883/Section W02
# Student Name: Tyler Higgins
# Assignment Number: 2
# Due Date: 2/7/25
# Purpose: This program reads student scores from an input file and calculates the average for each student then prints the results in descending order by grade
# List Specific resources used to complete the assignment: None

# Opens the input file and reads all the lines
with open('Assignment2input.txt', 'r') as file:
    lines = file.readlines()


student_averages = {}

# Go through each line to get the scores and calculate the average
for line in lines:
    parts = line.strip().split()  # This splits the line into words
    name = parts[0]  
    scores = list(map(int, parts[1:]))  # This changes the score strings to numbers
    average = sum(scores) / len(scores)  # This calculates the average score
    student_averages[name] = average  # This saves the average with the student's name

# This sorts the students by their average score from highest to lowest
sorted_students = sorted(student_averages.items(), key=lambda x: x[1], reverse=True)

# prints out each student's name and their average score
for student, average in sorted_students:
    print(f"{student} {average:.2f}")
