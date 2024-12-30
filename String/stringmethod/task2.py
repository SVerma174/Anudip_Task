# Q) 2. Write a Python program to remove duplicate characters from a given string.

apl = input("Enter the string: ")  # Take input string from user
i = 0  # Initialize index counter
ch = ""  # Initialize empty string to store unique characters

for x in apl:  # Loop through each character in the input string
    if apl.index(x) == i:  # Check if the current character's index matches its first occurrence
        ch += x  # Add the character to the result string

    i += 1  # Increment index counter
print(ch)  # Print the string with duplicates removed