'''Write a Python program to find the number of times 4 appears in the tuple.
Input: tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
Output: 3'''


# Take input from the user as a tuple
tuplex = tuple(map(int, input("Enter the tuple elements separated by spaces: ").split()))

# Count occurrences of 4
countning = tuplex.count(4)

# Output the result
print("The number 4 appears", countning, "times in the tuple.")
