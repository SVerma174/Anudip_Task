try:
    # Prompt the user to enter an integer
    num = int(input("Enter an integer: "))
except ValueError:
    # Handle invalid input when the input is not an integer
    print("Error: Invalid input, please enter a valid integer.")
