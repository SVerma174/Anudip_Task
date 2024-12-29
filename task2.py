#Q)1. Check if a number is even or odd
number = int(input("Enter a number: "))  # Take input from user
if number % 2 == 0:  # Check if number is divisible by 2
    print("The number is Even")
else:
    print("The number is Odd")

#Q)2. Swap two numberbers
number1 = int(input("Enter first number: "))  # Take first number
number2 = int(input("Enter second number: "))  # Take second number
print("Before swapping: number1 =", number1, ", number2 =", number2)
temp = number1  # Use a temporary variable to swap
number1 = number2
number2 = temp
print("After swapping: number1 =", number1, ", number2 =", number2)

#Q) 3. Convert kilometers to miles
kilometers = float(input("Enter distance in kilometers: "))  # Take distance input
miles = kilometers * 0.621371  # Convert kilometers to miles
print(kilometers, "kilometers is equal to", miles, "miles")

#Q)4. Calculate simple interest
principal = float(input("Enter the principal amount (Rs): "))  # Take principal input
rate = float(input("Enter the rate of interest (%): "))  # Take rate input
time = float(input("Enter the time (years): "))  # Take time input
simple_interest = (principal * rate * time) / 100  # Simple Interest formula
print("The Simple Interest is:", simple_interest)
