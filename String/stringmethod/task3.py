# Input string with mixed characters
s = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Count and print the number of uppercase letters
print("UpperCase:", sum(1 for c in s if c.isupper()))  # Check if each character is uppercase

# Count and print the number of lowercase letters
print("LowerCase:", sum(1 for c in s if c.islower()))  # Check if each character is lowercase

# Count and print the number of numeric characters
print("NumberCase:", sum(1 for c in s if c.isdigit()))  # Check if each character is a digit

# Count and print the number of special characters
print("SpecialCase:", sum(1 for c in s if not c.isalnum() and not c.isspace()))  # Check if character is neither alphanumeric nor a space
