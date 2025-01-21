def menu():
    """
    Display the menu of choices to the user and return the selected option.
    """
    print("\nChoose an operation:")
    print("a. Try except")
    print("b. Try multiple except")
    print("c. Try except else")
    print("d. Finally")
    print("e. Try single except")
    print("f. Raising exception")
    return input("Enter your choice: ")

while True:
    # Show the menu and get the user's choice
    choice = menu()
    
    if choice == 'a':
        try:
            # Prompt the user to enter a number
            x = int(input("Enter a number: "))
            print("You entered:", x)
        except ValueError:
            # Handle the case where the input is not a number
            print("Error: That's not a number!")
    
    elif choice == 'b':
        try:
            # Prompt the user to enter two numbers
            x = int(input("Enter a number: "))
            y = int(input("Enter another number: "))
            
            # Attempt to divide the two numbers
            result = x / y
            print("Result:", result)
        except ValueError:
            # Handle invalid input when the input is not a number
            print("Error: Invalid input, please enter numbers.")
        except ZeroDivisionError:
            # Handle division by zero
            print("Error: Division by zero is not allowed.")
    
    elif choice == 'c':
        try:
            # Prompt the user to enter a number
            x = int(input("Enter a number: "))
        except ValueError:
            # Handle the case where the input is not a number
            print("Error: Invalid input, please enter a number.")
        else:
            # This block executes if no exception is raised
            print("You entered a valid number:", x)
    
    elif choice == 'd':
        try:
            # Prompt the user to enter a number
            x = int(input("Enter a number: "))
        except ValueError:
            # Handle invalid input
            print("Error: Invalid input.")
        finally:
            # This block always executes
            print("This block is always executed.")
    
    elif choice == 'e':
        try:
            # Prompt the user to enter a number
            x = int(input("Enter a number: "))
            print("You entered:", x)
        except:
            # Handle any exception that occurs
            print("Error: Something went wrong.")
    
    elif choice == 'f':
        try:
            # Prompt the user to enter a number
            x = int(input("Enter a number: "))
            
            # Raise an exception if the number is negative
            if x < 0:
                raise ValueError("Negative number entered!")
            print("You entered a positive number:", x)
        except ValueError as e:
            # Handle the raised exception
            print("Error:", e)
    
    else:
        # Handle invalid menu choice
        print("Invalid choice. Please try again.")
