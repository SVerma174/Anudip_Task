# Write a Python program to find duplicate values from a list and display those.

# Input list from user
user_list = input("Enter elements separated by space: ").split()

# Initialize an empty list to store duplicates
duplicates = []

# Check for duplicates using a for loop
for item in user_list:
    if user_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

# Display duplicate values
print("Duplicate values:", duplicates)
