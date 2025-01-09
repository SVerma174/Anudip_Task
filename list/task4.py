# Initialize the original list
original_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Specify the length of the first part
first_part_length = 3

# Split the list into two parts
first_part = original_list[:first_part_length]  # Get the first part
second_part = original_list[first_part_length:]  # Get the second part

# Print the splitted lists
print("Splitted the said list into two parts:")
print(f"First part: {first_part}")
print(f"Second part: {second_part}")
