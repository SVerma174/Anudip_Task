# Q) 1. Write a Python program to count all letters, digits, and special symbols from the given string.

apl = input("Enter the input: ")  # Take input string from user

def apl_char(apl):
    count_char = 0  # Initialize counter for letters
    count_digit = 0  # Initialize counter for digits
    count_symb = 0  # Initialize counter for special symbols

    for char in apl:  # Loop through each character in the string
        if char.isalpha():  # Check if character is a letter
            count_char += 1
        elif char.isdigit():  # Check if character is a digit
            count_digit += 1
        else:  # If not a letter or digit, it is a special symbol
            count_symb += 1

    print("Characters =", count_char, ", Digits =", count_digit, ", Symbols =", count_symb)  # Print the counts

print("Total count of characters, digits, and symbols:")  # Display message
apl_char(apl)