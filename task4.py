'''#1) Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

def div(a,b):
    #function to perform of division of two numbers 
    if b!= 0:
        return a/b
    else:
        return"Divison by zero is not allowed"

number1=int(input("shubham enter the first number:"))
number2 =int(input("shubham enter the second number:"))

result = div(number1,number2) # calling the div function  

print("The division of number1 by number2 is: ",result)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Q 2). Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .

def square(a):
    return a * a     # Directly return the square of the number

a = int(input("shubham Enter the number: "))  # Ask the user for input
result = square(a)  # Call the square function
print("The square of the number is:", result)  # Display the result

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#3. Using max() and min() functions display the maximum and minimum of 5 random numbers.
# importing the random module for genarting random numbers
import random

# Generarteing  5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]

# Display the generated numbers
print("Random Numbers:",numbers)

# Find and display the maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)

print("Maximum Value:", max_value)
print("Minimum Value:", min_value)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#4. Accept a name from the user and display that in lower case using lower() function

def lowercase(s):
    return s.lower()  # Convert the input string to lowercase

s= input("shubham Enter the name: ")  # Get user input
result = lowercase(s)  # Call the function with the input
print("The string converted to lowercase is:", result)  # Print the result

#******************************************************************************************
# Q5). Write a lambda function that takes one argument and returns 'Positive' if the number is greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. Test it with different numbers
# Lambda function to determine if a number is positive, negative, or zero
check_number = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"   

# Take input from the user
num = float(input("shubham Enter a number: "))

# Test the lambda function
result = check_number(num)

# Print the result
print(f"The number is: {result}")'''

