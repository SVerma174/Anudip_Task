
s = "Welcome to Python Assig" 

# Initialize a counter for vowels
vowel_count = 0

                                              # Loop through each character in the string
for char in s:
    if char in "aeiouAEIOU":                        # Check if the character is a vowel
        vowel_count += 1                            # Increment the counter

# Print the total number of vowels
print("Number of vowels:", vowel_count)
