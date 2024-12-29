#Q2) sweeping the number 
# Input two numberbers
number1 = int(input("shubham Enter the first number: "))
number2 = int(input("shubham Enter the second number: "))

# Swap the numberbers without using a temporary variable
number1, number2 = number2, number1

# Output the swapped values
print(f"After swapping: First numberber = {number1}, Second number= {number2}")
