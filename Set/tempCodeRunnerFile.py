'''2. Write a Python program to Return a set of elements present in Set A or B, butnot both.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output:
{20, 70, 10, 60}'''

# Take input for set1
set1 = set(map(int, input("Enter the numbers for set1 separated by space: ").split()))

# Take input for set2
set2 = set(map(int, input("Enter the numbers for set2 separated by space: ").split()))

# Find unique items in either set1 or set2 but not both
unique_items = set1.symmetric_difference(set2)

# Output the unique items
print("Unique items of both sets are:", unique_items)



