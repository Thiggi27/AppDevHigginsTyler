# Program Name: ProgramA.py
# Course: IT3883/Section W02
# Student Name: Tyler Higgins
# Assignment Number: A4
# Due Date: 3/24/2025
# Purpose: This program sends a string to Program B using a socket then waits for a response and prints it.
# Resources: Python socket documentation

import socket

# Server address and port
HOST = '127.0.0.1'  # localhost
PORT = 50000        # use a port above 40000

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to server
    s.connect((HOST, PORT))

    # Prompt user for input
    message = input("Enter a message to send to Program B: ")

    # Send message
    s.sendall(message.encode())

    # Wait for response
    response = s.recv(1024)

    # Print response
    print("Received from Program B:", response.decode())
