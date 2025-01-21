try:
    # Prompt the user to enter the first number
    num1 = input("Enter the first number: ")
    
    # Prompt the user to enter the second number
    num2 = input("Enter the second number: ")
    
    # Check if both inputs are numerical
    if not (num1.isdigit() and num2.isdigit()):
        raise TypeError("Inputs must be numerical.")
    
    # Convert inputs to integers and calculate the sum
    num1, num2 = int(num1), int(num2)
    print("The sum is:", num1 + num2)
except TypeError as e:
    # Handle the case where inputs are not numerical
    print("Error:", e)
