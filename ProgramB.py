# Program Name: ProgramB.py
# Course: IT3883/Section W02
# Student Name: Tyler Higgins
# Assignment Number: A4
# Due Date: 3/24/2025
# Purpose: This program receives a string from Program A then converts it to uppercase and finally sends it back.
# Resources: Python socket documentation

import socket

# Host and port to listen on
HOST = '127.0.0.1'  # localhost
PORT = 50000        # same port as client

# Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Bind to the address
    s.listen()

    print("Program B is listening for a connection...")

    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)

        # Receive data
        data = conn.recv(1024)
        if data:
            print("Received:", data.decode())

            # Convert to uppercase
            upper_data = data.decode().upper()

            # Send back
            conn.sendall(upper_data.encode())
