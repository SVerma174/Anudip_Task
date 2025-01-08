# List of items
items = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Initialize largest and smallest with the first item in the list
largest = items[0]
smallest = items[0]

# Loop through the list to find the largest and smallest numbers
for num in items:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Print the results
print("The largest number is:", largest)
print("The smallest number is:", smallest)
