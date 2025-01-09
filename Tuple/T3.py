'''Write a Python program to calculate the sum of the numbers in a given tuple.
Input: tuples_list = [(1, 2), (3, 4), (5, 6)]'''




# Take input from the user
numbers = tuple(map(int, input("Enter the numbers separated by spaces: ").split()))

# Calculate the sum
total_sum = sum(numbers)

# Output the result
print("The sum of the numbers is:", total_sum)

