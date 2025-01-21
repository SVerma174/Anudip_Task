# Take input for set1
set1 = set(map(int, input("Enter the numbers for set1 separated by space: ").split()))

# Take input for set2
set2 = set(map(int, input("Enter the numbers for set2 separated by space: ").split()))

# Remove items from set1 that are not common to both sets
common_items = set1.intersection(set2)

# Output the result
print("Common items in both sets:", common_items)
