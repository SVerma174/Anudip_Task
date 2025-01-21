''' Write a Python program to Remove items from set1 that are not common to both set1 and set2.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output:
{40, 50, 30}'''


# Take input for set1
set1 = set(map(int, input("Enter the numbers for set1 separated by space: ").split()))

# Take input for set2
set2 = set(map(int, input("Enter the numbers for set2 separated by space: ").split()))

# Example operation: Get only unique items
unique_items = set1.union(set2)
print("Unique items:", unique_items)

