# Program Name: Assignment1.py
# Course: IT3883/Section W02
# Student Name: Tyler Higgins
# Assignment Number: 1
# Due Date: 01/27/2025
# Purpose: This program uses a textbased menu that allows the user to append data to an input buffer, clear the buffer, display the buffer, or exit the program.
# List Specific resources used to complete the assignment: None

# Initialize the input buffer as an empty string
input_buffer = ""

def display_menu():
    """Displays the menu options to the user."""
    print("\nMenu Options:")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

def append_to_buffer():
    """Prompts the user to enter a string and appends it to the input buffer."""
    global input_buffer
    data = input("Enter the string to append to the buffer: ")
    input_buffer += data
    print("Data appended successfully!")

def clear_buffer():
    """Clears the input buffer."""
    global input_buffer
    input_buffer = ""
    print("Input buffer cleared!")

def display_buffer():
    """Displays the current content of the input buffer."""
    if input_buffer:
        print(f"Current input buffer: {input_buffer}")
    else:
        print("Input buffer is empty.")

def main():
    """Main function to execute the program."""
    while True:     # Keeps the menu present until the user exits
        display_menu()
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if choice == 1:
                append_to_buffer()
            elif choice == 2:
                clear_buffer()
            elif choice == 3:
                display_buffer()
            elif choice == 4:
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")     # If the user enters a number that is not of the correct value
        except ValueError:
            print("Invalid input. Please enter a number.")      # In case the user does not enter a valid character

# Run the program
if __name__ == "__main__":
    main()
