try:
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    
    # Attempt to divide the number by zero
    result = num / 0
except ZeroDivisionError:
    # Handle the division by zero exception
    print("Error: Division by zero is not allowed.")
